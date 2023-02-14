--количество исполнителей в каждом жанре
SELECT name_genre, COUNT(name_singer) FROM genre g 
LEFT JOIN genresinger gs ON gs.genre_id  = g.id 
LEFT JOIN singer s ON s.id = gs.singer_id 
GROUP BY g.name_genre 
ORDER BY COUNT(*);


--количество треков, вошедших в альбомы 2019-2020 годов
SELECT COUNT(name_song) FROM album a
JOIN song s ON a.id = s.albumid
WHERE a.creations BETWEEN 2019 AND 2020;


--средняя продолжительность треков по каждому альбому
SELECT albumtitle, AVG(length) FROM album a 
LEFT JOIN song s ON s.albumid = a.id 
GROUP BY albumtitle 
ORDER BY AVG(length);


--все исполнители, которые не выпустили альбомы в 2020 году
SELECT name_singer  FROM singer s 
JOIN album a ON s.id  = a.id
WHERE a.creations !=2020;


--названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
SELECT name FROM compilation c
LEFT JOIN compilationsong c2   ON c.id = c2.songsid 
LEFT JOIN song s ON s.id = c2.songsid
LEFT JOIN album a ON a.id  = s.albumid 
LEFT JOIN albumsinger a2 ON a2.album_id  = a.id  
LEFT JOIN singer s2 ON s2.id = a2.singer_id  
WHERE s2.name_singer LIKE '%Billie Holiday'
ORDER BY name;


--название альбомов, в которых присутствую исполнители более 1 жанра
SELECT albumtitle  FROM album a
LEFT JOIN albumsinger a2 ON a2.album_id  = a.id
LEFT JOIN singer s ON s.id = a2.singer_id  
LEFT JOIN genresinger gs ON gs.singer_id = s.id 
LEFT JOIN genre g  ON g.id = gs.genre_id  
GROUP BY albumtitle 
HAVING count(DISTINCT g.name_genre) > 1
ORDER BY albumtitle;


--наименование треков, которые не входят в сборники
SELECT name_song FROM song s 
LEFT JOIN compilationsong cs ON s.id  = cs.songsid 
LEFT JOIN compilation c ON cs.compilationid = c.id
WHERE c.name IS NULL;


--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT name_singer FROM singer s 
LEFT JOIN albumsinger a2 ON a2.singer_id = s.id
LEFT JOIN album a ON a.id = a2.album_id 
LEFT JOIN song s2 ON s2.id = a.id 
GROUP BY name_singer, s2.length 
HAVING s2.length  = (SELECT min(length) FROM song )
ORDER BY s.name_singer;


--название альбомов, содержащих наименьшее количество треков.
SELECT albumtitle FROM album a 
JOIN song s ON s.albumid = a.id
WHERE s.albumid IN (SELECT albumid FROM song s2
GROUP BY albumid
HAVING count(id) = (SELECT count(id) FROM song s3 
GROUP BY albumid
ORDER BY count
LIMIT 1))
ORDER BY albumtitle;
GROUP BY albumtitle;


I


--название и год выхода альбомов, вышедших в 2018 году
SELECT albumtitle,creations FROM album
WHERE creations = 2018


--название и продолжительность самого длительного трека
SELECT name_song , length  FROM song  
WHERE length  = (SELECT MAX(length) FROM song );

--название треков, продолжительность которых не менее 3,5 минуты
SELECT length, name_song  FROM song
WHERE length <= 3.5;

--названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name FROM compilation
WHERE releasedate BETWEEN 2018 AND 2020;

--исполнители, чье имя состоит из 1 слова
SELECT name_singer FROM singer
WHERE  name_singer NOT LIKE '% %';


--название треков, которые содержат слово "мой"/"my".
SELECT name_song FROM song
WHERE name_song iLIKE ('%my%');
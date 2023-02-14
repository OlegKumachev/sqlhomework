INSERT INTO genre (name_genre)
VALUES  ('Disco'),
		('New Wave'),
		('Reggae'),
		('Jazz'),
		('Blues');


INSERT INTO singer (genre, name_singer)
VALUES   ('Disco', 'Village Peopl'),
	    ('New Wave', 'The Velvet Underground'),
	    ('Reggae', 'Desmond Dekker'),
		('Jazz', 'Billie Holiday'),
		('New Wave','Dead Boys'),
		('New Wave', ' The Runaways'),
		('New Wave', ' Blondie'),
		('Blues','Robert Leroy Johnson');

insert into album (albumtitle, creations)
values  ('Macho Man', 2008),
		('White Light/White Heat', 2020),
		('Intensified', 2014),
		('Solitude', 2010),
		('Young Loud and Snotty', 2018),
		('Queens of Noise', 2015),
		('Parallel Lines', 2012),
		('King of the Delta Blues Singers', 1936);

INSERT INTO song(albumid, name_song, length)
values  (2,'Key West', 5.5),
		(1,'The Gift', 8.1),
		(3,'A it Mek', 2.5),
		(4,'Strange Fruit', 3.1),
		(6,'I Need Lunch', 3.5),
		(6,'California Paradise', 2.8),
		(7,'One Way or Another', 3.9),
		(2,'Sweet Home Chicago', 3.5),
		(8,'Me and the Devil Blues', 2.5),
		(7,'Call me', 2.2),
		(1,'Y.M.C.A.', 4.5),
		(3,'Israelites', 2.5),
		(8,'Cross Road Blues', 2.2),
		(5,'Sonic reducer', 3.7),
		(3, 'All of Me', 3.5),
		(6,'Cherry Bomb', 2.2),
		(2,'After Hours', 2.3),
		(2, 'Pale Blue Eyes', 5.1);
		
INSERT INTO compilation(releasedate, name)
VALUES  (2010,'HIT ONE'),
		(2011, 'HIT TWO'),
		(1977, 'NEW HIT'),
		(2015, '100 BEST SONGS'),
		(2018, '50 SONGS'),
		(2020, 'WAVE'),
		(2008, 'ALL HIT'),
		(2018, 'LEGENT');
	
INSERT INTO genresinger (singer_id, genre_id)
VALUES  (1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,2),
		(6,2),
		(7,2),
		(8,5);

INSERT INTO albumsinger (singer_id, album_id)
VALUES  (1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		(6,6),
		(7,7),
		(8,8);
--		
INSERT INTO compilationSong (songsid, compilationid)
VALUES  (1,1),
		(2,2),
		(3,3),
		(5,4),
		(15,5),
		(8,6),
		(8,7),
		(9,8),
		(15,5),
		(13,4),
		(10,5),
		(11,3),
		(4,5);
		
INSERT INTO genresinger (singer_id, genre_id)
VALUES (8, 4)	

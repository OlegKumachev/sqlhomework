CREATE TABLE IF NOT EXISTS genre (
	id SERIAL primary key,
	name_genre VARCHAR(50) not null 
);

CREATE TABLE IF NOT EXISTS  singer (
	id SERIAL PRIMARY KEY,
	genre VARCHAR(50) not null,
	name_singer VARCHAR(50) not null  
);



CREATE TABLE IF NOT EXISTS albumsinger (
	id SERIAL PRIMARY KEY,
	singer_id INTEGER NOT NULL REFERENCES singer(id),
	album_id INTEGER NOT NULL REFERENCES album(id)
);




CREATE TABLE IF NOT EXISTS song (
	id SERIAL primary key,
	albumid INTEGER REFERENCES Album(id),
	length INTEGER not null,
	name_song VARCHAR(50) not null 
);


CREATE TABLE IF NOT EXISTS compilation (
	id SERIAL primary key,
	releasedate INTEGER not null check (releasedate < 2024),
	name VARCHAR(50) not NULL
);


CREATE TABLE IF NOT EXISTS genreSinger (
	id SERIAL PRIMARY KEY,
	Singer_id INTEGER NOT NULL REFERENCES Singer(id),
	genre_id INTEGER REFERENCES genre(id)
);


CREATE TABLE IF NOT EXISTS compilationSong (
	id SERIAL PRIMARY key,
	songsid INTEGER REFERENCES song(id),
	compilationid INTEGER REFERENCES compilation(id)
);

ALTER TABLE singer  DROP COLUMN genre;



		
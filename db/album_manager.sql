DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists(
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE albums(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id)
);
-- NOTE TO SELF!  ALWAYS USE   createdb database_name  in CONSOLE!  - to create the database before working on it
-- psql -d album_manager -f db/album_manager.sql in console to start

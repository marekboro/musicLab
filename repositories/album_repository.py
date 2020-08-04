from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (name, genre, artist_id) VALUES (%s,%s,%s) RETURNING *"
    values = [album.name, album.genre, album.artist]
    results = run_sql(sql,values)
    id = results[0]["id"]
    album.id= id
    return album



def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    value = [id]
    result = run_sql(sql,value)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['name'],result['genre'],artist)
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['name'],row['genre'],row['id'], artist) # and artist ID?   id or artist.id?
       # album = Album(row['name'],row['genre'],row['id']) 
        albums.append(album)
    
    return albums




def get_artist(album):
    artist = None
    sql = "SELECT artist FROM albums WHERE album = %s"
    values = [album]
    result = run_sql(sql,values)

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
    return artist


                # def select(id):
                    # artist = None
                    # sql = "SELECT * FROM artists WHERE id = %s"
                    # values = [id]
                    # result = run_sql(sql,values)[0] #  WHY are we using 0 here? 
                # 
                    # if result is not None:
                        # artist = Artist(result["name"], result['id'])
                    # return artist

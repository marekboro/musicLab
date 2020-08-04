from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository 


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"  # name and %s  NEED TO BE IN ()
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist



def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row["name"])
        artists.append(artist)
    
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0] #  WHY are we using 0 here? 

    if result is not None:
        artist = Artist(result["name"], result['id'])
    return artist



def all_albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql,values)
    for row in results:
        album = Album(row['name'],row['genre'],artist, row['id'])
        albums.append(album)
    return albums


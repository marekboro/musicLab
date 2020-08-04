from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
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







def tasks(user): # Get ALL tasks associated with one user
    tasks = []

    sql = "SELECT * FROM tasks WHERE user_id = %s"
    values = [user.id]    
    
    results = run_sql(sql, values)
    for row in results:
        task = Task(row['description'],user, row['duration'],row['completed'],row['id'])
        tasks.append(task)

    return tasks

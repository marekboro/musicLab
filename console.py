import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist1 = Artist("The Prodigy")
artist2 = Artist("Power Glove")
artist3 = Artist("Justice")
artist4 = Artist("Carpenter Brut")

artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)
artist_repository.save(artist4)

album1 = Album("Fat of the land","big beat",artist1.id)
album2 = Album("Playback","Synthwave",artist2.id)
album3 = Album("Woman","nu-disco",artist3.id)
album4 = Album("Leather Teeth","Synthwave",artist4.id)
album5 = Album("Invaders Must Die","New Rave",artist1.id)

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)
album_repository.save(album4)
album_repository.save(album5)


print(album_repository.get_artist(album1))


pdb.set_trace()

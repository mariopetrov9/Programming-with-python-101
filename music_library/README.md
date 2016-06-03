# A Music Library

An implemention of a music library, full of songs. Every song has:

* Title 
* Artist
* Album 
* Length - can be converted in seconds/ minutes/ hours. 

Several songs can be grouped in a collection of songs - a playlist, which has the options:

* `repeat` - when our playlist reaches the end, it should loop back again at the beginning
* `shuffle` - everytime we call `next_song()`, we should get a different song

In the playslist we can:

* Add/remove songs
* Add/remove list of songs
* Return a string representation of tha total length of all songs in the playlist
* Return a histogram of all artists in the playlist
* Save and load a playlist to a JSON file.

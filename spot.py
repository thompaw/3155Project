
#make sure to install spotipy by running the requirements.txt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8e72b0de3b8049fbb52cd94aaaab9a73",client_secret="51ad3604ef3246e0a4be039b3c988cca"))
#this is using my spotify client_id and secret. do not change these unless u wanna make ur own spotify api app and use that instead

def output(songname):
    #Pass a string which is the song name that the person searches for. A JSON will be returned with info about top 10 search results.

    results = sp.search(q=songname, limit=10, type='track')   #JSON file returned from spotify api
    #print(results) #this prints the JSON itself

    #example of how to output things from the returned JSON
    for idx, track in enumerate(results['tracks']['items']):  #this outputs the songs in the terminal
        for artist in track['artists']:                       #each song has several artists, so u gotta cycle thru for every song
            print(artist['name'])                             #this prints the artists one at a time
        print(idx, track['name'], track['preview_url'])       #this prints the name of the song and it's preview_url (30 second song preview)
        
    return results #this simply returns that original JSON file.


    #Here is how to iterate thru the JSON using JINJA2

    #return render_template('songs.html', songs=results['tracks']['items']) <<<--- PAY ATTENTION TO THIS

    #In songs.html
    # {% for tracks in songs %} 
    #     <h3>Name:{{ tracks.name }}</h3>
    #     <h3>
    #     {% for artist in tracks.artists %}
    #         {{ artist.name }},
    #     {% endfor %}
    #     </h3>
    #     <audio controls src="{{ tracks.preview_url }}">Your browser does not support the<code>audio</code> element.</audio>
    # {% endfor %}


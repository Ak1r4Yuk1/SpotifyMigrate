import spotipy

# Inserisci qui il tuo token
OLD_ACCOUNT_TOKEN = "INSERISCI_TOKEN_VECCHIO ACCOUNT"
NEW_ACCOUNT_TOKEN = "INSERISCI_TOKEN_NUOVO_ACCOUNT"

#################################################
#PER AVERE IL TOKEN ACCEDI A https://developer.spotify.com/
#FAI LOGIN
#CLICCA CONN IL TASTO DESTRO E POI ANALIZZA ELEMENTO
#VAI SU NETWORK/RETE
#SCORRI L'ELENCO DELLE RICHIESTE FINO A token
#CLICCA IN ALTO SU Risposta
#COPIA IL VALORE DI access_token
#RIPETI LA PROCEDURA PER ENTRAMBI GLI ACCOUNT
#################################################

# Autenticazione
old_sp = spotipy.Spotify(auth=OLD_ACCOUNT_TOKEN)
new_sp = spotipy.Spotify(auth=NEW_ACCOUNT_TOKEN)

# Ottieni le playlist dal vecchio account
def get_playlists(sp):
    playlists = sp.current_user_playlists()
    return playlists['items']

# Trasferisci playlist al nuovo account
def transfer_playlists():
    playlists = get_playlists(old_sp)
    for playlist in playlists:
        print(f"Trasferendo: {playlist['name']}")
        
        # Ottieni le tracce della playlist
        tracks = old_sp.playlist_tracks(playlist['id'])['items']
        track_uris = [track['track']['uri'] for track in tracks]

        # Crea la playlist sul nuovo account
        new_playlist = new_sp.user_playlist_create(new_sp.current_user()['id'], playlist['name'], public=True)
        new_sp.playlist_add_items(new_playlist['id'], track_uris)

    print("Tutte le playlist sono state trasferite!")

transfer_playlists()






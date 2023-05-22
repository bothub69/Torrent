import libtorrent as lt
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Get magnet URL from user
magnet_url = "magnet:?xt=urn:btih:1191DF6F58931334D0A7CEB7ADF378BBB978FEDC&dn=From.S02E05.WEB.x264-PHOENiX&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.birkenwald.de%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentor.org%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2970%2Fannounce&tr=https%3A%2F%2Ftracker.foreverpirates.co%3A443%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"

# Download torrent file using libtorrent
ses = lt.session()
params = {
    'save_path': '/Downloads/',
    'storage_mode': lt.storage_mode_t(2)
}    
handle = lt.add_magnet_uri(ses, magnet_url, params)
ses.start_dht()

print("Downloading metadata...")
while not handle.has_metadata():
    pass

print("Starting download...")
while handle.status().state != lt.torrent_status.seeding:
    s = handle.status()
    print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (
        s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, s.state))
    if s.is_seeding:
        break

# Authenticate with Google Drive using PyDrive
gauth = GoogleAuth()

# Set the client ID and client secret
gauth.client_config = {
    "client_id": "123530391775-vmcgl1seh9tmh48qrkvh6oga0mhd89qc.apps.googleusercontent.com",
    "client_secret": "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",
    "redirect_uri": "https://developers.google.com/oauthplayground"
}

# Set the access token
gauth.credentials.refresh_token = "1//04m2Sttzu9TuqCgYIARAAGAQSNwF-L9IrLlf5vz9QNhEZGgFpq9GBd0DIch6G5wDKx0veQQXfuTl6mulkbO8XXN3se8wks_CXmhg"

drive = GoogleDrive(gauth)

# Upload file to Google Drive
file1 = drive.CreateFile({'title': 'Downloaded Torrent File'})
file1.Upload()

print("File has been uploaded")
                                                                                          

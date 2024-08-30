from yandex_music import Client
from config import YM_API_TOKEN

client = Client(YM_API_TOKEN)
client.init()


def get_first_track():
    track = client.users_likes_tracks()[0].fetch_track()
    direct_link = track.get_download_info()[0].get_direct_link()
    return direct_link

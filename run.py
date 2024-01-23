from yandex_music import Client

client = Client('y0_AgAAAABk0xPPAAG8XgAAAAD45Ntf5Gmgg8K_Sw2TUefClukvbJJygh4').init()

def search(track_name):
    search_result = client.search(track_name)
    if search_result.best:
        type_ = search_result.best.type
        best = search_result.best.result
        if type_ != 'track':
            return None
        else:
            return best


print(search('go robot'))


def track_like(track_name):
    if search(track_name) != None:
        client.users_likes_tracks(search(track_name)['id'])
        print('done')


def track_dislike(track_name):
    if search(track_name) != None:
        client.usersLikesTracksRemove(search(track_name)['id'])
        print('done')


track_dislike('wet sand')

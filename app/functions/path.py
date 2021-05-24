from requests.sessions import session
from app.functions.data_store import list_all_entites


def get_all_folders(path):
    if path == "":
        all_folders = list_all_entites(session["username"])
    else:
        all_folders = list_all_entites(session["username"]+"/"+path)
    return all_folders
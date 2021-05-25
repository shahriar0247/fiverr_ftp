from flask import session
from app.functions.data_store import list_path_entites, store_data


def get_all_folders(path):
    if path == "" or path == None:

        all_folders = list_path_entites("/home/" + session["username"])
    else:
        all_folders = list_path_entites("/home/" + session["username"]+path)
    return all_folders

def create_folder(foldername, filepath):
    store_data(foldername, filepath, 00, 00, session["username"],"test","folder")
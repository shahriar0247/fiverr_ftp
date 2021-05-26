from app.functions.modify_files import upload_file
from flask import session
from app.functions.data_store import list_path_entites, store_data
import random
from urllib.parse import unquote



def get_all_folders(path):
    if path == "" or path == None:

        all_folders = list_path_entites("/home/" + session["username"])
    else:
        all_folders = list_path_entites("/home/" + session["username"]+path)
    return all_folders

def create_folder(foldername, filepath):
    all_folders = get_all_folders(filepath)
    
    for one_folder in all_folders:
        if foldername == one_folder["Filename"]:
            return "Folder already exists"
        
    filepath = "/home/" + session["username"] + filepath
    filepath = unquote(filepath)
    store_data(foldername, filepath, 00, 00, session["username"],"test","folder")
    return True

def upload_files(file, filepath):
    
    all_folders = get_all_folders(filepath)
    for one_folder in all_folders:
        if file.filename == one_folder["Filename"]:
            return file.filename +" already exists"
    
    filepath = "/home/" + session["username"] + filepath
    filepath = unquote(filepath)
    file_size = get_file_size(len(file.stream.read()))



    file.seek(0)
    file_data = file.stream.read()
    file_id =  random.randint(20, 5000000000)
    
    store_data(file.filename, filepath, file_id, file_size, session["username"],"test","file")
    upload_file(file_data, file.content_type, file_id)
    return True

def get_file_size(file_size):
    file_size = file_size / 8

    file_size_text = str(file_size) + " B"
    if file_size > 900:
        file_size = file_size / 1024
        file_size_text = str(file_size) + " KB"
        if file_size > 900:
            file_size = file_size / 1024
            file_size_text = str(file_size) + " MB"
            if file_size > 900:
                file_size = file_size / 1024
                file_size_text = str(file_size) + " GB"

    return file_size_text[0:2] + file_size_text[-4:-1] + "B"
        
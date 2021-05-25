
from google.cloud import datastore
import os


def get_data_store_client():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'
    client = datastore.Client()

    return client
    
def get_entity(entity_id):
    #5673082664517632
    client = get_data_store_client()
    entity = datastore.Entity(key=client.key('File Infp', entity_id))
    return entity

def get_entity_id(entity):
    return entity.key.id  

def store_data(filename, filepath, fileid, filesize, fileowner, fileshareurl, filetype):
    client = get_data_store_client()
    entity = datastore.Entity(client.key("File Infp"))

    entity.update({
        'Filename': filename,
        'Filepath': filepath,
        'Fileid': fileid,
        'Filesize': filesize,
        'Fileowner':fileowner,
        'Fileshareurl':fileshareurl,
        "Filetype" : filetype
    })
    client.put(entity)


def edit_data(filename, filepath, fileid, filesize, fileowner, fileshareurl, entity_id):
    client = get_data_store_client()
    entity = get_entity(entity_id)

    entity.update({
        'Filename': filename,
        'Filepath': filepath,
        'Fileid': fileid,
        'Filesize': filesize,
        'Fileowner':fileowner,
        'Fileshareurl':fileshareurl
    })
    client.put(entity)

def list_all_entites():
    client = get_data_store_client()
    query = client.query(kind='File Infp')
    results = list(query.fetch())
    return results


def list_path_entites(path):
    all_entites = list_all_entites()
    all_path_entites =[]
    for one in all_entites:
        filepath = one["Filepath"]
        username = one["Fileowner"]
        if path == filepath:
            all_path_entites.append(one)
    return all_path_entites



def delete_entity(entity_id):
    client = get_data_store_client()
    key = client.key("File Infp", entity_id)
    client.delete(key)

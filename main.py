import logging
import requests
import threading
from concurrent.futures import Future
import time
import view

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

names : list

def list_races(response):

    if response.status_code == 200:
        global names
        response_json = response.json()
        names = [i.get('name') for i in response_json ]
        view.start(names)
        # id = response_json[0].get('_id')
        # description = response_json[0].get('description')
        # roles = response_json[0].get('roles')
        # dictionary = { 'name ' : name, 'id ' : id, 'description ' : description, 'roles' : roles}




def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()

    return future




if __name__ == '__main__':
    
    response : list
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: list_races(future.result())
    )

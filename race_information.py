import logging
import requests
import threading
from concurrent.futures import Future



def run(search):
    response : list
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: show_race(future.result(), search)
    )




def show_race(response, search):
    if response.status_code == 200:
        print(search)
        response_json = response.json()
        names = [i.get('name') for i in response_json if i.get('name').lower() == search.lower()]
        print(f'La raza es {names}')




def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()

    return future
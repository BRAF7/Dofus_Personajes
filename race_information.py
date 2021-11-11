import requests
import threading
from concurrent.futures import Future
import view_information



def run(search):
    response : list
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: show_race(future.result(), search)
    )




def show_race(response, search) :
    if response.status_code == 200:
        print(search)
        response_json = response.json()
        for i in response_json:
            if i.get('name').lower() == search.lower():
                name = i.get('name')
                id_race = i.get('_id')
                description = i.get('description')
                roles = i.get('roles')
                url_image = i.get('femaleImg')
                view_information.show_image(url_image)
                view_information.start(name, id_race, description, roles)
                break
        




def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))
    thread.start()

    return future
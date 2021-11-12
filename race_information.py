import requests
import threading
from concurrent.futures import Future
#MODULE
from request_API import generate_request
import view_information




def run(search):
    
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: show_race(future.result(), search)
    )




def show_race(response, search) :
    if response.status_code == 200:
        
        response_json = response.json()
        for i in response_json:
            if i.get('name').lower() == search.lower():
                name = i.get('name')
                id_race = i.get('_id')
                description = i.get('description')
                roles = i.get('roles')
                url_image = i.get('femaleImg')
                
                #THREAD
                image = threading.Thread(target=view_information.show_image, args=(url_image, ))
                
                information = threading.Thread(
                    target=view_information.start,
                    args=(
                        name, 
                        id_race, 
                        description,
                        roles
                    )
                )
                information.start()
                image.start()
                break
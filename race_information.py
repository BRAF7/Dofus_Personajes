import requests
import threading
from concurrent.futures import Future
#MODULE
from request_API import generate_request
import view_information
#Google trans
from googletrans import Translator
translator = Translator()



def run(search : str) -> None:
    
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: show_race(future.result(), search)
    )




def show_race(response : any, search : str) -> None:
    if response.status_code == 200:
        
        response_json : dict = response.json()
        
        for i in response_json:
            
            if i.get('name').lower() == search.lower():
                #Information
                name : str        = i.get('name')
                id_race : str     = i.get('_id')
                description : str = i.get('description')
                roles : str       = i.get('roles')
                url_image : str   = i.get('femaleImg')
                print(type(roles), roles)
                translation_description = translator.translate(description, dest='es')
                for i in range(len(roles)):
                    pos = i-1
                    translation_roles = translator.translate(roles[pos],dest='es')
                    roles[pos] = translation_roles.text               
                description = translation_description.text
                

                #THREAD
                image :  threading      = threading.Thread(
                    target=view_information.show_image,
                    args=(url_image, )
                )
                
                information : threading = threading.Thread(
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
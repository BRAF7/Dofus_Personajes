#MODULE
from request_API import generate_request
import view



def list_races(response):
    
    if response.status_code == 200:
        response_json = response.json()
        names = [i.get('name') for i in response_json ]
        view.start(names)




if __name__ == '__main__':
    
    future = generate_request('https://fr.dofus.dofapi.fr/classes')
    future.add_done_callback(
        lambda future: list_races(future.result())
    )
import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))     # la solicitud que hicimos nos trajo los datos pero nos los trajo como string y un string no lo puedo empezar a editar entonces tenemos que transformalo
    
    #transformacion del string con requests

    categories = r.json()
    for category in categories:
        print(category['name'])
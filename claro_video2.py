import json
import requests

session = requests.session()
urls_movies = [
    #accion y aventura
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&quantity={quantity}&from={from_}&level_id=GPS&order_way=ASC&order_id=50&filter_id=39263',
    #biograficas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Firefox&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=e45j7l7c4k478gs5v8qf7cs7k6&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75890',
    #ciencia ficcion
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75890',
    #cine de oro
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75891',
    #clasicas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75892',
    #comedia
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75893',
    #deportes
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75894',
    #drama
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75895',
    #docu
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75896',
    #familiares
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75897',
    #historicas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75898',
    #infantiles
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75899',
    #latinas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75900',
    #musica
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75901',
    #romanticas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75902',
    #terror y suspenso
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75903',
    #descargables
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75904'
]
data = []
for url_movie in urls_movies:
    from_ = 0
    quantity = 50
    while True:
        url_request = url_movie.format(quantity = quantity, from_ = from_)       
        print(url_request)
        response = session.get(url_request)
        contenidos = response.json()
        contenidos = contenidos['response']['groups']
        if contenidos == []:   
            break
        for contenido in contenidos:
            title = contenido['title']
            description = contenido['description_large']
            year = contenido['year']
            type_ = contenido['is_series']
            id_ = contenido['id']
            if type_:
                type_ = 'serie'
            else:
                type_ = 'movie'
            data_contenido = {
                'Title': title,
                'Description': description,
                'Year': year,
                'Type': type_
            }
            data.append(data_contenido)   
            print(data_contenido)    
        from_ += quantity

urls_series = [
    #accion y aventura
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&quantity={quantity}&from={from_}&level_id=GPS&order_way=ASC&order_id=50&filter_id=39267',
    #anime y videojuego
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75742',
    #biograficas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75743',
    #ciencia ficcion
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75744',
    #clasicas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=7574',
    #comedia
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75747',
    #deportes
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75748',
    #docu
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75749',
    #drama
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75750',
    #series espanolas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75751',
    #familiares
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75752',
    #historicas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75753',
    #infantiles
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75754',
    #latinas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75755',
    #musica
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75756',
    #romanticas
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75757',
    #terror y suspenso
    'https://mfwkweb-api.clarovideo.net/services/content/list?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&order_id=200&order_way=DESC&level_id=GPS&from={from_}&quantity={quantity}&node_id=75758',
    ]
for url_serie in urls_series:
    from_ = 0
    quantity = 50
    while True:
        url_request = url_serie.format(quantity = quantity, from_ = from_)
        response = session.get(url_request)
        contenidos = response.json()
        contenidos = contenidos['response']['groups']
        if contenidos == []:   
            break
        for contenido in contenidos:
            
            title = contenido['title']
            description = contenido['description_large']
            year = contenido['year']
            type_ = contenido['is_series']
            id_ = contenido['id']
            if type_:
                type_ = 'serie'
            else:
                type_ = 'movie'
            #DATA DE CADA SERIE (TEMPORADAS, CAPITULOS, DESCRIPCION POR CAPITULO)
            # ID_first_episode == ID DE SERIE  <<<<<<<<<<             
            # url_series_each = 'https://mfwkweb-api.clarovideo.net/services/content/serie?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=j8krs81ssrrjjrc2cin4ni0r51&group_id={id_first_episode}'
            # url_request_each = url_series_each.format(id_first_episode = id_)
            # response_each = session.get(url_request_each)
            # data_each_serie = response_each.json()
            # data_each_serie = data_each_serie['response']['seasons']
            # for data_each in data_each_serie:
            #     episodes_count = data_each['episodes_count']
            #     seasons = data_each['seasons']
            #     episodes = data_each['episodes']
            #     print(episodes) 
            # seasons = {
            #     ''
            # }
            #print(data_each_serie)
        data_contenido = {
                'Title': title,
                'Description': description,
                'Year': year,
                'Type': type_,
                'id' : id_
                #'season': seasons
        }
        #print(data_contenido)
        data.append(data_contenido)    
         
        from_ += quantity

with open('data.json', 'w', encoding='utf-8') as file:
   json.dump(data, file, ensure_ascii=False, indent=4)

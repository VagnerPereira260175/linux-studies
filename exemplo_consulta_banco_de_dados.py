#!/usr/bin/env python
#!/usr/bin/env python

#from pymongo import MongoClient
from pymongo import MongoClient

# Conexão com o Cosmos DB
#mongo_client = MongoClient('mongodb://cg-prd-cosmos-iot-001:0pyMomAFW3TEs6Bm7M5NBsuT3RYakLV8jjwJPL80tORZSEoH2l85UN8GYDe8KWKMNWaKHZ9LiIapxjGYgM6usQ==@cg-prd-cosmos-iot-001.mongo.cosmos.azure.com:10255/?ssl=true')
mongo_client = MongoClient('entrar com a url')
db = mongo_client["nome do banco"]
#db = mongo_client['iothub_plataforma']
coll_disp_config = db['nome de collection']
#coll_disp_config = db['iothub_dispositivo_configuracao']

# Função para extrair os dados necessários
def extract_geolocation():
    query = {}
    projection = {
        'Campo' : 1,
        'Campo2': 1,
        'Campo3':1,
        '_id':0
    }

    query_result = coll_disp_config.find(query,projection)

    for item in query_result:
        nome_campo = item.get("Campo")
        nome_campo = item.get("Campo2")
        nome_campo = item.get("Campo3")

        print(f"Campo: {nome_campo}, Campo1: {nome_campo}, Campo2: {nome_campo}") 


# Executar a função
if __name__ == "__main__":
    extract_geolocation()


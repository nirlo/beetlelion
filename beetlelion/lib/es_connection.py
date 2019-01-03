from elasticsearch import Elasticsearch

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print("We're good, moving forward")
    else:
        print("issues, please close and fix before pushing")
    return _es

def create_index(es_object, index_name, ):

  settings = {}


  try: 
    if not es_object.indices.exists(index_name):
      es_object.indices.create(index=index_name, ignore=400, body=settings)
      print('Created Index')
      created = True
  except Exception as ex:
    print(str(ex))
  finally:
    return created



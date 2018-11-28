from elasticsearch import Elasticsearch


def create_connection(host, port, ssl):
  es = Elasticsearch(
    {'host': host, 'port': port, 'use_ssl': ssl}
  )

  return es

def add_index(es, index, info):
  es.index(index, info)




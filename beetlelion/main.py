from es_connection import *
from tokenize import extract_keywords

if __name__ == '__main__':

  es = connect_elasticsearch()

  """
  This section here is for extract the data from the database.
  It should all be done up here before processing.
  I have put the es connection first to ensure we can post
  to the es instance before extracting.
  """
  settings = {
    "settings": {
      "number_of_shards": 1, 
      "number_of_replicas": 0
    },
    "mappings": {
      "members": {
        "dynamic": "strict",
        "properties": {
          "nct_id": {
            "type": "text"
          },
          "official_title": {
            "type": "text"
          },
          "last_update_submitted_date": {
            "type": "date"
          },
          "completion_date": {
            "type": "date"
          },
          "study_type": {
            "type": "text"
          },
          "overall_status": {
            "type": "text"
          },
          "phase": {
            "type": "text"
          },
          "why_stopped": {
            "type": "text"
          },
          "min_age": {
            "type": "Integer"
          },
          "max_age": {
            "type": "Integer"
          },
          "gender": {
            "type": "text"
          },
          "healthy_volunteers": {
            "type": "text"
          },
          "location_city": {
            "type": "text"
          },
          "location_name": {
            "type": "text"
          },
          "url": {
            "type": "text"
          },
          "keywords": {
            "type": "text"
          },
          "conditions": {
            "type": "text"
          },
          "intervention_name": {
            "type": "text"
          },
        }
      }
    }
  }
  index_name = 'keywords'

  create_index(es, index_name, settings)
  
  
  #these should be within a loop system
  #for _ in _:
    key_words = extract_keywords(text)
    outcome = store_info(es, index_name, index_name, keywords)
    


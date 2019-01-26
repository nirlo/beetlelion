from sqlalchemy import create_engine

# postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]



#       Hostname:  aact-db.ctti-clinicaltrials.org
#       Port: 5432
#       Database name:  aact
#       User name: (sign up/in to get a username)
#       Password:  'your AACT password' 

def getEngine():
    return create_engine("postgresql+psycopg2://lou00011:uBcff4C3iQzt7-w`@aact-db.ctti-clinicaltrials.org:5432/aact")

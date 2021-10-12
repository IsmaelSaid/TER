import psycopg2 as ps
from traitementsbd import *


##### Se connecter a la base et créer les tables
host = "localhost"
user = "ismael"
password = "admin"
database = "projet"
conn = ps.connect("host=%s dbname=%s user=%s password=%s" % (host, database, user,password))
cur = conn.cursor()


#####Création des tables
# Suppression des tables existantes
for request in RequetesSuppressionTables():
    cur.execute(request)


# Création de toutes les tables 
for request in RequetesCreationTables():
    cur.execute(request)


#####Remplissage des tables
# Remplir la table essai
for request in RequetesInsertionEssaiSql():
    print(request)
    cur.execute(request)



#####Commit des résultats dans la base
conn.commit()
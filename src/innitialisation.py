# Ce script sert a innitialiser les données de la base de donnée

# Connexion a la base de donnée postGresql
import psycopg2 as ps
host = "localhost"
user = "ismael"
password = "admin"
database = "projet"
conn = ps.connect("host=%s dbname=%s user=%s password=%s" % (host, database, user,password))

cur = conn.cursor()

# Commandes de création de la table
# table 

request1 = "CREATE TABLE utilisateur(\
    id INT PRIMARY KEY NOT NULL,\
    nom VARCHAR(100),\
    prenom VARCHAR(100),\
    email VARCHAR(255),\
    date_naissance DATE,\
    pays VARCHAR(255),\
    ville VARCHAR(255),\
    code_postal VARCHAR(5),\
    nombre_achat INT\
)"

request2 ="DROP TABLE  utilisateur"

cur.execute(request2)
conn.commit()
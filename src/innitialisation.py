# Ce script sert a innitialiser les données de la base de donnée
import psycopg2 as ps

# ======================= Connexion a la base de donnée postGresql ================================
host = "localhost"
user = "ismael"
password = "admin"
database = "projet"
conn = ps.connect("host=%s dbname=%s user=%s password=%s" % (host, database, user,password))


# =======================Commandes de création de la table =======================================

cur = conn.cursor()


#Table Essai
createEssaiSql = "CREATE TABLE Essai(\
    codeEssai INT PRIMARY KEY,\
    nomEssai VARCHAR(250))"

#  Table Parcelle
createParcelleSql="CREATE TABLE Parcelle(\
    codeParcelle INT PRIMARY KEY NOT NULL,\
    bloc VARCHAR(255),\
    nomParcelle VARCHAR)"

# # Table EssaiParcelle
createEssaiParcelleSql="CREATE TABLE EssaiParcelle(\
    dateDebut DATE,\
    codeParcelle INT FOREIGN KEY REFERENCES Parcelle(codeParcelle),\
    codeEssai INT FOREIGN KEY REFERENCES Essai(nomEssai))"


# # Table Facteur
createFacteurSql="CREATE TABLE Facteur(\
    codeFacteur INT PRIMARY KEY NOT NULL,\
    descriptionFacteur VARCHAR(250))"

# # Table Modalite
createModaliteSql="CREATE TABLE Modalite(\
    dateApplicationModalite DATE,\
    codeParcelle INT FOREIGN KEY REFERENCES Parcelle(codeParcelle),\
    codeFacteur INT FOREIGN KEY REFERENCES Facteur(codeFacteur))" 


# # Table Adventice t

createAdventiceSql="CREATE Adventice(codeAdventice INT PRIMARY KEY NOT NULL,\
    nomAdventice VARCHAR(250))"

# # Table noteAdventice 
createNoteAdventice = "CREATE NoteAdventice(dateNotation DATE,\
    localisation VARCHAR(250))"



createdBy =[createEssaiSql,createParcelleSql,createEssaiParcelleSql,createFacteurSql,createFacteurSql,createAdventiceSql,createNoteAdventice]

for request in createdBy:
    print(request)

# cur.execute(createEssaiSql)
conn.commit()
# Ce script sert a innitialiser les données de la base de donnée
import psycopg2 as ps

# ======================= Connexion a la base de donnée postGresql ================================
host = "localhost"
user = "ismael"
password = "admin"
database = "projet"
conn = ps.connect("host=%s dbname=%s user=%s password=%s" % (host, database, user,password))
cur = conn.cursor()

# ======================= Commandes de création des tables =======================================

#Table Essai
createEssaiSql = "CREATE TABLE Essai(\
    codeEssai INT PRIMARY KEY,\
    nomEssai VARCHAR(250))"

# Table Projet 
createProjetSql ="CREATE TABLE Projet(codeProjet INT PRIMARY KEY,descriptionProjet VARCHAR(250))"

#  Table Parcelle
createParcelleSql="CREATE TABLE Parcelle(\
    codeParcelle INT PRIMARY KEY NOT NULL,\
    bloc VARCHAR(255),\
    nomParcelle VARCHAR)"

# Table Essaiprojet
createEssaiProjetSql="CREATE TABLE Essaiprojet(\
    codeEssai INT REFERENCES Essai(codeEssai),\
    codeProjet INT REFERENCES Projet(codeProjet))"

# # Table EssaiParcelle
createEssaiParcelleSql="CREATE TABLE EssaiParcelle(\
    dateDebut DATE,\
    codeParcelle INT REFERENCES Parcelle(codeParcelle),\
    codeEssai INT REFERENCES Essai(codeEssai))"


# # Table Facteur
createFacteurSql="CREATE TABLE Facteur(\
    codeFacteur INT PRIMARY KEY NOT NULL,\
    descriptionFacteur VARCHAR(250))"

# # Table Modalite
createModaliteSql="CREATE TABLE Modalite(\
    dateApplicationModalite DATE,\
    codeParcelle INT REFERENCES Parcelle(codeParcelle),\
    codeFacteur INT REFERENCES Facteur(codeFacteur),\
    PRIMARY KEY (codeFacteur,dateApplicationModalite))"


# # Table Adventice

createAdventiceSql="CREATE TABLE Adventice(codeAdventice INT PRIMARY KEY NOT NULL,\
    nomAdventice VARCHAR(250))"

# # Table noteAdventice 
createNoteAdventice = "CREATE TABLE NoteAdventice(dateNotation DATE,\
    localisation VARCHAR(250))"

# TODO: Ecrire les CI pour: Localisation data_notation & date_application_modalite

createdBy =[\
    createEssaiSql,\
    createParcelleSql,\
    createEssaiParcelleSql,\
    createFacteurSql,\
    createModaliteSql,\
    createAdventiceSql,\
    createNoteAdventice,\
    createProjetSql]


# ======================= Commandes suppression des tables  =======================================
deletedBy=[\
    "DROP TABLE IF EXISTS EssaiParcelle",\
    "DROP TABLE IF EXISTS Essai",\
    "DROP TABLE IF EXISTS Parcelle CASCADE",\
    "DROP TABLE IF EXISTS Facteur CASCADE",\
    "DROP TABLE IF EXISTS Modalite",\
    "DROP TABLE IF EXISTS Adventice",\
    "DROP TABLE IF EXISTS NoteAdventice",\
    "DROP TABLE IF EXISTS Projet"]

# =======================Execution =======================================

for req in deletedBy:
    print(req)
    cur.execute(req)

for request in createdBy:
    print(request)
    cur.execute(request)


# ======================= Données de test =======================================
# TODO

# Toute les parcelles seront dans cette table

# Ajout de parcelles
cur.execute(\
    "INSERT INTO Parcelle (codeParcelle,bloc,nomParcelle) VALUES\
    (1,'1','nom parcelle 1'),\
    (2,'2','nom parcelle 2'),\
    (3,'1','nom parcelle 3')")

# Ajout d'essai

cur.execute(\
    "INSERT INTO Essai (codeessai,nomessai) VALUES\
    (1,'nom essai 1'),\
    (2,'nom essai 1'),\
    (3,'nom essai 2')")


conn.commit()
# =======================Données réels=====================================
def fillDatabase():
    # TODO 
    print("a développer")
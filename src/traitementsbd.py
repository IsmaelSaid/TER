import os
from pathlib import Path
import pandas as pd


def RequetesCreationTables():
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
    return [\
        createEssaiSql,\
        createParcelleSql,\
        createEssaiParcelleSql,\
        createFacteurSql,\
        createModaliteSql,\
        createAdventiceSql,\
        createNoteAdventice,\
        createProjetSql]

def RequetesSuppressionTables():
    return ["DROP TABLE IF EXISTS EssaiParcelle",\
        "DROP TABLE IF EXISTS Essai",\
        "DROP TABLE IF EXISTS Parcelle CASCADE",\
        "DROP TABLE IF EXISTS Facteur CASCADE",\
        "DROP TABLE IF EXISTS Modalite",\
        "DROP TABLE IF EXISTS Adventice",\
        "DROP TABLE IF EXISTS NoteAdventice",\
        "DROP TABLE IF EXISTS Projet"]

    # TODO Automatiser la rechercher des fichiers correspondant
    # TODO OU récuperer le nom du sheet correspondant a la lecture du csv
    # Ecriture des noms de fichier en dure pour l'instant
   
def RequetesInsertionEssaiSql():
    nomsfichiers=["modalite1.csv","modalite2.csv"]
    code = 0
    result=[]
    # Pour tout les fichiers
    for f in nomsfichiers:
        fichier=(os.path.dirname(os.path.realpath(__file__))).replace("\\","/")+"/ressources/"+f
        
        # chargement du fichier
        data = pd.read_csv(fichier)
        df = pd.DataFrame(data)

        # Selection des colonnes 
        selected_cols= df.iloc[:, 0].drop_duplicates()
        
        for val in selected_cols:
            request = "INSERT INTO essai VALUES"+"('"+str(code)+"','"+val+"')"
            result.append(request)
            # print(request)
            code += 1
    return result
    
def RequeteInsertionAdventiceSql():
    # TODO 
    result = []
    return result

def RequeteInsertionProjetSql():
    # TODO 
    result = []
    return result

def RequeteInsertionParcelleSql():
    # TODO 
    result = []
    return result
def RequeteInsertionNotationSql():
    # TODO 
    result = []
    return result
def RequeteInsertionFacteurSql():
    # TODO 
    result = []
    return result
def RequeteInsertionModaliteSql():
    # TODO 
    result = []
    return result
def RequeteInsertionPratiqueSql():
    # TODO 
    result = []
    return result
def RequeteInsertionPratiqueParcelleSql():
    # TODO 
    result = []
    return result
def RequeteInsertionProduitSql():
    # TODO 
    result = []
    return result
def RequeteInsertionMatiereActiveSql():
    # TODO 
    result = []
    return result



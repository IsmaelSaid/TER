import os
from pathlib import Path
import pandas as pd


def RequetesCreationTables():
    #Table Essai
    createEssaiSql = "CREATE TABLE Essai(\
        codeEssai INT PRIMARY KEY,\
        nomEssai VARCHAR(250))"

    # Table Projet 
    createProjetSql ="CREATE TABLE Projet(codeprojet INT PRIMARY KEY,descriptionprojet VARCHAR(250))"

    #  Table Parcelle
    createParcelleSql="CREATE TABLE Parcelle(\
        codeparcelle INT PRIMARY KEY NOT NULL,\
        bloc VARCHAR(255),\
        nomparcelle VARCHAR)"

    # Table Essaiprojet
    createEssaiProjetSql="CREATE TABLE Essaiprojet(\
        codeessai INT REFERENCES Essai(codeessai),\
        codeprojet INT REFERENCES Projet(codeprojet))"

    # # Table EssaiParcelle
    createEssaiParcelleSql="CREATE TABLE Essaiparcelle(\
        datedebut DATE,\
        codeparcelle INT REFERENCES Parcelle(codeparcelle),\
        codeessai INT REFERENCES Essai(codeessai))"


    # # Table Facteur
    createFacteurSql="CREATE TABLE Facteur(\
        codefacteur INT PRIMARY KEY NOT NULL,\
        descriptionfacteur VARCHAR(250))"

    # # Table Modalite
    createModaliteSql="CREATE TABLE Modalite(\
        dateapplicationmodalite DATE,\
        codeparcelle INT REFERENCES Parcelle(codeparcelle),\
        codefacteur INT REFERENCES Facteur(codefacteur),\
        PRIMARY KEY (codefacteur,dateapplicationmodalite))"


    # # Table Adventice

    createAdventiceSql="CREATE TABLE Adventice(codeadventice INT PRIMARY KEY NOT NULL,\
        nomadventice VARCHAR(250))"

    # # Table noteAdventice 
    createNoteAdventice = "CREATE TABLE NoteAdventice(datenotation DATE,\
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
    return ["DROP TABLE IF EXISTS Essaiparcelle",\
        "DROP TABLE IF EXISTS Essai",\
        "DROP TABLE IF EXISTS Parcelle CASCADE",\
        "DROP TABLE IF EXISTS Facteur CASCADE",\
        "DROP TABLE IF EXISTS Modalite",\
        "DROP TABLE IF EXISTS Adventice",\
        "DROP TABLE IF EXISTS Noteadventice",\
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



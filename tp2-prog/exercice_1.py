import json
import csv

# Fonction pour écrire des nombres complexes dans un fichier CSV
def ecrire_fichier_csv(nombres_complexes, nom_fichier):
    with open(nom_fichier, 'w', newline='') as fichier:
        writer = csv.writer(fichier)
        # Écrire l'en-tête du fichier CSV
        writer.writerow(['reel', 'imaginaire'])
        # Écrire chaque nombre complexe dans une ligne du fichier CSV
        for nombre in nombres_complexes:
            writer.writerow([nombre.real, nombre.imag])

# Fonction pour lire un fichier JSON et retourner des nombres complexes
def lire_fichier_json(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        donnees = json.load(fichier)
    nombres_complexes = [complex(donnee['reel'], donnee['imaginaire']) for donnee in donnees]
    return nombres_complexes

# Nom des fichiers
fichier_json = 'data.json'
fichier_csv = 'nombres_complexes.csv'

# Lire le fichier JSON
nombres_complexes = lire_fichier_json(fichier_json)

# Écrire les nombres dans le fichier CSV
ecrire_fichier_csv(nombres_complexes, fichier_csv)

print("Les nombres complexes ont été écrits dans '{}'.".format(fichier_csv))

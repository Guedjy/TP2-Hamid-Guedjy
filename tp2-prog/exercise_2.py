import csv


def pokémons_csv(chemin):
    pokemons = {}
    with open(chemin, mode='r', newline='', encoding='utf-8') as fichier:
        lecteur_csv = csv.reader(fichier)
        for ligne in lecteur_csv:
            if ligne:
                nom = ligne[0].strip()
                stats = [int(stat) for stat in ligne[1:]]
                pokemons[nom] = stats
    return pokemons

if __name__ == "__main__":
    chemin = "pokemon.csv"
    pokemon = pokémons_csv(chemin)
    for nom, stats in pokemon.items():
        print(f"{nom}: {stats}")

    print(isinstance(pokemon, dict))
    print(isinstance(pokemon["Pikachu"], list))
    print(isinstance(pokemon["Pikachu"][0], int))

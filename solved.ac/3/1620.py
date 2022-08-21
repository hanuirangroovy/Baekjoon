import sys

n, m = map(int, sys.stdin.readline().strip().split())

pokemon = {}

for i in range(1, n+1):
    pokemon_name = sys.stdin.readline().strip()
    pokemon[i] = pokemon_name
    pokemon[pokemon_name] = i

for _ in range(m):
    find_pokemon = sys.stdin.readline().strip()
    if find_pokemon.isdigit():
        print(pokemon[int(find_pokemon)])
    else:
        print(pokemon[find_pokemon])
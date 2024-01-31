genero = input("¿Cuál es tu genero? (M/F): ").upper()

while genero not in ['M', 'F']:
    print("Por favor, ingresa M o F.")
    genero = input("¿Cuál es tu genero? (M/F): ").upper()

if genero == 'M':
    genero_definido = "señor"
    saludar = "Bienvenido"
else:
    genero_definido = "señora"
    saludar = "Bienvenida"

region = input(f"{saludar} {genero_definido}! ¿De qué región eres?: ")
pokemon_preferido = input(f"¿Cuál es tu Pokemon preferido? (Venusaur/Ivysaur/Charizard): ").capitalize()

if pokemon_preferido == "Venusaur":
    mensaje_de_eleccion = print("Buena eleccion, Venusaur tambien es uno de mis preferidos.")
elif pokemon_preferido == "Ivysaur":
    mensaje_de_eleccion = print("Ivysaur sin duda es un Pokemon inigualable")
elif pokemon_preferido == "Charizard":
    mensaje_de_eleccion = print("Charizard es un Pokemon muy potente, buena eleccion")
else:
    mensaje_de_no_eleccion = print("Todos los pokemon son buenos, pero debes escoger entre los 3 señalados")
    pokemon_preferido = input(f"¿Cuál es tu Pokemon preferido? (Venusaur/Ivysaur/Charizard): ").capitalize()

print(f"\n{saludar} {genero_definido} de {region}, tu Pokemon preferido es {pokemon_preferido}.")
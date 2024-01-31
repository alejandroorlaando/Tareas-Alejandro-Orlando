genero = input("¿Cuál es tu genero? (Masculino/Femenino): ").upper()

while genero not in ['Masculino', 'Femenino']:
    print("Por favor, ingresa Masculino o Femenino.")
    genero = input("¿Cuál es tu genero? (Masculino/Femenino): ").upper()

if genero == 'Masculino':
    genero_definido = "señor"
    saludar = "Bienvenido"
else:
    genero_definido = "señora"
    saludar = "Bienvenida"

region = input(f"{saludar} {genero_definido}! ¿De qué región eres?: ")
pokemon_preferido = input(f"¿Cuál es tu Pokemon preferido? (Venusaur/Ivysaur/Charizard): ").capilize()

if pokemon_preferido == "Venusaur":
    mensaje_de_eleccion = "Buena eleccion, Venusaur mbien es uno de mis preferidos."
elif pokemon_preferido == "	Ivysaur":
    mensaje_de_eleccion = "Ivysaur sin duda es un Pokemon inigualable"
elif pokemon_preferido == "Charizard":
    mensaje_de_eleccion = "Charizard es un Pokemon muy potente, buena eleccion"
else:
    mensaje_de_eleccion = "No seleccionaste ninguno de los 3 pokemon, ¡pero todos son buenos de todos modos!"

print(f"\n{saludar} {genero_definido} de {region}, tu Pokemon preferido es {pokemon_preferido}. {mensaje_de_eleccion}")
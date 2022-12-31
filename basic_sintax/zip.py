#lo que hacemos aqui e convinar varias listas
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinacion = zip(paises,capitales)

for pais,capital in combinacion:
    print(f"La capital de {pais} es {capital}")

with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

caracteres_distintos = len(set(texto))
palabras_distintas = len(set(texto.split()))

print(f"El número de caracteres distintos es: {caracteres_distintos}")
print(f"El número de palabras distintas es: {palabras_distintas}")
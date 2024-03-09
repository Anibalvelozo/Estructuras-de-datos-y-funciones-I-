import sys

tasas = [float(sys.argv[i]) for i in range(1, 4)]
valor_en_pesos = float(sys.argv[4])

soles = valor_en_pesos * tasas[0]
pesos_argentinos = valor_en_pesos * tasas[1]
dolares = valor_en_pesos * tasas[2]

valor_en_pesos = int(float(sys.argv[4]))

print(f"Los {valor_en_pesos} pesos equivalen a:") 
print(f"{soles} Soles")   
print(f"{pesos_argentinos} Pesos Argentinos") 
print(f"{dolares} Dólares") 

from numpy import character

frase = "Curso de Python"
print(frase , "\n")

print(frase[0: 6])
print(frase[1: 6])
print(frase[6])

print("\n Find")
print(frase.find('C'))

print("\n Replace")
print(frase.replace('C', 'O'))

print("\n Join")
print(frase.join("Curso"))

print("\n Strip")
print(frase.strip('Curso'))

print("\n Split")
print(frase.split('o'))
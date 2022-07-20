try:
    f = open('texto.txt')
    s = []
    abc = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    str = ''
    c = 0
    frase = [',', '.', ';', ':','@','&','$','#','^','-','_','¡','!','¿','?','*','+','/','=',]
    contaParra = 0
    contaPalabras = 0
    contFrases = 0
    contLetras = [0 for i in range(len(abc))]
    contSimbolos = [0 for i in range(len(frase))]
    arrayPalabras = []
    resultRepe = 0

    while (s != ""):
        s = f.readline()
        str += s.lower()
        if (len(s.split()) != 0):
            contaParra += 1
        c += len(s.split())

    arrayPalabras = str.split()
    conjuntoPalabras = set(arrayPalabras)

    listPalabras = list(conjuntoPalabras)

    contRepe = [0 for i in range(len(listPalabras))]

    for i in range(len(frase)):
        contFrases += str.count(frase[i])
        contSimbolos[i] = str.count(frase[i])

    for i in range(len(abc)):
        contaPalabras += str.count(abc[i])
        contLetras[i] = str.count(abc[i])

    for i in range(len(listPalabras)):
        contRepe[i] = arrayPalabras.count(listPalabras[i])

    print("\n * * * Contadores * * * \n")
    print("Palabras:", c)
    print("Parrafos:", contaParra)
    print("Letras:", contaPalabras)
    print("Frases:", contFrases)
    print("Simbolos:", contFrases)

    print("\n * * * Ranking * * * \n")
    print("Letras:\n")
    for i in range(len(abc)):
        if (contLetras[i] != 0):
            print(abc[i], ":", contLetras[i])

    print("\n")

    print("Simbolos:\n")
    for i in range(len(frase)):
        if (contSimbolos[i] > 0):

            print(frase[i], ":", contSimbolos[i])

    print("\n")
    resultRepe = 0
    print("Palabras:\n")
    for i in range(len(contRepe)):
        if (contRepe[i] != 0 and contRepe[i] > 1):
            print(listPalabras[i], ":", contRepe[i])
            resultRepe += contRepe[i]

    print("\nPalabras Repetidas:", resultRepe)

except BaseException as err:
    print("Inesperado", {err}, {type(err)})
    raise

date = (2021, 2, 24)
metrajes = [{"id" : 1234,
             "nombre" : "Peter Pan",
             "descripción" : "Se trata de un niño que nunca crece, tiene diez años y odia el mundo de los adultos",
             "genero" : "Infantil",
             "duración" : 77,
             "fecha_lanz" : (1953, 2, 5),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 4.7},
            {"id" : 5678,
             "nombre" : "Coco",
             "descripción" : "Se trata de Miguel, un niño de 12 años en un típico pueblo mexicano llamado Santa Cecilia, quien quiere ser músico",
             "genero" : "Infantil",
             "duración" : 109,
             "fecha_lanz" : (2017, 10, 20),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 4.8},
            {"id" : 2468,
             "nombre" : "Crespúsculo",
             "descripción" : "Esta película se centra en el desarrollo de la relación entre Bella Swan (una adolescente) y Edward Cullen (un vampiro), y los esfuerzos posteriores de Edward y su familia para mantener a Bella a salvo de un grupo de vampiros malvados",
             "genero" : "Romance",
             "duración" : 126,
             "fecha_lanz" : (2009, 1, 1),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 4.8},
            {"id" : 1012,
             "nombre" : "Catwoman",
             "descripción" : "Catwoman se llama Patience Phillips, que es una diseñadora gráfica que trabaja en una empresa cosmética, sumergida en una enorme conspiración",
             "genero" : "Thriller",
             "duración" : 104,
             "fecha_lanz" : (2004, 7, 23),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 3},
            {"id" : 1416,
             "nombre" : "Lucifer",
             "descripción" : "Se centra en Lucifer Morningstar (Tom Ellis), un ángel hermoso y poderoso que fue expulsado del cielo por traición",
             "genero" : "Horror",
             "duración" : 53,
             "fecha_lanz" : (2016, 1, 25),
             "serie_pelicula" : "Serie",
             "puntuación" : 4.9},
            {"id" : 1820,
             "nombre" : "Soul",
             "descripción" : "Joe Gardner es un profesor de música y pianista de Jazz quien sueña con formar parte de una banda y finalmente dedicarse a la música",
             "genero" : "Infantil",
             "duración" : 107,
             "fecha_lanz" : (2020, 12, 25),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 4.6},
            {"id" : 2224,
             "nombre" : "Rapidos y furiosos 9",
             "descripción" : "'Dom' Toretto tiene una vida tranquila fuera del radar, con Letty y su hijo, el pequeño Brian, pero saben que el peligro siempre acecha en su horizonte pacífico",
             "genero" : "Acción",
             "duración" : 188,
             "fecha_lanz" : (2021, 4, 1),
             "serie_pelicula" : "Pelicula",
             "puntuación" : 4.6}]

for i in metrajes:
    if i["serie_pelicula"] == "Serie" and i["puntuación"] >= 4.5:
        print ("La serie " + i["nombre"] + " ya se estrenó y tiene una puntuación mayor o igual a 4.5")
    elif i["serie_pelicula"] == "Pelicula" and i["duración"] < 120:
        print ("La pelicula " + i["nombre"] + " dura menos de 2 horas")
        if i["genero"] == "Thriller":
            print ("La pelicula " + i["nombre"] + " es de genero thriller y tiene una puntuación de " + str(i["puntuación"]))
        elif i["fecha_lanz"] == date:
            print ("La pelicula " + i["nombre"] + " se estrena hoy")
        if i["fecha_lanz"] > date:
            print ("La pelicula " + i["nombre"] + " no se ha estrenado")
            i["puntuación"] = 0
        else:
            print ("La pelicula " + i["nombre"] + " ya se estrenó")

for j in metrajes:
    if j["serie_pelicula"] == "Pelicula" and j["duración"]>120:
        print ("La pelicula " + j["nombre"] + " dura más de 2 horas")
    elif j["fecha_lanz"] == date and j["duración"]>120:
        print ("La pelicula " + j["nombre"] + " se estrena hoy")
    if j["fecha_lanz"] > date and j["duración"]>120:
        print ("La pelicula " + j["nombre"] + " no se ha estrenado")
        j["puntuación"] = 0
    elif j["fecha_lanz"] < date and j["duración"]>120:
        print ("La pelicula " + j["nombre"] + " ya se estrenó")
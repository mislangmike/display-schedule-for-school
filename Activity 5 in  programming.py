classlist = ["AMISTAD, GODFREY II GANGAN",
"AWINGAN, JARED CALIBUGAR",
"AYES, KURT MICHAEL BERMUNDO",
"BARTOLOME, ADRIL SEAN CABAGAY",
"BASCUGUIN, DEVON PALOMA",
"BERSABE, RODWAYNE VARICK SANTILLAN",
"BUSTAMANTE, ADRIAN RUIZ",
"CABAGUA, MIKE LORENZ MISLANG",
"CADELI—A, KIAN SAWAN",
"CARANDANG, KYLE CEDRIC BAYLON",
"CRUZ, CHESTER ARWIN ENIEGO",
"DELA CRUZ, JOSHUA NI—ALGA",
"DIAZ, CHRISTIAN GABRIEL CHIPONGIAN",
"DIENZO, MARK ANGELO DEYTO",
"FELONIA, MIGUEL ANDREI EBREO",
"ESTONILO, KENZU",
"GALAPON, JOSHUA BATA",
"JARDIN, JOSE VILLAR",
"LABERINTO, GIO DANIEL CANAG",
"LUMACAD, RONE GIDEON BARCENA",
"MAGGAY, HAROLD ADRIAN VELUZ",
"MALANA, JOSIAH KEN ESCUADRO",
"MANUSON, JOHANN SEBASTIAN DE ASIS",
"MARQUEZ, AESON JAYME GABRIEL",
"MI—OZA, ELYZAH MARIS",
"OGAY, JOHN LOUIZ SUYOT",
"OREJUDOS, MARC GIAN OREIRO",
"ORO, YENDOR IGNATIUS AQUINO",
"PAULIN, MARK ANTHONY SATSATIN",
"QUILO, DHIMRIX ANGEL FERNAND OFFICIAL",
"QUI—ONES, TREZ ADRIEN NIEGAS",
"RIANO, VOHN ANDREI JIMENEZ",
"RIVERA, FRANZ GEOFF DESTREZA",
"RIVERA, JOHN EDETH VIREYNATO",
"SARAZA, MARIE KATHLEEN GARLITO",
"SATUROS, FRANCIS MEL ALVAREZ",
"TANIERLA, JOSHIA NIBEL VALDERRAMA",
"VANCUYLENBERG, REEZA MARIES FRANCISCO"]
print(classlist)
classlist.sort()

print("Lumacad is in Index" + str(classlist.index("LUMACAD, RONE GIDEON BARCENA")))
print("Diaz is in Index" + str(classlist.index("DIAZ, CHRISTIAN GABRIEL CHIPONGIAN")))
print("Carandang is in Index" + str(classlist.index("CARANDANG, KYLE CEDRIC BAYLON")))
print("Qui-ones is in Index" + str(classlist.index("QUI—ONES, TREZ ADRIEN NIEGAS")))
print("Cruz is in Index" + str(classlist.index("CRUZ, CHESTER ARWIN ENIEGO")))
print("Marquez is in Index" + str(classlist.index("MARQUEZ, AESON JAYME GABRIEL")))
print("Tanierla is in Index" + str(classlist.index("TANIERLA, JOSHIA NIBEL VALDERRAMA")))
print("Orejudos is in Index" + str(classlist.index("OREJUDOS, MARC GIAN OREIRO")))
print("Vancuylenberg is in Index" + str(classlist.index("VANCUYLENBERG, REEZA MARIES FRANCISCO")))


Updatedlist = [("GODFREY II GANGAN" + str(classlist.remove("AMISTAD, GODFREY II GANGAN"))),
("JARED CALIBUGAR" + str(classlist.remove("AWINGAN, JARED CALIBUGAR"))),
("KURT MICHAEL BERMUNDO" + str(classlist.remove("AYES, KURT MICHAEL BERMUNDO"))),
("ADRIL SEAN CABAGAY" + str(classlist.remove("BARTOLOME, ADRIL SEAN CABAGAY"))),
("DEVON PALOMA" + str(classlist.remove("BASCUGUIN, DEVON PALOMA"))),
("RODWAYNE VARICK SANTILLAN" + str(classlist.remove("BERSABE, RODWAYNE VARICK SANTILLAN"))),
("ADRIAN RUIZ" + str(classlist.remove("BUSTAMANTE, ADRIAN RUIZ"))),
("MIKE LORENZ MISLANG" + str(classlist.remove("CABAGUA, MIKE LORENZ MISLANG"))),
("KIAN SAWAN" + str(classlist.remove("CADELI—A, KIAN SAWAN"))),
("KYLE CEDRIC BAYLON" + str(classlist.remove("CARANDANG, KYLE CEDRIC BAYLON"))),
("CHESTER ARWIN ENIEGO" + str(classlist.remove("CRUZ, CHESTER ARWIN ENIEGO"))),
("JOSHUA NI—ALGA" + str(classlist.remove("DELA CRUZ, JOSHUA NI—ALGA"))),
("CHRISTIAN GABRIEL CHIPONGIAN" + str(classlist.remove("DIAZ, CHRISTIAN GABRIEL CHIPONGIAN"))),
("MARK ANGELO DEYTO" + str(classlist.remove("DIENZO, MARK ANGELO DEYTO"))),
("MIGUEL ANDREI EBREO" + str(classlist.remove("FELONIA, MIGUEL ANDREI EBREO"))),
("JOSHUA BATA" + str(classlist.remove("GALAPON, JOSHUA BATA"))),
("JOSE VILLAR" + str(classlist.remove("JARDIN, JOSE VILLAR"))),
("GIO DANIEL CANAG" + str(classlist.remove("LABERINTO, GIO DANIEL CANAG"))),
("RONE GIDEON BARCENA" + str(classlist.remove("LUMACAD, RONE GIDEON BARCENA"))),
("HAROLD ADRIAN VELUZ" + str(classlist.remove("MAGGAY, HAROLD ADRIAN VELUZ"))),
("JOSIAH KEN ESCUADRO" + str(classlist.remove("MALANA, JOSIAH KEN ESCUADRO"))),
("JOHANN SEBASTIAN DE ASIS" + str(classlist.remove("MANUSON, JOHANN SEBASTIAN DE ASIS"))),
("AESON JAYME GABRIEL" + str(classlist.remove("MARQUEZ, AESON JAYME GABRIEL"))),
("ELYZAH MARIS" + str(classlist.remove("MI—OZA, ELYZAH MARIS"))),
("JOHN LOUIZ SUYOT" + str(classlist.remove("OGAY, JOHN LOUIZ SUYOT"))),
("MARC GIAN OREIRO" + str(classlist.remove("OREJUDOS, MARC GIAN OREIRO"))),
("YENDOR IGNATIUS AQUINO" + str(classlist.remove("ORO, YENDOR IGNATIUS AQUINO"))),
("MARK ANTHONY SATSATIN" + str(classlist.remove("PAULIN, MARK ANTHONY SATSATIN"))),
("DHIMRIX ANGEL FERNAND OFFICIAL" + str(classlist.remove("QUILO, DHIMRIX ANGEL FERNAND OFFICIAL"))),
("TREZ ADRIEN NIEGAS" + str(classlist.remove("QUI—ONES, TREZ ADRIEN NIEGAS"))),
("VOHN ANDREI JIMENEZ" + str(classlist.remove("RIANO, VOHN ANDREI JIMENEZ"))),
("FRANZ GEOFF DESTREZA" + str(classlist.remove("RIVERA, FRANZ GEOFF DESTREZA"))),
("JOHN EDETH VIREYNATO" + str(classlist.remove("RIVERA, JOHN EDETH VIREYNATO"))),
("FRANCIS MEL ALVAREZ" + str(classlist.remove("SATUROS, FRANCIS MEL ALVAREZ"))),
("JOSHIA NIBEL VALDERRAMA" + str(classlist.remove("TANIERLA, JOSHIA NIBEL VALDERRAMA"))),
("REEZA MARIES FRANCISCO" + str(classlist.remove("VANCUYLENBERG, REEZA MARIES FRANCISCO")))]
Updatedlist.sort()
print(Updatedlist)

print("engr.Jemar Rivadeneira Penarroyo")
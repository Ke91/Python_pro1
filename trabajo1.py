# Este es mi primer diccionario en python pro, aunque no recuerdo bien python. 

None

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            "FAKE": "Algo que es falso",
            "CAUSA": "Manera de decirle a alguien amigo",
            "BAMBA": "Objeto que es una falsificación",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")


if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(word)
else: 
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no está en el diccionario")

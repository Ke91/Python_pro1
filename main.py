import random
caracteres = "+-~/!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
print(f'tu contraseña es{contraseña}')
""" Las variables de tipo diccionario, se abren y cierran con llaves {},
    los elementos que componen el diccionario a su vez estan compuestos por 
    un atributo y un valor de atributo
"""

user_type = {'id': 1, 'name': 'Admin'}

user_types = [
    {'id': 1, 'name': 'Admin'},
    {'id': 2, 'name': 'Cliente'}
]

my_user = {
    'id': 4455722,
    'name': 'Julio Gaviria',
    'email': 'julio123@gmail.com',
    'age': 14,
    'user_type': 1
}

print ("Usuario: " + my_user['name'])
print ("Email: " + my_user['email'])

if my_user['age'] > 59:
    print ("El usuario " + my_user['name'] + " es un adulto mayor.")
    if my_user['user_type'] == 1:
        print ("El usuario " + my_user['name'] + " es administrador.")
elif my_user['age'] >= 18:
    print ("El usuario " + my_user['name'] + " es mayor de edad.")
    if my_user['user_type'] == 1:
        print ("El usuario " + my_user['name'] + " es administrador.")
else:
    print ("El usuario " + my_user['name'] + " es un menor de edad.")
    if my_user['user_type'] == 1:
        print ("El usuario " + my_user['name'] + " es administrador.")

users =[
    {'id': 4455722, 'name': 'Julio Gaviria', 'email': 'julio123@gmail.com', 'age': 24,'user_type': 1},
    {'id': 1452268, 'name': 'Hernesto Salas', 'email': 'hernesto123@gmail.com', 'age': 65,'user_type': 2},
    {'id': 1452268, 'name': 'Fernanda Rueda', 'email': 'fernandarueda@gmail.com', 'age': 18,'user_type': 1},
    {'id': 1452268, 'name': 'Maria Juliana', 'email': 'mariajuliana@gmail.com', 'age': 17,'user_type': 2}
]

for u in users:
    print ()

user_type_found = next((x for x in user_types if x['id'] == my_user['user_type']), None)
print (user_type_found)

print ("Usuario: " + my_user['name'])
print ("Rol: " + user_type_found['name'])

for u in users:
    if u['age'] > 59:
        print ("El usuario " + u['name'] + " es un adulto mayor.")
        if u['user_type'] == 1:
            print ("El usuario " + u['name'] + " es administrador.")
    elif u['age'] >= 18:
        print ("El usuario " + u['name'] + " es mayor de edad.")
        if u['user_type'] == 1:
            print ("El usuario " + u['name'] + " es administrador.")
    else:
        print ("El usuario " + u['name'] + " es un menor de edad.")
        if u['user_type'] == 1:
            print ("El usuario " + u['name'] + " es administrador.")
# import sys

try: 
    f = open('./ManejoArchivos/myfile.txt')
    s = f.readline()
    i = int(s.strip('x'))
    a = 3 / i
except OSError as err:
    print("OS error: { 0 }".format(err))
except ValueError:
    print("No se puede convertir dato a entero")
except ZeroDivisionError as err:
    print("No se puede dividir entre cero")
except BaseException as err:
    print(f"Inesperado", { err } , { type(err) })
    raise

print(i)
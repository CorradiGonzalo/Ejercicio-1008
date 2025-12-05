import pickle
import os
from register import *
import random
def menu():
    print("1 - Generar un arreglo")
    print("2 - Mostrar todos los datos del arreglo generado")
    print("3 - Determinar  si  existe  un  registro  cuyo  número  de  dni  sea  num  (cargar num  por  teclado). ")
    print("4 - Determinar  el monto acumulado que se pagó  para cada combinación entre tipo de servicio y forma de pago")
    print("5 - Determinar si existe un interno cuyo nombre sea nom")
    print("6 -  Grabar  en  un  archivo  binario  los  datos  de  los  registros  del  arreglo  generado  en  el  punto  1  que  correspondan  a internos  cuyo  tipo  de  servicio  sea  mayor  a  3  y  tengan  un  monto  pagado  superior  al  valor  mon  que  se  carga  por teclado")
    print("7 -  Mostrar el archivo generado.Muestre al final una línea extra indicando la cantidad de registros que se mostraron")
    print("0 - Salir ")


def validar_mayor_que(inf, mensaje):
    n = int(input(mensaje))
    while n < inf:
        print("Error")
        n = int(input(mensaje))
    return n


def add_in_order(v, interno):
    izq, der = 0, len(v)-1
    pos = 0
    while izq <= der:
        c = izq + der // 2
        if v[c].nombre == interno.nombre:
            pos = c
        if v[c].nombre > interno.nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [interno]





def cargar_arreglo(n):
    v = [] * n
    noms = ('Juan', 'Eduardo', 'Pepe', 'Domingo', 'Mundo', 'Leticia', 'Norma', 'Barbara', 'Nora', 'Mariela', 'Claudia')
    for i in range(n):
        dni = random.randint(10000,58000)
        nombre = random.choice(noms) + str(i)
        servicio = random.randint(0, 5)
        pago = random.randint(0, 4)
        edad = random.randint(60, 100)
        cobro = random.randint(60000, 150000)
        interno = Interno(dni, nombre, servicio, pago, edad, cobro)
        add_in_order(v, interno)
    return v


def guardar_v(v, fd):
    if os.path.exists(fd):
        m = open(fd, 'at')
        for i in range(len(v)):
            pickle.dump(m, v[i])
        m.close()
        print("El CSV ya existia, se agregaron los elementos nuevos.")
    else:
        m = open(fd, 'wt')
        for i in range(len(v)):
            pickle.dump(m, v[i])
        m.close()
        print("El CSV fue creado.")




def main():
    op = -1
    while op != 0:
        fd = 'Internos.csv'
        menu()
        op = int(input("Ingrese una opcion:"))
        if op == 1:
            n = validar_mayor_que(0, 'Ingrese la cantidad de internos a cargar:')
            v = cargar_arreglo(n)
            print("Vector generado.")
            guardar_v(v, fd)
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 0:
            print("Hasta luego")



if __name__ == "__main__":
    main()
        
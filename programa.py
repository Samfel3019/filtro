#SAMUEL FELIPE RODRIGUEZ RUBIO
#FILTRO CICLO 1 

import json
import os

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

def cargar_datos():
    try:
        with open('manuales.json', 'r', encoding="utf-8") as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return {"manuales": {}} 

def guardar_datos(datos):
    with open('manuales.json', 'w', encoding="utf-8") as file:
        json.dump(datos, file, indent=4)

def crear(datos):
    manual = input("Ingrese nombre del manual: ")
    while not manual:
        msgError("No puede ser vacío")
        manual = input("Ingrese nombre del manual: ")

    autor = input("Ingrese nombre del autor: ")
    while not autor:
        msgError("No puede ser vacío")
        autor = input("Ingrese nombre del autor: ")

    paginas = None
    while paginas is None:
        try:
            paginas = int(input("Número de páginas: "))
        except ValueError:
            msgError("Debe ser un número válido")

    temas = None
    while temas is None:
        try:
            temas = int(input("Número de temas a agregar: "))
        except ValueError:
            msgError("Debe ser un número válido")

    temas_lista = []
    for i in range(temas):
        titulo = input(f"Ingrese el titulo del tema{i+1}: ")
        while not titulo:
            msgError("Debe ser un titulo válido")
            titulo = input(f"Ingrese el titulo del tema{i+1}: ")
        clasificacion = None
        if clasificacion <= 3:
            while clasificacion is None:
                try:
                    clasificacion = int(input(f"Clasificación del tema {i+1} (1 a 3): "))
                except ValueError:
                    msgError("Debe ser un número válido")

        temas_lista.append({"Titulo": titulo, "Clasificacion": clasificacion})

    datos["manuales"][manual]={
        "author": autor,
        "paginas": paginas,
        "temas": temas_lista
    }
    guardar_datos(datos)
    os.system("clear")
    print("================================")
    print(" MANUAL CREADO CORRECTAMENTE :) ")
    print("================================")

def modificar(datos):
    listar(datos)
    while True:
        encontrado = False
        manual = input("Ingrese el nombre del manual: ")
        if manual in datos["manuales"]:
            encontrado = True
            titulo = input("Ingrese el titulo del tema a modificar: ")
            for tema in datos["manuales"][manual]["temas"]:
                if tema["titulo"] == titulo:
                    encontrado = True
                    clasificacion = int(input("Nueva actualización del tema: "))
                    tema["clasificacion"] = clasificacion
                    guardar_datos(datos)
                    print("==================================")
                    print(" TEMA MODIFICADO CORRECTAMENTE :)")
                    print("==================================")
                    return
                msgError("El titulo del tema no fue encontrado en el manual.")
            if not encontrado:
                msgError("Manual no encontrado.")
            else:
                break

def eliminar(datos):
    listar(datos)
    while True:
        encontrado= False
        manual = input("Digite el nombre del manual: ")
        if manual in datos["manuales"]:
            encontrado = True
            titulo = input("Digite el título del tema a eliminar: ")
            for tema in datos["manuales"][manual]["temas"]:
                if tema["Titulo"] == titulo:
                    datos["manuales"][manual]["temas"].remove(tema)
                    guardar_datos(datos)
                    os.system("clear")
                    print("=================================")
                    print(" TEMA ELIMINADO CORRECTAMENTE :) ")
                    print("=================================")
                    return
            msgError("El título del tema no fue encontrado en el manual.")
        if not encontrado:
            msgError("El manual no fue encontrado")
        else:
            break

def listar():
    print("Nombre del manual","Autor","Páginas","Temas")
    print("titulo","clasificación")
    print("="*50)
    for manual, info in guardar_datos["manuales"].items():
        autor = info["author"]
        paginas = info["paginas"]
        for tema in info["temas"]:
            titulo = tema["titulo"]
            clasificacion = tema["clasificacion"]
            print("manual, autor, paginas, titulo, clasificacion")

def generarTxt():
    datos = cargar_datos
    res = ""
    for lenguage in datos["manuales"].keys():
        c1, c2, c3=0, 0, 0
        res += f"Manual {lenguage}: \n"
        if "temas" in datos["manuales"][lenguage]:
            for tema in datos["manuales"][lenguage]["temas"]:
                if tema["clasificacion"] == 1:
                    c1 += 1
                if tema["clasificacion"] == 2:
                    c2 += 1
                if tema["clasificacion"] == 3:
                    c3 += 1
        res +=f"***Temas Básicos: {c1}*** Temas intermedios: {c2}*** Temas avanzados: {c3}***"
    with open("datos.txt","w",encoding="utf-8") as file:
        file.write(res)
    print("===================================")
    print(" ARCHIVO GENERADO CORRECTAMENTE :)")
    print("===================================")

def menu():
    while True:
        try:
            print("\n\n***** SISTEMA GESTOR DE LIBROS *****")
            print("                            ")
            print("======= MENÚ PRINCIPAL =======")
            print("                            ")
            print("1. Crear")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Listar")
            print("5. Generar informe de datos.txt")
            print("6. Salir")
            op = int(input("\t>>> Escoja una opción (1-6): "))
            if op < 1 or op > 6:
                msgError("Error. Opción Inválida (de 1 a 6).")
                continue
            return op
        except ValueError:
            msgError("Error. Opción Inválida (de 1 a 6).")
            continue

def main():
    os.system("clear")
    datos = cargar_datos()
    while True:
        op = menu()
        if op == 1:
            os.system("clear")
            crear(datos)
        elif op == 2:
            modificar(datos)
        elif op == 3:
            eliminar(datos)
        elif op == 4:
            listar(datos)
        elif op == 5:
            generarTxt(datos)
        elif op == 6:
            salir = input("¿Está seguro que desea salir? (SI/NO): ")
            if salir.upper() == "SI":
                print("\nGracias por usar el programa... Adiós...\n".center(80))
                break
            elif salir.upper() == "NO":
                continue
            else:
                msgError("Error. Digite una opción válida.")
                continue

main()
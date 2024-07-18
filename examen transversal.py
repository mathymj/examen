import random
import csv
from statistics import geometric_mean

# Lista de los trabajadores de la empresa
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

salarios = []

#este codigo asigna aleatoriamente los sueldos con el metodo random
def asignar_sueldos_aleatorios():
    global salarios
    salarios = [random.randint(300000, 2500000) for x in range(10)]
    print("Sueldos asignados aleatoriamente.")

# Funcion para clasificar los sueldos de cada trabajador para almacenarlos en una lista segun su rango salarial.
def clasificar_sueldos():
    print("Clasificación de Sueldos:")
    bajo_800k = []
    entre_800k_y_2m = []
    sobre_2m = []
    
    for i in range(len(trabajadores)):
        nombre = trabajadores[i]
        sueldo = salarios[i]
        
        if sueldo < 800000:
            bajo_800k.append((nombre, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800k_y_2m.append((nombre, sueldo))
        else:
            sobre_2m.append((nombre, sueldo))
    
    print(f"Sueldos menores a $800.000 TOTAL: {len(bajo_800k)}")
    for nombre, sueldo in bajo_800k:
        print(f"{nombre} ${sueldo}")
    
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(entre_800k_y_2m)}")
    for nombre, sueldo in entre_800k_y_2m:
        print(f"{nombre} ${sueldo}")
    
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(sobre_2m)}")
    for nombre, sueldo in sobre_2m:
        print(f"{nombre} ${sueldo}")
    
    total_sueldos = sum(salarios)
    print(f"TOTAL SUELDOS: ${total_sueldos}.")


#ver estadisticas de los salrios de los trabajadores
def ver_estadisticas():
    if not salarios:
        print("Primero debe asignar sueldos aleatorios.")
        return
    
    sueldo_maximo = max(salarios)
    sueldo_minimo = min(salarios)
    promedio_sueldos = sum(salarios) / len(salarios)
    media_geometrica = geometric_mean(sueldo_maximo,sueldo_minimo,promedio_sueldos)
    
    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica: ${media_geometrica:.2f}")


#reporte del salario mediante archivo csv
def reporte_de_sueldos():
    if not salarios:
        print("Primero debe asignar sueldos aleatorios.")
        return
    
    filename = "reporte_sueldos.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for i in range(len(trabajadores)):
            nombre = trabajadores[i]
            sueldo_base = salarios[i]
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            
            writer.writerow([nombre, sueldo_base, desc_salud, desc_afp, sueldo_liquido])
    
    print(f"Reporte de sueldos generado en '{filename}'.")

def main():
    print("Bienvenido al sistema de análisis de sueldos")
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_de_sueldos()
        elif opcion == '5':
            print("Finalizando programa...")
            print("Desarrollado por Carlos Vergara\nRUT 12.345.678-9")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    main()
"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
#Vicmara

import temperatura
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] Calcular Celsius a Fahrenheit")
        print("[2] Calcular Celsius a Kelvin")
        print("[3] Calcular Fahrenheit a Celsius")
        print("[4] Calcular Fahrenheit a Kelvin")
        print("[5] Calcular Kelvin a Celsius")
        print("[6] Calcular Kelvin a Fahrenheit")
        print("[7] Calcular Kilogramos (kg) a Gramos (g)")
        print("[8] Calcular Kilogramos (kg) Toneladas (t)")
        print("[9] Calcular Gramos (g) a Kilogramos (kg)")
        print("[10] Calcular Gramos (g) a Toneladas (t)")
        print("[11] Calcular Toneladas (t) a Kilogramos (kg)")
        print("[12] Calcular Toneladas (t) a Gramos (g)")
        print("[13] Calcular Segundos a Minutos")
        print("[14] Calcular Segundos a Horas ")
        print("[15] Calcular Minutos a Segundos ")
        print("[16] Calcular Minutos a Horas ")
        print("[17] Calcular Horas a Segundos  ")
        print("[18] Calcular Horas a Minutos ")
        
        print("[0] Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valor_inicial=int(input("ingrese valor inicial"))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                resultado = temperatura.celsius_a_fahrenheit(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 2:
                resultado = temperatura.celsius_a_kelvin(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 3:
                resultado = temperatura.fahrenheit_a_celsius(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 4:
                resultado = temperatura.fahrenheit_a_kelvin(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 5:
                resultado = temperatura.kelvin_a_celsius(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 6:
                resultado = temperatura.kelvin_a_fahrenheit(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 7:
                resultado = masa.Kilogramos_a_Gramos (valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 8:
                resultado = masa.Kilogramos_a_Toneladas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 9:
                resultado = masa.gramos_a_kilogramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 10:
                resultado = masa.gramos_a_toneladas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 11:
                resultado = masa.tonelada_a_kilogramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 12:
                resultado = masa.tonelada_a_gramos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 13:
                resultado = tiempo.segundos_a_Minutos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 14:
                resultado = tiempo.Segundos_a_Horas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 15:
                resultado = tiempo.Minutos_a_Segundos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 16:
                resultado = tiempo.Minutos_a_Horas(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 17:
                resultado = tiempo.Horas_a_Segundos(valor_inicial)
                print("el resultado es: ", resultado)
            elif opcion == 18:
                resultado = tiempo.Horas_a_Minutos(valor_inicial)
                print("el resultado es: ", resultado)

                
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()
    #https://github.com/VicmaraRios/conversor_de_unidades.git

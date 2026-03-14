"""
Generador de Arte ASCII Animado
Proyecto de Animación

Equipo:
- Estudiante 1: [Nombre] - Menú y Patrones Geométricos
- Estudiante 2: [Nombre] - Generadores de Texto Artístico
- Estudiante 3: [Nombre] - Animaciones

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================

import os


def mostrar_menu_principal():
    """Muestra el menú de la galería de arte ASCII"""
    print("\n" + "="*60)
    print("     🎨 GALERÍA DE ARTE ASCII v1.0 🎨")
    print("     Creado por: [Nombres del equipo]")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Salir")
    print("-"*60)


# ============================================
# SECCIÓN 2: PATRONES GEOMÉTRICOS (Estudiante 1)
# ============================================

def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada.
    """
    for i in range(1, altura + 1):
        print('*' * i)


def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.
    """
    if lado < 2:
        print("Error: El tamaño mínimo debe ser 2")
        return

    for i in range(lado):
        if i == 0 or i == lado - 1:
            print('*' * lado)
        else:
            print('*' + ' ' * (lado - 2) + '*')


def piramide(altura):
    """
    Genera una pirámide centrada de altura especificada.
    """
    for i in range(altura):
        espacios = ' ' * (altura - i - 1)
        estrellas = '*' * (2 * i + 1)
        print(espacios + estrellas)


def menu_patrones():
    """Menú para seleccionar patrones geométricos"""
    while True:
        limpiar_pantalla_simple()
        print("\n--- PATRONES GEOMÉTRICOS ---")
        print("1. Triángulo")
        print("2. Cuadrado")
        print("3. Pirámide")
        print("4. Volver al menú principal")

        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "4":
            break
        
        if opcion in ["1", "2", "3"]:
            try:
                tamano = int(input("Ingrese el tamaño/altura del patrón: "))
                print("\nResultado:\n")
                
                if opcion == "1":
                    triangulo(tamano)
                elif opcion == "2":
                    cuadrado(tamano)
                elif opcion == "3":
                    piramide(tamano)
                
                pausar()
            except ValueError:
                print("\n❌ Error: Por favor, ingrese un número entero válido.")
                pausar()
        else:
            print("\n❌ Opción inválida.")
            pausar()
            
# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    """
    Genera un banner con el texto ingresado.
    """
    ancho = len(texto) + 8
    print("╔" + "═" * ancho + "╗")
    print("║" + " " * ancho + "║")
    print(f"║    {texto.upper()}    ║")
    print("║" + " " * ancho + "║")
    print("╚" + "═" * ancho + "╝")

def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.
    """
    # designacion de simbolo por cada estilo
    if estilo == 2:
        simbolo = "★"
    elif estilo == 3:
        simbolo = "@"
    else:
        simbolo = "*" 
    borde = simbolo * (len(texto) + 4)
    print(borde)
    print(f"{simbolo} {texto} {simbolo}")
    print(borde


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.
    """
    titulo = f" TABLA DEL {numero} "
    print("╔" + "═" * 20 + "╗")
    print(f"║{titulo:^20}║")
    print("╠" + "═" * 20 + "╣")
    
    for i in range(1, 11):
        resultado = numero * i
        # Usamos f-strings para alinear los números ( :2d es para 2 dígitos )
        linea = f"{numero} x {i:2d} = {resultado:2d}"
        print(f"║  {linea:^16}  ║")
        
    print("╚" + "═" * 20 + "╝")


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    while True:
        limpiar_pantalla_simple()
        print("\n--- GENERADORES DE TEXTO ---")
        print("1. Crear Banner")
        print("2. Marco Decorativo")
        print("3. Tabla de Multiplicar")
        print("4. Volver al menú principal")

        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            texto = input("Ingrese el texto para el banner: ")
            generar_banner(texto)
            pausar()
        elif opcion == "2":
            texto = input("Ingrese el texto a enmarcar: ")
            print("Estilos: 1 (*), 2 (★), 3 (@)")
            try:
                est = int(input("Seleccione estilo (1-3): "))
                marco_decorativo(texto, est)
            except ValueError:
                print("Entrada no válida, usando estilo por defecto.")
                marco_decorativo(texto, 1)
            pausar()
        elif opcion == "3":
            try:
                num = int(input("¿De qué número quieres la tabla? (1-10): "))
                tabla_multiplicar_visual(num)
            except ValueError:
                print("Por favor, ingresa un número válido.")
            pausar()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")
            pausar()

# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """Crea un retraso usando un loop vacío (sin importar time)"""
    for _ in range(duracion * 1000000):
        pass
    
def barra_progreso():
    """Muestra una barra de progreso animada."""
    print("\nProcesando arte...")
    for i in range(0, 101, 5):
        relleno = "■" * (i // 5)
        vacio = "-" * (20 - (i // 5))
        # Requisito: usar \r para sobrescribir
        print(f"\r[{relleno}{vacio}] {i}%", end="", flush=True)
        crear_retraso(2)
    print("¡Completo!")

def animacion_texto_movil(texto="STARS"):
    """Anima un texto moviéndose de izquierda a derecha."""
    print("\nPresione Ctrl+C para detener o espere a que termine...")
    try:
        for i in range(30):
            espacios = " " * i
            print(f"\r{espacios}☆ {texto} ☆", end="", flush=True)
            crear_retraso(1)
        print("\nAnimación finalizada.")
    except KeyboardInterrupt:
        print("\nAnimación interrumpida.")

def animar_barra_progreso():
    """Animación de barra de progreso simple."""
    import sys
    print("\nBarra de progreso:")
    for i in range(31):
        barra = '[' + '#' * i + ' ' * (30 - i) + ']'
        porcentaje = int((i / 30) * 100)
        print(f"\r{barra} {porcentaje}%", end="", flush=True)
        crear_retraso(1)
    print("\n¡Progreso completo!")

def menu_animaciones():
    """Menú para animaciones"""
    while True:
        limpiar_pantalla_simple()
        print("\n--- SECCIÓN DE ANIMACIONES ---")
        print("1. Barra de Progreso")
        print("2. Texto en Movimiento")
        print("3. Volver al menú principal")
        
        opcion = input("\nSeleccione (1-3): ")
        if opcion == "1":
            animar_barra_progreso()
            pausar()
        elif opcion == "2":
            txt = input("Texto a animar: ")
            animacion_texto_movil(txt)
            pausar()
        elif opcion == "3":
            break
# ============================================
# FUNCIONES AUXILIARES
# ============================================

def limpiar_pantalla_simple():
    """Imprime líneas en blanco para simular limpieza de pantalla"""
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ¡Bienvenido a la Galería de Arte ASCII!         ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación  ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_patrones()
        elif opcion == "2":
            print("\n--- GENERADOR DE BANNER ---")
            # TODO: Solicitar texto y generar banner
            pass
        elif opcion == "3":
            menu_texto_artistico()
        elif opcion == "4":
            menu_animaciones()
        elif opcion == "5":
            print("\n--- TABLA DE MULTIPLICAR VISUAL ---")
            # TODO: Solicitar número y generar tabla
            pass
        elif opcion == "6":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: [Nombres del equipo]")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

        if continuar and opcion != "6":
            pausar()

    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

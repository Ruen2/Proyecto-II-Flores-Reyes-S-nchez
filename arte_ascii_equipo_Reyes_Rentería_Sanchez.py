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

    Args:
        texto (str): Texto a enmarcar
        estilo (int): Tipo de estilo (1, 2, o 3)
    """
    # TODO: Implementar diferentes estilos de marcos
    # Estilo 1: Simple con ═ ║
    # Estilo 2: Doble con bordes decorativos
    # Estilo 3: Con asteriscos o caracteres especiales

    # Caracteres útiles:
    # ═ ║ ╔ ╗ ╚ ╝ (estilo 1)
    # ★ ☆ (estilo 2)
    # * # @ (estilo 3)

    pass  # Reemplazar con su código


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.

    Args:
        numero (int): Número para generar la tabla (1-10)
    """
    # TODO: Implementar tabla decorada
    # - Crear encabezado decorativo
    # - Generar tabla del 1 al 10
    # - Alinear números correctamente
    # - Cerrar con pie decorativo

    # Ejemplo:
    # ╔════════════════════════╗
    # ║  TABLA DEL 5           ║
    # ╠════════════════════════╣
    # ║  5 x  1 =  5           ║
    # ║  5 x  2 = 10           ║
    # ║  ...                   ║
    # ╚════════════════════════╝

    pass  # Reemplazar con su código


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    print("\n--- GENERADORES DE TEXTO ---")
    print("1. Crear Banner")
    print("2. Marco Decorativo")
    print("3. Tabla de Multiplicar")
    print("4. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    # TODO: Implementar retraso
    # Usar un loop for que no haga nada
    # Ejemplo: for _ in range(duracion * 100000):
    #              pass

    pass  # Reemplazar con su código


def barra_progreso():
    """Muestra una barra de progreso animada"""
    # TODO: Implementar barra de progreso
    # - Usar un loop de 0 a 100
    # - En cada iteración, mostrar la barra actualizada
    # - Usar caracteres como █ ■ o # para la barra llena
    # - Usar - o espacio para la parte vacía
    # - Mostrar el porcentaje

    # Ejemplo de salida:
    # Procesando...
    # [■■■■■■■■■■----------] 50%
    # [■■■■■■■■■■■■■■■■----] 80%
    # [■■■■■■■■■■■■■■■■■■■■] 100% ¡Completo!

    # Pista: usar end="\r" en print para sobrescribir la misma línea

    pass  # Reemplazar con su código


def animacion_texto_movil():
    """Anima un texto moviéndose de izquierda a derecha"""
    # TODO: Implementar animación de texto
    # - Definir el texto a animar
    # - Usar un loop para cada posición
    # - En cada iteración, imprimir espacios + texto
    # - Incrementar los espacios para simular movimiento
    # - Limpiar la línea anterior con \r

    # Ejemplo:
    # ☆                (frame 1)
    #  ☆               (frame 2)
    #   ☆              (frame 3)
    # ...

    pass  # Reemplazar con su código


def menu_animaciones():
    """Menú para animaciones"""
    print("\n--- ANIMACIONES ---")
    print("1. Barra de Progreso")
    print("2. Texto en Movimiento")
    print("3. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


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

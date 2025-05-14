#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.

def convert_dicc(cadena):
    diccionario = {}
    for c in cadena:
        if c != " ":
            if c in diccionario:
                diccionario[c] += 1
            else:
                diccionario[c] = 1
    return diccionario
 
#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble(num):
    numero=num*2
    return numero

numeros=[1,2,3,4,5]
resultado_map=map(doble,numeros)
print(list(resultado_map))

#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def objetivo(list_palabras, palabra_obj):
    nuevalista=[]
    for elemento in list_palabras: 
     if palabra_obj in elemento:
         nuevalista.append(elemento)
    return nuevalista

#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def resta(a, b):
    return a - b

def diferencias(lista1, lista2):
    return list(map(resta, lista1, lista2))

#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado

def funcion(lista,nota_aprobado):
    estado=""
    media=sum(lista)/len(lista)
    if media >= nota_aprobado:
        estado="aprobado"
    else:
        estado="suspenso"
    return (media,estado)

#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: " ".join(tupla), lista_tuplas))

#8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
#indicando si la división fue exitosa o no.

def division(num1, num2):
    try:
        resultado = num1 / num2
        print("División exitosa")
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Solo se pueden dividir números.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return "División no exitosa"

#9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
#"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

#10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
#excepción personalizada y maneja el error adecuadamente.

def promedio(l):
    if len(l)==0:
        return 'lista vacia'
    else:
        return sum(l)/len(l)
    
#11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
#valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
#adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            print("Error: La edad debe estar entre 0 y 120.")
        else:
            print(f"Edad válida: {edad} años")
    except ValueError:
        print("Error: Debes ingresar un número entero.")

#12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud(frase):
    palabras = frase.split()
    return list(map(len, palabras))

#13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def mayusculas_minusculas(conjunto):
    # Convertir el conjunto a una lista sin duplicados
    conjunto = set(conjunto)  # Usamos un set para eliminar duplicados
    # Usamos map para crear las tuplas de mayúscula y minúscula
    return list(map(lambda letra: (letra.upper(), letra.lower()), conjunto))

#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
#función filter()

def palabras_que_comienzan_con(letra, lista_palabras):
    return list(filter(lambda palabra: palabra[0].lower() == letra.lower(), lista_palabras))

#15. Crea una función lambda que sume 3 a cada número de una lista dada.

funcion_lambda=lambda lista:[elem+3 for elem in lista]


#16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
#todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas(texto, n):
    # Dividimos el texto en palabras
    palabras = texto.split()
    # Filtramos las palabras cuyo tamaño es mayor que n
    palabras_filtradas = list(filter(lambda palabra: len(palabra) > n, palabras))
    return palabras_filtradas


#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
#corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

#18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
#(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
#90. Usa la función filter()

def filtrar_estudiantes(estudiantes):
    return list(filter(lambda estudiante: estudiante['calificación'] >= 90, estudiantes))
    

#19. Crea una función lambda que filtre los números impares de una lista dada.

resultado_lambda=lambda lista: [elem for elem in lista if elem % 2 !=0]

#20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
#filter()

solo_enteros = list(filter(lambda x: type(x) == int, lista))

#21. Crea una función que calcule el cubo de un número dado mediante una función lambda
cubo = lambda x: x**3

#22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
from functools import reduce

def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)

#23. Concatena una lista de palabras.Usa la función reduce() .

from functools import reduce

def concatenar_palabras(lista):
    return reduce(lambda x, y: x + y, lista)

#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

from functools import reduce

def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)

#25. Crea una función que cuente el número de caracteres en una cadena de texto dada

def contar(cadena):
    lista_palabras=cadena.split()
    return len(lista_palabras)

#26. Crea una función lambda que calcule el resto de la división entre dos números dados.
funcion_lambda=lambda x,y: x%y

#27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    return sum(lista)/len(lista)

#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    for i in range(len(lista)):
        if lista[i] in lista[:i]:
            return lista[i]
    return None

#29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
#carácter '#', excepto los últimos cuatro.


def enmascarar(valor):
    valor = str(valor)
    return "#" * (len(valor) - 4) + valor[-4:]

#30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#pero en diferente orden.

def anagramas(p1, p2):
    return sorted(p1) == sorted(p2)

#31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
#esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#lanza una excepción.

def buscar():
    nombres = input("Nombres separados por coma: ").split(",")
    nombre = input("Nombre a buscar: ")
    if nombre in nombres:
        print("Nombre encontrado.")
    else:
        print("Nombre NO encontrado."

#32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
#devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
#no trabaja aquí.

def buscar_empleado(nombre, lista):
    for e in lista:
        if e["nombre"] == nombre:
            return e["puesto"]
    return "No trabaja aquí."

#33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

"""
34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
Código a seguir:
1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
6. Implementar el método 
info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
mismas.
Caso de uso:
1. Crear un árbol.
2. Hacer crecer el tronco del árbol una unidad.
3. Añadir una nueva rama al árbol.
4. Hacer crecer todas las ramas del árbol una unidad.
5. Añadir dos nuevas ramas al árbol.
6. Retirar la rama situada en la posición 2.
7. Obtener información sobre el árbol.
"""

class Arbol:
    def __init__(self,tronco,ramas):
        self.tronco=1
        self.ramas=[]
    
    def crecer_tronco(self):
        self.tronco=self.tronco+1

    def nueva_rama(self):
      self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
    
    def quitar_rama(self,posicion):
        self.ramas.pop(posicion)
    
    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
    
""""
    36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
PROYECTO LÓGICA: Katas de Python 3
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".

"""

class UsuarioBanco:
    def __init__(self,nombre,saldo,cuenta):
        self.nombre=nombre
        self.saldo=saldo
        self.cuenta=cuenta # True o False indica si tiene cuenta corriente

    
       def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para retirar {cantidad} unidades.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad} unidades.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad < 0:
            raise ValueError("No se puede agregar una cantidad negativa.")
        self.saldo += cantidad

""""
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , 
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto .
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
"""

def contar_palabras(texto):
    conteo={}
    palabras=texto.split()
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    resultado = []
    for p in palabras:
        if p != palabra:
            resultado.append(p)
    return ' '.join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para reemplazar, se necesitan palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para eliminar, se necesita solo una palabra.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")

#38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
    
from datetime import datetime

# Obtener la hora actual del sistema
hora_actual = datetime.now().hour

# Determinar si es de día, tarde o noche
if 6 <= hora_actual < 12:
    print("Es de día.")
elif 12 <= hora_actual < 18:
    print("Es de tarde.")
elif 18 <= hora_actual < 24 or 0 <= hora_actual < 6:
    print("Es de noche.")


"""
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
"""    

# Pedir al usuario que ingrese la calificación numérica
calificacion = int(input("Introduce la calificación numérica del alumno (0-100): "))

# Determinar la calificación en texto
if calificacion < 70:
    print("Insuficiente")
elif calificacion < 80:
    print("Bien")
elif calificacion < 90:
    print("Muy bien")
else:
    print("Excelente")


#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o 
#"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        return datos[0] * datos[1]  # base * altura
    elif figura == "circulo":
        return math.pi * datos[0] ** 2  # pi * radio^2
    elif figura == "triangulo":
        return 0.5 * datos[0] * datos[1]  # 0.5 * base * altura
    else:
        return "Figura no válida"

""""
41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python
"""

# Solicitar el precio original
precio = float(input("Introduce el precio original del artículo: "))

# Preguntar si tiene cupón
tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

# Si tiene cupón, pedir el valor del descuento
if tiene_cupon == "sí":
    descuento = float(input("Introduce el valor del cupón de descuento: "))
    if descuento > 0:
        precio -= descuento  # Aplicar el descuento directamente

# Mostrar el precio final
print(f"El precio final de la compra es: {precio}€")
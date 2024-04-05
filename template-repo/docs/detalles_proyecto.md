# Nombre del Proyecto: Count A,T,C,G

Fecha: 21 de marzo del 2024

**Participantes**:

- Erika Ordoñez erikaog@lcg.unam.mx

## Descripción del Problema

Es un programa al que se le va a pasar un archivo con una secuencia y va a leer la de ATCG.


## Especificación de Requisitos

Requisitos funcionales

- Requisito: Archivo llamado 'sequence.txt'



## Análisis y Diseño

Para el análisis de datos, se toman en cuenta únicamente las letras en mayúsculas, debido a que la maypr parte de los archivos que contienen secuencias, contienen este formato. El programa únicamente recibirá archivos con el nombre 'sequence.txt', de no ingresar el archivo correcto, se muestra un mensaje en pantalla aclarando al usuario como debe llamar al archivo. Todo esto para finalmente imprimir a pantalla el conteo de nucleótidos en el archivo. 



```
# Logica del código

# Recibe el archivo que debe estar nombrado como 'sequence.txt'.
try: 

    with open('sequence.txt', 'r') as file:

# Lee todas las líneas del archivo. 
        sequence = file.read()         

# De no ser correcto, se imprime un mensaje de error al usuario.
except:
    print("El archivo ingresado no es el correcto, favor de renombrar")

# Cuenta los hallazgos encontrados.
count_A = sequence.count('A')
count_T = sequence.count('T')
count_G = sequence.count('G')
count_C = sequence.count('C') 

# Imprime a pantalla los resultados del conteo. 
print("Número de A's:", count_A)
print("Número de T's:", count_T)
print("Número de G's:", count_G)
print("Número de C's:", count_C)
```

Formato .txt del archivo input que recibe el programa, contará e imprimirá en pantalla la cantidad de As, Ts, Gs y Cs que se encuentran en el archivo, siempre que los nucleótidos estén en mayúsculas.


#### Caso de uso: Sumar contenido de nucleótidos. 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada nombrado como 'sequence.txt'.
                 v
         +-------+-------+
         |Contar los     |
         |nucleótidos    |
         |imprime la     |
         |cantidad       |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada llamado 'sequence.txt' y se contará el contenido de nucleótidos en el siempre que estén en mayúsculas.
- **Flujo principal**:

	1. El programa recibe el archivo de texto.
	2. Se crean contadores que registran los nucleótidos a medida que se encuentran.
	3. Se imprime en pantalla la cantidad total de cada nucleótido. 
	
- **Flujos alternativos**:
	- Si no se proporciona un archivo o si este no es el correcto, entonces el programa no trabajará y proporcionará un mensaje de error.
        - Si los nucleótidos contenidos en el archivo no están en mayúsculas entonces no se contrarán.                


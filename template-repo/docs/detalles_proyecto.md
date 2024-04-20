# Nombre del Proyecto: Count A,T,C,G

Fecha: 21 de marzo del 2024
Actualización: 20 de abril del 2024

**Participantes**:

- Erika Ordoñez erikaog@lcg.unam.mx

## Descripción del Problema

Es un programa al que se le va a pasar un archivo con una secuencia y va a leer la de ATCG.


## Especificación de Requisitos

Requisitos funcionales

- Requisito 1: Un archivo que contenga la secuencia de DNA a analizar. 

- Requisito 2: Al ingresar el archivo, deberá copiar la ruta absoluta del mismo para que el programa pueda encontrarlo.  

Requisitos no funcionales

- Requisito 1: Especificar la secuencia a analizar del archivo. 



## Análisis y Diseño

Para el análisis de datos, se toman en cuenta únicamente las letras ingresadas, ya sean estas mayúsculas o minúsculas, incluso letras que no correspondan a nucleótidos. El programa con la función 'upper' busca transformar todas las letras ingresadas por mayúsculas, además se creó un contador que de ingresar letras que no contenga el archivo, el contador no avanzará del número cero y por tanto imprime en pantalla un mensaje de error. El programa recibe archivos con cualquier nombre que exista, las únicas condiciones son que el archivo debe existir y se deberá ingresar la ruta absoluta del mismo para que el programa lo encuentre. En caso de no ser encontrado o que esté vacío, el programa imprimirá en pantalla dos mensajes de error respectivamente. Todo esto para finalmente imprimir a pantalla el conteo de nucleótidos en el archivo. 



```
# Logica del código

1. Recibe el archivo que debe estar en el dispositivo, aclarando la ruta absoluta del mismo. De no ser así, entonces imprime un mensaje de error. 
2. En caso de recibir un archivo vacío el programa también imprime a pantalla un mensaje de error. 
3. En caso contrario, comienza a contar las ocurrencias de nucleótidos: 
        3.1 Recibe, si el usuario lo desea, una secuencia definida para encontrarse en el archivo a analizar.
        3.2 De no recibir la especificación de las secuencias, enntonces el programa toma todo el archivo para analizar. 
        3.3 En caso de recibir allguna letra que no sea un nucleótido, el programa imprime un mensaje de error. 
        3.4 Puede buscar ocurrencias de una letra o muchas. 
```

Formato del archivo input que recibe el programa, contará e imprimirá en pantalla la cantidad de As, Ts, Gs y Cs que se encuentran en el archivo, siempre que los nucleótidos estén en el archivo y este no se encuentra vacío.


#### Caso de uso: Sumar contenido de nucleótidos. 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada 
                 |aclarando su ruta absoluta.
                 |2. (opcional) Especifica la    
                 |secuencia de nucleótidos a buscar. 
                 |
                 v
         +-------+-------+
         |Contar los     |
         |nucleótidos    |
         |imprime la     |
         |cantidad       |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada y se contará el contenido de nucleótidos en el siempre que se encuentren en el archivo.
- **Flujo principal**:

	1. El programa recibe el archivo.
	2. Se crean contadores que registran los nucleótidos a medida que se encuentran.
	3. Se imprime en pantalla la cantidad total de cada nucleótido. 
	
- **Flujos alternativos**:
	- Si no se proporciona un archivo o si este no es el correcto, entonces el programa proporcionará un mensaje de error.
        - Si los nucleótidos contenidos en el archivo no están, es decir, si el archivo está vacío o las letras especificadas no se encuentran.                


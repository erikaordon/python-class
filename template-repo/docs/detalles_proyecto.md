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





```
# Logica del código
```

Formato .txt del archivo input que recibe el programa, contará e imprimirá en pantalla la cantidad de As, Ts, Gs y Cs que se encuentran en el archivo, siempre que los nucleótidos estén en mayúsculas.


#### Caso de uso: Sumar contenido de nucleótidos. 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada/ o parámetros en la terminal
                 v
         +-------+-------+
         |   Programa    |
         |               |
         |               |
         |		 |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El actor proporciona un archivo de entrada con terminación .txt y se contará el contenido de nucleótidos en el siempre que estén en mayúsculas.
- **Flujo principal**:

	1. El programa recibe el archivo de texto.
	2. Se crean contadores que registran los nucleótidos a medida que se encuentran.
	3. Se imprime en pantalla la cantidad total de cada nucleótido. 
	
- **Flujos alternativos**:
	- Si no se proporciona un archivo o si este no es el correcto, entonces el programa no trabajará.
        - Si los nucleótidos contenidos en el archivo no están en mayúsculas entonces no se contrarán.                


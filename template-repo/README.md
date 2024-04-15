
# Conteo de nucleotidos

El código recibe un archivo que contiene una secuencia de nucleótidos. Si el nombre no es correcto, entonces imprime un mensaje de error. Se parsea el documento ingresado, recibiendo del usuario dos argumentos, el archivo y los nucleótidos que sea contar, en caso de no especificar los nucleótidos, el programa imprime en pantalla el conteo de todos los nucleótidos del archivo. 

## Uso

El script acepta dos argumentos, el nombre del archivo a leer y el(los) nucleótidos a conta. El programa está diseñado para que el usuario ingrese cualquier archivo de su preferencia, en el formato que sea, sin embargo, deberá ingresar un archivo existente o que se encuentre en la carpeta especificada, de otro modo se imprimirá un mensaje de error. Además, recibe otro argumento en el que se espeficica el o los nucleótidos de los que se desea obtener su frecuencia. El código recibe más de un nucleótido que puede ser en mayúscula o minúscula. En caso de que el usuario no espeficique nucléotido, el programa imprime en pantalla todas las frecuencias de nucleótidos en el archivo. 

```
python conteo_nucleotidos.py [archivo] 
```


donde `[archivo]` es el nombre del archivo que contiene la secuencia de nucleótidos, que puede ser cualquiera, siempre que se encuentre en la carpeta establecida o que exista en el dispositivo.

```
Python conteo_nucleotidos.py [archivo] -n[nucleotido(s)]
```
```
Python conteo_nucleotidos.py [archivo] -nucleotido[nucleotido(s)]
```
donde `-n[nucleotido(s)]` o `-nucleotido[nucleotido(s)]` se refiere a las maneras en que se puede especificar en el programa los nucleótidos a contar, en esta opción se pueden especificar los nucleótidos tanto en mayúscula como en minúscula. Se puede no especificar el nucleótido y el programa regresará la frecuencia de todos los nucelótidos disponibles en el archivo. 



## Salida

Se imprime la cantidad de cada nucleótido, ya sea A, T, C o G. 

## Control de errores

Si el archivo correcto no fue escrito de la manera adecuada, el archivo no existe en el dispositivo o no fue ingresada de manera correcta el path, entonces imprimirá en pantalla  un mensaje de error. 

## Pruebas

El script presenta un archivo con el que se llevaron a cabo las pruebas pertinentes de robustez, mismo que se puede ejecutar para hacer pruebas de la siguiente manera:

```
python more secuencia_prueba.py
```

## Datos

El script está diseñado para operar en archivos de tipo raw, con las letras acordes a los cuatro nucleótidos. No hay restricciones en el número de líneas en el archivo. Además, los datos pueden estar espaciados, con tabuladores, separados por comas, en mayúsculas o minúsculas.  

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte.
También se pueden agregar nuevos datos para complementar los datos existentes. 

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.
El código está disponible a cambios.

## Términos de uso

Este script está disponible bajo la licencia MIT license. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [información de citación].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: [erikaog@lcg.unam.mx].


# Conteo de nucleotidos

El código recibe un archivo que contiene una secuencia de nucleótidos. El programa se encarga de contar el contenido e imprime en pantalla el resultado.

## Uso

El script acepta un solo argumento, el nombre del archivo a leer:

```
python conteo_nucleotidos.py -inputfile [sequence.txt]
```


donde `[sequence.txt]` es el nombre del archivo que contiene la secuencia de nucleótidos. 



## Salida

Se imprime la cantidad de cada nucleótido, ya sea A, T, C o G. 

## Control de errores

Si el archivo proporcionado no existe, el script generará un mensaje de error. Del mismo modo, si el archivo contiene únicamente nucleótidos escritos con letras minúsculas, el script no podrá hacer ningún conteo.

## Pruebas

El script incluye un conjunto de pruebas unitarias. Puede ejecutar estas pruebas con:

```
python -m unittest conteo_nucleotidos.py
```

## Datos

El script está diseñado para operar en archivos de texto plano, con los nucleótidos en mayúscula. No hay restricciones en el número de líneas en el archivo.

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte [Enlace a la documentación].
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

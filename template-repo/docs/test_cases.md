# Casos de prueba o escenarios

Este documento describe los casos de prueba para el script de Python desarrollado para el programa que se encarga de contar el contenido de nucleótidos en el archivo ingresado. El objetivo de estas pruebas es validar y garantizar que el script funciona correctamente y cumple con las especificaciones.

Los casos de prueba se han diseñado teniendo en cuenta las diferentes funcionalidades del script así como los posibles errores que puedan surgir.

El script está diseñado para dar una idea al usuario del funcionamiento del programa. El script no está diseñado para manejar errores como la ausencia del archivo de entrada o el ingreso de archivos sin mayúsculas. 

Los casos de prueba cubren las características clave del programa y prueban varias condiciones para garantizar la robustez y fiabilidad del script.

La ejecución exitosa de estos casos de prueba asegura que el script está listo para su uso y puede manejar diferentes condiciones de entrada y situaciones de error.

A continuación, presentamos los detalles de los casos de prueba. Cada caso de prueba incluye una descripción del caso de prueba, los datos de entrada utilizados y el resultado esperado.

Para el presente código, se realizó un archivo con todas las eventualidades que se pueden presentar. Este archivo se llama "secuencia_prueba.txt" y se encuentra en la siguiente ubicación: "C:\Users\erika_6xdeulp\OneDrive\Escritorio\biopython\python-class\template-repo\src\secuencia_prueba.txt". 
    
 ### Caso de prueba 1: 

 - Descripción: El usuario no ingresó correctamente el archivo deseado a analizar, no existe en el dispositivo o no ingresó la ruta absoluta.
 - Datos de entrada: Nombre el archivo mal escrito. 
 - Resultado esperado: imprime el siguinete mensaje: "sorry, couldn't find the file"

### Caso de prueba 2:

- Descripción: El usuario ingresó un archivo vacío. 
- Datos de entrada: Nombre del archivo vacío. 
- Resultado esperado: El programa verifica el tamaño del archivo, por lo que en caso de que este esté vacío imprimirá el siguiente mensaje de error: 
 "sorry, the file is empty"

### Caso de prueba 3:

- Descripción: El usuario ingresa los nucleótido en minúscula o mayúscula. 
- Datos de entrada: "A" y/o "T" y/o "C" y/o "G" y/o "a" y/o "t" y/o "c" y/o "g". 
- Resultado esperado: Depende de la letra que ingrese el usuario. El programa muestra el número correcto de nucleótidos en el archivo. El programa es lo suficientemente robusto para aceptar tanto letras minúsculas como mayúscculas. 

### Caso de prueba 4: 

- Descripción: Más de una letra ingresada, además combina letras mayúsculas y minúsculas. 
- Datos de entrada: 
    Ejemplo: A t c G
- Resultado esperado: La robustez del programa permite recibir cualquiera de las letras, la cantidad que sea determinado por el usuario, así como la mezcla de mayúsculas y minúsculas, imprimiendo en pantalla, la frecuencia correcta que se encuentra en el archivo. 

### Caso de prueba 5: 

- Descripción: El archivo, es recibido con escasa uniformidad en el formato.
- Datos de entrada: El archivo no está escrito en un formato definido, en el se pueden encontrar: espacios, comas, tabuladores, saltos de línea
- Resultado esperado: El conteo de nucleótidos es correcto, a pesar de todas las eventualidades. 

### Caso de prueba 6: 

- Descripción: En caso de que el programa reciba letras que no correspondan a los nucleótidos o a las letras que se encuentran en el archivo.
- Datos de entrada: 'd', 'f', 'h', 'sst'
- Resultado esperado: El programa imprime en pantalla un el siguiente mensaje de error.
"Sequence contains '{nucleotide}', it is invalid character" donde nucleotide es el caracter no encontrado en el archivo.   



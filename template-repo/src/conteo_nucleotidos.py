'''
NAME Conteo de nucleótidos 
       

VERSION: primera
        

AUTHOR Erika Ordoñez
        

DESCRIPTION El programa acepta un archivo con el contenido de nucleótidos representados con letras mayúsculas, se utilizan contadores
para contar la cantidad de As, Ts, CS y Gs para imprimir las cantidades en pantalla.  
        
        

USAGE

    % python conteo_nucleotidos.py
    


        
'''
import argparse 

parser = argparse.ArgumentParser(description="Conteo de nucleótidos")

# El usuario ingresa el nombre de un archivo, este es obligatorio
parser.add_argument("input_file", type = str, help='Nombre del archivo a parsear')

# Abre el archivo y lee la secuencia de ADN
try:
    args = parser.parse_args()
    with open(args.input_file, 'r') as file:
        sequence = file.read()
    print(f'Proporcion de nucleotidos presentes en la secuencia: A: {sequence.count('A')}, C: {sequence.count('C')}, T:{sequence.count('T')}, G:{sequence.count('G')}')

# En caso de no encontrar el archivo imprime este mensaje de error. 
except FileNotFoundError:
    print(f'El archivo no fue encontrado, inténtelo de nuevo')


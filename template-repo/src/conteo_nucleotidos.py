'''
NAME Conteo de nucleótidos 
       

VERSION: 3.12.3
        

AUTHOR Erika Ordoñez
        

DESCRIPTION El programa acepta un archivo con el contenido de nucleótidos representados con letras mayúsculas, se utilizan contadores
para contar la cantidad de As, Ts, CS y Gs para imprimir las cantidades en pantalla.  

CATEGORY DNA sequence  

USAGE 

Python conteo_nucleotidos.py

ARGUMENTS
    posicional [archivo]
    opcional -n --nucleotido
    
SEE ALGO 
    None
        
'''
# Importamos librerías para el parseo y para manejar archivo desde sistema operativo, respectivamente 
import argparse
import os

# Crear el parser de argumentos
parser = argparse.ArgumentParser(description='Contar la frecuencia de nucleótidos en un archivo de secuencia de ADN')
# El archivo es un argumento obligatorio
parser.add_argument('archivo', type=str, help='Archivo de secuencia de ADN')
# Aclarar secuencia, es un argumento opcional, acepta una letra o más. 
parser.add_argument('-n', '--nucleotido', nargs='+', type=str, help='Nucleótido(s) a contar')
args = parser.parse_args()

# Intentar abrir el archivo
try:
    with open(args.archivo, 'r') as file:
        sequence = file.read().upper()

# Si no es el archivo correcto o si no existe, imprime un mensaje de error
except FileNotFoundError:
    if os.path.exists(args.archivo)==False: 
        print("sorry, couldn't find the file")
    exit()

# Buscamos el tamaño del archivo, si es diferente a cero se ejecuta el código. 
if os.path.getsize(args.archivo) != 0:
    # Contar la frecuencia de los nucleótidos
    if args.nucleotido:
        for nucleotide in args.nucleotido:
            count = sequence.count(nucleotide.upper())
            if count !=0:
                print(f"Frecuencia de '{nucleotide.upper()}': {count}")
            # Si la letra no es parte de los nucleótidos, entonces el conteo será cero y se imprimirá un mensaje de error
            # Esto suponiendo que el archivo del usuario únicamente contiene una secuencia de nucleotidos 
            else: print(f"Sequence contains '{nucleotide}', it is invalid character")
    else:
        for nucleotide in ['A', 'C', 'G', 'T']:
            count = sequence.count(nucleotide)
            print(f"Frecuencia de '{nucleotide}': {count}")
# si se encuentra que el archivo es tamaño del archivo es cero, entonces significa que está vacío e imprime un mensaje de error. 
else: print("sorry, the file is empty")

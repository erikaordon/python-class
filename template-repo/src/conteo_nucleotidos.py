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

# Crear el parser de argumentos
parser = argparse.ArgumentParser(description='Contar la frecuencia de nucleótidos en un archivo de secuencia de ADN')
parser.add_argument('archivo', type=str, help='Archivo de secuencia de ADN')
parser.add_argument('-n', '--nucleotido', nargs='+', type=str, help='Nucleótido(s) a contar')
args = parser.parse_args()

# Intentar abrir el archivo
try:
    with open(args.archivo, 'r') as file:
        sequence = file.read().upper()
        
# Si no es el archivo correcto, imprime un mensaje de error
except FileNotFoundError:
    print(f"Error: No se pudo abrir el archivo '{args.archivo}'")
    exit()

# Contar la frecuencia de los nucleótidos
if args.nucleotido:
    for nucleotide in args.nucleotido:
        try:
            count = sequence.count(nucleotide.upper())
            print(f"Frecuencia de '{nucleotide.upper()}': {count}")
        except ValueError:
            print(f"Error: Nucleótido '{nucleotide}' inválido")
else:
    for nucleotide in ['A', 'C', 'G', 'T']:
        count = sequence.count(nucleotide)
        print(f"Frecuencia de '{nucleotide}': {count}")
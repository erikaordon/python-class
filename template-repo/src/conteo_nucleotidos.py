'''
NAME Conteo de nucleótidos 
       

VERSION: primera
        

AUTHOR Erika Ordoñez
        

DESCRIPTION El programa acepta un archivo con el contenido de nucleótidos representados con letras mayúsculas, se utilizan contadores
para contar la cantidad de As, Ts, CS y Gs para imprimir las cantidades en pantalla.  
        
        

USAGE

    % python conteo_nucleotidos.py
    


        
'''

# Abre el archivo y lee la secuencia de ADN
with open('sequence.txt', 'r') as file:
    sequence = file.read()

# Inicializa el contador para cada nucleótido
count_A = sequence.count('A')
count_T = sequence.count('T')
count_G = sequence.count('G')
count_C = sequence.count('C')

# Muestra los resultados
print("Número de A's:", count_A)
print("Número de T's:", count_T)
print("Número de G's:", count_G)
print("Número de C's:", count_C)
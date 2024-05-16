"""
calculate_restriction_sites.py: Script para calcular los sitios de restricción en una secuencia, con los sitios de "EcoRI": "GAATTC", "EcoRI": "GAATTC" y "HindIII": "AAGCTT" en una secuencia de DNA. 

Este script lee una secuencia de DNA desde un archivo dado y muestra los sitios donde se encuentran en la secuencia. La secuencia de DNA debe estar en un archivo de texto o en formato FASTA y solo puede contener los caracteres 'A', 'C', 'T', 'G' o 'N' (este último representa cualquier nucleótido). Opcionalmente, el cálculo puede mostrar la ubicación de los sitios de restricción seleccionados, sin embargo, es excluirán los caracteres 'N' de la secuencia. 

Uso: 
    python calculate_sitios_restriccion.py <path_to_dna_file> [--sites]

Argumentos: 
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de DNA. 
    --sites            : Opción para encontrar los sitios de restricción especificados: en la secuencia "EcoRI": "GAATTC", "EcoRI": "GAATTC" y "HindIII": "AAGCTT" en una secuencia de DNA. 
"""

import argparse 
from dna_analysis.operations.sitios_restriccion import read_dna_sequence
from dna_analysis.operations.sitios_restriccion import find_restriction_sites
from dna_analysis.utils.validators import validate_dna_sequence
from dna_analysis.utils.validators import validate_fasta_fromat 
from dna_analysis.utils.validators import check_sequence_length 

def main(): 
    parser = argparse.ArgumentParser(description="Muestra los sitios donde se encontraron los sitios de restricción especificados")
    parser.add_argument("file", type=str, help="Archivo de DNA del cual leer la secuencia.")
    parser.add_argument("-s", "--enzymes", action="store_true", help="Muestra los sitios de restricción encontrados en la secuencia dada")

    args = parser.parse_args()
    file_path = args.file
    enzymes = args.enzymes

    try:

        secuence = read_dna_sequence(file_path)

        sitios_restriccion = find_restriction_sites(secuence, enzymes=enzymes)

        print(f"Los sitios donde fue encontrado el sitio de restricción son: {sitios_restriccion}")

    except Exception as e: 
        print(f"Error: {str(e)}")

if __name__=="__main__":
    main()

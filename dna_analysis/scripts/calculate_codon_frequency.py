"""
calculate_codon_frequency.py: Script para calcular la frecuencia de codones.

Este script lee una secuencia de DNA desde un archivo dado y clacula la frecuencia de codones, recordando que un triplete es un conjunto de tres nucleótidos, en una secuencia.  La secuencia de DNA debes estar en un archivo de texto o un archivo FASTA, de aproximadamente 100 nucleótidos o más y solo puede contener los caracteres 'A', 'C', 'G', 'T' o 'N' (este último representa cualquier nucleótido). Opcionalmente, el cálculo puede normalizar el contenido excluyendo los caracteres 'N'.

Uso: 
    python calculate_codo_frequency.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de DNA. 
    --normalize        : Opción para normalizar la frecuencia de codones. 
"""

import argparse
from dna_analysis.operations.frecuencia_codones import calculate_codon_frequency
from dna_analysis.utils.validators import validate_dna_sequence
from dna_analysis.utils.validators import validate_fasta_format
from dna_analysis.utils.validators import check_sequence_length
from dna_analysis.utils.file_io import read_dna_sequence 

def main(): 
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia")
    parser.add_argument("file", type=str, help="Archivo con la secuencia de DNA")
    parser.add_argument("-n", "normalize", action="store_true", help="Normaliza la frecuencia de codones")

    args = parser.parse_args()
    file_path = args.file
    normalize = args.normalize

    try:
        secuencia = read_dna_sequence(file_path)

        frecuencia_codon = calculate_codon_frequency(secuencia, normalize=normalize)

        print(f"Esta es la frecuencia del coddon: {frecuencia_codon}%")

    except Exception as e:
        print(f" El error es: {str(e)}")

if __name__=="__main__": 
    main()
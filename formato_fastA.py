from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import re 

def codones(frame, secuencias):
    """
    Función para encontrar los codones y los primeros tres marcos de lectura de la secuencia original.
    Args:
        frame: Recibe los tres números correspondientes a los marcos de lectura.
        secuencias: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función una lista con las secuencias de nucleótidos.
    """
    codon_list = []
    if isinstance(secuencias, list): 
        secuencias=", ".join(secuencias)
    secuencias = secuencias.split(", ")
    for secuencia in secuencias:
        secuencia_codones = []
        secuencia = secuencia[frame:]
        for nucleotido in re.findall(r"(.{3})", str(secuencia)):
            secuencia_codones.append(nucleotido[0:3])
        codon_list.append("".join(secuencia_codones))
    return codon_list

def complemento(secuencias): 
    """
    Función para encontrar el complementario de la secuencia original de nucleotidos.
    Args:
        secuencias: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función una lista con el complementario de las secuencias de nucleótidos.
    """
    complement_list=[]
    if isinstance(secuencias, list):
        secuencias=", ".join(secuencias)
    secuencias = secuencias.split(", ")
    for secuencia in secuencias:
        seq_obj=Seq(secuencia)
        complement_seq=str(seq_obj.complement())
        complement_seq=("".join(complement_seq))
        complement_list.append(complement_seq)
    return complement_list

def write_and_read_fasta(secuencias_codones, output_filename="Frame1.fasta"):
    sequences = []
    """
    Función para leer y escribir las secuencias en formato fasta.
    Args:
        secuencias_codones: Recibe lista con secuencias.
    Returns:
        El valor que regresa la función es un archivo de las secuencias en formato fasta.
    """
    for i, seq in enumerate(secuencias_codones):
        seq_record = SeqRecord(Seq(seq), id=f">seq{i+1}", description="")
        sequences.append(seq_record)

    with open("Frame1.fasta", "w") as output_handle:
        SeqIO.write(sequences, output_handle, "fasta")

    with open("Frame1.fasta", "r") as input_handle:
        read_sequences = list(SeqIO.parse(input_handle, "fasta"))

    for seq_record in read_sequences:
        print(seq_record.id)
        print(seq_record.seq)
        
# PROGRAMA PRINCIPAL: 
# Lectura del archivo fasta
secuencias=[]
for record in SeqIO.parse("seq.nt.fa", "fasta"):
    secuencias.append(("".join(record.seq)))
# Primeros tres marcos de lectura correspondientes a la cadena original.
for frame in range(3):
    secuencias_codones=codones(frame, secuencias)
    print(f"Marco de lectura {frame}: {secuencias_codones}")
    write_and_read_fasta(secuencias_codones, f"nucleotide_sequences_frame_{frame}.fasta")
# Primero tres marcos de lectura correspondientes a la cadena complementaria. 
complementary_sequences=complemento(secuencias)
for frame in range(3):
    secuencias_codones_complementarias = codones(frame, complementary_sequences)
    print(f"Marco de lectura {frame} de la cadena complementaria: {secuencias_codones_complementarias}")
    write_and_read_fasta(secuencias_codones_complementarias, f"complementary_nucleotide_sequences_frame_{frame}.fasta")
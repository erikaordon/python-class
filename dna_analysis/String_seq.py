from Bio.Seq import Seq
from Bio import SeqUtils
from Bio import SeqIO
""""
seqobj= Bio.Seq.Seq ("AGCTGCTGACGT")
seqobj

## Seq ('AGCTGCTGACGT')
seq_str = str (seqobj)
print ('{} tiene {} nucleotidos'.format(seq_str , len(seq_str)))

# AGCTGCTGACGT tiene 12 nucleotidos
# len (seqobj) no 
seq_str=str(seqobj)
print (" {} tiene {}".format(seq_str,len(seq_str)))

"------------------------------------------------------"
seq_str 
seq_str = seq_str[::-1]
print(seq_str)

#Seq('AGCTGCTGACGT')
print(seqobj.complement())
print(seqobj.reverse_complement())
print(seqobj.translate(to_stop=True))

rna = seqobj.transcribe()
print(f"RNA {rna}")

#print(f"back transcribe{rna.back_transcribe}")
seqobj = "AGCTGCTGACGT" 
print(seqobj[::1])

pattern = Seq("ACG")
sequence = ("ATGCGCGACGGCGTGATCAGCTTATAGCCGTACGACTGCTGC")

result = SeqUtils.nt_search(str(sequence), pattern)
print(result)

consensus = "RGWYV"
sequence = "CGTAGCTAGCTCAGAGCAGGGACACGTGCTAGCAACAGCGCT"
print(SeqUtils.nt_search(sequence, consensus))
"""


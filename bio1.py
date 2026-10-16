##
##def reverse_complement(dna_seq):
##    reverse_complement =""
##    for base in dna_seq:
##        if base =="A":
##            reverse_complement += "T"
##        elif base =="T":
##            reverse_complement += "A"
##        elif base =="C":
##            reverse_complement += "G"
##        elif base =="G":
##            reverse_complement += "C"
##    return reverse_complement
##dna_seq = "AGCTGACT"
##print(reverse_complement(dna_seq))

##def rna(dna_seq):
##    rna = ""
##    for base in dna_seq:
##        if base =="T":
##            rna += "U"
##        elif base =="A":
##            rna += "A"
##        elif base =="G":
##            rna += "G"
##        elif base =="C":
##            rna += "C"
##    return rna
##        
##            
##    return rna
##dna_seq = "AGCTGACT"
##print(rna(dna_seq))

##from Bio.Seq import Seq
##dna_seq=input("Enter dna sequence:")
##my_dna= Seq(dna_seq)
##rna_seq=my_dna.transcribe()
##print(my_dna)
##print(rna_seq)

##from Bio.Seq import Seq
##mes_rna = Seq(input("Enter mRNA sequence:"))
##prot_seq = mes_rna.translate()
##print(mes_rna)
##print(prot_seq)

##from Bio.Seq import Seq
##dna_seq=input("Enter dna sequence:")
##my_dna= Seq(dna_seq)
##rna_seq=my_dna.transcribe()
##prot_seq = rna_seq.translate()
##print(rna_seq)
##print(prot_seq)










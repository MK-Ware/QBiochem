#!/usr/bin/env python


class DNA:

    def __init__(self, nucleotides, table_file):
        if "U" in nucleotides or "u" in nucleotides:
            self.nucleotides = nucleotides.upper().replace("U", "T")
            print ("DNA nucleatides can't contain the base Uracil, replaced with Thymine.")
        self.nucleotides = nucleotides.upper()
        self.pairs = {"G" : "C", "C" : "G", "T" : "A", "A" : "U"}
        self.DNA = self.nucleotides.split(" ")
        self.table_file = table_file

    def template2mRNA(self):
        res_RNA = []
        for nuc in self.DNA:
            RNA_nuc = ""
            for base in nuc:
                try:
                    RNA_nuc += self.pairs[base]
                except:
                    return "invalid sequence"
            res_RNA.append(RNA_nuc)
        return " ".join(res_RNA)

    def coding2mRNA(self):
        res_RNA = []
        for nuc in self.DNA:
            RNA_nuc = ""
            for base in nuc:
                if not base in "AUGCT":
                    return "invalid sequence"
                if base == "T":
                    RNA_nuc += "U"
                else:
                    RNA_nuc += base
            res_RNA.append(RNA_nuc)
        return " ".join(res_RNA)

    def _load_table(self):
        table = {}
        with open(self.table_file) as tf:
            content = tf.readlines()
            for i in range(len(content)):
                content[i] = content[i].strip("\n")
                content[i] = content[i].split(",")
            for row in content[1:]:
                table[row[0]] = {'SLC' : row[1], 'Abbv' : row[2], 'Codons' : row[3]}
        return table

    def translate(self, codon_seq=None):
        if not codon_seq:
            codon_seq = self.DNA

        try:
            codon_seq = codon_seq.upper().split(" ")
        except:
            return "mRNA seems to be empty "

        codon_seq1 = []
        for i in range(len(codon_seq)):
            codon_seq1.append(codon_seq[i].upper())
        print(codon_seq1)
        
        for i in range(len(codon_seq1)):
            if "U" in codon_seq1[i]:
                codon_seq1[i] = codon_seq1[i].replace("U", "T")
        print(codon_seq1)
        
        amino_acids = []
        table = self._load_table()
        
        for codon in codon_seq1:
            found = False
            for amino in table:
                if codon in table[amino]['Codons']:
                    amino_acids.append(amino)
                    found = True
                    break
            if not found:
                amino_acids.append("Unrecognized codon")
        return " - ".join(amino_acids)

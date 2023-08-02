import random

class GenerateSeq:
    def __init__(self, length):
        self.sequence = self.generate_random_sequence(length)

    def generate_random_sequence(self, length):
        return ''.join(random.choice('ATCG') for _ in range(length))

    def transcribe(self):
        return self.sequence.replace('T', 'U')

    def translate(self):
        codon_map = {
            'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
            'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
            'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
            'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
            'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
            'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
            'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
            'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
            'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
            'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
            'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
            'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
            'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
            'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
            'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
            'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
        }
        rna_seq = self.transcribe()
        protein_seq = ''
        for i in range(0, len(rna_seq) - 2, 3):
            codon = rna_seq[i:i+3]
            amino_acid = codon_map.get(codon, '')
            if amino_acid == 'Stop':
                break
            protein_seq += amino_acid
        return protein_seq

    def insert(self, position, nucleotide):
        current_seq_len = len(self.sequence)
        if position < 1 or position > current_seq_len:
            raise ValueError("Position out of range")
        if nucleotide not in 'ATCG':
            raise ValueError("Invalid nucleotide")
        if position == 1:
            self.sequence = nucleotide + self.sequence
        elif position == current_seq_len:
            self.sequence += nucleotide
        else:
            self.sequence = self.sequence[:position-1] + nucleotide + self.sequence[position-1:]

    def delete(self, position):
        current_seq_len = len(self.sequence)
        if position < 1 or position > current_seq_len:
            raise ValueError("Position out of range")
        nucleotide = self.sequence[:position-1]
        if position == 1:
            self.sequence = self.sequence[1:]
        elif position == current_seq_len:
            self.sequence = self.sequence[:-1]
        else:
            self.sequence = self.sequence[:position-1] + self.sequence[position:]
        print(f"Nucleotide {nucleotide} deleted from position {position}")

    def random_mutation(self):
        position = random.randint(0, len(self.sequence) - 1)
        original_nucleotide = self.sequence[position]
        mutated_nucleotide = random.choice('ATCG'.replace(original_nucleotide, ''))
        self.sequence = self.sequence[:position] + mutated_nucleotide + self.sequence[position+1:]
        print(f"Nucleotide {original_nucleotide} at position {position+1} mutated to {mutated_nucleotide}")

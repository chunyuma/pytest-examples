import random
from srcs.genseq import GenerateSeq

def test_generate_random_sequence_length():
    seq_len = 100
    gen_seq = GenerateSeq(seq_len)
    assert len(gen_seq.sequence) == seq_len

def test_transcribe():
    gen_seq = GenerateSeq(100)
    transcribed_seq = gen_seq.transcribe()
    assert 'T' not in transcribed_seq
    assert 'U' in transcribed_seq

def test_translate():
    gen_seq = GenerateSeq(100)
    protein_seq = gen_seq.translate()
    # Checking for a valid amino acid sequence length
    assert len(protein_seq) * 3 <= len(gen_seq.sequence)

def test_insert_valid_nucleotide():
    gen_seq = GenerateSeq(100)
    gen_seq.insert(5, 'A')
    assert gen_seq.sequence[5-1] == 'A'
    assert len(gen_seq.sequence) == 101

def test_insert_invalid_nucleotide1():
    gen_seq = GenerateSeq(100)
    try:
        gen_seq.insert(5, 'Z')
    except ValueError as e:
        assert str(e) == "Invalid nucleotide"

def test_insert_invalid_nucleotide2():
    gen_seq = GenerateSeq(100)
    try:
        gen_seq.insert(0, 'A')
    except ValueError as e:
        assert str(e) == "Position out of range"

def test_delete():
    gen_seq = GenerateSeq(100)
    gen_seq.delete(5)
    assert len(gen_seq.sequence) == 99

def test_random_mutation():
    random.seed(42)
    gen_seq = GenerateSeq(10)
    original_sequence = gen_seq.sequence
    gen_seq.random_mutation()
    assert gen_seq.sequence != original_sequence
from srcs.seqactions import SequenceActions
import pytest

def test_alignment():
    seq1 = 'GATTACA'
    seq2 = 'GTTACAC'
    align1, align2 = SequenceActions.alignment(seq1, seq2)
    assert align1 == 'GATTACA-'
    assert align2 == 'G-TTACAC'

    seq1 = 'ACGT'
    seq2 = 'ACGT'
    align1, align2 = SequenceActions.alignment(seq1, seq2)
    assert align1 == seq2
    assert align2 == seq1

@pytest.mark.group1
def test_split_into_kmers():
    sequence = 'ATCGATCG'
    k = 3
    kmers = SequenceActions.split_into_kmers(sequence, k)
    assert kmers == ['ATC', 'TCG', 'CGA', 'GAT', 'ATC', 'TCG']

def test_generate_all_kmers():
    kmers = SequenceActions.generate_all_kmers('ACGT')
    print(f"All possible kmers from 'ATGT': {kmers}")
    assert len(kmers) == 10

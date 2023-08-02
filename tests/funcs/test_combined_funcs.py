import random
import pytest
from srcs.genseq import GenerateSeq
from srcs.seqactions import SequenceActions

@pytest.mark.slow
def test_generate_all_kmers_from_long_seq():
    random.seed(42)
    gen_seq = GenerateSeq(3000)
    kmers = SequenceActions.generate_all_kmers(gen_seq.sequence)
    assert len(kmers) == 4486575
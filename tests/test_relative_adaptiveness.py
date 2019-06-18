from CAI import RSCU, relative_adaptiveness
import pytest


def test_bad_args():
    # make sure bad arguments raise errors
    with pytest.raises(TypeError):
        relative_adaptiveness()
    with pytest.raises(TypeError):
        relative_adaptiveness(sequences=["AAC"], RSCUs=RSCU(["AAC"]))


def test_arg_equivalence():
    # should be able to take either reference sequences or an RSCU dict
    assert relative_adaptiveness(sequences=["AAC"]) == relative_adaptiveness(
        RSCUs=RSCU(["AAC"])
    )


def test_weights():
    assert relative_adaptiveness(sequences=["AAC"]) == {
        "AAA": 1.0,
        "AAC": 1.0,
        "AAG": 1.0,
        "AAT": (0.5 / (0.5 * (1 + 0.5))) / (1 / (0.5 * (1 + 0.5))),
        "ACA": 1.0,
        "ACC": 1.0,
        "ACG": 1.0,
        "ACT": 1.0,
        "AGA": 1.0,
        "AGC": 1.0,
        "AGG": 1.0,
        "AGT": 1.0,
        "ATA": 1.0,
        "ATC": 1.0,
        "ATG": 1.0,
        "ATT": 1.0,
        "CAA": 1.0,
        "CAC": 1.0,
        "CAG": 1.0,
        "CAT": 1.0,
        "CCA": 1.0,
        "CCC": 1.0,
        "CCG": 1.0,
        "CCT": 1.0,
        "CGA": 1.0,
        "CGC": 1.0,
        "CGG": 1.0,
        "CGT": 1.0,
        "CTA": 1.0,
        "CTC": 1.0,
        "CTG": 1.0,
        "CTT": 1.0,
        "GAA": 1.0,
        "GAC": 1.0,
        "GAG": 1.0,
        "GAT": 1.0,
        "GCA": 1.0,
        "GCC": 1.0,
        "GCG": 1.0,
        "GCT": 1.0,
        "GGA": 1.0,
        "GGC": 1.0,
        "GGG": 1.0,
        "GGT": 1.0,
        "GTA": 1.0,
        "GTC": 1.0,
        "GTG": 1.0,
        "GTT": 1.0,
        "TAC": 1.0,
        "TAT": 1.0,
        "TCA": 1.0,
        "TCC": 1.0,
        "TCG": 1.0,
        "TCT": 1.0,
        "TGC": 1.0,
        "TGG": 1.0,
        "TGT": 1.0,
        "TTA": 1.0,
        "TTC": 1.0,
        "TTG": 1.0,
        "TTT": 1.0,
    }


def test_alternate_genetic_code():
    assert relative_adaptiveness(sequences=["AAC"], genetic_code=10) == {
        "AAA": 1.0,
        "AAC": 1.0,
        "AAG": 1.0,
        "AAT": (0.5 / (0.5 * (1 + 0.5))) / (1 / (0.5 * (1 + 0.5))),
        "ACA": 1.0,
        "ACC": 1.0,
        "ACG": 1.0,
        "ACT": 1.0,
        "AGA": 1.0,
        "AGC": 1.0,
        "AGG": 1.0,
        "AGT": 1.0,
        "ATA": 1.0,
        "ATC": 1.0,
        "ATG": 1.0,
        "ATT": 1.0,
        "CAA": 1.0,
        "CAC": 1.0,
        "CAG": 1.0,
        "CAT": 1.0,
        "CCA": 1.0,
        "CCC": 1.0,
        "CCG": 1.0,
        "CCT": 1.0,
        "CGA": 1.0,
        "CGC": 1.0,
        "CGG": 1.0,
        "CGT": 1.0,
        "CTA": 1.0,
        "CTC": 1.0,
        "CTG": 1.0,
        "CTT": 1.0,
        "GAA": 1.0,
        "GAC": 1.0,
        "GAG": 1.0,
        "GAT": 1.0,
        "GCA": 1.0,
        "GCC": 1.0,
        "GCG": 1.0,
        "GCT": 1.0,
        "GGA": 1.0,
        "GGC": 1.0,
        "GGG": 1.0,
        "GGT": 1.0,
        "GTA": 1.0,
        "GTC": 1.0,
        "GTG": 1.0,
        "GTT": 1.0,
        "TAC": 1.0,
        "TAT": 1.0,
        "TCA": 1.0,
        "TCC": 1.0,
        "TCG": 1.0,
        "TCT": 1.0,
        "TGA": 1.0,  # this is not a stop codon in genetic code 10
        "TGC": 1.0,
        "TGG": 1.0,
        "TGT": 1.0,
        "TTA": 1.0,
        "TTC": 1.0,
        "TTG": 1.0,
        "TTT": 1.0,
    }

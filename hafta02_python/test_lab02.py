import numpy as np, pandas as pd
from lab02 import normalize, kelime_sayac, en_yuksek_k

def test_normalize():
    assert np.allclose(normalize(np.array([2., 4., 6.])), [0, .5, 1])
    assert np.allclose(normalize(np.array([5., 5.])), [0, 0])

def test_kelime_sayac():
    assert kelime_sayac("Bulut, bulut! Zekâ.") == {"bulut": 2, "zekâ": 1}

def test_en_yuksek_k():
    df = pd.DataFrame({"a": [1, 9, 5]})
    assert en_yuksek_k(df, "a", 2)["a"].tolist() == [9, 5]

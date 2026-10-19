import pandas as pd
from inf8239_u01.green import pareto_flags

def test_pareto_marks_dominated_rows():
    df = pd.DataFrame({
        "f1_macro": [0.90, 0.90, 0.88],
        "fit_s": [2.0, 0.1, 0.3]
    })
    assert pareto_flags(df, score="f1_macro", cost="fit_s") == [False, True, False]

def test_single_model_is_pareto():
    df = pd.DataFrame({
        "f1_macro": [0.80],
        "fit_s": [1.0]
    })
    assert pareto_flags(df, score="f1_macro", cost="fit_s") == [True]

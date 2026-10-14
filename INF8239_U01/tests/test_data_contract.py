import pandas as pd

# --- Adult Income ---
def load_adult():
    columns_adult = [
        "age","workclass","fnlwgt","education","education_num","marital_status",
        "occupation","relationship","race","sex","capital_gain","capital_loss",
        "hours_per_week","native_country","income"
    ]
    df = pd.read_csv("data/raw/adult.csv", names=columns_adult)
    df["income"] = df["income"].str.strip()  # limpiar espacios
    return df

def test_adult_dataset_is_not_empty():
    assert not load_adult().empty

def test_adult_required_columns_exist():
    REQUIRED = {"income", "age"}
    assert REQUIRED <= set(load_adult().columns)

def test_adult_target_has_no_missing_and_two_classes():
    y = load_adult()["income"]
    assert y.notna().all()
    assert y.nunique() >= 2


# --- Student Dropout ---
def load_student():
    return pd.read_csv("data/raw/student.csv")

def test_student_dataset_is_not_empty():
    assert not load_student().empty

def test_student_required_columns_exist():
    REQUIRED = {"Target", "Admission grade"}  # ajusta a columnas reales
    assert REQUIRED <= set(load_student().columns)

def test_student_target_has_no_missing_and_two_classes():
    y = load_student()["Target"]
    assert y.notna().all()
    assert y.nunique() >= 2

from pathlib import Path
import pandas as pd

def download_csv(url: str, destination: str) -> Path:
    if not url.startswith(("https://", "http://")):
        raise ValueError("La fuente debe ser una URL HTTP(S)")
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(url, header=None)
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")
    frame.to_csv(path, index=False)
    return path

# Adult Income
URL_ADULT = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
path_adult = download_csv(URL_ADULT, destination="data/raw/adult.csv")
print("Adult Income guardado en:", path_adult)

# Student Dropout & Academic Success
from ucimlrepo import fetch_ucirepo

student_data = fetch_ucirepo(id=697)

frame_student = pd.concat(
    [
        student_data.data.features,
        student_data.data.targets
    ],
    axis=1
)

path_student = Path("data/raw/student.csv")
path_student.parent.mkdir(parents=True, exist_ok=True)

frame_student.to_csv(path_student, index=False)

print("Student Dropout guardado en:", path_student)
print("Dimensiones de Student Dropout:", frame_student.shape)
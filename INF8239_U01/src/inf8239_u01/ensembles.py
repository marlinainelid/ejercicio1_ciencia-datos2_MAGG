from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

def build_models(preprocess):
 
    return {
        "logistic": Pipeline([
            ("prep", preprocess),
            ("model", LogisticRegression(max_iter=1000, random_state=42))
        ]),
        "svm_c1": Pipeline([
            ("prep", preprocess),
            ("model", SVC(C=1, probability=True, random_state=42))
        ]),
        "svm_c10": Pipeline([
            ("prep", preprocess),
            ("model", SVC(C=10, probability=True, random_state=42))
        ]),
        "rf_100": Pipeline([
            ("prep", preprocess),
            ("model", RandomForestClassifier(n_estimators=100, random_state=42))
        ]),
        "rf_300": Pipeline([
            ("prep", preprocess),
            ("model", RandomForestClassifier(n_estimators=300, random_state=42))
        ]),
        "boost": Pipeline([
            ("prep", preprocess),
            ("model", HistGradientBoostingClassifier(random_state=42))
        ])
    }

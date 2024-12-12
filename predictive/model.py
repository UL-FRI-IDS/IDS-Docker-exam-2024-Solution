import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

FEATURE_COLUMNS = ['loan_amount', 'loan_interest_rate', 'loan_percent_income', 'age', 'income', 'years_work_experience', 'owns_home', 'credit_history_length_years', 'credit_score', 'previous_loan_defaults']
TARGET_COLUMN = "loan_approved"

df = pd.read_csv('/model/data/applicants_loan_applications.csv')

X = df[FEATURE_COLUMNS]
y = df[TARGET_COLUMN]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, shuffle=True)

# baseline
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X_train, y_train)
y_pred = dummy_clf.predict(X_test)
print("Baseline (majority classifier)")
print(classification_report(y_test, y_pred, zero_division=0, target_names=['loan_not_approved', 'loan_approved']))

# random forest
rf = RandomForestClassifier(random_state=1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print("Random forest classifier")
print(classification_report(y_test, y_pred, target_names=['loan_not_approved', 'loan_approved']))

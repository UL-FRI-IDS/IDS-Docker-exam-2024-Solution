import psycopg2
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="ulfriids",
    host="dbserver",
    port="5432"
)

feature_query = """
SELECT loan_amount, loan_interest_rate, loan_percent_income, age, income, years_work_experience, owns_home, credit_history_length_years, credit_score, previous_loan_defaults
FROM loan_applications
JOIN applicants
ON loan_applications.applicant_id = applicants.applicant_id
"""

X = pd.read_sql_query(feature_query, conn)

target_query = """
SELECT loan_approved
FROM loan_applications
"""

y = pd.read_sql_query(target_query, conn).values.ravel()

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, shuffle=True)

# baseline
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X_train, y_train)
y_pred = dummy_clf.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0, target_names=['loan_not_approved', 'loan_approved']))

# random forest
rf = RandomForestClassifier(random_state=1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=['loan_not_approved', 'loan_approved']))

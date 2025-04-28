import joblib
import pandas as pd

# Muat model terbaik (pipeline) yang telah disimpan
MODEL_PATH = 'best_pipeline.pkl'
model = joblib.load(MODEL_PATH)

# === Hardcoded input values ===
# Ganti nilai di bawah sesuai skenario yang diinginkan
# Pastikan mencakup kolom yang dipakai pipeline: EmployeeId, EmployeeCount, StandardHours, Over18

data = {
    'Age': [35],
    'BusinessTravel': ['Travel_Rarely'],
    'DailyRate': [800],
    'Department': ['Sales'],
    'DistanceFromHome': [5],
    'Education': [3],
    'EducationField': ['LifeSciences'],
    'EmployeeCount': [1],            # default 1
    'EnvironmentSatisfaction': [2],
    'Gender': ['Male'],
    'HourlyRate': [100],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': ['SalesExecutive'],
    'JobSatisfaction': [3],
    'MaritalStatus': ['Married'],
    'MonthlyIncome': [5000],
    'MonthlyRate': [15000],
    'NumCompaniesWorked': [2],
    'Over18': ['Y'],                # default Y
    'OverTime': ['Yes'],
    'PercentSalaryHike': [15],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [3],
    'StandardHours': [80],           # constant 80
    'StockOptionLevel': [1],
    'TotalWorkingYears': [10],
    'TrainingTimesLastYear': [3],
    'WorkLifeBalance': [4],
    'YearsAtCompany': [5],
    'YearsInCurrentRole': [3],
    'YearsSinceLastPromotion': [1],
    'YearsWithCurrManager': [3]
}

# Buat DataFrame
# Drop Attrition column if present; pipeline expects only features
df_input = pd.DataFrame(data).drop(columns=['Attrition'], errors='ignore')

# Jalankan prediksi
pred_label = model.predict(df_input)[0]
pred_proba = model.predict_proba(df_input)[0, 1]

# Interpretasi hasil
status = 'Resign' if pred_label == 1 else 'Stay'
print(f"Prediksi: {status} (label {pred_label})")
print(f"Probabilitas attrition: {pred_proba:.3f}")

import pandas as pd
import xgboost as xgb

# Load model
model = xgb.XGBClassifier()
model.load_model("model_xgb.json")

data = pd.DataFrame({
    'Age': [20],
    'BusinessTravel': [1],
    'Department': [0],
    'DistanceFromHome': [11],
    'EducationField': [4],
    'EnvironmentSatisfaction': [3],
    'Gender': [1],
    'JobInvolvement': [3],
    'JobLevel': [2],
    'JobRole': [4],
    'JobSatisfaction': [2],
    'MaritalStatus': [0],
    'MonthlyIncome': [4777],
    'OverTime': [0],
    'StockOptionLevel': [0],
    'TotalWorkingYears': [15],
    'YearsAtCompany': [1],
    'YearsInCurrentRole': [0],
    'YearsWithCurrManager': [0]
})


# Prediksi kelas (0 atau 1)
predictions = model.predict(data)

# Loop tiap baris hasil prediksi
for i, pred in enumerate(predictions):
    if pred == 1:
        print(f"Attrition")
    else:
        print(f"No Attrition")



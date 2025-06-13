import pandas as pd
import xgboost as xgb
import sys

model = xgb.XGBClassifier()
model.load_model("model_xgb.json")


input_file = sys.argv[1]  
data = pd.read_csv(input_file)


predictions = model.predict(data)

output = pd.DataFrame(predictions, columns=["Prediction"])
output.to_csv("predictions.csv", index=False)

print("Prediksi selesai! Disimpan di predictions.csv")

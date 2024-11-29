import pandas as pd
from stroke.models import StrokePatient

# Load data from CSV
data = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Populate MongoDB
for _, row in data.iterrows():
    StrokePatient.objects.create(
        id=row['id'],
        gender=row['gender'],
        age=row['age'],
        hypertension=row['hypertension'],
        ever_married=row['ever_married'],
        work_type=row['work_type'],
        Residence_type=row['Residence_type'],
        avg_glucose_level=row['avg_glucose_level'],
        bmi=row['bmi'],
        smoking_status=row['smoking_status'],
        stroke=row['stroke']
    )
print("Database populated successfully!")

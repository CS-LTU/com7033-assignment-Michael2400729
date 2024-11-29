from django.db import models

class StrokePatient(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=10)
    age = models.FloatField()
    hypertension = models.BooleanField()
    ever_married = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')])
    work_type = models.CharField(max_length=20)
    Residence_type = models.CharField(max_length=6)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.CharField(max_length=20)
    stroke = models.BooleanField()

    class Meta:
        app_label = 'stroke'

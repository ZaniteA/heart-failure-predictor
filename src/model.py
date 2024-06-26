import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.ensemble import _gb

from patient_data import PatientData



class Model(object):
    def __init__(self):
        with open('assets/models/gbc_model.pkl', 'rb') as model_file:
            self.model = pickle.load(model_file)
        with open('assets/models/scaler.pkl', 'rb') as scaler_file:
            self.scaler = pickle.load(scaler_file)

        self.numerical_columns = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']


    def predict(self, patient_data: PatientData) -> str:
        # If any values are unspecified, fill them
        if patient_data.age is None:
            patient_data.age = 54

        if patient_data.sex is None:
            patient_data.sex = 'M'

        if patient_data.chest_pain_type is None:
            patient_data.chest_pain_type = 'ASY'

        if patient_data.resting_bp is None:
            patient_data.resting_bp = 133

        if patient_data.cholesterol is None:
            patient_data.cholesterol = 244

        if patient_data.fasting_bs is None:
            patient_data.fasting_bs = 0

        if patient_data.resting_ecg is None:
            patient_data.resting_ecg = 'Normal'

        if patient_data.max_hr is None:
            patient_data.max_hr = 137

        if patient_data.exercise_angina is None:
            patient_data.exercise_angina = 'N'

        if patient_data.oldpeak is None:
            patient_data.oldpeak = 0.9

        if patient_data.st_slope is None:
            patient_data.st_slope = 'Flat'

        # Transform into dataframe
        df_dict = {
            'Age'              : [patient_data.age],
            'Sex'              : [0 if patient_data.sex == 'M' else 1],
            'RestingBP'        : [patient_data.resting_bp],
            'Cholesterol'      : [patient_data.cholesterol],
            'FastingBS'        : [patient_data.fasting_bs],
            'MaxHR'            : [patient_data.max_hr],
            'ExerciseAngina'   : [0 if patient_data.exercise_angina == 'N' else 1],
            'Oldpeak'          : [patient_data.oldpeak],
            'ChestPainType_ATA': [1 if patient_data.chest_pain_type == 'ATA' else 0],
            'ChestPainType_NAP': [1 if patient_data.chest_pain_type == 'NAP' else 0],
            'ChestPainType_TA' : [1 if patient_data.chest_pain_type == 'TA' else 0],
            'RestingECG_LVH'   : [1 if patient_data.resting_ecg == 'LVH' else 0],
            'RestingECG_ST'    : [1 if patient_data.resting_ecg == 'ST' else 0],
            'ST_Slope_Down'    : [1 if patient_data.st_slope == 'Down' else 0],
            'ST_Slope_Up'      : [1 if patient_data.st_slope == 'Up' else 0],
        }
        df = pd.DataFrame(df_dict)

        # Log transform Oldpeak
        df['Oldpeak'] = np.log(np.max([df['Oldpeak'] + 2.6, np.zeros(1)], axis=0) + 1)

        # Sqrt transform RestingBP and Cholesterol
        df['RestingBP'] = np.sqrt(np.max([df['RestingBP'] - 80, np.zeros(1)], axis=0))
        df['Cholesterol'] = np.sqrt(np.max([df['Cholesterol'] - 85, np.zeros(1)], axis=0))

        # Standardize numerical columns with scaler
        df[self.numerical_columns] = self.scaler.transform(df[self.numerical_columns])

        prediction = self.model.predict(df)[0]

        return 'Heart Failure: Yes' if prediction == 1 else 'Heart Failure: No'

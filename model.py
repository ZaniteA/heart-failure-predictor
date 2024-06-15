import random

from patient_data import PatientData



class Model(object):
    def __init__(self):
        pass


    def predict(self, patient_data: PatientData) -> str:
        return random.choice(['Heart Failure: Yes', 'Heart Failure: No'])

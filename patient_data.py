class PatientData(object):
    # Should be initialized with the same format as the dataset.
    def __init__(self,
                 age: int = None,
                 sex: str = None,
                 chest_pain_type: str = None,
                 resting_bp: int = None,
                 cholesterol: int = None,
                 fasting_bs: int = None,
                 resting_ecg: str = None,
                 max_hr: int = None,
                 exercise_angina: str = None,
                 oldpeak: float = None,
                 st_slope: str = None):
        self.age = age
        self.sex = sex
        self.chest_pain_type = chest_pain_type
        self.resting_bp = resting_bp
        self.cholesterol = cholesterol
        self.fasting_bs = fasting_bs
        self.resting_ecg = resting_ecg
        self.max_hr = max_hr
        self.exercise_angina = exercise_angina
        self.oldpeak = oldpeak
        self.st_slope = st_slope

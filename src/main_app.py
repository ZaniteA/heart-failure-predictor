from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QFormLayout
from PyQt6.QtGui import QFontDatabase, QFont
from PyQt6.QtCore import Qt

import configs
from components import IntegerLineInput, FloatLineInput, RadioButtonInput
from model import Model
from patient_data import PatientData



class HeartFailurePredictor(QWidget):
    def __init__(self):
        super().__init__()
        self.model = Model()
        self.init_ui()


    def import_font(self, font_path: str) -> QFont:
        # Try importing custom font
        fallback_font_family = configs.FALLBACK_FONT
        try:
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id < 0:
                self.logger.log('Error loading font:')
                return QFont(fallback_font_family)
            else:
                return QFont(QFontDatabase.applicationFontFamilies(font_id)[0])
        except (FileNotFoundError, PermissionError):
            self.logger.log('Font file not found:')
            return QFont(fallback_font_family)
        

    def get_font(self, points) -> QFont:
        sized_font = self.font_object
        sized_font.setPointSize(points)
        return sized_font


    def init_ui(self):
        self.setWindowTitle('Heart Failure Predictor')
        self.setObjectName('MainApp')
        self.setAutoFillBackground(True)

        # Size shenanigans
        self.setFixedSize(configs.WINDOW_WIDTH, configs.WINDOW_HEIGHT) # Set fixed size
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)  # Disable maximize button

        # Fonts
        self.font_object = self.import_font('assets/fonts/Switzer-Regular.otf')

        # Style sheet
        self.setStyleSheet(configs.STYLE_SHEET)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel('Heart Failure Predictor')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(self.get_font(configs.TITLE_FONT_SIZE))
        main_layout.addWidget(title)
        
        # Scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setViewportMargins(10, 10, 10, 10)
        
        # Form layout widget
        form_widget = QWidget()
        form_widget.setObjectName('InputForm')
        form_widget.setAutoFillBackground(True)

        form_layout = QFormLayout(form_widget)
        form_layout.setVerticalSpacing(20)

        self.inputs = []
        
        # Age
        self.age_input = IntegerLineInput(self, 1, 150)
        form_layout.addRow('Age:', self.age_input)
        self.inputs.append(self.age_input)
        
        # Sex
        self.sex_input = RadioButtonInput(
            parent = self,
            prompts = ['Male', 'Female'],
            results = ['M', 'F']
        )
        form_layout.addRow('Sex:', self.sex_input)
        self.inputs.append(self.sex_input)

        # Chest pain type
        self.cpt_input = RadioButtonInput(
            parent = self,
            prompts = ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'],
            results = ['TA', 'ATA', 'NAP', 'ASY']
        )
        form_layout.addRow('Chest pain type:', self.cpt_input)
        self.inputs.append(self.cpt_input)
        
        # Resting blood pressure
        self.bp_input = IntegerLineInput(self, 1, 400)
        form_layout.addRow('Resting blood pressure:', self.bp_input)
        self.inputs.append(self.bp_input)

        # Serum cholesterol
        self.chol_input = IntegerLineInput(self, 1, 900)
        form_layout.addRow('Serum cholesterol:', self.chol_input)
        self.inputs.append(self.chol_input)
        
        # Fasting blood sugar
        self.fbs_input = RadioButtonInput(
            parent = self,
            prompts = ['> 120 mg/dl', '≤ 120 mg/dl'],
            results = [1, 0]
        )
        form_layout.addRow('Fasting blood sugar:', self.fbs_input)
        self.inputs.append(self.fbs_input)
        
        # Resting ECG
        self.ecg_input = RadioButtonInput(
            parent = self,
            prompts = ['Normal', 'ST-T wave abnormality', 'Probable or definite left ventricular hypertrophy'],
            results = ['Normal', 'ST', 'LVH']
        )
        form_layout.addRow('Resting ECG:', self.ecg_input)
        self.inputs.append(self.ecg_input)
        
        # Maximum heart rate
        self.hr_input = IntegerLineInput(self, 1, 300)
        form_layout.addRow('Maximum heart rate:', self.hr_input)
        self.inputs.append(self.hr_input)
        
        # Exercise angina
        self.angina_input = RadioButtonInput(
            parent = self,
            prompts = ['Yes', 'No'],
            results = ['Y', 'N']
        )
        form_layout.addRow('Exercise angina:', self.angina_input)
        self.inputs.append(self.angina_input)
        
        # Oldpeak (ST segment depression)
        self.oldpeak_input = FloatLineInput(self, 0, 6, 2)
        form_layout.addRow('Oldpeak (ST segment depression):', self.oldpeak_input)
        self.inputs.append(self.oldpeak_input)
        
        # Slope of peak exercise ST segment
        self.slope_input = RadioButtonInput(
            parent = self,
            prompts = ['Up', 'Flat', 'Down'],
            results = ['Up', 'Flat', 'Down']
        )
        form_layout.addRow('Slope of peak exercise ST segment:', self.slope_input)
        self.inputs.append(self.slope_input)

        for input_widget in self.inputs:
            form_layout.labelForField(input_widget).setFont(self.get_font(configs.BODY_FONT_SIZE))
        
        scroll_area.setWidget(form_widget)
        main_layout.addWidget(scroll_area)
        
        # Predict button
        self.predict_button = QPushButton('Predict')
        self.predict_button.setFixedWidth(100)
        self.predict_button.clicked.connect(self.predict)
        self.predict_button.setFont(self.get_font(configs.BODY_FONT_SIZE))
        main_layout.addWidget(self.predict_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Result label
        self.result_widget = QWidget()
        self.result_widget.setObjectName('ResultWidget')
        self.result_widget.setFixedHeight(70)

        self.result_layout = QVBoxLayout()

        self.result_title = QLabel('Prediction result:')
        self.result_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_title.setFont(self.get_font(configs.BODY_FONT_SIZE))

        self.result_label = QLabel('')
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(self.get_font(configs.RESULT_FONT_SIZE))

        self.result_layout.addWidget(self.result_title)
        self.result_layout.addWidget(self.result_label)

        self.result_widget.setLayout(self.result_layout)
        main_layout.addWidget(self.result_widget)
        
        self.setLayout(main_layout)


    def predict(self):
        # Extract data from inputs
        age             = self.age_input.extract()  
        sex             = self.sex_input.extract()
        chest_pain_type = self.cpt_input.extract()
        resting_bp      = self.bp_input.extract()
        cholesterol     = self.chol_input.extract()
        fasting_bs      = self.fbs_input.extract()
        resting_ecg     = self.ecg_input.extract()
        max_hr          = self.hr_input.extract()
        exercise_angina = self.angina_input.extract()
        oldpeak         = self.oldpeak_input.extract()
        st_slope        = self.slope_input.extract()

        pdt = PatientData(
            age = age,
            sex = sex,
            chest_pain_type = chest_pain_type,
            resting_bp = resting_bp,
            cholesterol = cholesterol,
            fasting_bs = fasting_bs,
            resting_ecg = resting_ecg,
            max_hr = max_hr,
            exercise_angina = exercise_angina,
            oldpeak = oldpeak,
            st_slope = st_slope
        )
        
        # For now, we randomize the result
        prediction = self.model.predict(pdt)
        
        # Set the result label
        self.result_label.setText(prediction)

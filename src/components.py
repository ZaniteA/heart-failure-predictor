from PyQt6.QtWidgets import QLineEdit, QVBoxLayout, QButtonGroup, QRadioButton, QPushButton
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from PyQt6.QtCore import Qt

import configs



class IntegerLineInput(QLineEdit):
    def __init__(self, parent, min_value: int, max_value: int):
        super().__init__()
        self.parent = parent
        self.setFixedWidth(configs.LINE_INPUT_WIDTH)
        self.setValidator(QIntValidator(min_value, max_value))
        self.setFont(self.parent.get_font(configs.BODY_FONT_SIZE))


    def extract(self) -> int:
        if not self.text():
            return None
        
        try:
            return int(self.text())
        except ValueError:
            return int(0)
        


class FloatLineInput(QLineEdit):
    def __init__(self, parent, min_value: float, max_value: float, decimal: int):
        super().__init__()
        self.parent = parent
        self.setFixedWidth(configs.LINE_INPUT_WIDTH)
        self.setValidator(QDoubleValidator(min_value, max_value, decimal))
        self.validator().setNotation(QDoubleValidator.Notation.StandardNotation)
        self.setFont(self.parent.get_font(configs.BODY_FONT_SIZE))


    def extract(self) -> float:
        if not self.text():
            return None
        
        try:
            return float(self.text())
        except ValueError:
            return float(0)
        


class RadioButtonInput(QVBoxLayout):
    def __init__(self, parent, prompts: list, results: list):
        super().__init__()
        self.button_group = QButtonGroup(self)
        self.buttons = []
        self.parent = parent
        for prompt in prompts:
            self.buttons.append(QRadioButton(prompt))
            self.buttons[-1].setFont(self.parent.get_font(configs.BODY_FONT_SIZE))
        for button in self.buttons:
            self.button_group.addButton(button)
            self.addWidget(button)

        self.addSpacing(5)

        self.clear_button = QPushButton('Clear')
        self.clear_button.setFont(self.parent.get_font(configs.BODY_FONT_SIZE))
        self.clear_button.setFixedWidth(100)
        self.clear_button.clicked.connect(lambda: self.clear_selection())
        self.addWidget(self.clear_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.results = results


    def clear_selection(self):
        self.button_group.setExclusive(False)
        for button in self.button_group.buttons():
            button.setChecked(False)
        self.button_group.setExclusive(True)

    
    def extract(self):
        for button, result in zip(self.button_group.buttons(), self.results):
            if button.isChecked():
                return result
            
        return None

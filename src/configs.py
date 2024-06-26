WINDOW_WIDTH  = 750
WINDOW_HEIGHT = 600

LINE_INPUT_WIDTH = 100

FALLBACK_FONT    = 'Arial'
TITLE_FONT_SIZE  = 24
RESULT_FONT_SIZE = 20
BODY_FONT_SIZE   = 11

# Colors
BACKGROUND_1   = '#F3EEEA'
BACKGROUND_2   = '#EBE3D5'
INPUT_FIELD    = '#F8F5E2'
HIGHLIGHT      = '#FFFEF5'
OUTLINE        = '#B3A492'
LIGHT_OUTLINE  = '#DDCBB5'
SELECTION      = '#E25E3E'
BUTTON         = '#E25E3E'
BUTTON_PRESSED = '#C63D2F'
BUTTON_HOVER   = '#E68252'

STYLE_SHEET = f'''
#MainApp {{
    background-color: {BACKGROUND_1};
}}

QLabel {{
    color: black;
}}

QScrollArea, #InputForm, #ResultWidget {{
    background-color: {BACKGROUND_2};
    border-radius: 10px;
}}

QLineEdit {{
    background-color: {INPUT_FIELD};
    color: black;

    border: 1px solid;
    border-color: {OUTLINE};
    border-radius: 5px;
    padding: 2px;

    selection-color: white;
    selection-background-color: {SELECTION};
}}
QLineEdit:hover {{
    background-color: {HIGHLIGHT};
}}

QRadioButton {{
    color: black;
}}
QRadioButton::indicator::unchecked {{
    width: 13px;
    height: 13px;
    border-radius: 7px;

    border: 1px solid;
    background-color: {INPUT_FIELD};
    border-color: {BUTTON};
}}
QRadioButton::indicator:unchecked:hover {{
    border: 1px solid;
    background-color: {HIGHLIGHT};
    border-color: {BUTTON_HOVER};
}}
QRadioButton::indicator:unchecked:pressed {{
    border: 1px solid;
    background-color: {INPUT_FIELD};
    border-color: {BUTTON_PRESSED};
}}
QRadioButton::indicator::checked {{
    width: 5px;
    height: 5px;
    border-radius: 7px;

    border: 5px solid;
    border-color: {BUTTON};
}}
QRadioButton::indicator:checked:hover {{
    border: 5px solid;
    background-color: {HIGHLIGHT};
    border-color: {BUTTON_HOVER};
}}
QRadioButton::indicator:checked:pressed {{
    border: 5px solid;
    background-color: {INPUT_FIELD};
    border-color: {BUTTON_PRESSED};
}}

QPushButton {{
    background-color: {BUTTON};
    color: white;
    border: 1px solid;
    border-color: {OUTLINE};
    border-radius: 5px;
    padding: 2px;
}}
QPushButton:hover {{
    background-color: {BUTTON_HOVER};
}}
QPushButton:pressed {{
    background-color: {BUTTON_PRESSED};
}}

QScrollBar:vertical {{
    background: {BACKGROUND_2};
    width: 18px;
    border-radius: 9px;
}}
QScrollBar::handle:vertical {{
    background: {OUTLINE};
    min-height: 20px;
    width: 8px;
    border: 5px solid;
    border-color: {BACKGROUND_2};
    border-radius: 9px;
}}
QScrollBar::add-line:vertical {{
    height: 0px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
    height: 0px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}}
QScrollBar::left-arrow:vertical, QScrollBar::right-arrow:vertical {{
    border: 2px solid grey;
    width: 3px;
    height: 3px;
    background: white;
}}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
    background: none;
}}
'''

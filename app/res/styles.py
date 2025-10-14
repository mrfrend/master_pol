from string import Template
from res.colors import MAIN_COLOR, SECONDARY_COLOR, ACCENT_COLOR
from res.fonts import MAIN_FONT

styles_template = Template(
    """
    QWidget {
        font-family: {MAIN_FONT};
        background-color: {MAIN_COLOR}
        color: {SECONDARY_COLOR};
    }
    QPushButton {
        background-color: {ACCENT_COLOR};
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: {SECONDARY_COLOR};
    }
    QLineEdit {
        padding: 6px;
        border: 1px solid {ACCENT_COLOR};
        border-radius: 4px;
        background-color: white;
    }
"""
)

styles = styles_template.substitute(
    MAIN_FONT=MAIN_FONT,
    MAIN_COLOR=MAIN_COLOR,
    SECONDARY_COLOR=SECONDARY_COLOR,
    ACCENT_COLOR=ACCENT_COLOR,
)

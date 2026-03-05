# qt_styles_project/src/qt_styles/dark.py

import os

"""
Ayu One Dark theme for PyQt6.

This stylesheet is an adaptation of the Ayu One Dark theme from VS Code.
"""

# --- Color Palette (Ayu One Dark) ---
# Primary
BACKGROUND = "#0F1015"
FOREGROUND = "#E6E1CF"
# UI Elements
UI_BACKGROUND = "#14161B"
UI_FOREGROUND = "#C5C5C5"
# Accents
ACCENT_ORANGE = "#FFB454"
ACCENT_BLUE = "#39BAE6"
# Other
BORDER_COLOR = "#393B44"
SELECTION_BACKGROUND = "#303340"
TOOLTIP_BACKGROUND = "#1F2229"
ERROR_RED = "#F07178"

# --- Stylesheet ---
ICON_PATH = os.path.dirname(__file__).replace('\\', '/')

STYLESHEET = f"""
/* ------------------- Global ------------------- */
QWidget {{
    background-color: {BACKGROUND};
    color: {FOREGROUND};
    font-family: "Segoe UI", "Roboto", "Helvetica Neue", "Arial", sans-serif;
    font-size: 14px;
    border: none;
}}

QToolTip {{
    background-color: {TOOLTIP_BACKGROUND};
    color: {FOREGROUND};
    border: 1px solid {BORDER_COLOR};
    padding: 5px;
    border-radius: 3px;
}}

/* ------------------- Checkboxes and Radio Buttons ------------------- */
QCheckBox, QRadioButton {{
    spacing: 8px;
    color: {FOREGROUND};
}}

QCheckBox::indicator, QRadioButton::indicator {{
    width: 16px;
    height: 16px;
    border: 2px solid {ACCENT_BLUE};
    border-radius: 3px;
    background-color: {UI_BACKGROUND};
}}

QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
    border-color: {ACCENT_ORANGE};
    background-color: {SELECTION_BACKGROUND};
}}

QCheckBox::indicator:pressed, QRadioButton::indicator:pressed {{
    border-color: {ACCENT_ORANGE};
    background-color: {SELECTION_BACKGROUND};
}}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {{
    background-color: {ACCENT_BLUE};
    border-color: {ACCENT_BLUE};
}}

QCheckBox::indicator:checked:hover, QRadioButton::indicator:checked:hover {{
    background-color: {ACCENT_ORANGE};
    border-color: {ACCENT_ORANGE};
}}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled {{
    border-color: {BORDER_COLOR};
    background-color: transparent;
}}

QCheckBox::indicator:checked:disabled, QRadioButton::indicator:checked:disabled {{
    background-color: {BORDER_COLOR};
    border-color: {BORDER_COLOR};
}}

/* ------------------- Buttons ------------------- */
QPushButton {{
    background-color: transparent;
    color: {FOREGROUND};
    border: 1px solid transparent;
    padding: 8px 16px;
    border-radius: 4px;
}}

QPushButton:hover {{
    background-color: {SELECTION_BACKGROUND};
    border-color: {ACCENT_BLUE};
}}

QPushButton:pressed {{
    background-color: {ACCENT_BLUE};
    color: {FOREGROUND};
}}

QPushButton:disabled {{
    color: {UI_FOREGROUND};
    border-color: transparent;
}}

/* ------------------- Input Fields ------------------- */
QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, QComboBox {{
    background-color: {UI_BACKGROUND};
    color: {FOREGROUND};
    border: 1px solid {BORDER_COLOR};
    border-radius: 4px;
    padding: 5px;
}}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus {{
    border-color: {ACCENT_ORANGE};
}}

QComboBox::drop-down {{
    border: none;
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
}}

QComboBox::down-arrow {{
    image: url({ICON_PATH}/down_arrow.svg);
    width: 12px;
    height: 12px;
}}

QComboBox::down-arrow:hover {{
    image: url({ICON_PATH}/down_arrow.svg);
}}

QComboBox::down-arrow:pressed {{
    image: url({ICON_PATH}/down_arrow.svg);
}}

/* ------------------- Spin Box Arrows ------------------- */
QSpinBox::up-button, QDoubleSpinBox::up-button {{
    subcontrol-origin: border;
    subcontrol-position: top right;
    width: 20px;
    height: 16px;
    border: none;
    background-color: transparent;
}}

QSpinBox::down-button, QDoubleSpinBox::down-button {{
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width: 20px;
    height: 16px;
    border: none;
    background-color: transparent;
}}

QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {{
    image: url({ICON_PATH}/up_arrow.svg);
    width: 12px;
    height: 12px;
    subcontrol-position: center;
}}

QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {{
    image: url({ICON_PATH}/down_arrow.svg);
    width: 12px;
    height: 12px;
    subcontrol-position: center;
}}

QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover {{
    background-color: {SELECTION_BACKGROUND};
}}

QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {{
    background-color: {SELECTION_BACKGROUND};
}}

/* ------------------- Progress Bar ------------------- */
QProgressBar {{
    border: 1px solid {BORDER_COLOR};
    border-radius: 4px;
    text-align: center;
    color: {FOREGROUND};
    background-color: {UI_BACKGROUND};
    font-weight: bold;
}}

QProgressBar::chunk {{
    background-color: {ACCENT_BLUE};
    border-radius: 3px;
}}

QProgressBar::chunk:disabled {{
    background-color: {BORDER_COLOR};
}}

/* ------------------- Scroll Bars ------------------- */
QScrollBar:vertical {{
    border: none;
    background: transparent;
    width: 10px;
    margin: 0px 0px 0px 0px;
}}

QScrollBar::handle:vertical {{
    background: {SELECTION_BACKGROUND};
    min-height: 20px;
    border-radius: 5px;
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    border: none;
    background: transparent;
    height: 10px;
    margin: 0px 0px 0px 0px;
}}

QScrollBar::handle:horizontal {{
    background: {SELECTION_BACKGROUND};
    min-width: 20px;
    border-radius: 5px;
}}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0px;
}}

/* ------------------- Other Widgets ------------------- */
QHeaderView::section {{
    background-color: {UI_BACKGROUND};
    color: {UI_FOREGROUND};
    padding: 4px;
    border: 1px solid {BORDER_COLOR};
}}

QTableView {{
    gridline-color: {BORDER_COLOR};
}}

/* ------------------- Group Box ------------------- */
QGroupBox {{
    font-weight: bold;
    border: 2px solid {BORDER_COLOR};
    border-radius: 5px;
    margin-top: 10px;
    padding-top: 10px;
    background-color: transparent;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
    background-color: {UI_BACKGROUND};
}}

QMenu {{
    background-color: {UI_BACKGROUND};
    border: 1px solid {BORDER_COLOR};
}}

QMenu::item {{
    padding: 5px 20px;
}}

QMenu::item:selected {{
    background-color: {SELECTION_BACKGROUND};
}}

QMenuBar {{
    background-color: {BACKGROUND};
}}

QMenuBar::item {{
    background-color: transparent;
    padding: 4px 8px;
}}

QMenuBar::item:selected {{
    background-color: {SELECTION_BACKGROUND};
}}
"""

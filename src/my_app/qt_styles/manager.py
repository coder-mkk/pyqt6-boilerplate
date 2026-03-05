# qt_styles_project/src/qt_styles/manager.py

import logging
from PyQt6.QtWidgets import QApplication
from . import dark
from . import light

# Set up a logger for the library
log = logging.getLogger(__name__)

THEMES = {
    'dark': dark.STYLESHEET,
    'light': light.STYLESHEET,
}

def apply_theme(theme: str):
    """
    Applies a theme to the running QApplication instance.

    Args:
        theme (str): The name of the theme to apply.
                     Available themes: 'dark', 'light'.
    """
    app = QApplication.instance()
    if not app:
        raise RuntimeError("No QApplication instance found. Please create one before applying a theme.")

    if theme.lower() in THEMES:
        stylesheet = THEMES[theme.lower()]
        app.setStyleSheet(stylesheet)
        log.info(f"Applied '{theme}' theme.")
    else:
        log.warning(f"Theme '{theme}' not found. Available themes: {list(THEMES.keys())}")
        raise ValueError(f"Theme '{theme}' not found. Available themes: {list(THEMES.keys())}")


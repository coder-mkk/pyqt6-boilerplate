
import sys
import os
import logging
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QSettings
from my_app.presentation.main_window import MainWindow
from my_app.qt_styles import dark, light
from my_app.config.logging_config import setup_logging

def main():
    # Ensure we can find resources if needed
    os.environ["APP_NAME"] = "MyApp"  # Example of setting an environment variable for resource paths
    
    app = QApplication(sys.argv)
    app.setOrganizationName("MyOrg")
    app.setApplicationName("MyApp")

    # Initialize Logging
    setup_logging("MyApp")
    
    # Load and apply saved theme
    settings = QSettings()
    saved_theme = settings.value("theme", "dark")
    
    if saved_theme == "light":
        app.setStyleSheet(light.STYLESHEET)
    else:
        app.setStyleSheet(dark.STYLESHEET)

    window = MainWindow()
    logging.info("Main window created and shown.")
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
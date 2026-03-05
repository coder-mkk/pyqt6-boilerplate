import logging
import sys
import traceback

from PyQt6.QtWidgets import QApplication, QMessageBox


def global_exception_hook(exc_type, exc_value, exc_traceback):
    """
    Global exception handler that logs the exception and shows a dialog.
    """
    # Ensure we don't enter a recursive loop if the handler itself fails
    # This can happen if QApplication is not available
    sys.excepthook = sys.__excepthook__

    try:
        # 1. Log the exception
        logging.critical(
            "Unhandled exception caught by global handler.",
            exc_info=(exc_type, exc_value, exc_traceback),
        )

        # 2. Format the traceback for the dialog
        traceback_details = "".join(
            traceback.format_exception(exc_type, exc_value, exc_traceback)
        )

        # 3. Create and show the message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Application Crash")
        msg_box.setText("An unexpected error occurred.")
        msg_box.setInformativeText(
            "A critical error has been logged. Please check the log file for details."
        )
        msg_box.setDetailedText(traceback_details)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setStyleSheet("QTextEdit { min-width: 600px; }")
        msg_box.exec()

    finally:
        # 4. Exit the application gracefully
        QApplication.instance().quit()

from my_app.presentation.main_window import MainWindow


def test_main_window_creation(qtbot):
    """
    Test that the MainWindow can be created without errors.
    """
    window = MainWindow()
    qtbot.addWidget(window)

    assert not window.isVisible()
    assert window.windowTitle() == "My App"

    window.show()
    assert window.isVisible()

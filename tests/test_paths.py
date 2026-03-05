import sys
from pathlib import Path

import pytest
from my_app.utils.paths import PROJECT_ROOT, get_asset_path


def test_get_asset_path_dev_mode():
    """
    Verify get_asset_path returns correct path in a normal dev environment.
    """
    # Ensure we are not in a frozen environment for this test
    if hasattr(sys, "_MEIPASS"):
        pytest.skip("This test is for development mode only.")

    # Test with a known directory
    relative_dir = "src/my_app/qt_styles"
    expected_path = PROJECT_ROOT / relative_dir
    actual_path = get_asset_path(relative_dir)

    assert actual_path == expected_path
    assert actual_path.exists(), f"Path does not exist: {actual_path}"
    assert actual_path.is_dir()

    # Test with a known file
    relative_file = "pyproject.toml"
    expected_path = PROJECT_ROOT / relative_file
    actual_path = get_asset_path(relative_file)

    assert actual_path == expected_path
    assert actual_path.exists(), f"Path does not exist: {actual_path}"
    assert actual_path.is_file()


def test_get_asset_path_frozen_mode(monkeypatch, tmp_path: Path):
    """
    Verify get_asset_path returns correct path when running as a frozen executable.
    """
    # Simulate the PyInstaller environment by setting sys._MEIPASS
    monkeypatch.setattr(sys, "_MEIPASS", str(tmp_path), raising=False)

    relative_asset = "assets/icon.png"
    expected_path = tmp_path / relative_asset
    assert get_asset_path(relative_asset) == expected_path

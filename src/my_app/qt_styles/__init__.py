# qt_styles_project/src/qt_styles/__init__.py

from .manager import apply_theme
from .icon_manager import (
    get_icon, get_folder_icon, get_file_icon, get_save_icon,
    get_open_icon, get_close_icon, get_settings_icon, get_search_icon,
    get_add_icon, get_delete_icon, get_edit_icon, get_copy_icon,
    get_paste_icon, get_play_icon, get_pause_icon, get_stop_icon,
    get_refresh_icon, get_download_icon, get_upload_icon,
    get_info_icon, get_warning_icon, get_error_icon,
    get_heart_icon, get_star_icon, get_home_icon,
    get_all_file_icons, get_all_action_icons, get_all_media_icons,
    get_all_status_icons, get_all_system_icons, get_all_icons,
    apply_icons_to_widgets, create_toolbar_with_icons, icon_manager
)

# This defines the public API of the package.
__all__ = [
    'apply_theme', 'get_icon', 'get_folder_icon', 'get_file_icon',
    'get_save_icon', 'get_open_icon', 'get_close_icon',
    'get_settings_icon', 'get_search_icon', 'get_add_icon',
    'get_delete_icon', 'get_edit_icon', 'get_copy_icon',
    'get_paste_icon', 'get_play_icon', 'get_pause_icon',
    'get_stop_icon', 'get_refresh_icon', 'get_download_icon',
    'get_upload_icon', 'get_info_icon', 'get_warning_icon',
    'get_error_icon', 'get_heart_icon', 'get_star_icon',
    'get_home_icon', 'get_all_file_icons', 'get_all_action_icons',
    'get_all_media_icons', 'get_all_status_icons', 'get_all_system_icons',
    'get_all_icons', 'apply_icons_to_widgets', 'create_toolbar_with_icons',
    'icon_manager'
]


from app.automation.app_commands import (
    open_chrome,
    open_notepad,
    open_calculator,
    open_paint,
    open_vscode
)

from app.automation.browser_commands import (
    open_browser
)

from app.automation.system_commands import (
    open_camera,
    open_settings,
    open_task_manager,
    open_cmd,
    open_explorer,
    open_downloads
)


COMMANDS = {

    # ==========================
    # Browser
    # ==========================

    "chrome": open_chrome,
    "google chrome": open_chrome,
    "browser": open_browser,
    "open browser": open_browser,

    # ==========================
    # Apps
    # ==========================

    "notepad": open_notepad,
    "calculator": open_calculator,
    "calc": open_calculator,
    "paint": open_paint,
    "vs code": open_vscode,
    "visual studio code": open_vscode,

    # ==========================
    # System
    # ==========================

    "camera": open_camera,
    "webcam": open_camera,
    "settings": open_settings,
    "task manager": open_task_manager,
    "command prompt": open_cmd,
    "cmd": open_cmd,
    "file explorer": open_explorer,
    "explorer": open_explorer,
    "downloads": open_downloads,
}
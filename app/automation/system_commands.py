import subprocess
import os


def open_camera():

    subprocess.Popen(
        "start microsoft.windows.camera:",
        shell=True
    )

    return "📷 Opening Camera."


def open_settings():

    subprocess.Popen(
        "start ms-settings:",
        shell=True
    )

    return "⚙️ Opening Windows Settings."


def open_task_manager():

    subprocess.Popen("taskmgr.exe")

    return "📊 Opening Task Manager."


def open_cmd():

    subprocess.Popen("cmd.exe")

    return "⌨️ Opening Command Prompt."


def open_explorer():

    subprocess.Popen("explorer")

    return "📂 Opening File Explorer."


def open_downloads():

    downloads = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    subprocess.Popen(["explorer", downloads])

    return "📥 Opening Downloads."
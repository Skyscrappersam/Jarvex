import subprocess


def open_chrome():
    subprocess.Popen(
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
    return "🌐 Opening Google Chrome."


def open_notepad():
    subprocess.Popen("notepad.exe")
    return "📝 Opening Notepad."


def open_calculator():
    subprocess.Popen("calc.exe")
    return "🧮 Opening Calculator."


def open_paint():
    subprocess.Popen("mspaint.exe")
    return "🎨 Opening Paint."


def open_vscode():
    subprocess.Popen("code")
    return "💻 Opening VS Code."
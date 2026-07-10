import subprocess


def open_browser():
    subprocess.Popen(
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
    return "🌐 Opening Browser."
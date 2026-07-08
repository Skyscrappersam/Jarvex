import subprocess

def execute_command(command):
    command = command.lower()

    if "chrome" in command:
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        return "Opening Google Chrome."

    elif "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    elif "calculator" in command or "calc" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    elif "paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint."

    elif "vs code" in command or "visual studio code" in command:
        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    else:
        return None
from app.automation.command_registry import COMMANDS


def execute_command(command):

    command = command.lower().strip()

    for keyword, action in COMMANDS.items():

        if keyword in command:

            return action()

    return None
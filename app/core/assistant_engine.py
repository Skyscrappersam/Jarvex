class AssistantEngine:

    def __init__(self):

        self.version = "4.0"

        self.name = "Jarvex"

    def get_info(self):

        return {
            "name": self.name,
            "version": self.version
        }

    def greet(self):

        return "Hello! I'm Jarvex AI Assistant."
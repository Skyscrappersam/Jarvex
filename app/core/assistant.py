class JarvexAssistant:

    def __init__(self):
        self.name = "Jarvex"


    def process(self, message):

        message = message.lower()


        if "hello" in message or "hi" in message:
            return "Hello Suraj. How can I help you?"


        elif "your name" in message:
            return "I am Jarvex, your personal AI assistant."


        elif "time" in message:
            import datetime
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"


        elif "date" in message:
            import datetime
            today = datetime.date.today()
            return f"Today's date is {today}"


        elif "bye" in message:
            return "Goodbye Suraj. I will be here when you need me."


        else:
            return "I am still learning. Please teach me more commands."
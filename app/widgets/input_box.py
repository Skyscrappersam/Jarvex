import customtkinter as ctk


class InputBox(ctk.CTkFrame):
    def __init__(self, parent, send_callback, mic_callback):
        super().__init__(parent)

        self.send_callback = send_callback
        self.mic_callback = mic_callback


        self.entry = ctk.CTkEntry(
            self,
            placeholder_text="Type your message...",
            height=40,
            font=("Arial", 14)
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=10
        )


        self.send_button = ctk.CTkButton(
            self,
            text="Send",
            width=80,
            command=self.send_message
        )

        self.send_button.pack(
            side="left",
            padx=5
        )


        self.mic_button = ctk.CTkButton(
            self,
            text="🎤 Mic",
            width=80,
            command=self.mic_callback
        )

        self.mic_button.pack(
            side="left",
            padx=5
        )


        self.entry.bind(
            "<Return>",
            lambda event: self.send_message()
        )


    def send_message(self):
        message = self.entry.get()

        if message.strip():
            self.send_callback(message)
            self.entry.delete(0, "end")
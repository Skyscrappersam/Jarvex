import customtkinter as ctk


class ChatArea(ctk.CTkTextbox):

    def __init__(self, master):

        super().__init__(
            master,
            width=900,
            height=500,
            font=("Arial", 15),
            corner_radius=12
        )

        self.pack(padx=15, pady=10)

        self.configure(state="disabled")

        self.add_message(
            "Jarvex",
            "Hello Suraj! 👋\nHow can I help you today?"
        )

    def add_message(self, sender, message):

        self.configure(state="normal")

        if sender == "You":
            self.insert("end", f"👤 You: {message}\n\n")
        else:
            self.insert("end", f"🤖 Jarvex: {message}\n\n")

        self.configure(state="disabled")

        self.see("end")

    def clear(self):

        self.configure(state="normal")

        self.delete("1.0", "end")

        self.configure(state="disabled")

        self.add_message(
            "Jarvex",
            "Hello Suraj! 👋\nHow can I help you today?"
        )
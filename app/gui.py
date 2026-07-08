import customtkinter as ctk

from app.router import process_command
from app.voice import speak
from app.listener import listen


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JarvexGUI:

    def __init__(self):

        self.window = ctk.CTk()

        self.voice_enabled = True

        self.window.title("🤖 Jarvex AI Assistant")
        self.window.geometry("900x650")
        self.window.resizable(False, False)

        title = ctk.CTkLabel(
            self.window,
            text="🤖 Jarvex AI Assistant",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.chat = ctk.CTkTextbox(
            self.window,
            width=820,
            height=430,
            font=("Arial", 15)
        )
        self.chat.pack(pady=10)

        self.chat.insert("end", "Jarvex: Hello Suraj! 👋\n")
        self.chat.insert("end", "Jarvex: How can I help you today?\n\n")
        self.chat.configure(state="disabled")

        bottom = ctk.CTkFrame(self.window)
        bottom.pack(pady=15)

        self.entry = ctk.CTkEntry(
            bottom,
            width=500,
            height=40,
            placeholder_text="Type your message..."
        )
        self.entry.grid(row=0, column=0, padx=10)

        self.entry.bind("<Return>", self.send_message)

        self.send_button = ctk.CTkButton(
            bottom,
            text="📤 Send",
            width=90,
            command=self.send_message
        )
        self.send_button.grid(row=0, column=1, padx=5)

        self.mic_button = ctk.CTkButton(
            bottom,
            text="🎤",
            width=60,
            command=self.voice_input
        )
        self.mic_button.grid(row=0, column=2, padx=5)

        self.voice_button = ctk.CTkButton(
            bottom,
            text="🔊 Voice: ON",
            width=120,
            command=self.toggle_voice
        )
        self.voice_button.grid(row=0, column=3, padx=5)

        self.entry.focus()

        self.window.mainloop()

    def add_chat(self, speaker, message):

        self.chat.configure(state="normal")

        self.chat.insert("end", f"{speaker}: {message}\n\n")

        self.chat.configure(state="disabled")

        self.chat.see("end")

    def send_message(self, event=None):

        user = self.entry.get().strip()

        if user == "":
            return

        self.add_chat("You", user)

        self.entry.delete(0, "end")

        self.window.update()

        reply = process_command(user)

        self.add_chat("Jarvex", reply)

        if self.voice_enabled:
            speak(reply)

    def voice_input(self):

        self.add_chat("Jarvex", "🎤 Listening...")

        self.window.update()

        user = listen()

        if not user:
            self.add_chat("Jarvex", "I didn't hear anything.")
            return

        self.add_chat("You", user)

        reply = process_command(user)

        self.add_chat("Jarvex", reply)

        if self.voice_enabled:
            speak(reply)

    def toggle_voice(self):

        self.voice_enabled = not self.voice_enabled

        if self.voice_enabled:
            self.voice_button.configure(text="🔊 Voice: ON")
            self.add_chat("Jarvex", "Voice responses enabled.")
        else:
            self.voice_button.configure(text="🔇 Voice: OFF")
            self.add_chat("Jarvex", "Voice responses disabled.")


if __name__ == "__main__":
    JarvexGUI()
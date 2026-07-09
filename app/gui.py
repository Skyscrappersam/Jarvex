import customtkinter as ctk

from app.router import process_command
from app.voice import speak
from app.listener import listen

from app.widgets.header import Header
from app.widgets.chat_area import ChatArea


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class JarvexGUI:

    def __init__(self):

        self.window = ctk.CTk()

        self.voice_enabled = True

        self.window.title("🤖 Jarvex AI Assistant")
        self.window.geometry("950x700")
        self.window.resizable(False, False)

        # ==========================
        # Header
        # ==========================

        self.header = Header(
            self.window,
            self.clear_chat
        )

        # ==========================
        # Chat Area
        # ==========================

        self.chat = ChatArea(self.window)

        # ==========================
        # Bottom Input Area
        # ==========================

        bottom = ctk.CTkFrame(self.window, corner_radius=12)
        bottom.pack(fill="x", padx=15, pady=15)

        self.entry = ctk.CTkEntry(
            bottom,
            placeholder_text="Type your message...",
            height=42,
            width=520
        )

        self.entry.grid(row=0, column=0, padx=10, pady=15)

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
            text="🔊 Voice ON",
            width=120,
            command=self.toggle_voice
        )

        self.voice_button.grid(row=0, column=3, padx=10)

        self.entry.focus()

        self.window.mainloop()

    # ========================================

    def add_chat(self, speaker, message):

        self.chat.add_message(speaker, message)

    # ========================================

    def clear_chat(self):

        self.chat.clear()

        self.header.set_status("🟢 Ready")

    # ========================================

    def send_message(self, event=None):

        user = self.entry.get().strip()

        if not user:
            return

        self.add_chat("You", user)

        self.entry.delete(0, "end")

        self.header.set_status("🤖 Thinking...")

        self.window.update()

        reply = process_command(user)

        self.add_chat("Jarvex", reply)

        if self.voice_enabled:

            self.header.set_status("🔊 Speaking...")

            speak(reply)

        self.header.set_status("🟢 Ready")

    # ========================================

    def voice_input(self):

        self.header.set_status("🎤 Listening...")

        self.add_chat("Jarvex", "Listening...")

        self.window.update()

        user = listen()

        if not user:

            self.add_chat(
                "Jarvex",
                "I didn't hear anything."
            )

            self.header.set_status("🟢 Ready")

            return

        self.add_chat("You", user)

        self.header.set_status("🤖 Thinking...")

        reply = process_command(user)

        self.add_chat("Jarvex", reply)

        if self.voice_enabled:

            self.header.set_status("🔊 Speaking...")

            speak(reply)

        self.header.set_status("🟢 Ready")

    # ========================================

    def toggle_voice(self):

        self.voice_enabled = not self.voice_enabled

        if self.voice_enabled:

            self.voice_button.configure(
                text="🔊 Voice ON"
            )

            self.add_chat(
                "Jarvex",
                "Voice responses enabled."
            )

        else:

            self.voice_button.configure(
                text="🔇 Voice OFF"
            )

            self.add_chat(
                "Jarvex",
                "Voice responses disabled."
            )


if __name__ == "__main__":
    JarvexGUI()
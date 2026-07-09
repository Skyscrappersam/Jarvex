import threading
import customtkinter as ctk

from app.router import process_command
from app.voice import speak
from app.listener import listen

from app.widgets.header import Header
from app.widgets.chat_area import ChatArea
from app.widgets.settings_window import SettingsWindow
from app.widgets.typing_indicator import TypingIndicator

from app.config.settings import load_settings, save_settings

from app.history.history_manager import (
    load_history,
    add_message,
    clear_history
)


class JarvexGUI:

    def __init__(self):

        # ==========================
        # Load Settings
        # ==========================

        self.settings = load_settings()

        ctk.set_appearance_mode(
            self.settings.get("theme", "dark").capitalize()
        )

        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()

        self.voice_enabled = self.settings.get("voice", True)

        self.window.title("🤖 Jarvex AI Assistant")
        self.window.geometry("950x700")
        self.window.resizable(False, False)

        # ==========================
        # Header
        # ==========================

        self.header = Header(
            self.window,
            self.clear_chat,
            self.open_settings
        )

        # ==========================
        # Chat Area
        # ==========================

        self.chat = ChatArea(self.window)

        # ==========================
        # Load Conversation History
        # ==========================

        history = load_history()

        if history:

            for item in history:
                self.chat.add_message(
                    item["sender"],
                    item["message"]
                )

        else:

            self.chat.add_message(
                "Jarvex",
                "Hello Suraj! 👋"
            )

            self.chat.add_message(
                "Jarvex",
                "How can I help you today?"
            )

            add_message("Jarvex", "Hello Suraj! 👋")
            add_message("Jarvex", "How can I help you today?")

        # ==========================
        # Bottom Frame
        # ==========================

        bottom = ctk.CTkFrame(
            self.window,
            corner_radius=12
        )

        bottom.pack(fill="x", padx=15, pady=15)

        self.entry = ctk.CTkEntry(
            bottom,
            width=520,
            height=42,
            placeholder_text="Type your message..."
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
            width=120,
            command=self.toggle_voice
        )

        if self.voice_enabled:
            self.voice_button.configure(text="🔊 Voice ON")
        else:
            self.voice_button.configure(text="🔇 Voice OFF")

        self.voice_button.grid(row=0, column=3, padx=10)

        self.entry.focus()

        self.window.mainloop()

    # ======================================

    def open_settings(self):

        SettingsWindow(self.window)

    # ======================================

    def add_chat(self, speaker, message):

        self.chat.add_message(speaker, message)

        add_message(speaker, message)

    # ======================================

    def clear_chat(self):

        self.chat.clear()

        clear_history()

        self.header.set_status("🟢 Ready")

    # ======================================

    def send_message(self, event=None):

        user = self.entry.get().strip()

        if not user:
            return

        self.add_chat("You", user)

        self.entry.delete(0, "end")

        self.entry.configure(state="disabled")
        self.send_button.configure(state="disabled")
        self.mic_button.configure(state="disabled")

        self.header.set_status("🤖 Thinking...")

        self.typing = TypingIndicator(self.chat)
        self.typing.start()

        threading.Thread(
            target=self.process_text_request,
            args=(user,),
            daemon=True
        ).start()

    # ======================================

    def process_text_request(self, user):

        reply = process_command(user)

        self.window.after(
            0,
            lambda: self.finish_response(reply)
        )

    # ======================================

    def finish_response(self, reply):

        self.typing.stop()

        self.add_chat("Jarvex", reply)

        if self.voice_enabled:

            self.header.set_status("🔊 Speaking...")

            threading.Thread(
                target=speak,
                args=(reply,),
                daemon=True
            ).start()

        self.entry.configure(state="normal")
        self.send_button.configure(state="normal")
        self.mic_button.configure(state="normal")

        self.entry.focus()

        self.header.set_status("🟢 Ready")

    # ======================================

    def voice_input(self):

        self.header.set_status("🎤 Listening...")

        user = listen()

        if not user:

            self.add_chat(
                "Jarvex",
                "I didn't hear anything."
            )

            self.header.set_status("🟢 Ready")

            return

        self.add_chat("You", user)

        self.entry.configure(state="disabled")
        self.send_button.configure(state="disabled")
        self.mic_button.configure(state="disabled")

        self.typing = TypingIndicator(self.chat)
        self.typing.start()

        threading.Thread(
            target=self.process_voice_request,
            args=(user,),
            daemon=True
        ).start()

    # ======================================

    def process_voice_request(self, user):

        reply = process_command(user)

        self.window.after(
            0,
            lambda: self.finish_response(reply)
        )

    # ======================================

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

        self.settings["voice"] = self.voice_enabled

        save_settings(self.settings)


if __name__ == "__main__":
    JarvexGUI()
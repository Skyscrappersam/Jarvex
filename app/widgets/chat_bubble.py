import customtkinter as ctk
from datetime import datetime


class ChatBubble(ctk.CTkFrame):

    def __init__(self, master, sender, message):

        super().__init__(master, fg_color="transparent")

        # ==========================
        # Sender Style
        # ==========================

        if sender == "You":
            anchor = "e"
            bubble_color = "#2563EB"
            sender_text = "👤 You"
            text_color = "white"
        else:
            anchor = "w"
            bubble_color = "#2B2B2B"
            sender_text = "🤖 Jarvex"
            text_color = "white"

        self.pack(
            fill="x",
            padx=15,
            pady=8
        )

        # ==========================
        # Container
        # ==========================

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(anchor=anchor)

        # ==========================
        # Sender Label
        # ==========================

        sender_label = ctk.CTkLabel(
            container,
            text=sender_text,
            font=("Arial", 12, "bold")
        )

        sender_label.pack(anchor=anchor)

        # ==========================
        # Bubble
        # ==========================

        bubble = ctk.CTkLabel(
            container,
            text=message,
            wraplength=520,
            justify="left",
            fg_color=bubble_color,
            text_color=text_color,
            corner_radius=18,
            padx=18,
            pady=12,
            font=("Arial", 15)
        )

        bubble.pack(anchor=anchor, pady=(2, 0))

        # ==========================
        # Timestamp
        # ==========================

        current_time = datetime.now().strftime("%I:%M %p")

        timestamp = ctk.CTkLabel(
            container,
            text=current_time,
            font=("Arial", 10),
            text_color="gray"
        )

        timestamp.pack(anchor=anchor, pady=(2, 0))
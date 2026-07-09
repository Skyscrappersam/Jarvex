import customtkinter as ctk


class ChatBubble(ctk.CTkFrame):

    def __init__(self, master, sender, message):

        super().__init__(master, fg_color="transparent")

        if sender == "You":
            anchor = "e"
            bubble_color = "#2563EB"
            text_color = "white"
            sender_text = "👤 You"
        else:
            anchor = "w"
            bubble_color = "#2B2B2B"
            text_color = "white"
            sender_text = "🤖 Jarvex"

        self.pack(fill="x", padx=15, pady=5, anchor=anchor)

        sender_label = ctk.CTkLabel(
            self,
            text=sender_text,
            font=("Arial", 12, "bold")
        )

        sender_label.pack(anchor=anchor, padx=10)

        bubble = ctk.CTkLabel(
            self,
            text=message,
            justify="left",
            wraplength=500,
            fg_color=bubble_color,
            corner_radius=15,
            text_color=text_color,
            padx=15,
            pady=10,
            font=("Arial", 15)
        )

        bubble.pack(anchor=anchor, padx=10)
import customtkinter as ctk
from app.widgets.chat_bubble import ChatBubble


class ChatArea(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=12,
            fg_color="#1E1E1E"
        )

        self.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

    def add_message(self, sender, message):

        ChatBubble(
            self,
            sender,
            message
        )

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()
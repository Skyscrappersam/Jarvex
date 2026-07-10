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

        self.streaming_bubble = None

    # =====================================
    # Normal Message
    # =====================================

    def add_message(self, sender, message):

        ChatBubble(
            self,
            sender,
            message
        )

        self.scroll_to_bottom()

    # =====================================
    # Start Streaming
    # =====================================

    def start_stream(self, sender="Jarvex"):

        self.streaming_bubble = ChatBubble(
            self,
            sender,
            ""
        )

        self.scroll_to_bottom()

    # =====================================
    # Update Streaming Bubble
    # =====================================

    def update_stream(self, text):

        if self.streaming_bubble:

            self.streaming_bubble.update_message(text)

            self.scroll_to_bottom()

    # =====================================
    # Finish Streaming
    # =====================================

    def finish_stream(self):

        if self.streaming_bubble:

            self.streaming_bubble.finish()

            self.streaming_bubble = None

    # =====================================
    # Auto Scroll
    # =====================================

    def scroll_to_bottom(self):

        self.update_idletasks()

        try:
            self._parent_canvas.yview_moveto(1.0)
        except Exception:
            pass

    # =====================================
    # Clear Chat
    # =====================================

    def clear(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.streaming_bubble = None
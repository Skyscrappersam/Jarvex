import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master, clear_callback):

        super().__init__(master, corner_radius=12)

        self.pack(fill="x", padx=15, pady=15)

        # ==========================
        # Title
        # ==========================

        self.title = ctk.CTkLabel(
            self,
            text="🤖 Jarvex AI Assistant",
            font=("Arial", 28, "bold")
        )

        self.title.pack(side="left", padx=20, pady=15)

        # ==========================
        # Clear Chat Button
        # ==========================

        self.clear_button = ctk.CTkButton(
            self,
            text="🗑 Clear Chat",
            width=120,
            command=clear_callback
        )

        self.clear_button.pack(side="right", padx=10)

        # ==========================
        # Status
        # ==========================

        self.status = ctk.CTkLabel(
            self,
            text="🟢 Ready",
            font=("Arial", 16, "bold")
        )

        self.status.pack(side="right", padx=15)

    def set_status(self, text):

        self.status.configure(text=text)
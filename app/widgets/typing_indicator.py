import customtkinter as ctk


class TypingIndicator(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, fg_color="transparent")

        self.pack(fill="x", padx=15, pady=8)

        self.label = ctk.CTkLabel(
            self,
            text="🤖 Jarvex is typing",
            font=("Arial", 13, "italic")
        )

        self.label.pack(anchor="w")

        self.dots = 0
        self.running = False

    def start(self):

        self.running = True
        self.animate()

    def stop(self):

        self.running = False
        self.destroy()

    def animate(self):

        if not self.running:
            return

        self.dots = (self.dots + 1) % 4

        self.label.configure(
            text="🤖 Jarvex is typing" + "." * self.dots
        )

        self.after(400, self.animate)
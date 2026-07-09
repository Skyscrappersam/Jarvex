import customtkinter as ctk


class SettingsWindow(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Jarvex Settings")
        self.geometry("450x450")
        self.resizable(False, False)

        self.grab_set()

        title = ctk.CTkLabel(
            self,
            text="⚙️ Settings",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=20)

        appearance_label = ctk.CTkLabel(
            self,
            text="Appearance",
            font=("Arial", 16, "bold")
        )
        appearance_label.pack(anchor="w", padx=25, pady=(10, 5))

        appearance = ctk.CTkOptionMenu(
            self,
            values=["Dark", "Light", "System"]
        )
        appearance.set("Dark")
        appearance.pack(fill="x", padx=25)

        voice_switch = ctk.CTkSwitch(
            self,
            text="Enable Voice Responses"
        )
        voice_switch.select()
        voice_switch.pack(anchor="w", padx=25, pady=20)

        info = ctk.CTkLabel(
            self,
            text=(
                "Jarvex AI Assistant\n"
                "Version 3.2\n\n"
                "More settings coming soon..."
            ),
            justify="center"
        )
        info.pack(side="bottom", pady=30)
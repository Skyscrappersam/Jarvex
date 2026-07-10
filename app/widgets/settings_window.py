import customtkinter as ctk

from app.config.settings import load_settings, save_settings


class SettingsWindow(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.title("Jarvex Settings")
        self.geometry("450x500")
        self.resizable(False, False)

        self.grab_set()

        # ==========================
        # Load Settings
        # ==========================

        self.settings = load_settings()

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="⚙️ Jarvex Settings",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # ==========================
        # Theme
        # ==========================

        theme_label = ctk.CTkLabel(
            self,
            text="Theme",
            font=("Arial", 16, "bold")
        )

        theme_label.pack(anchor="w", padx=25)

        self.theme_menu = ctk.CTkOptionMenu(
            self,
            values=[
                "Dark",
                "Light",
                "System"
            ]
        )

        current_theme = self.settings.get("theme", "dark").capitalize()

        self.theme_menu.set(current_theme)

        self.theme_menu.pack(
            fill="x",
            padx=25,
            pady=(5, 20)
        )

        # ==========================
        # Voice
        # ==========================

        self.voice_switch = ctk.CTkSwitch(
            self,
            text="Enable Voice Responses"
        )

        if self.settings.get("voice", True):
            self.voice_switch.select()
        else:
            self.voice_switch.deselect()

        self.voice_switch.pack(
            anchor="w",
            padx=25,
            pady=10
        )

        # ==========================
        # Save Button
        # ==========================

        save_button = ctk.CTkButton(
            self,
            text="💾 Save Settings",
            command=self.save
        )

        save_button.pack(pady=25)

        # ==========================
        # Info
        # ==========================

        info = ctk.CTkLabel(
            self,
            text=(
                "Jarvex AI Assistant\n"
                "Version 3.6\n\n"
                "Theme changes will apply\n"
                "the next time you launch Jarvex."
            ),
            justify="center"
        )

        info.pack(side="bottom", pady=25)

    # ==========================
    # Save Settings
    # ==========================

    def save(self):

        self.settings["theme"] = (
            self.theme_menu.get().lower()
        )

        self.settings["voice"] = (
            self.voice_switch.get() == 1
        )

        save_settings(self.settings)

        self.destroy()
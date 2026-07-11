
from PySide6.QtWidgets import QDialog

from controllers.language_settings import LanguageSettingsController
from ui.settings.settings_ui import Ui_Settings
from utils.mixins import RetranslateMixin


class Settings(RetranslateMixin, QDialog):

    def setup_ui(self):
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        language_settings_controller = LanguageSettingsController(self)
        language_settings_controller.setup_ui()

        self.ui.setting_stackwidget_main.addWidget(language_settings_controller)

        self.ui.language_btn.clicked.connect(self.open_language_settings)

    def open_language_settings(self):
        self.ui.setting_stackwidget_main.setCurrentIndex(1)

from typing import override

from PySide6.QtWidgets import QTabWidget

from utils.logger import get_logger

# Codes Here

logger = get_logger()


class BaseScreen(QTabWidget):
    """Screen that comes inside main application procss
    """

    def __init__(self, *args, **kwargs) -> None:
        super(BaseScreen, self).__init__(*args, **kwargs)
        self.logger = logger

    @override
    def setup_ui(self):  # type: ignore
        pass

    @property
    @override
    def NAME(self) -> str:  # type: ignore
        """Sidebar label, re-evaluated on every access for live translation."""
        return self.tr  # type: ignore

from PySide6.QtCore import QEvent


class RetranslateMixin:
    """
    Requirements:
        - self.ui exists
        - self.ui has retranslateUi()
    """

    def changeEvent(self, event: QEvent, /) -> None:
        super().changeEvent(event)  # pyright: ignore[reportAttributeAccessIssue]

        if event.type() == QEvent.Type.LanguageChange or event.type() == QEvent.Type.FontChange:
            if hasattr(self, "ui") and hasattr(self.ui, "retranslateUi"):  # pyright: ignore[reportAttributeAccessIssue]
                self.ui.retranslateUi(self)  # pyright: ignore[reportAttributeAccessIssue]
                
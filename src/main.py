#! /usr/bin/env python3
import sys

# Reources
import source_rc
# Local imports
from app import Application
from main_window import MainWindow
from utils.logger import get_logger
from utils.settings import APP_NAME
from utils.shortcutes import get_database_path, initialize_database

# Codes Here
logger = get_logger(APP_NAME)


def main():
    try:
        # Initialize database
        db_path = get_database_path()
        initialize_database(db_path)

        # Set up application
        app = Application().run()

        # Create and show main window
        main_window = MainWindow()
        # main_window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # main_window.setWindowState(Qt.WindowState.WindowMaximized)
        main_window.setMinimumWidth(1024)
        main_window.setMinimumHeight(768)

        main_window.show()

        # Start event loop
        exit_code = app.exec()

        sys.exit(exit_code)

    except Exception as e:
        logger.critical(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

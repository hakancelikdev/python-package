import logging

__all__ = ("logger",)

ColoredStringFormat = "%(asctime)s [%(levelname)s] %(processName)s/%(threadName)s | %(filename)s:%(lineno)d - %(name)s.%(funcName)s(): %(message)s"

logger = logging.getLogger("{{cookiecutter.project_slug}}")  # unexport: public
logger.setLevel(logging.DEBUG)

_COLORS = {
    "DEBUG": "\033[94m",  # Blue
    "INFO": "\033[92m",  # Green
    "WARNING": "\033[93m",  # Yellow
    "ERROR": "\033[91m",  # Red
    "CRITICAL": "\033[41m\033[97m",  # White text on red background
}

_RESET_COLOR = "\033[0m"  # Reset to default color


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        msg = super().format(record)
        color = _COLORS.get(levelname, _RESET_COLOR)
        return f"{color}{msg}{_RESET_COLOR}"


if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = ColoredFormatter(ColoredStringFormat)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)


if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

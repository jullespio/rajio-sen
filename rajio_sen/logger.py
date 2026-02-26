import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(
        show_path=False,    # Removes 'handler.py:87'
        show_level=False,   # Removes the 'INFO' tag for a cleaner look
        markup=True,
        rich_tracebacks=True
    )]
)

log = logging.getLogger("rajio")
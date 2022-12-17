import logging
from mkdocs.utils import warning_filter

# Set up a logger for my code to use
LOGGER = logging.getLogger("mkdocs.plugins.autotags")
LOGGER.addFilter(warning_filter)

def warning(message: str) -> None:
    LOGGER.warning(f"[auto-tags] {message}")

# Import local files in the correct order
# from .utils import replace_regex_matches
# from .normal_badge import replace_normal_badges
from .plugin import Plugin

__all__ = ["Plugin"]

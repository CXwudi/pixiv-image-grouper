import logging

def setup_logging() -> None:
    """Configure logging for the entire application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def get_logger(name: str) -> logging.Logger:
    """Get a configured logger for the given module name."""
    return logging.getLogger(name)
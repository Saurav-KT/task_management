from loguru import logger
import sys
class GenericLogger:
    def __init__(
            self,
            log_file: str = "app.log",
            rotation: str = "10 MB",
            retention: str = "30 days",
            level: str = "INFO",
            date_format: str = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
            serialize: bool = False
    ):
        """
                Initialize the generic logger with Loguru.

                Args:
                    log_file: Path to the log file. If None, logs only to console.
                    rotation: Log rotation condition (e.g., "10 MB", "1 day")
                    retention: Log retention period (e.g., "30 days")
                    level: Minimum logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    format: Log message format
                    serialize: Whether to serialize logs as JSON
                """
        # Remove default handler if present
        logger.remove()

        # Add console handler
        logger.add(
            sys.stderr,
            level=level,
            format=format,
            colorize=True
        )
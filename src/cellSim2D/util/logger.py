
import logging
from typing import Optional 
from pathlib import Path

# SHARED LOGGER FOR THIS PACKAGE

_logger = logging.getLogger('cellSim2D')

def configure_logger(print_level: str = 'info', logfile: Optional[Path] = None):
    """
    Configuration of Logger
    """

    _logger.setLevel(logging.DEBUG)

    # Remove any existing handlers
    while _logger.hasHandlers():
        _logger.handlers[0].close
        _logger.removeHandler(_logger.handlers[0])

    # Create a handler for console output, format the messages
    stdout_level = None
    match print_level.lower():
        case 'debug':
            stdout_level = logging.DEBUG
        case 'info':
            stdout_level = logging.INFO
        case 'warning':
            stdout_level = logging.WARNING
        case 'error':
            stdout_level = logging.ERROR
        case 'critical':
            stdout_level = logging.CRITICAL
        case _:
            pass

    # If a valid log level for output provided, create stream handler
    if stdout_level != None:
        handler = logging.StreamHandler()
        handler.setLevel(stdout_level)

        formatter = logging.Formatter(
            "[%(filename)s: %(lineno)d || %(funcName)s]: %(Message)s"
        )
        handler.setFormatter(formatter)
        _logger.addHandler(handler)

    # Create a handler for file output, format messages
    if logfile is not None:

        #If logfile already exists, delete it first
        if logfile.exists():
            logfile.unlink()
        
        handler = logging.FileHandler(logfile)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(levelname)s] [%(asctime)s] [%(filename)s : %(lineno)d || %(funcName)s]: %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        _logger.addHandler(handler)
    
    return

from template_project.util.logger import _logger, configure_logger

if __name__ == "__main__":
    configure_logger(print_level='info', logfile=None)
    _logger.info("This is an example project.")
    _logger.warning("This file is unnecessary, please delete when creating project.")
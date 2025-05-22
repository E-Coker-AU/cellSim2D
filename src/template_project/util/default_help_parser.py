
from argparse import ArgumentParser
import sys

class DefaultHelpParser(ArgumentParser):
    """
    'argparse' provides classes and methods for parsing arguments provided
    from the command line. 

    Adapted from C. Pulley, who adapted from:
    https://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    """
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
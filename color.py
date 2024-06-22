from enum import Enum

class Foreground(Enum):
    BLACK           = '\033[30m'
    RED             = '\033[31m'
    GREEN           = '\033[32m'
    YELLOW          = '\033[33m'
    BLUE            = '\033[34m'
    MAGENTA         = '\033[35m'
    CYAN            = '\033[36m'
    WHITE           = '\033[37m'
    BRIGHT_BLACK    = '\033[90m'
    BRIGHT_RED      = '\033[91m'
    BRIGHT_GREEN    = '\033[92m'
    BRIGHT_YELLOW   = '\033[93m'
    BRIGHT_BLUE     = '\033[94m'
    BRIGHT_MAGENTA  = '\033[95m'
    BRIGHT_CYAN     = '\033[96m'
    BRIGHT_WHITE    = '\033[97m'
    RESET           = '\033[39m'

    def __str__(self):
        return self.value

class Background(Enum):
    BLACK           = '\033[40m'
    RED             = '\033[41m'
    GREEN           = '\033[42m'
    YELLOW          = '\033[43m'
    BLUE            = '\033[44m'
    MAGENTA         = '\033[45m'
    CYAN            = '\033[46m'
    WHITE           = '\033[47m'
    BRIGHT_BLACK    = '\033[100m'
    BRIGHT_RED      = '\033[101m'
    BRIGHT_GREEN    = '\033[102m'
    BRIGHT_YELLOW   = '\033[103m'
    BRIGHT_BLUE     = '\033[104m'
    BRIGHT_MAGENTA  = '\033[105m'
    BRIGHT_CYAN     = '\033[106m'
    BRIGHT_WHITE    = '\033[107m'
    RESET           = '\033[49m'

    def __str__(self):
        return self.value

class Style(Enum):
    BRIGHT          = '\033[1m'
    DIM             = '\033[2m'
    ITALIC          = '\033[3m'
    UNDERLINE       = '\033[4m'
    BLINK           = '\033[5m'
    REVERSE         = '\033[7m'
    HIDDEN          = '\033[8m'
    STRIKETHROUGH   = '\033[9m'
    NORMAL          = '\033[22m'
    RESET_ALL       = '\033[0m'

    def __str__(self):
        return self.value
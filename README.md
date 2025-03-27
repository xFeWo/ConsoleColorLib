# ConsoleColorLib

## Overview
This Python project defines three classes for easy use of ANSI escape codes to customize terminal output colors and styles. This module can be used in any Python project that requires colored and formatted terminal output.

## Features:
- **Foreground**: Sets text color.
- **Background**: Sets background color.
- **Style**: Enables various text styles such as bold, italic, or underline.

## Usage
Here are some examples of usage:

```python
print(Foreground.RED, "This is red text", Foreground.RESET)
print(Background.BLUE, "Blue background", Background.RESET)
print(Style.UNDERLINE, "Underlined text", Style.RESET_ALL)
```

## Available Colors and Styles

### Foreground Colors
- `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- `BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_YELLOW`, `BRIGHT_BLUE`, `BRIGHT_MAGENTA`, `BRIGHT_CYAN`, `BRIGHT_WHITE`
- `RESET`

### Background Colors
- `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`
- `BRIGHT_BLACK`, `BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_YELLOW`, `BRIGHT_BLUE`, `BRIGHT_MAGENTA`, `BRIGHT_CYAN`, `BRIGHT_WHITE`
- `RESET`

### Styles
- `BRIGHT`, `DIM`, `ITALIC`, `UNDERLINE`, `BLINK`, `REVERSE`, `HIDDEN`, `STRIKETHROUGH`
- `NORMAL`, `RESET_ALL`

## Setup
No additional dependencies are required. The module can be directly integrated into a project.

```python
from color import Foreground, Background, Style
```

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

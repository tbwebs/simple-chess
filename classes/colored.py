from colored import fg, bg, attr


class Coloring:
    reset = attr("reset")
    bold = attr("bold")
    red = fg("red")
    blue = fg("blue")
    bg_light_gray = bg("light_gray")
    bg_dark_gray = bg("dark_gray")
    white = fg("white")
    black = fg("black")


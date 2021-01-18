from pygame import draw

def draw_borders(surface, color, width):
    draw.line(surface, color, (300, 100), (800, 100), width=width)
    draw.line(surface, color, (300, 500), (800, 500), width=width)
    draw.line(surface, color, (300, 100), (300, 500), width=width)
    draw.line(surface, color, (800, 100), (800, 500), width=width)

def draw_internal_lines(surface, color, width):
    draw.line(surface, color, (450, 100), (450, 500), width=width)
    draw.line(surface, color, (650, 100), (650, 500), width=width)
    draw.line(surface, color, (300, 220), (800, 220), width=width)
    draw.line(surface, color, (300, 380), (800, 380), width=width)

def draw_game_board(surface, color, width):
    draw_borders(surface, color, width)
    draw_internal_lines(surface, color, width)
from manim import *


CALCULATOR_WIDTH = 5
CALCULATOR_HEIGHT = 5


class Calculator(Scene):
    def construct(self):
        # main rect
        calc_rect = Rectangle(
            ORANGE, width=CALCULATOR_WIDTH, height=CALCULATOR_HEIGHT)
        # output line
        calc_out_line = Line([-CALCULATOR_WIDTH/2, (CALCULATOR_HEIGHT*0.25), 0],
                             [CALCULATOR_WIDTH/2, (CALCULATOR_HEIGHT*0.25), 0])
        calc_out_line.set_color(ORANGE)
        # calculator buttons
        calc_buttons = Text(str(1), font='sans-serif', color=ORANGE)
        self.play(Create(calc_rect))
        self.play(Create(calc_out_line))
        self.play(Write(calc_buttons))

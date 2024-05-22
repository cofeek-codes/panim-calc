from manim import *


CALCULATOR_WIDTH = 5
CALCULATOR_HEIGHT = 5

calc_buttons_rects = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]


class Calculator(Scene):
    def construct(self):
        # main rect
        calc_rect = Rectangle(
            ORANGE, width=CALCULATOR_WIDTH, height=CALCULATOR_HEIGHT)
        # output line
        calc_out_line = Line([-CALCULATOR_WIDTH/2, (CALCULATOR_HEIGHT*0.25), 0],
                             [CALCULATOR_WIDTH/2, (CALCULATOR_HEIGHT*0.25), 0])
        calc_out_line.set_color(ORANGE)
        self.play(Create(calc_rect))
        self.play(Create(calc_out_line))
        # calculator buttons
        for i in range(2, 5):
            for j in range(2, 5):
                r = RoundedRectangle(width=1, height=1, corner_radius=0.1)
                r.move_to([
                    # FIXME: for some reason i am unable to put `r.points` into a variable
                    calc_out_line.points[0][0] -
                    calc_out_line.points[0][0] * 0.2,  # x
                    calc_out_line.points[0][1] - \
                    calc_out_line.points[0][1] * 0.2,  # y
                    0
                ])
                self.play(Create(r))

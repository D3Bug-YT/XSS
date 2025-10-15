from manim import *

class XSSBrace(Scene):
    def construct(self):
        title = Text("Cross-Site Scripting", color=WHITE)
        self.play(Write(title))
        self.wait(5)

        brace = Brace(title, direction=DOWN, color=WHITE)
        self.play(GrowFromCenter(brace))
        xss = Text("XSS", color=WHITE)
        xss.next_to(brace, DOWN, buff=0.2)
        xss.set_x(brace.get_center()[0])
        self.play(Write(xss))

        self.wait(5)
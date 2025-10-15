# manim -p -r 1920,1080 --fps 60 URL.py Domain

from manim import *

class dom(Scene):
    def construct(self):
        scale_factor = 1.6

        dom = Text("DOM", color=WHITE).scale(scale_factor)
        self.play(Write(dom, run_time=1.5))
        self.wait(5)

        D, O, M = [dom[i] for i in range(len(dom))]

        c_doc, c_obj, c_model = ORANGE, BLUE, GREEN
        word_D = Text("Document", color=c_doc).scale(scale_factor)
        word_O = Text("Object",   color=c_obj).scale(scale_factor)
        word_M = Text("Model",    color=c_model).scale(scale_factor)

        words = VGroup(word_D, word_O, word_M).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        words.move_to(ORIGIN)

        word_M.shift(UP * 0.15)

        self.play(
            D.animate.move_to(word_D[0]),
            O.animate.move_to(word_O[0]),
            M.animate.move_to(word_M[0]),
            run_time=0.6
        )
        self.wait(5)
        self.play(TransformMatchingShapes(D, word_D), run_time=0.7)
        self.play(TransformMatchingShapes(O, word_O), run_time=0.7)
        self.play(TransformMatchingShapes(M, word_M), run_time=0.7)
        self.wait(5)

        stack = VGroup(word_D, word_O, word_M)
        self.play(
            stack.animate.arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(ORIGIN),
            run_time=0.4
        )
        self.wait(5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(5)

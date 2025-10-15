from manim import *

class Domain(Scene):
    def construct(self):
        proto  = Text("https", color=WHITE)
        sep    = Text("://", color=WHITE)
        domain = Text("example.com", color=WHITE)
        slash = Text("/", color=WHITE)
        path   = Text("blog", color=WHITE)
        qsep   = Text("?", color=WHITE)
        query  = Text("name=alice", color=WHITE)

        url = VGroup(proto, sep, domain, slash, path, qsep, query).arrange(RIGHT, buff=0.03).move_to(ORIGIN)

        self.play(Write(url))
        self.wait(5)

        self.play(Indicate(sep, color=YELLOW, scale_factor=1.25), 
                  Indicate(slash, color=YELLOW, scale_factor=1.25), 
                  Indicate(qsep,  color=YELLOW, scale_factor=1.25), 
                  Indicate(proto,  color=GREY_C, scale_factor=0.75),
                  Indicate(domain,  color=GREY_C, scale_factor=0.75),
                  Indicate(path,  color=GREY_C, scale_factor=0.75),
                  Indicate(query,  color=GREY_C, scale_factor=0.75),
                  run_time=5)

        self.wait(5)


        proto_brace = Brace(proto, UP, buff=0.15).set_color(YELLOW)
        proto_label = proto_brace.get_text("Protocol").scale(0.6).set_color(YELLOW)

        domain_brace = Brace(domain, DOWN, buff=0.15).set_color(GREEN)
        domain_label = domain_brace.get_text("Domain").scale(0.6).set_color(GREEN)

        path_brace = Brace(path, UP, buff=0.15).set_color(BLUE)
        path_label = path_brace.get_text("Subdirectory").scale(0.6).set_color(BLUE)

        query_brace = Brace(query, DOWN, buff=0.15).set_color(ORANGE)
        query_label = query_brace.get_text("Query String").scale(0.6).set_color(ORANGE)


        self.play(Create(proto_brace), Write(proto_label, shift=UP*0.15), proto.animate.set_color(YELLOW))
        self.wait(5)
        self.play(Create(domain_brace), Write(domain_label, shift=DOWN*0.15), domain.animate.set_color(GREEN))
        self.wait(5)
        self.play(Create(path_brace), Write(path_label, shift=UP*0.15), path.animate.set_color(BLUE))
        self.wait(5)
        self.play(Create(query_brace), Write(query_label, shift=DOWN*0.15), query.animate.set_color(ORANGE))

        self.wait(5)

        others = VGroup(proto, sep, domain, slash, path, qsep,
                        proto_brace, proto_label,
                        domain_brace, domain_label,
                        path_brace, path_label, query_brace, query_label)
        self.play(FadeOut(others, shift=DOWN*0.1))

        self.wait(5)

        self.play(query.animate.scale(1.6).move_to(ORIGIN))

        name_part = VGroup(*query.submobjects[:4])
        eq_part   = VGroup(query.submobjects[4])
        val_part  = VGroup(*query.submobjects[5:])



        name_brace  = Brace(name_part, UP, buff=0.15).set_color(TEAL)
        name_label  = name_brace.get_text("Parameter name").scale(0.6).set_color(TEAL)

        value_brace = Brace(val_part, DOWN, buff=0.15).set_color(PURPLE)
        value_label = value_brace.get_text("Parameter value").scale(0.6).set_color(PURPLE)

        self.play(eq_part.animate.set_color(WHITE))
        self.play(Create(name_brace), FadeIn(name_label, shift=UP*0.15), name_part.animate.set_color(TEAL))
        self.wait(5)
        self.play(Create(value_brace), FadeIn(value_label, shift=DOWN*0.15), val_part.animate.set_color(PURPLE))
        self.wait(5)


        
        
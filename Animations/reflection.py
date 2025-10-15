from manim import *

# manim -p -r 1920,1080 --fps 60 intro.py XSSBrace

class Reflection(Scene):
    def construct(self):

        self.wait(5)
        title = Text("Reflected XSS").to_edge(UP)
        self.play(Write(title))
        self.wait(0.2)

        box_width = 4.0
        box_height = 4.0
        corner_radius = 0.3

        client_box = RoundedRectangle(
            corner_radius=corner_radius,
            width=box_width,
            height=box_height
        ).set_stroke(GREEN, width=2)
        client_box.set_fill(GREEN, opacity=0.10)

        client_label = Text("Client", color=GREEN)
        client_label.move_to(client_box.get_top() + DOWN * 0.4)

        client_group = VGroup(client_box, client_label).shift(LEFT * 3.5)

        server_box = RoundedRectangle(
            corner_radius=corner_radius,
            width=box_width,
            height=box_height
        ).set_stroke(BLUE, width=2)
        server_box.set_fill(BLUE, opacity=0.10)

        server_label = Text("Server", color=BLUE)
        server_label.move_to(server_box.get_top() + DOWN * 0.4)

        server_group = VGroup(server_box, server_label).shift(RIGHT * 3.5)

        client_group.to_edge(LEFT, buff=0.4) 
        server_group.to_edge(RIGHT, buff=0.4)

        self.play(DrawBorderThenFill(client_box, run_time=1.2), Write(client_label, run_time=0.8), DrawBorderThenFill(server_box, run_time=1.2), Write(server_label, run_time=0.8))

        self.wait(5)

        # Arrow 1
        y_level = client_box.get_top()[1] - 0.6
        start = client_box.get_right().copy()
        end = server_box.get_left().copy()
        start[1] = y_level
        end[1] = y_level

        arrow = Arrow(start, end, buff=0.15, color=GREEN)
        msg = Text("Hey send me the web page", color=GREEN).scale(0.4)
        msg.next_to(arrow, UP, buff=0.1)

        self.play(Create(arrow, run_time=1.0))
        self.play(Write(msg, run_time=0.8))

        self.wait(5)
        # Arrow 2
        y_level_2 = y_level - 1.0

        start2 = server_box.get_left().copy()
        end2 = client_box.get_right().copy()
        start2[1] = y_level_2
        end2[1] = y_level_2

        arrow2 = Arrow(start2, end2, buff=0.15, color=BLUE)
        msg2 = Text("Here's the webpage, send me some input", color=BLUE).scale(0.4)
        msg2.next_to(arrow2, UP, buff=0.1)

        self.play(Create(arrow2, run_time=1.0))
        self.play(Write(msg2, run_time=0.8))

        self.wait(5)
        # Arrow 3
        y_level_3 = y_level_2 - 1.0

        start3 = client_box.get_right().copy()
        end3 = server_box.get_left().copy()
        start3[1] = y_level_3
        end3[1] = y_level_3

        arrow3 = Arrow(start3, end3, buff=0.15, color=GREEN)
        msg3 = Text("Here's my input", color=GREEN).scale(0.4)
        msg3.next_to(arrow3, UP, buff=0.1)

        self.play(Create(arrow3, run_time=1.0))
        self.play(Write(msg3, run_time=0.8))

        self.wait(5)
        # Arrow 4
        y_level_4 = y_level_3 - 1.0

        start4 = server_box.get_left().copy()
        end4 = client_box.get_right().copy()
        start4[1] = y_level_4
        end4[1] = y_level_4

        arrow4 = Arrow(start4, end4, buff=0.15, color=BLUE)
        msg4 = Text("Here's a webpage with your input in it", color=BLUE).scale(0.4)
        msg4.next_to(arrow4, UP, buff=0.1)

        self.play(Create(arrow4, run_time=1.0))
        self.play(Write(msg4, run_time=0.8))

        self.wait(5)

        # transform msg3 to show malicious input
        new_msg3 = Text(
            "Here's my (malicious) input",
            color=GREEN,
            t2c={"(malicious)": RED},
        ).scale(0.4).move_to(msg3)

        self.play(TransformMatchingShapes(msg3, new_msg3, run_time=1.0))
        msg3 = new_msg3
        self.wait(5)

        content = VGroup(
            client_group, server_group,
            arrow, msg,
            arrow2, msg2,
            arrow3, msg3,
            arrow4, msg4
        )

        self.play(content.animate.scale(0.5).shift(UP * 1.5), run_time=1.2)
        self.wait(5)

        victim_box = RoundedRectangle(
            corner_radius=corner_radius,
            width=box_width,
            height=box_height
        ).set_stroke(YELLOW, width=2).set_fill(YELLOW, opacity=0.10)

        victim_label = Text("Victim", color=YELLOW)
        victim_label.move_to(victim_box.get_top() + DOWN * 0.4)

        victim_group = VGroup(victim_box, victim_label)

        x_center = 0.0 
        row_y = client_box.get_center()[1]
        offset_down = 3.0 
        victim_group.move_to([x_center, row_y - offset_down, 0])
        victim_group.scale(0.5)

        self.play(DrawBorderThenFill(victim_box, run_time=1.0), Write(victim_label, run_time=0.6))

        self.wait(5)




        content_scale = 0.5
        ref_width = arrow.get_stroke_width()  # match original arrows' width

        # Start at the client's bottom middle
        start = client_box.get_bottom()

        # Same X as client, Y of the victim's center
        junction = start.copy()
        junction[1] = victim_box.get_center()[1]

        # End a bit before the Victim's LEFT edge so the tip doesn't poke in
        end = victim_box.get_left() + LEFT * 0.12

        # --- Compute half the stroke thickness in scene units (no extra imports) ---
        px_per_unit = self.camera.pixel_width / self.camera.frame_width
        half_thickness_units = (ref_width / px_per_unit) / 2.0

        # Segment 1: vertical line — extend *past* junction by half thickness
        vert = Line(start, junction + DOWN * half_thickness_units).set_stroke(GREEN, width=ref_width)

        # Segment 2: horizontal arrow — start *left* of junction by half thickness
        horiz = Arrow(
            junction - RIGHT * half_thickness_units,  # start at left edge of the vertical stroke
            end,
            buff=0,
            color=GREEN,
            tip_length=0.2 * content_scale,
            max_tip_length_to_length_ratio=0.04
        ).set_stroke(width=ref_width)

        # Label below the horizontal segment, nudged down a bit
        label = Text("Hey click on this link", color=GREEN).scale(0.4 * content_scale)
        label.next_to(horiz, DOWN, buff=0.26 * content_scale)

        # Z-order so the joint looks seamless
        vert.set_z_index(1)
        horiz.set_z_index(2)
        label.set_z_index(3)

        # Animate
        self.play(Create(vert, run_time=0.6))
        self.play(Create(horiz, run_time=0.6))
        self.play(Write(label, run_time=0.6))

        self.wait(5)



        start_vr = victim_box.get_right()

        # Junction directly to the right of Victim, aligned with Server's bottom center X
        server_bottom = server_box.get_bottom()
        junction_vr = np.array([server_bottom[0], start_vr[1], 0])

        # End a bit BEFORE the Server bottom so the tip doesn't poke in
        end_vr = server_bottom + DOWN * 0.12  # set to server_bottom for exact edge

        # Half the stroke thickness in scene units (no new imports)
        px_per_unit = self.camera.pixel_width / self.camera.frame_width
        half_thickness_units = (ref_width / px_per_unit) / 2.0

        # 1) Horizontal segment: go RIGHT first, ending at the vertical stroke's right edge
        horiz3 = Line(
            start_vr,
            #junction_vr + RIGHT * half_thickness_units
            junction_vr + RIGHT * half_thickness_units
        ).set_stroke(YELLOW, width=ref_width)

        # 2) Vertical arrow UP: start slightly BELOW the junction for a square overlap
        vert3 = Arrow(
            #junction_vr - DOWN * half_thickness_units,  # start at bottom edge of the vertical stroke
            junction_vr + DOWN * half_thickness_units, 
            end_vr,
            buff=0,
            color=YELLOW,
            tip_length=0.2 * content_scale,
            max_tip_length_to_length_ratio=0.04
        ).set_stroke(width=ref_width)

        label3 = Text("Here's my (malicious) input", color=YELLOW, t2c={"(malicious)": RED}).scale(0.4 * content_scale)

        label3.next_to(horiz3, DOWN, buff=0.26 * content_scale)
        label3.shift(RIGHT * 0.45 * content_scale) 

        horiz3.set_z_index(1)
        vert3.set_z_index(2)
        label3.set_z_index(3)

        # Animate
        self.play(Create(horiz3, run_time=0.6))
        self.play(Create(vert3, run_time=0.6))
        self.play(Write(label3, run_time=0.6))
        self.wait(5)


        content_scale = 0.5
        ref_width = arrow.get_stroke_width()  # match your original arrows

        # Start a bit to the right of the server's bottom center
        offset_x = server_box.width * 0.25  # adjust how far right of center you want
        start_sv = server_box.get_bottom() + RIGHT * offset_x

        # Target Y: below the Victim's vertical center
        drop = victim_box.height * 0.20     # adjust how far below center you want
        y_target = victim_box.get_center()[1] - drop

        # Junction directly below the server's start point, at the target Y
        junction_sv = start_sv.copy()
        junction_sv[1] = y_target

        # End just to the RIGHT of Victim's right edge (small gap so tip doesn't poke in)
        end_sv = victim_box.get_right().copy()
        end_sv[1] = y_target
        end_sv += RIGHT * 0.12

        # Make the elbow joint a perfect square overlap
        px_per_unit = self.camera.pixel_width / self.camera.frame_width
        half_thickness_units = (ref_width / px_per_unit) / 2.0

        # Vertical segment: extend *past* the junction by half the thickness
        vert4 = Line(start_sv, junction_sv + DOWN * half_thickness_units).set_stroke(BLUE, width=ref_width)

        # Horizontal arrow LEFT: start at the left edge of the vertical stroke
        horiz4 = Arrow(
            junction_sv + RIGHT * half_thickness_units,  # left edge of vertical stroke
            end_sv,
            buff=0,
            color=BLUE,
            tip_length=0.2 * content_scale,
            max_tip_length_to_length_ratio=0.04
        ).set_stroke(width=ref_width)

        # (Optional) label:
        label4 = Text("Here's the webpage with (malicious) content", color=BLUE, t2c={"(malicious)": RED}).scale(0.4 * content_scale)
        label4.next_to(horiz4, DOWN, buff=0.26 * content_scale).set_z_index(3)
        label4.shift(RIGHT * 0.7 * content_scale)

        # Z-order so the joint looks seamless
        vert4.set_z_index(1)
        horiz4.set_z_index(2)

        # Animate
        self.play(Create(vert4, run_time=0.6))
        self.play(Create(horiz4, run_time=0.6))
        self.play(Write(label4, run_time=0.6))

        self.wait(5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.wait(0.2)






from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class BooleanOperations(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Create two ellipses
        ellipse1 = Circle(radius=2.0, fill_opacity=0.5, color=BLUE)
        ellipse2 = Circle(radius=2.0, fill_opacity=0.5, color=RED)
        
        # Title for Boolean Operations
        bool_ops_text = Text("Boolean Operations", font_size=40).move_to(ORIGIN)
        
        with self.voiceover(text="In this video, we will explore Boolean operations using two ellipses."):
            self.play(Write(bool_ops_text), run_time=2)
            self.wait(1)

        # shift the text top left
        self.play(bool_ops_text.animate.move_to(UP * 2.5 + LEFT * 3), run_time=1)

        with self.voiceover(text="First, let's draw two ellipses."):
            self.play(Create(ellipse1.move_to(DOWN * 1 + LEFT * 4.5)), run_time=1)
            self.play(Create(ellipse2.move_to(DOWN * 1 + LEFT * 2)), run_time=1)
        
        # Display the ellipses
        with self.voiceover(text="Here are the two ellipses."):
            self.play(Create(ellipse1.move_to(DOWN * 1 + LEFT * 4.5)), run_time=1)
            self.play(Create(ellipse2.move_to(DOWN * 1 + LEFT * 2)), run_time=1)

        # Intersection
        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        with self.voiceover(text="This green area represents the intersection of the two ellipses."):
            self.play(i.animate.scale(0.3).move_to(RIGHT * 5 + UP * 2.5), run_time=1)
        intersection_text = Text("Intersection", font_size=20).next_to(i, UP)
        self.play(FadeIn(intersection_text), run_time=1)

        # Union
        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=20)
        with self.voiceover(text="This orange area represents the union of the two ellipses."):
            self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3), run_time=1)
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text), run_time=1)

        # Exclusion
        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=20)
        with self.voiceover(text="This yellow area represents the exclusion of the two ellipses."):
            self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3), run_time=1)
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text), run_time=1)

        # Difference
        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=20)
        with self.voiceover(text="This pink area represents the difference of the two ellipses."):
            self.play(d.animate.scale(0.3).next_to(e, DOWN, buff=exclusion_text.height * 3), run_time=1)
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text), run_time=1)

        # Optional: Hold the final view for a moment
        with self.voiceover(text="These are the basic Boolean operations on two shapes."):
            self.wait(2)

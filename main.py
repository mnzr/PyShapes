from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class DrawingBoard(Widget):
    """Main widget that will be used as drawing board"""

    def on_touch_down(self, touch):
        """log touches"""
        color = (random(), 1., 1.)  # so that colors are bright
        #  only work with this canvas
        with self.canvas:
            # color of the line
            Color(*color, mode='hsv')  # choosing HSV color space, as in, smaller number of colors
            # diameter of circle
            d = 30.
            # an ellipse with equal width and height is a circle
            # -d/2 means the circle will be centered right at the tip of pointer
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # setting up a line for drawing. canvas knows how to do it coz 'with'
            # we are just storing the reference of it in touch.ud dict using
            # the name 'Line'..
            touch.ud['line'] = Line(points=(touch.x, touch.y))  # passing initial touch point

    # what to do when touched and moving, just updating already defined
    def on_touch_move(self, touch):
        # add more lines after the previous line
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):
    """The main paint app where all other widgets get added"""

    def build(self):
        parent = Widget()
        # This part I don't understand
        self.board = DrawingBoard()
        # new button named Clear
        clearbtn = Button(text='Clear', font_size='30sp')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.board)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj):
        self.board.canvas.clear()


if __name__ == '__main__':
    PaintApp().run()

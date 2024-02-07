from util import is_running_on_raspberry_pi, resource_path

from inky.auto import auto
from PIL import Image, ImageDraw, ImageColor

class EInk:
    def __init__(self, font, minor_font):
        self.font = font
        self.minor_font = minor_font
        self.display = auto(ask_user=True)
        self.reset_image()

        self.BLACK = self.display.BLACK
        self.WHITE = self.display.WHITE
        self.GREEN = self.display.GREEN
        self.BLUE = self.display.BLUE
        self.RED = self.display.RED
        self.YELLOW = self.display.YELLOW
        self.ORANGE = self.display.ORANGE
        self.CLEAN = self.display.CLEAN

    def reset_image(self):
        self.image = Image.new("P", self.display.resolution)
        self.draw = ImageDraw.Draw(self.image)
        # TODO - is this required on the real hardware?
        self.fill_image_with_colour(self.display.CLEAN)

    def fill_image_with_colour(self, colour):
        for y in range(0, self.display.height):
            for x in range(0, self.display.width):
                self.image.putpixel((x, y), colour)

    def draw_text(self, coordinate, text, colour=None, minor=False):
        if colour is None:
            colour = self.BLACK
        font = self.minor_font if minor else self.font
        self.draw.text(coordinate, text, colour, font=font)

    def draw_full_width_line(self, y, colour=None):
        if colour is None:
            colour = self.BLACK
        self.draw.line([(0, y), (self.display.width), y], fill=colour)

    def show(self):
        if is_running_on_raspberry_pi():
            self.display.set_image(self.image)
            self.display.show()
        else:
            # Convert the image to a normal rgb image and save it
            colour_mapping = [""] * 8
            colour_mapping[self.display.BLACK] = "#000000"
            colour_mapping[self.display.WHITE] = "#ffffff"
            colour_mapping[self.display.GREEN] = "#00ff00"
            colour_mapping[self.display.BLUE] = "#0000ff"
            colour_mapping[self.display.RED] = "#ff0000"
            colour_mapping[self.display.YELLOW] = "#ffff00"
            colour_mapping[self.display.ORANGE] = "#ffa500"
            colour_mapping[self.display.CLEAN] = colour_mapping[self.display.WHITE]

            rgbImage = Image.new("RGB", self.display.resolution)
            for y in range(0, self.display.height):
                for x in range(0, self.display.width):
                    eink_colour = self.image.getpixel((x, y))
                    hex_colour = colour_mapping[eink_colour]
                    rgbImage.putpixel((x, y), ImageColor.getrgb(hex_colour))
            rgbImage.save(resource_path("eink-screen.png"))

from util import is_running_with_eink_screen, resource_path, log
from layout_settings import LayoutSettings

from inky.auto import auto
from PIL import Image, ImageDraw, ImageColor, ImageFont

class EInk:
    def __init__(self):
        self.font = ImageFont.truetype(LayoutSettings.font_path, LayoutSettings.font_size)
        self.minor_font = ImageFont.truetype(LayoutSettings.font_path, LayoutSettings.minor_font_size)
        self.display = auto(ask_user=True)

        if LayoutSettings.orientation == "landscape":
            self.width = self.display.width
            self.height = self.display.height
        elif LayoutSettings.orientation == "portrait":
            self.width = self.display.height
            self.height = self.display.width
        else:
            raise Exception(f"Invalid orientation: {LayoutSettings.orientation}")

        self.image = Image.new("P", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        self.BLACK = self.display.BLACK
        self.WHITE = self.display.WHITE
        self.GREEN = self.display.GREEN
        self.BLUE = self.display.BLUE
        self.RED = self.display.RED
        self.YELLOW = self.display.YELLOW
        self.ORANGE = self.display.ORANGE
        self.CLEAN = self.display.CLEAN

    def reset_image(self):
        # TODO - is this required on the real hardware?
        self.fill_image_with_colour(self.display.CLEAN)

    def fill_image_with_colour(self, colour):
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.image.putpixel((x, y), colour)

    def draw_text(self, coordinate, text, colour=None, minor=False):
        if colour is None:
            colour = self.BLACK
        font = self.minor_font if minor else self.font
        self.draw.text(coordinate, text, colour, font=font)

    def draw_full_width_line(self, y, colour=None):
        if colour is None:
            colour = self.BLACK
        self.draw.line([(0, y), (self.width, y)], fill=colour)

    def show(self):
        if is_running_with_eink_screen():
            if LayoutSettings.orientation == "portrait":
                self.display.set_image(self.image.rotate(90, expand=True))
            else:
                self.display.set_image(self.image)
            self.display.show()
        else:
            image_file_path = resource_path("eink-screen.png")
            log(f"Simulating eink screen, rendering screen contents to {image_file_path}")
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

            rgbImage = Image.new("RGB", (self.width, self.height))
            for y in range(0, self.height):
                for x in range(0, self.width):
                    eink_colour = self.image.getpixel((x, y))
                    hex_colour = colour_mapping[eink_colour]
                    rgbImage.putpixel((x, y), ImageColor.getrgb(hex_colour))
            rgbImage.save(image_file_path)

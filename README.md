# chores-eink-display

Displays overdue chores (provided by the [chores app API](https://github.com/sizlo/chores)) on an eink display connected to a Raspberry Pi.

<!--- TODO - Update this when I have the hardware --->
The intention is for this to be run on a [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/) connected to an [Inky Impression 4"](https://shop.pimoroni.com/products/inky-impression-4), but currently I do not own the hardware, so am just experimenting with the [python library provided by pimoroni/inky](https://github.com/pimoroni/inky).

## Running

### Running on a desktop for dev/testing

This is set up to run via docker as the inky library cannot be installed on macos ([see here](https://github.com/pimoroni/inky/issues/185)). The inky library does provide a display simulation using tkinter, but I couldn't be bothered setting that up to work through docker, so the program writes an image file to disk whenever it would refresh the eink display.

`docker compose up --build`

The file `resources/eink-screen.png` will be written to every time the eink display would refresh. If you have this image file selected in finder the preview will live update.

### Running on a raspberry pi

TODO
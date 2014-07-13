from modules import BaseModule, Icons, CWD

__icon__ = Icons.Cube
__title__ = "Cube"
__order__ = 1

import random
import os
r = lambda: random.randint(0, 255)

# import pyimgur
# CLIENT_ID = "8f072037a8b8e7c"
# im = pyimgur.Imgur(CLIENT_ID)
# image = im.get_image('xqTKvMK')

class CubeModule(BaseModule):
    def clickedAction(self):
        self.loadContent("content.qml")
        self.app.openContent()

    def hoveredAction(self):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def unhoveredAction(self):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def message(self, msg):
        getattr(self, msg.split(":")[0])(msg.split(":")[1:])

    def exit(self, *args):
        exit()
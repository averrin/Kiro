from modules import BaseModule, Icons

__icon__ = Icons.Cube
__title__ = "Cube"
__order__ = 1

import random
import os
r = lambda: random.randint(0, 255)

class CubeModule(BaseModule):
    def clickedAction(self, parent):
        parent.ContentLoader.setProperty("source", os.path.join("modules", "test2", "content.qml"))
        parent.openContent()

    def hoveredAction(self, parent):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def unhoveredAction(self, parent):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def message(self, parent, msg):
        getattr(self, msg.split(":")[0])(msg.split(":")[1:])

    def exit(self, *args):
        exit()
from modules import BasePlugin, Icons

__icon__ = Icons.Cube
__title__ = "Cube"
__order__ = 1

import random
r = lambda: random.randint(0, 255)

class CubePlugin(BasePlugin):
    def clickedAction(self, parent):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def hoveredAction(self, parent):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())

    def unhoveredAction(self, parent):
        self.icon_color = '#%02X%02X%02X' % (r(), r(), r())
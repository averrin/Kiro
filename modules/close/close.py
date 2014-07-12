from modules import BasePlugin, Icons

__icon__ = Icons.Remove
__title__ = "Close"
__order__ = 99


class TestPlugin(BasePlugin):
    def clickedAction(self, parent):
        exit()

    def hoveredAction(self, parent):
        self.icon_color = '#ff2222'

    def unhoveredAction(self, parent):
        self.icon_color = '#eee'
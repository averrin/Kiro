from modules import BasePlugin, Icons

__icon__ = Icons.Home
__title__ = "Test"
__order__ = 0


class TestPlugin(BasePlugin):
    def clickedAction(self, parent):
        parent.toggleContent()
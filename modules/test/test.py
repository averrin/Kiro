from modules import BasePlugin, Icons

__icon__ = Icons.Home
__title__ = "Test"
__order__ = 0


class TestPlugin(BasePlugin):
    def clickedAction(self, parent):
        print(parent.Screen.width(), parent.elements_width)
        if parent.Screen.width() != parent.elements_width:
            parent.Screen.setProperty("width", parent.Panel.width())
        else:
            parent.Screen.setProperty("width", parent.elements_width + parent.content_width)
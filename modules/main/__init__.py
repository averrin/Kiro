from modules import BaseModule, Icons

__icon__ = Icons.Home
__title__ = "Test"
__order__ = 0


class Main(BaseModule):
    def clickedAction(self):
        self.loadContent("content.qml")
        self.app.openContent()
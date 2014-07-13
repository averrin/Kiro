from modules import BaseModule, Icons
import os

__icon__ = Icons.Home
__title__ = "Test"
__order__ = 0


class Main(BaseModule):
    def clickedAction(self, parent):
        parent.ContentLoader.setProperty("source", os.path.join("modules", "main", "content.qml"))
        parent.toggleContent()
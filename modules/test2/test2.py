from modules import BasePlugin

__icon__ = BasePlugin.Icons.Cube
__title__ = "Cube"
__order__ = 1


class CubePlugin(BasePlugin):
    def clickedAction(self):
        print("looooo")
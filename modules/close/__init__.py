from modules import BaseModule, Icons

__icon__ = Icons.ChevronRight
__title__ = "Close"
__order__ = 99


class TestModule(BaseModule):
    def clickedAction(self):
        if self.icon == Icons.ChevronRight:
            self.app.toggleContent()
            self.icon = Icons.Remove
        else:
            self.app.icon.hide()
            exit()

    def hoveredAction(self):
        self.icon_color = '#D34836'

    def unhoveredAction(self):
        self.icon_color = '#ccc'

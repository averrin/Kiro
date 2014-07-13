from modules import BaseModule, Icons
from modules.plus import notifications

__icon__ = Icons.Comment
__title__ = "Plus"
__order__ = 3


class Main(BaseModule):
    def clickedAction(self):
        self.loadContent("content.qml")
        self.app.openContent()

    def initAction(self):
        self.icon_color = '#D34836'

    def beforeLoad(self):
        self.app.ctx.setContextProperty('NotificationModel', notifications.notifications)
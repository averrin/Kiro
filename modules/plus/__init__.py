from modules import BaseModule, Icons
from modules.plus import notifications
from PyQt5.QtQml import *

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
        qmlRegisterType(notifications.NotificationModel, 'NModel', 1, 0, 'NModel')
        self.app.ctx.setContextProperty('NotificationModel', notifications.notifications)

    def message(self, msg):
        getattr(self, msg.split(":")[0])(msg.split(":")[1:])

    def add_test(self, msg):
        notifications.notifications.addItem(notifications.Notification(Icons.Comment, msg[0], "bzzzz!"))
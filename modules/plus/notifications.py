from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *
import datetime
from modules import Icons


class NotificationModel(QAbstractListModel):
    def __init__(self, mlist):
        QAbstractListModel.__init__(self)

        # Store the passed data list as a class member.
        self._items = mlist

    # We need to tell the view how many rows we have present in our data. see tutorial #3
    def rowCount(self, parent=None):
        return len(self._items)

    def getItems(self, index, role):
        raise Exception()
    def get(self, index):
        raise Exception()

    def flags(self, index):
        print("bzz")
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled

    def addItem(self, item):
        print(item.title)
        self.beginInsertRows(QModelIndex(), len(self._items), len(self._items))
        self._items.append(item)
        self.endInsertRows()

class Notification(QVariant):
    iconChanged = pyqtSignal()
    titleChanged = pyqtSignal()
    clicked = pyqtSignal()
    colorChanged = pyqtSignal()

    shorttextChanged = pyqtSignal()
    timeChanged = pyqtSignal()

    @pyqtProperty(str, notify=colorChanged)
    def icon_color(self):
        return self._color

    @pyqtProperty(str, notify=shorttextChanged)
    def short_text(self):
        return self._short_text

    @pyqtProperty(str, notify=timeChanged)
    def time(self):
        return self._time


    @icon_color.setter
    def icon_color(self, color):
        if self._color != color:
            self._color = color
            self.colorChanged.emit()

    @pyqtProperty(str, notify=iconChanged)
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):
        if self._icon != icon:
            self._icon = icon
            self.iconChanged.emit()

    @pyqtProperty(str, notify=titleChanged)
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if self._title != title:
            self._title = title
            self.titleChanged.emit()

    def __init__(self, icon='', title='', short_text='', parent=None):
        super(Notification, self).__init__(parent)

        self.app = None
        self._icon = icon
        self._title = title
        self._color = '#ccc'
        self._short_text = short_text
        self._time = str(datetime.datetime.now().time().strftime("%H:%M"))

        print(self.__dict__)


notifications = NotificationModel([
    # Notification(Icons.PaperPlane, "Plane", "To the sky..."),
    # Notification(Icons.Fire, "Fire", "Burn Forest, BURN!!!!")
])
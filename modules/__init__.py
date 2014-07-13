from collections import namedtuple
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *
import sys
import os

CWD = sys.path[0] + os.sep
import os
import inspect
import json

_icons = json.load(open(os.path.join(CWD, "modules", "icons.json"), "r"))
Icons = namedtuple("Icons", _icons.keys())(**_icons)


class BaseModule(QObject):
    iconChanged = pyqtSignal()
    titleChanged = pyqtSignal()
    clicked = pyqtSignal()
    colorChanged = pyqtSignal()

    @pyqtProperty(str, notify=colorChanged)
    def icon_color(self):
        return self._color

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

    def __init__(self, icon='', title='', parent=None):
        super(BaseModule, self).__init__(parent)

        self.app = None
        self._icon = icon
        self._title = title
        self._color = '#ccc'

    def loadContent(self, fname):
        self.app.ContentLoader.setProperty("source", os.path.join("modules", self.name.split(".")[1], fname))

    def clickedAction(self):
        pass

    def hoveredAction(self):
        pass

    def unhoveredAction(self):
        pass

    def initAction(self):
        pass

    def message(self, msg):
        print(msg)


modules = []
import importlib
for m in os.listdir('modules'):
    if os.path.isdir(os.path.join(CWD, 'modules', m)) and not m.startswith("_"):
        modules.append(importlib.import_module("." + m, __name__))


def processPlugin(module):
    """
        Create plugin instance from module
    """
    if module is not None:
        for obj in list(module.__dict__.values()):
            try:
                if inspect.isclass(obj) and issubclass(obj, BaseModule) and obj is not BaseModule:
                    plugin = obj(module.__icon__, module.__title__)
                    plugin.name = module.__name__
                    plugin.order = module.__order__
                    try:
                        return plugin
                    except Exception as e:
                        raise e
            except Exception as e:
                raise e

elements = sorted([processPlugin(p) for p in modules], key=lambda x: x.order)
named_elements = {e.title: e for e in elements}

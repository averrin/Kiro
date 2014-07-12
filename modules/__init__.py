from collections import namedtuple

__author__ = 'averrin'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQuick import *
import sys

CWD = sys.path[0] + '/'
import os
import imp
import inspect
import json

_icons = json.load(open(os.path.join(CWD, "modules", "icons.json"), "r"))
Icons = namedtuple("Icons", _icons.keys())(**_icons)


class BasePlugin(QObject):
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
        super(BasePlugin, self).__init__(parent)

        self._icon = icon
        self._title = title
        self._color = '#eee'

    def clickedAction(self, parent):
        pass

    def hoveredAction(self, parent):
        pass

    def unhoveredAction(self, parent):
        pass


def findModules():
    """
        Search plugin files
        http://wiki.python.org/moin/ModulesAsPlugins
    """
    modules = set()
    for folder in os.listdir(CWD + 'modules'):
        if os.path.isdir(CWD + 'modules/' + folder):
            for filename in os.listdir(CWD + 'modules/' + folder):
                module = None
                if not filename.startswith("__init__"):
                    if filename.endswith(".py"):
                        module = filename[:-3]
                    elif filename.endswith(".pyc"):
                        module = filename[:-4]
                    if module is not None:
                        modules.add(module)
    return list(modules)


def loadModule(name, path="modules/"):
    """
        Return a named module found in a given path.
        http://wiki.python.org/moin/ModulesAsPlugins
    """
    (file, pathname, description) = imp.find_module(name, [CWD + path + name])
    try:
        return imp.load_module(name, file, pathname, description)
    except Exception as e:
        print("Module %s cant be loaded" % name)
        print(e)
        return None


def processPlugin(module):
    """
        Create plugin instance from module
    """
    if module is not None:
        for obj in list(module.__dict__.values()):
            try:
                if inspect.isclass(obj) and issubclass(obj, BasePlugin) and obj is not BasePlugin:
                    plugin = obj(module.__icon__, module.__title__)
                    plugin.name = module.__name__
                    plugin.order = module.__order__
                    try:
                        return plugin
                    except Exception as e:
                        raise e
            except Exception as e:
                raise e


plugins = [loadModule(name) for name in findModules()]
elements = sorted([processPlugin(p) for p in plugins], key=lambda x: x.order)
named_elements = {e.title: e for e in elements}
print(elements)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexey "Averrin" Nabrodov'
__version__ = '0.0.0'

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *
import modules


class App(object):
    def __init__(self):
        self.view = QQuickView()
        self.elementModel = modules.elements

        self.view.setObjectName("View")
        self.view.setFlags(Qt.FramelessWindowHint)
        self.ctx = self.view.rootContext()
        self.ctx.setContextProperty("viewerWidget", self.view)
        self.ctx.setContextProperty("viewerPosition", self.view.position())
        self.ctx.setContextProperty('ElementModel', self.elementModel)
        self.content_width = 300
        self.ctx.setContextProperty("contentWidth", self.content_width)
        self.elements_width = 48
        self.ctx.setContextProperty("elementsWidth", self.elements_width)
        self.view.setSource(QUrl("frontend/qml/kiro.qml"))

        self.Screen = self.view.rootObject()
        self.Screen.resized.connect(self.widthChanged)
        self.Panel = self.Screen.findChild(QObject, "ElementPanel")
        self.Content = self.Screen.findChild(QObject, "Content")
        self.Elements = self.Panel.findChild(QObject, "Elements")
        self.Elements.itemClicked.connect(self.elementClicked)

        width = self.content_width + self.elements_width
        top_offset = 40
        self.view.setWidth(width)
        self.view.setResizeMode(QQuickView.SizeViewToRootObject)
        sc = QApplication.desktop().screenGeometry()
        self.Screen.setProperty("height", sc.height() - top_offset)
        self.view.setPosition(QPoint(sc.width() - width, top_offset))
        self.view.show()
        self.view.setFlags(Qt.WindowStaysOnTopHint)

    def elementClicked(self, item):
        item = modules.named_elements[item]
        item.clickedAction(self)

    def widthChanged(self, w):
        sc = QApplication.desktop().screenGeometry()
        self.view.setPosition(QPoint(sc.width() - w, self.view.position().y()))

app = QApplication(sys.argv)
kiro = App()


def main():
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



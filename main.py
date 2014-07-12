#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alexey "Averrin" Nabrodov'
__version__ = '0.0.0'

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *
import modules


class App(object):
    def __init__(self):
        self.view = QQuickView()
        self.elementModel = modules.elements
        self.icon = QSystemTrayIcon(QIcon("frontend/cube.png"))
        self.icon.activated.connect(self.trayClicked)
        self.icon.show()

        self.content_width = 300
        self.elements_width = 48
        self.collapsed = False
        self.onTop = True

        self.view.setObjectName("View")
        self.view.setFlags(Qt.FramelessWindowHint)
        self.ctx = self.view.rootContext()
        self.ctx.setContextProperty("viewerWidget", self.view)
        self.ctx.setContextProperty("viewerPosition", self.view.position())
        self.ctx.setContextProperty('ElementModel', self.elementModel)

        self.ctx.setContextProperty("contentWidth", self.content_width)
        self.ctx.setContextProperty("elementsWidth", self.elements_width)
        self.view.setSource(QUrl("frontend/qml/kiro.qml"))

        self.Screen = self.view.rootObject()
        self.Screen.resized.connect(self.widthChanged)
        self.Panel = self.Screen.findChild(QObject, "ElementPanel")
        self.Content = self.Screen.findChild(QObject, "Content")
        self.Elements = self.Panel.findChild(QObject, "Elements")
        self.Elements.itemClicked.connect(self.elementClicked)
        self.Elements.itemHovered.connect(self.elementHovered)
        self.Elements.itemUnhovered.connect(self.elementUnhovered)

        width = self.content_width + self.elements_width
        self.view.setWidth(width)
        self.view.setResizeMode(QQuickView.SizeViewToRootObject)
        self.sc = QApplication.desktop().availableGeometry()
        self.Screen.setProperty("height", self.sc.height())
        self.view.setPosition(QPoint(self.sc.width() - width, self.sc.top()))
        if self.collapsed:
            self.Screen.setProperty("width", self.Panel.width())
        if self.onTop:
            self.view.setFlags(self.view.flags() | Qt.WindowStaysOnTopHint)

        self.view.show()

    def elementClicked(self, item):
        item = modules.named_elements[item]
        item.clickedAction(self)

    def elementHovered(self, item):
        item = modules.named_elements[item]
        item.hoveredAction(self)
    def elementUnhovered(self, item):
        item = modules.named_elements[item]
        item.unhoveredAction(self)

    def widthChanged(self, w):
        self.view.setPosition(QPoint(self.sc.width() - w, self.view.position().y()))

    def trayClicked(self, ev):
        if ev == QSystemTrayIcon.Context:
            exit()
        elif ev == QSystemTrayIcon.Trigger:
            self.onTop = not self.onTop
            if self.onTop:
                self.view.setFlags(self.view.flags() | Qt.WindowStaysOnTopHint)
            else:
                self.view.setFlags(self.view.flags() & ~Qt.WindowStaysOnTopHint)
            print(bin(int(self.view.flags())), self.onTop)
            self.view.hide()
            self.view.show()

    def toggleContent(self):
        if self.Screen.width() != self.elements_width:
            self.Screen.setProperty("width", self.Panel.width())
        else:
            self.Screen.setProperty("width", self.elements_width + self.content_width)


app = QApplication(sys.argv)
kiro = App()


def main():
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



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

        self.view.setObjectName("View")
        self.view.setFlags(Qt.FramelessWindowHint)
        self.ctx = self.view.rootContext()
        self.ctx.setContextProperty("viewerWidget", self.view)
        self.ctx.setContextProperty("viewerPosition", self.view.position())
        self.ctx.setContextProperty('ElementModel', modules.elements)
        self.view.setSource(QUrl("frontend/qml/kiro.qml"))
        self.view.setResizeMode(QQuickView.SizeRootObjectToView)

        self.Screen = self.view.rootObject()
        # self.Titlebar = self.Screen.findChild(QObject, "Titlebar")
        # self.Tabs = self.Titlebar.findChild(QObject, "Tabs")
        # self.Panel = self.Screen.findChild(QObject, "Panel")
        #
        # self.Screen.move.connect(self.moveWindow)
        # self.Screen.findChild(QObject, "CloseButton").clicked.connect(exit)
        # # self.Screen.findChild(QObject, "MinButton").clicked.connect(self.view.showMinimized)
        # self.Screen.findChild(QObject, "MinButton").clicked.connect(self.addTab)
        # self.Screen.toggleMax.connect(self.toggleMaxWindow)

        # self.addTab("child")
        width = 48
        top_offset = 40
        self.view.setWidth(width)
        sc = QApplication.desktop().screenGeometry()
        self.view.setHeight(sc.height() - top_offset)
        self.view.setPosition(QPoint(sc.width() - width, top_offset))
        self.view.show()
        self.view.setFlags(Qt.WindowStaysOnTopHint)

app = QApplication(sys.argv)
kiro = App()


def main():
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



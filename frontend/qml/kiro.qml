import QtQuick 2.3
import QtQuick.Controls 1.2
import "font.js" as Font
import "custom"
import "widgets"

Rectangle {
    width: contentWidth + elementPanel.width
    signal resized(int w)
    onWidthChanged: resized(width)
    Behavior on width { PropertyAnimation {} }

    Rectangle {
        id: "content"
        objectName: "Content"
        anchors.right: parent.right
        anchors.top: parent.top
        color: "#232323"
        height: parent.height
        width: parent.width - elementPanel.width
        signal message(string sender, string msg)

        Loader {
            id: contentLoader
            objectName: "ContentLoader"
            asynchronous: true
            //container: content
            //Behavior on source { PropertyAnimation {} }
            width: parent.width
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.horizontalCenter : parent.horizontalCenter
        }
        Connections {
            target: contentLoader.item
            onMessage: content.message(sender, msg)
        }
    }


    Rectangle {
        color: "#232323"
        width: elementsWidth
        height: parent.height
        anchors.left: parent.left
        objectName: "ElementPanel"
        id: elementPanel

        FontLoader {
            source: "fontawesome.ttf"
        }
        ListView {
            orientation: Qt.Vertical
            id: "elements"
            objectName: "Elements"
            height: parent.height
            width: parent.width
            model: ElementModel
            clip: true
            signal itemClicked(string title)
            signal itemHovered(string title)
            signal itemUnhovered(string title)
            signal itemLoaded(string title)
            delegate: Element {
                icon: model.icon
                title: model.title
                icon_color: model.icon_color
                Component.onCompleted: {
                    clicked.connect(elements.itemClicked)
                    onEntered.connect(elements.itemHovered)
                    onExited.connect(elements.itemUnhovered)
                    elements.itemLoaded(model.title)
                }
            }

        }
    }
}
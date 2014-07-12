import QtQuick 2.3
import QtQuick.Controls 1.2
import "font.js" as Font
import "custom"

Rectangle {
    width: contentWidth + elementPanel.width
    signal resized(int w)
    onWidthChanged: resized(width)
    Behavior on width { PropertyAnimation {} }
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
            delegate: Element {
                icon: model.icon
                title: model.title
                icon_color: model.icon_color
                Component.onCompleted: {
                    clicked.connect(elements.itemClicked)
                }
            }

        }
    }
    Rectangle {
        id: "content"
        objectName: "Content"
        anchors.right: parent.right
        color: "#552222"
        height: parent.height
        width: parent.width - elementPanel.width
    }
}
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

        Row {
            spacing: 8
            width: parent.width
            //color: "lightblue"
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.leftMargin: 24;
            anchors.topMargin: 18;
            anchors.horizontalCenter : parent.horizontalCenter

            DRoundImage {
                id: round_image

                roundRadius: 30
                borderWidth: 2
                glowRadius: 2
                imageSource: "avatar.png"

            }
            Text {
                font.pointSize: 10
                color: "#eee"
                text: "Alexey 'Averrin' Nabrodov"
            }
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
            delegate: Element {
                icon: model.icon
                title: model.title
                icon_color: model.icon_color
                Component.onCompleted: {
                    clicked.connect(elements.itemClicked)
                    onEntered.connect(elements.itemHovered)
                    onExited.connect(elements.itemUnhovered)
                }
            }

        }
    }
}
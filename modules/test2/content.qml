import QtQuick 2.3
import QtQuick.Controls 1.2
import "frontend/qml/font.js" as Font
import "frontend/qml/widgets"

Row {
    spacing: 8
    width: parent.width
    //color: "lightblue"
    anchors.top: parent.top
    anchors.left: parent.left
    anchors.leftMargin: 24;
    anchors.topMargin: 18;
    anchors.horizontalCenter : parent.horizontalCenter
    signal message(string sender, string msg)

    DTextButton{
        text: "Exit"
        onClicked: {
            parent.message("Cube", "exit")
        }
    }
}
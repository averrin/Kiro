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

    DRoundImage {
        id: round_image

        roundRadius: 30
        borderWidth: 2
        glowRadius: 2
        imageSource: "frontend/qml/avatar.png"

    }
    Text {
        font.pointSize: 10
        color: "#eee"
        text: "Alexey <strong><font color='#3f79ff'>Averrin</font></strong> Nabrodov"
    }
}
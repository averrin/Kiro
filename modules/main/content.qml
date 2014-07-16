import QtQuick 2.2
import QtQuick.Controls 1.1
import "../../frontend/qml/font.js" as Font
import "../../frontend/qml/widgets"

Row {
    spacing: 8
    signal message(string sender, string msg)

    DRoundImage {
        id: round_image

        roundRadius: 30
        borderWidth: 2
        glowRadius: 2
        imageSource: "../../frontend/qml/avatar.png"

    }
    Text {
        font.pointSize: 10
        color: "#eee"
        text: "Alexey <strong><font color='#3f79ff'>Averrin</font></strong> Nabrodov"
    }
}

import QtQuick 2.2
import QtQuick.Controls 1.1
import "../../frontend/qml/font.js" as Font
import "../../frontend/qml/widgets"

Grid {
    signal message(string sender, string msg)
    columns: 2
    spacing: 3
    Column {
        Image {
            width: 150; height: 75
            source: "../../frontend/qml/wall.jpg"
            fillMode: Image.PreserveAspectCrop
        }
            Image {
            width: 150; height: 75
            source: "../../frontend/qml/wall2.png"
            fillMode: Image.PreserveAspectCrop
        }
    }
    Image {
        width: 150; height: 150
        source: "../../frontend/qml/avatar.png"
        fillMode: Image.PreserveAspectCrop
    }
}

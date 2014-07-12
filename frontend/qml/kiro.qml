import QtQuick 2.3
import QtQuick.Controls 1.2
import "font.js" as Font
import "custom"

Rectangle {
    color: "#232323"

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
        delegate: Element {
            icon: model.icon
            title: model.title
        }

    }
}
import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import "frontend/qml/font.js" as Font
import "frontend/qml/widgets"
import "modules/plus/ui"

ListView {
    //height: parent.height
    signal message(string sender, string msg)
    anchors.fill: parent
    model: NotificationModel
    orientation: Qt.Vertical
    clip: true

    delegate: NotificationItem {
        title: model.title
        short_text: model.short_text
        time: model.time
        icon: model.icon
    }
}
import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import "frontend/qml/font.js" as Font
import "frontend/qml/widgets"
import "modules/plus/ui"

ListView {
    signal message(string sender, string msg)
    anchors.fill: parent

    NotificationItem {
        title: "Really Important Notification"
        short_text: "for some reason"
        time: "20:54"
    }
}
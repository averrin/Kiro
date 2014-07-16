import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import "../../../frontend/qml/font.js" as Font
import "../../../frontend/qml/widgets"
import NModel 1.0

Rectangle {
    id: notification
    color: "#171717"
    height: 54
    width: parent.width
    border.width: 1
    border.color: "#3c3c3c"

    property variant notification_item

    RowLayout {
        id: layout
        anchors.fill: parent
        spacing: 6
        Rectangle {
            Layout.fillWidth: true
            Layout.minimumWidth: notification.height
            Layout.preferredWidth: notification.height
            Layout.maximumWidth: notification.height
            Layout.minimumHeight: notification.height
            id: noti_icon
            //height: notification.height
            //width: notification.height
            color: "#1D3741"

            Text {
                anchors.centerIn: parent
                font.pointSize: 18
                font.family: "FontAwesome"
                text: notification_item.icon
                color: "#eee"
            }
        }

        ColumnLayout {
            anchors.left: noti_icon.right
            height: parent.height
            Layout.fillWidth: true
            spacing: 2

            RowLayout {
                Layout.fillWidth: true
                anchors.left: parent.left
                anchors.leftMargin: 4
                anchors.topMargin: 2
                Layout.minimumWidth: notification.width - noti_icon.width - 16
                Layout.preferredWidth: notification.width - noti_icon.width - 16
                Layout.maximumWidth: notification.width - noti_icon.width - 16

                Text {

                    color: "#eee"
                    font.pointSize: 10
                    text: notification_item.title
                }

                Text {
                    anchors.right: parent.right
                    color: "#ccc"
                    font.pointSize: 8
                    text: notification_item.time
                }

            }
            RowLayout {
                Layout.fillWidth: true
                anchors.left: parent.left
                anchors.leftMargin: 12
                anchors.topMargin: 2
                Layout.minimumWidth: notification.width - noti_icon.width - 20
                Layout.preferredWidth: notification.width - noti_icon.width - 20
                Layout.maximumWidth: notification.width - noti_icon.width - 20

                Text {
                    color: "#ccc"
                    font.pointSize: 8
                    text: notification_item.short_text
                }
                Text {
                    anchors.right: parent.right
                    color: "#eee"
                    font.pointSize: 10
                    text: ""
                }
            }
        }
    }


}
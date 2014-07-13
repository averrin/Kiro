import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import "frontend/qml/font.js" as Font
import "frontend/qml/widgets"

ListView {
    signal message(string sender, string msg)
    anchors.fill: parent

    Rectangle {
        id: notification
        color: "#171717"
        height: 54
        width: parent.width
        border.width: 1
        border.color: "#3c3c3c"

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
                    text: Font.Icon.PaperPlane
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

                    Text {

                        color: "#eee"
                        font.pointSize: 10
                        text: "Really Important Notification"
                    }

                    Text {
                        anchors.right: parent.right
                        color: "#eee"
                        font.pointSize: 10
                        text: "20:30"
                    }

                }
                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 12
                    anchors.topMargin: 2
                    color: "#ccc"
                    font.pointSize: 8
                    text: "notification text"
                }
            }
        }


    }

}
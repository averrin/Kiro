import QtQuick 2.1
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import "../../frontend/qml/font.js" as Font
import "../../frontend/qml/widgets"
import "ui"

Column {
    anchors.top: parent.top
    width: parent.width
    anchors.fill: parent
    signal message(string sender, string msg)
    id: notification_pane
    
        DBaseLine{
            width: parent.width
            id: header
            leftLoader.sourceComponent: DssH2 {
                text: "Notifications"
                font.bold: true
                style: Text.Raised
                styleColor: Qt.rgba(0, 0, 0, 0.9)
            }
            rightLoader.sourceComponent: DTextButton {
                text: "Add"
                onClicked: {
                    notification_pane.message("Plus", "add_test:UFO!!")
                    //notifications_list.model.append({"title": "UFO", "short_text": "bzzz", "time":"16:20", "icon":Font.Icon.Comment})
                }
            }
        }

        DSeparatorHorizontal {
            width: parent.width
            id: sep
        }
    
    ListView {
        height: parent.height
        width: parent.width
        model: NotificationModel
        orientation: Qt.Vertical
        clip: true
        id: notifications_list
        objectName: "NotificationsList"
    
        delegate: NotificationItem {
            notification_item: model
            Component.onCompleted: {
                console.log(notification_item.title)
            }
        }

    }
}
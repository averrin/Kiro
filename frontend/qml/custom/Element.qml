import QtQuick 2.3
import QtQuick.Controls 1.2
import QtGraphicalEffects 1.0
import "../font.js" as Font

Rectangle {
        id: btn
        height: parent.width
        width: parent.width
        color: "#2f2f2f"
        property string icon
        property string title
        property color active_color: "#555"
        property color normal_color: "#2f2f2f"
        property color icon_color: "#ccc"
        signal clicked(string title)
        signal onEntered(string title)
        signal onExited(string title)

        Behavior on icon_color { PropertyAnimation {} }

        property bool hovered
        Text {
            id: icon
            color: parent.icon_color
            anchors.centerIn: parent
            font.pointSize: 18
            font.family: "FontAwesome"
            text: parent.icon
        }
        states: [
            State {
                name: "active"; when: hovered
                PropertyChanges { target: btn; color: btn.active_color}
            },
            State {
                name: "normal"; when: !hovered
                PropertyChanges { target: btn; color: btn.normal_color}
            }
        ]
        transitions: Transition {
            ColorAnimation { duration: 300 }
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                btn.clicked(parent.title)
            }
            hoverEnabled: true

            onEntered: {
                parent.hovered = true
                btn.onEntered(parent.title)
            }
            onExited: {
                parent.hovered = false
                btn.onExited(parent.title)
            }
        }
    }
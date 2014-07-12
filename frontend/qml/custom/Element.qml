import QtQuick 2.3
import QtQuick.Controls 1.2
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
        signal clicked

        property bool hovered
        Text {
            color: '#eee'
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
                btn.clicked()
            }
            hoverEnabled: true

            onEntered: { parent.hovered = true }
            onExited: { parent.hovered = false }
        }
    }
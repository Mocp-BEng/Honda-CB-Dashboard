import QtQuick 2.9
import QtQuick.Window 2.2
import QtGraphicalEffects 1.0

ApplicationWindow 
{

    id:root
    visible: true
    width: 1024
    height: 600
    property int external_width: 534
    property int external_height: 533
    property bool external_reverse: false
    property int external_angle: 0
    property int externalstart_angle: 138 //138
    property int external_angle_limit: 360//264
    property int external_radius: 235
    property int external_lineWidth: 60

    Canvas {
        id: external_progress_bar
        width: root.external_width
        height: root.external_height
        x: (root.width - width)/2
        y: (root.height - height)/2
        property real angle: 260
        property real nextAngle: (Math.PI/180)*angle
        property color col: "red"
        onPaint: {
            var ctx = getContext("2d");
            ctx.reset();
            ctx.beginPath();
            ctx.arc(width/2, height/2, root.external_radius, (Math.PI/180) * root.externalstart_angle,(Math.PI/180) * root.externalstart_angle + nextAngle, root.center_reverse);
            ctx.lineWidth = root.external_lineWidth
            ctx.strokeStyle = col
            ctx.stroke()
        }
    }
}
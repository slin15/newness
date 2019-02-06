// Team gg3 - Joyce Liao, Susan Lin
// SoftDev2 pd8
// K #02: Connecting the Dots
// 2019-02-01

var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#6bf9d1";
ctx.strokeStyle = "#389178";

var clear = document.getElementById("clear");
var clearCanvas = function() {
    // the rectangle is the canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
clear.addEventListener("click", clearCanvas);

var drawShape = function(e) {
    // console.log(e);
    // coordinates of where event occurred w.r.t. the target node
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    ctx.closePath();

    moveTo(mouseX, mouseY);

    // start new path
    ctx.beginPath();
    //ctx.lineTo(mouseX, mouseY);
    // ellipse (startX, startY, majorAxis, minorAxis, rotation, startAngle, endAngle)
    // add ellipse to path
    ctx.ellipse(mouseX, mouseY, 30, 30, 0, 0 , Math.PI * 2);
    // draw path
    //ctx.stroke();
    ctx.fill();
    //ctx.closePath();

    // console.log(mouseX + ", " + mouseY);
};
canvas.addEventListener("click", drawShape);

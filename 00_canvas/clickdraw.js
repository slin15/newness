// Susan Lin
// SoftDev2 pd8
// K #00: I See a Red Door...
// 2019-01-30


var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
ctx.fillRect(50,50,100,200);

function clear() {
  var ctx = document.getElementById("slate").getContext("2d");
  ctx.clearRect(0,0,ctx.width,ctx.height);
}
function switch(){
  var ctx = document.getElementById("slate").getContext("2d");
  if (state == 0){
    state = 1;
    document.getElementById("switch").innerHTML = '<button class="button" style="width: 200px;">Rectangle Mode</button>';
  }
  else{
    state = 0;
    document.getElementById("switch").innerHTML = '<button class="button" style="width: 200px;">Dot Mode</button>';
  }
  function main(event){
    var c = document.getElementById("slate");
    var ctx = c.getContext("2d");
    var rect = c.getBoundingClientRect();
    ctx.fillStyle = "#FF0000";

    if (state == 0){
      ctx.fillRect(event.clientX - rect.left-75, event.clientY - rect.top-50, 150, 100);
    }
    else {
      ctx.beginPath();
      ctx.ellipse(event.clientX - rect.left, event.clientY - rect.top, 40, 40, Math.PI, 0, 2 * Math.PI);
      ctx.stroke();
    }
}

// fillStyle
//strokeStyle
//clearRect
//fillText
//ellipse

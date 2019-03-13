var clear_button = document.getElementById("button_clear");
var pic = document.getElementById('vimage');
var oldX, oldY = null;

var drawCircle = function(p, x, y, r, color) {
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", r);
  c.setAttribute("fill", color);
  c.setAttribute("stroke", "black");
  pic.appendChild(c);
};

var drawLine = function (p, x1, y1, x2, y2, color) {
  var c = document.createElementNS("http://www.w3.org/2000/svg", "line");
  c.setAttribute("x1", x1);
  c.setAttribute("y1", y1);
  c.setAttribute("x2", x2);
  c.setAttribute("y2", y2);
  c.setAttribute("fill", color);
  c.setAttribute("stroke", "black");
  pic.appendChild(c);
};

pic.addEventListener('click', function(e)) {
  var x = e.offsetX;
  var y = e.offsetY;
  if (oldX != null && oldY != null) {
    drawline(pic, oldX, oldY, x, y, 'black')
  }
  drawCircle(pic, x, y, 10, 'black')
};

clear_button.addEventListener('click', function()){
  while (pic.firstChild) {
  pic.removeChild(pic.firstChild)
  oldX = null;
  oldY= null;
  }
}

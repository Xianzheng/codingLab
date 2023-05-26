
var canvas;
var ctx;
var x = 50;
var y = 50;
var dx = 5;
var dy = 5;
var WIDTH = 500;
var HEIGHT = 500;

function startGame() {
  canvas = document.getElementById("gameCanvas");
  ctx = canvas.getContext("2d");
  return setInterval(draw, 10);
}

function draw() {
  ctx.clearRect(0,0,WIDTH,HEIGHT);
  ctx.beginPath();
  ctx.fillStyle = "red";
  ctx.fillRect(x,y,10,10);
  if(x + dx > WIDTH || x + dx < 0) {
    dx = -dx;
  }
  if(y + dy > HEIGHT || y + dy < 0) {
    dy = -dy;
  }
  x += dx;
  y += dy;
}
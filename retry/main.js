import { boxes, canvas } from './physics.js';
function main() {

  // Update physics at fixed rate:
  var last = performance.now();
  setInterval(function (time) {
    var now = performance.now();
    do_physics(boxes, canvas.width, canvas.height, now - last);
    last = now;
  }, 50);

  requestAnimationFrame(draw);
}
init_boxes();
main();
var snake = [
  {word: "there", x: 250, y: 400},
  {word: "is", x: 350, y: 400},
  {word: "too", x: 450, y: 400},
  {word: "much", x: 550, y: 400},
  {word: "work", x: 650, y: 400}
];
var words = ["there", "is", "too", "much", "work"];
var grow = true;
var fillVal = 255;
var iter = 1;

function setup() {
  createCanvas(1000, 800);
  textSize(36);
  textAlign(CENTER);
  textStyle(NORMAL);
}

function draw() {
  background(255);
  fill(0, 0, 0, fillVal);
  for (var item of snake) {
    if (item) {
      text(item.word, item.x, item.y);
    }
  }
  if (frameCount % 120 == 0 && grow){
    var newLink = getNext();
    snake.push(newLink)
  } else if (!grow) {
    if (iter <= 3 && frameCount % 10 == 0){
      fillVal -= 10;
    }
    if (fillVal < -100) {
      if (iter == 1){
        snake = [
          {word: "there", x: 250, y: 400},
          {word: "was", x: 350, y: 400},
          {word: "too", x: 450, y: 400},
          {word: "much", x: 550, y: 400},
          {word: "work", x: 650, y: 400}
        ];
        words = ["there", "was", "too", "much", "work"];
        iter += 1;
        grow = true;
        fillVal = 255;
      } else if (iter == 2) {
        snake = [
          {word: "there", x: 250, y: 400},
          {word: "is", x: 350, y: 400},
          {word: "still", x: 450, y: 400},
          {word: "too", x: 550, y: 400},
          {word: "much", x: 650, y: 400},
          {word: "work", x: 750, y: 400}
        ];
        words = ["there", "is", "still", "too", "much", "work"];
        iter += 1;
        grow = true;
        fillVal = 255;
      } else {
        snake = [
          {word: "there", x: 250, y: 750},
          {word: "is", x: 350, y: 750},
          {word: "always", x: 450, y: 750},
          {word: "too", x: 550, y: 750},
          {word: "much", x: 650, y: 750},
          {word: "work", x: 750, y: 750}
        ];
        fillVal = 80;
        iter += 1;
      }
    }
  }
}

function getNext() {
  var prev = snake.length - 1;
  var prevWord = snake[prev].word;
  var prevX = snake[prev].x;
  var prevY = snake[prev].y;
  var next = []
  var possible = [
    {x: prevX + 100, y: prevY},
    {x: prevX - 100, y: prevY},
    {x: prevX, y: prevY + 50},
    {x: prevX, y: prevY - 50}
  ];
  for (var pos of possible) {
    if (isValidPlace(pos)){
      var nextWord = random(words);
      while (nextWord == prevWord) {
        var nextWord = random(words);
      }
      pos.word = nextWord;
      next.push(pos);
    }
  }
  if (next.length == 0){
    grow = false;
  }
  return random(next);
}

function isValidPlace(pos) {
  if (pos.x <= 0 || pos.x >= width || pos.y <= 0 || pos.y >= height) {
    return false;
  }
  for (var other of snake) {
    if (pos.x == other.x && pos.y == other.y){
      return false;
    }
  }
  return true;
}

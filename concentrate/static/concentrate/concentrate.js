$(document).ready(function() {
  squareClickOnOff();
  
  $('#boardinput').mask('SSSSSSSSSSSSSSSSSSSSSSSSS');
});

boardKeyPress = function() {
  var $board = $("#board");
  var $boardinput = $("#boardinput");
  var inputletters = $boardinput.val();
  $board.children().each(function(i) {
    if ('undefined' !== typeof inputletters[i]) {
      this.innerText=inputletters[i].toUpperCase().trim();
    } else {
      this.innerText="";
    }
  });
}

editBoard = function() {
   $("#boardletters").toggleClass("hidden");
   squareClickOnOff();
}

squareClickOnOff = function() {
  var $boardletters = $("#boardletters");
  var $squares = $(".sq");
  if ($boardletters.hasClass("hidden")) {
      $squares.each(function(i) {
        $(this).off("click");
      });
   } else {
      $squares.each(function(i) {
        $(this).on("click",cycleColor);
      });
   }
}



function cycleColor(event) {
   var $square = $(event.target);
   var num = $square.attr("id").slice(1,3);
   var row = Math.floor(num/5);
   var col = num%5;
   if ($square.hasClass('blue') || $square.hasClass('blue2')) {
      update_colors($square,row,col,'red');
   } else if ($square.hasClass('red') || $square.hasClass('red2')) {
      update_colors($square,row,col,'');
   } else {
      update_colors($square,row,col,'blue');
   }
   save_colors();
}

function update_colors($square,row,col,color) {
   if (color == 'blue') {
      $square.removeClass('red');
      $square.removeClass('red2');
      $square.addClass('blue');
   } else if (color == 'red') {
      $square.removeClass('blue');
      $square.removeClass('blue2');
      $square.addClass('red');
   } else {
      $square.removeClass('blue');
      $square.removeClass('blue2');
      $square.removeClass('red');
      $square.removeClass('red2');
   }
   
   //check if I'm defended
   check_defended(row,col);
   
   //check if my neighbors are defended
   check_defended(row-1,col);
   check_defended(row,col-1);
   check_defended(row+1,col);
   check_defended(row,col+1);
}

function check_defended(row,col) {
   //array of colors
   var colors = {};
   colors['B'] = false;
   colors['R'] = false;
   colors['W'] = false;
   if (in_5by5(row,col)) {
      colors[(get_color(row, col))] = true;
      if (in_5by5(row, col-1)) {
         colors[get_color(row, col-1)]= true;
      }
      if (in_5by5(row-1, col)) {
         colors[get_color(row-1, col)] = true;
      }
      if (in_5by5(row, col+1)) {
         colors[get_color(row, col+1)] = true;
      }
      if (in_5by5(row+1, col)) {
         colors[get_color(row+1, col)] = true;
      }
      var num = row*5+col
      var $square = $("#b"+num);
      if (!colors['B'] && !colors['W']) {
         // red defended
         $square.removeClass('red');
         $square.addClass('red2');
      } else if (!colors['R'] && !colors['W']) {
         // blue defended
         $square.removeClass('blue');
         $square.addClass('blue2');
      } else {
         //undefended
         if ($square.hasClass('blue') || $square.hasClass('blue2')) {
            $square.removeClass('blue2');
            $square.removeClass('blue');
            $square.addClass('blue');
         } else if ($square.hasClass('red') || $square.hasClass('red2')) {
            $square.removeClass('red2');
            $square.removeClass('red');
            $square.addClass('red');
         } 
      }
   }

}

function in_5by5(row,col) {
   return (row >= 0 && row <5 && col >= 0 && col < 5);
}

function get_color(row,col) {
   num = row*5+col;
   var $square = $("#b"+num);
   if ($square.hasClass("blue") || $square.hasClass("blue2")) {
      return 'B';
   } else if ($square.hasClass("red") || $square.hasClass("red2")) {
      return 'R';
   } else {
      return 'W';
   }
}

function save_colors() {
   var c = "";
   for (var row=0; row<5; row++) {
      for (var col=0; col<5; col++) {
         c+=get_color(row,col);
      }
   }
   $("#colors").val(c);
}

function set_colors(colors) {
   
}
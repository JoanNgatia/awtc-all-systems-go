$('input[type=submit]').click(function(event){
    event.preventDefault();
  });

$('div.login').find("input.register").on('click', function(){
  $("div.login").toggle();
  $("div.register").fadeToggle("fast");
})

$('div.register').find("input.login").on('click', function(){
  $("div.register").toggle();
  $("div.login").fadeToggle("fast");
})

$(document).ready(function(){
  $("div.register").hide();
})

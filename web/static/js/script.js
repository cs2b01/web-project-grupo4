$('input').focusin(function(){
  $(this).parent('div').addClass("border-input");
})

$('input').focusout(function(){
  $(this).parent('div').removeClass("border-input")
})

var elementTop = $('.nav').offset().top;

$(window).scroll(function(){
  if($(window).scrollTop() >= elementTop){
    $('body').addClass('nav_fixed');
  }
  else{
    $('body').removeClass('nav_fixed');
  }
});

$('.btn-menu').on('click', function(){
  $('.nav').toggleClass('nav-toggle');
  $('.theClient').toggleClass('nav-toggle');
})

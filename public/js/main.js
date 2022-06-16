
  // Collapse arrow animation
  function faqArrowAnimation(){
    $('.faq-content').on('show.bs.collapse', function (e) {
      $('.faq-svg').removeClass('rotated');
      $('#heading-'+($(this).attr('id'))+' .faq-svg').addClass('rotated');
    });
    $('.faq-content').on('hide.bs.collapse', function (e) {
      $('#heading-'+($(this).attr('id'))+' .faq-svg').removeClass('rotated');
    })
  }

document.addEventListener("DOMContentLoaded", function(event) { 
  var innerWidth = window.innerWidth;
  if(innerWidth<768){
    var element = document.querySelectorAll("#search-home #search-input")[0]; 
    element.addEventListener('focus', function(){
      $('html, body').animate({scrollTop: $(element).offset().top -90 }, 'slow');
     });
  }  
});

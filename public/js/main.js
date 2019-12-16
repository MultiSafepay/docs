
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


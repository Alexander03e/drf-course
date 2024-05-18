var swiper = new Swiper(".mySwiper",{
    spaceBetween:30,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination:{
      el: "swiper-pagination"
    }
  });

  $(document).ready(function() {
    $('.btn-custom').click(function() {
        var ilm_id = $(this).data('ilm-id');
        $.ajax({
            url: '{% url "film:like_film" %}',
            data: {
                'ilm_id': ilm_id
            },
            dataType: 'json',
            success: function(data) {
                alert(data.message);
            }
        });
    });
});
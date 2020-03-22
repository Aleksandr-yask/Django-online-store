
(function ($) {
    "use strict";

    /*[ Load page ]
    ===========================================================*/
    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 1500,
        outDuration: 800,
        linkElement: '.animsition-link',
        loading: true,
        loadingParentElement: 'html',
        loadingClass: 'animsition-loading-1',
        loadingInner: '<div data-loader="ball-scale"></div>',
        timeout: false,
        timeoutCountdown: 5000,
        onLoadEvent: true,
        browser: [ 'animation-duration', '-webkit-animation-duration'],
        overlay : false,
        overlayClass : 'animsition-overlay-slide',
        overlayParentElement : 'html',
        transition: function(url){ window.location.href = url; }
    });
    
    /*[ Back to top ]
    ===========================================================*/
    var windowH = $(window).height()/2;

    $(window).on('scroll',function(){
        if ($(this).scrollTop() > windowH) {
            $("#myBtn").css('display','flex');
        } else {
            $("#myBtn").css('display','none');
        }
    });

    $('#myBtn').on("click", function(){
        $('html, body').animate({scrollTop: 0}, 300);
    });


    /*[ Show header dropdown ]
    ===========================================================*/
    $('.js-show-header-dropdown').on('click', function(){
        $('.header-favorites').removeClass('show-header-dropdown');
        $('.js-show-header-dropdown').parent().find('.header-dropdown')

    });

    var menu = $('.js-show-header-dropdown');
    var sub_menu_is_showed = -1;

    for(var i=0; i<menu.length; i++){
        $(menu[i]).on('click', function(){

                if(jQuery.inArray( this, menu ) == sub_menu_is_showed){
                    $('.js-show-header-dropdown').parent().find('.header-dropdown').toggleClass('show-header-dropdown');
                    sub_menu_is_showed = -1;
                }
                else {
                    for (var i = 0; i < menu.length; i++) {
                        $(menu[i]).parent().find('.header-dropdown').removeClass("show-header-dropdown");
                    }

                    $(this).parent().find('.header-dropdown').toggleClass('show-header-dropdown');
                    sub_menu_is_showed = jQuery.inArray( this, menu );
                }
        });
    }

    $(".js-show-header-dropdown, .header-dropdown").click(function(event){
        event.stopPropagation();
    });

    $(window).on("click", function(){
        for (var i = 0; i < menu.length; i++) {
            $(menu[i]).parent().find('.header-dropdown').removeClass("show-header-dropdown");
        }
        sub_menu_is_showed = -1;
    });


     /*[ Fixed Header ]
    ===========================================================*/
    var posWrapHeader = $('.topbar').height();
    var header = $('.container-menu-header');

    $(window).on('scroll',function(){

        if($(this).scrollTop() >= posWrapHeader) {
            $('.header1').addClass('fixed-header');
            $(header).css('top',-posWrapHeader); 

        }  
        else {
            var x = - $(this).scrollTop(); 
            $(header).css('top',x); 
            $('.header1').removeClass('fixed-header');
        } 

        if($(this).scrollTop() >= 200 && $(window).width() > 992) {
            $('.fixed-header2').addClass('show-fixed-header2');
            $('.header2').css('visibility','hidden');
            $('.header2').find('.header-dropdown').removeClass("show-header-dropdown");

        }
        else {
            $('.fixed-header2').removeClass('show-fixed-header2');
            $('.header2').css('visibility','visible');
            $('.fixed-header2').find('.header-dropdown').removeClass("show-header-dropdown");
        } 

    });
    
    /*[ Show menu mobile ]
    ===========================================================*/
    $('.btn-show-menu-mobile').on('click', function(){
        $(this).toggleClass('is-active');
        $('.wrap-side-menu').slideToggle();
    });

    var arrowMainMenu = $('.arrow-main-menu');

    for(var i=0; i<arrowMainMenu.length; i++){
        $(arrowMainMenu[i]).on('click', function(){
            $(this).parent().find('.sub-menu').slideToggle();
            $(this).toggleClass('turn-arrow');
        })
    }

    $(window).resize(function(){
        if($(window).width() >= 992){
            if($('.wrap-side-menu').css('display') == 'block'){
                $('.wrap-side-menu').css('display','none');
                $('.btn-show-menu-mobile').toggleClass('is-active');
            }
            if($('.sub-menu').css('display') == 'block'){
                $('.sub-menu').css('display','none');
                $('.arrow-main-menu').removeClass('turn-arrow');
            }
        }
    });


    /*[ remove top noti ]
    ===========================================================*/
    $('.btn-romove-top-noti').on('click', function(){
        $(this).parent().remove();
    })


    /*[ Block2 button wishlist ]
    ===========================================================*/
    $('.block2-btn-addwishlist').on('click', function(e){
        e.preventDefault();
        $(this).addClass('block2-btn-towishlist');
        $(this).removeClass('block2-btn-addwishlist');
        $(this).off('click');
    });

    /*[ +/- num product ]
    ===========================================================*/
    $('.btn-num-product-down').on('click', function(e){
        e.preventDefault();
        var numProduct = Number($(this).next().val());
        if(numProduct > 1) $(this).next().val(numProduct - 1);
    });

    $('.btn-num-product-up').on('click', function(e){
        e.preventDefault();
        var numProduct = Number($(this).prev().val());
        $(this).prev().val(numProduct + 1);
    });


    /*[ Show content Product detail ]
    ===========================================================*/
    $('.active-dropdown-content .js-toggle-dropdown-content').toggleClass('show-dropdown-content');
    $('.active-dropdown-content .dropdown-content').slideToggle('fast');

    $('.js-toggle-dropdown-content').on('click', function(){
        $(this).toggleClass('show-dropdown-content');
        $(this).parent().find('.dropdown-content').slideToggle('fast');
    });


    /*[ Play video 01]
    ===========================================================*/
    var srcOld = $('.video-mo-01').children('iframe').attr('src');

    $('[data-target="#modal-video-01"]').on('click',function(){
        $('.video-mo-01').children('iframe')[0].src += "&autoplay=1";

        setTimeout(function(){
            $('.video-mo-01').css('opacity','1');
        },300);      
    });

    $('[data-dismiss="modal"]').on('click',function(){
        $('.video-mo-01').children('iframe')[0].src = srcOld;
        $('.video-mo-01').css('opacity','0');
    });

})(jQuery);

// ========================================================================
// ================Add Card===================================
// ========================================================================

$('.add_card_product').click(function () {
    var number = $('.num-product').val();
    var img = $('#product_img_main').attr("img");
    if (number != 0 || number != ''){
       var token = $(' input[name="csrfmiddlewaretoken"]').val();
       var id = $(this).attr('id');
       $.ajax({
           url: '/order/add/',
           type: 'GET',
           data: {
               id: id,
               number: number,
               img: img
           }
      })
      .done(function(data) {
         console.log(data.total_nmb);
         $('.header-icons-noti').html(data.total_nmb);
          $('.header-cart-wrapitem').html(" ");
          var arr = [];
          $.each(data.products, function (k, v) {
              $('.header-cart-wrapitem').append("<li class='header-cart-item'><div onclick='delete_from_cart("+v.id+")' class='header-cart-item-img delete-object' id = '"+v.id+"'><img src='"+ v.img + "' alt='IMG'></div><div class='header-cart-item-txt'><a href='/products/product/"+ v.product_id + "' class='header-cart-item-name'> " + v.name  +"</a><span class='header-cart-item-info'>" + v.nmb +" x $" + v.price_per_item + "</span></div></li>");
              price = v.nmb * v.price_per_item;
              arr.push(price);
          });
          var sum = 0;
          for(var i = 0; i < arr.length; i++){
              sum = sum + arr[i];
          }
          $('.total-price').text(sum.toFixed(2));

         var nameProduct = $('.product-detail-name').html();
         swal(nameProduct, "is added to cart !", "success");

      })
      .fail(function() {
          var nameProduct = $('.product-detail-name').html();
         swal("Error", "We have a problem this a server, try again later", "error");
        console.log("error");
      })
    }
    else{
        console.log("error");
    }
});

// ========================================================================

$('.add_card_shop').click(function () {
       var img = $(this).parent().parent().parent().find('img').attr("src");
       var id = $(this).attr('id');
       var number = 1;
       $.ajax({
           url: '/order/add/',
           type: 'GET',
           data: {
               id: id,
               number: number,
               img: img
           }
      })
      .done(function(data) {
         $('.header-icons-noti').html(data.total_nmb);
          $('.header-cart-wrapitem').html(" ");
          var arr = [];
          $.each(data.products, function (k, v) {
              $('.header-cart-wrapitem').append("<li class='header-cart-item'><div onclick='delete_from_cart("+v.id+")' class='header-cart-item-img delete-object' id = '"+v.id+"''><img src='"+ v.img + "' alt='IMG'></div><div class='header-cart-item-txt'><a href='/products/product/"+ v.product_id + "' class='header-cart-item-name'> " + v.name  +"</a><span class='header-cart-item-info'>" + v.nmb +" x $" + v.price_per_item + "</span></div></li>");
              price = v.nmb * v.price_per_item;
              arr.push(price);
          });
          var sum = 0;
          for(var i = 0; i < arr.length; i++){
              sum = sum + arr[i];
          }
          $('.total-price').text(sum.toFixed(2));
            var bbb = $('.block2-btn-addcart[cart_id='+id+']');
            bbb.each(function() {
                var nameProduct = $(this).parent().parent().parent().find('.block2-name').html();
                swal(nameProduct, "is added to cart !", "success");
            });
      })
      .fail(function() {
          swal("Error", "We have a problem this a server, try again later", "error");
      });
});

// ========================================================================

function delete_from_cart(id){

    $.ajax({
           url: '/order/delete/',
           type: 'GET',
           data: {
               id: id
           }
      })
      .done(function(data) {
          $('.header-icons-noti').html(data.total_nmb);
          var arr = [];
          $('#'+id).parent().hide();
          if  (data.products.length == 0) {
              $('.header-cart-wrapitem').html("Basket is empty");
          }
          $.each(data.products, function (k, v) {
              price = v.nmb * v.price_per_item;
              arr.push(price);
          });
          var sum = 0;
          for(var i = 0; i < arr.length; i++){
              sum = sum + arr[i];
          }
          $('.total-price').text(sum.toFixed(2));

      })
      .fail(function() {
          swal("Error", "We have a problem this a server, try again later", "error");
      });
}

$('.delete-object').click(function () {
    var id = $(this).attr("id");
    $.ajax({
           url: '/order/delete/',
           type: 'GET',
           data: {
               id: id
           }
      })
      .done(function(data) {
          $('.header-icons-noti').html(data.total_nmb);
          var arr = [];
          $('.table-row[id_product = '+id+']').hide();
          $('.deleted-obj[id_product = '+id+']').hide();

          if  (data.products.length == 0) {
              $('.crt').html("Cart is empty");
          }
          if  (data.products.length == 0) {
              $('.header-cart-wrapitem').html("Basket is empty");
          }
          $.each(data.products, function (k, v) {
              price = v.nmb * v.price_per_item;
              arr.push(price);
          });
          var sum = 0;
          for(var i = 0; i < arr.length; i++){
              sum = sum + arr[i];
          }
          $('.total-price').text(sum.toFixed(2));

      })
      .fail(function() {
          swal("Error", "We have a problem this a server, try again later", "error");
      });
});

// ========================================================================
$('.send-message').click(function () {
    swal('Message sent', "Thank. We will contact you.", "success");
});
// ========================================================================
// ===========================Filter=================================
// ========================================================================

$('#filt-price').click(function () {
    var lower = $('#value-lower').html();
    var upper = $('#value-upper').html();
    window.location.href = "/products/price/?min="+lower+"&max="+upper;
});
$('#sort-def').change(function () {
   console.log($(this).val());
   window.location.href = "/products/?sort="+$(this).val();
});


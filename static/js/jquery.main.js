$(document).ready(function() {
	"use strict";
    initAddClass();
    // Add Class  init
    function initAddClass() {
        "use strict";

        jQuery('.nav-opener').on( "click", function(e){
            e.preventDefault();
            jQuery("body").toggleClass("nav-active");
        });
    }
	
//    initSlickSlider();
    // Slick Slider init
    function initSlickSlider() {
        "use strict";

        jQuery('.testimonail-slider').slick({
            dots: true,
            speed: 800,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: lay,
            adaptiveHeight: true,
            autoplay: true,
            arrows: true,
            autoplaySpeed: 4000
        });
    }
    initTabs();
    // content tabs init
    function initTabs() {
        jQuery('.tabset').tabset({
            tabLinks: 'a',
            addToParent: true,
            defaultTab: true
        });
    }
    $('.account').mouseover(function(){
        $('.account').css('border','1px solid #E2DEDB')
        $('.account').css('backgroud-color','#FFFFFF')
        $('.user_select').css('display','block')
    });
    $(".account").mouseout(function(){
        $('.account').removeAttr('style')
        $('.user_select').css('display','none')
      });
    $('.account .user_select a').mouseover(function(){
        $(this).css('color','red')
    });
    $('.account .user_select a').mouseout(function(){
        $(this).removeAttr('style')
    })
});



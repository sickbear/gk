$(document).ready(function () {

	// везде: открытие бокового меню
	function openMenu() {
		$('.burger-panel').css({
			'animation-name': 'toRight',
			'animation-duration': '0.3s',
			'animation-timing-function': 'linear',
		});
		$(".background").addClass("opened");
		$("html").addClass("no-scroll");
	};

	// везде: закрытие бокового меню
	function closeMenu() {
		$('.burger-panel').css({
			'animation-name': 'toLeft',
			'animation-duration': '0.3s',
			'animation-timing-function': 'linear'
		});

		setTimeout(function () {
			$(".background").removeClass("opened");
			$("html").removeClass("no-scroll");
		}, 300);
	};

	// модалка: показать/ скрыть пароль
	var passButton = $('.modal__password-btn');

	passButton.click(function () {
		var pasInput = $(this).prev();
		var typeInput = pasInput.attr('type');
		if (typeInput === 'password') {
			$(this).addClass('modal__password-btn-open');
			pasInput.prop("type", "text")
		} else if (typeInput === 'text') {
			$(this).removeClass('modal__password-btn-open');
			pasInput.prop("type", "password");
		}
	});

	function resizeContent() {
		if ($(".rubric-news").length > 0) {
			if (window.innerWidth > 1024) {
				$(".rubric-news").removeClass('hide')
			} else if (window.innerWidth <= 1024) {
				$(".rubric-news").addClass('hide')

				$(document).on('click', '.rubric-item__toggle', function () {
					$(".rubric-news").toggleClass('hide')
					slider.slick("slickSetOption", "draggable", true, true)
				})
			};
		}
	}

	resizeContent()

	// везде: закрыть горячую новость
	$(".attention .button--close").click(function (evt) {
		evt.preventDefault();
		$(this).closest(".attention").css({
			display: "none"
		});
	});

	// везде: нижний фиксированный баннер ПЕРЕДЕЛАТЬ НА ФУНКЦИИ
	$(".button--banner").click(function (evt) {
		evt.preventDefault();
		$(this).toggleClass("button--banner-close");
		var elem = $(this).closest(".banner-wide--fixed");

		if (window.innerWidth > 1024) {
			if (elem.hasClass("banner-wide--fixed-desc-open") == true) {
				elem.removeClass("banner-wide--fixed-desc-open");
			} else {
				elem.addClass("banner-wide--fixed-desc-open");
			}
		} else {
			elem.removeClass("banner-wide--fixed-desc-open");
		}
	});

	$(".button--burger").click(function (evt) {
		evt.preventDefault();
		if ($(".burger-panel").hasClass("opened-flex") == false) {
			openMenu();
		} else {
			closeMenu();
		}
	});

	$(".button--dark-close").click(function () {
		if ($(".burger-panel").hasClass("opened-flex") == true) {
			closeMenu();
		} else {
			openMenu();
		}
	});

	$(".background").click(function () {
		closeMenu();
	});

	// toggle вход/ регистрация

	$(".enter__link").click(function () {
		$(".modal-enter__button").removeClass("modal-enter__button--active");
		if ($(this).data("btn") == "enter") {
			$("#enterbtn").addClass("modal-enter__button--active");
			$(".login").show();
			$(".registration").hide();
		} else if ($(this).data("btn") == "registr") {
			$("#registrbtn").addClass("modal-enter__button--active");
			$(".login").hide();
			$(".registration").show();
		}
	});

	$("#enterbtn").click(function () {
		$(".modal-enter__button").removeClass("modal-enter__button--active");
		$("#enterbtn").addClass("modal-enter__button--active")
		$(".login").show();
		$(".registration").hide();
	});

	$("#registrbtn").click(function () {
		$(".modal-enter__button").removeClass("modal-enter__button--active");
		$("#registrbtn").addClass("modal-enter__button--active")
		$(".login").hide();
		$(".registration").show();
	});

	// переворот стрелочки
	$(".button--arrow").click(function () {
		$(this).toggleClass("button--arrow--rotate");
	});

	$(".button[data-button='hotnews']").click(function () {
		$(".news-feed").slideToggle().toggleClass("closed");
	});

	// modals

	$(".search__link").fancybox();

	$(".modal-enter__link").click(function () {
		$.fancybox.close(true);
	});

	// закрытие нижнего баннера

	$('.button--fixbanner-close').click(function (evt) {
		evt.preventDefault()
		$(this).closest('.banner-wide--fixed').remove()
	})


	// sliders

	// ГЛАВНАЯ слайдер рубрик
	if ($('.is-js-rubric-slider').length > 0) {
		var slider = $('.is-js-rubric-slider').slick({
			fade: true,
			cssEase: 'linear',
			adaptiveHeight: true,
			prevArrow: $('.slick-prev'),
			nextArrow: $('.slick-next'),
		});

		$('.is-js-rubric-slider').removeClass('hide')
	}

	if ($('.third-card-slider').length > 0) {
		$('.third-card-slider').slick({
			speed: 500,
			fade: true,
			cssEase: 'linear',
			autoplay: true
		});

		$('.third-card-slider').removeClass('visually-hide')
	}

	if ($('.half-card-slider').length > 0) {
		$('.half-card-slider').slick({
			speed: 500,
			fade: true,
			cssEase: 'linear',
			autoplay: true
		});

		$('.half-card-slider').removeClass('visually-hide')
	}

	if ($('.photorep-slider').length > 0) {
		$('.photorep-slider').slick({
			dots: true,
			adaptiveHeight: true,
		})

		$('.photorep-slider').removeClass('hide')
	}

	// commercial
	if ($('.review').length > 0) {
		$('.review').slick({
			speed: 500,
			adaptiveHeight: true,
			arrows: true,
			autoplay: true
		});

		$('.review').removeClass('hide')
	}

	// добавить смайлы
	if ($('.progect-textarea--add-comment').hasClass('add-smile')) {
		$(".add-smile").emojioneArea();
	}

	// перелистывание

	if ($('.main-content-wrapper').length > 0) {
		$('.main-content-wrapper').stickyStack({
			containerElement: '.main-content-wrapper',
			stackingElement: 'div',
			boxShadow: '0 -3px 20px rgba(0, 0, 0, 0.25)'
		});
	}

	$(window).resize(function () {

		if (window.innerWidth > 1024) {
			$(window).scroll(function () {
				var left = $(this).scrollLeft();
				$('.headhesive').css({
					'left': -left,
					'min-width': "1280px"
				});
			});
			
			$('.news-feed').removeClass('closed')
			$('.news-feed').removeAttr('style')
			
		} else if (window.innerWidth <= 1024) {
			$(window).scroll(function () {
				$('.headhesive').removeAttr('style')
			})
			
			$(".button--banner").removeClass("button--banner-close");	
			$(".banner-wide--fixed").removeClass("banner-wide--fixed-desc-open")
			
		}

		resizeContent()

	})

	
	
	

	if (window.innerWidth <= 1024) {
		$(".rubric__news").hide();
		$(".rubric__more").hide();
		$(".rubric__sub-text").click(function () {
			$(".rubric__news").toggle();
			$(".rubric__more").toggle();
			slider.slick("slickSetOption", "adaptiveHeight", true, true);
		});
	}

	if (window.innerWidth <= 767) {
		$("#float-banner").fancybox();
		$('#float-banner').trigger('click');
	}

	if (window.innerWidth > 1024) {
		$(window).scroll(function () {
			var left = $(this).scrollLeft();
			$('.headhesive').css({
				'left': -left,
				'min-width': "1280px"
			});
		});
	} else if (window.innerWidth <= 1024) {
		$(window).scroll(function () {
			$('.headhesive').removeAttr('style')
		})
	}

});

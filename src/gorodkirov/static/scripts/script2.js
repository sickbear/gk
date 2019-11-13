$(document).ready(function () {

    var registrationForm = $('#registration_form');
    window.onSubmitRegistrationForm = onSubmitRegistrationForm;

    // проверка скрытой капчи перед отправкой регистрационной формы
    function onSubmitRegistrationForm(token) {
        if ($('#check1').is(':checked')) {
            registrationForm.submit();
        } else {
            grecaptcha.reset();
        }
    }

    // отправка регистрационной формы
    registrationForm.on('submit', function(e) {
        e.preventDefault();
        var thisForm = $(this);
        var actionEndpoint = thisForm.attr('action');
        var httpMethod = thisForm.attr('method');
        var formData = thisForm.serialize();

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            dataType: 'json',
            success: function(data) {
                if (data['success'])  {
                    $('.registration').html(data['html']);
                } else {
                    grecaptcha.reset();
                    $('.registration_form_errors').empty();
                    for (var error in data['errors']) {
                        if (error != 'password2') {
                            $('.registration_form_errors').append('<p>' + error + ': ' + data['errors'][error] + '</p>');
                        }
                    }
                }
            },
            error: function() {
                $('.registration_form_errors').empty().append('<p>Нет ответа от сервера, попробуйте позже.</p>');
            }
        });

    });

    // поиск по сайту
    $('#search_form').on('submit', function(e) {
        e.preventDefault();
        var thisForm = $(this);
        var actionEndpoint = thisForm.attr('action');
        var httpMethod = thisForm.attr('method');
        var formData = thisForm.serialize();
        var searchResult = $('.search-block__list');

        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            dataType: 'html',
            success: function(data) {
                searchResult.html(data)
            },
            error: function() {
                searchResult.html('<p style="color:#fff;">Нет ответа от сервера, попробуйте позже.</p>');
            }
        });
    });

});
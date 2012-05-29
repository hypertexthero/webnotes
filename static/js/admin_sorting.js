// http://stackoverflow.com/questions/7646781/django-jquery-ajax-403-error
// https://docs.djangoproject.com/en/dev/ref/contrib/csrf/#ajax

jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

// http://djangosnippets.org/snippets/2047/
$(function() {
    $("#content-main").sortable({
        axis: 'y',
        items: '.row1, .row2',
        stop: function(event, ui) {
            var indexes = Array();
            var url = "";
            $("#content-main").find(".row1, .row2").each(function(i){
                var id = $(this).find('.order_link').html();
                // the bad way i know.
                url = $(this).find('.order_link').attr('href');
                indexes.push(id);
            });
            $.ajax({
               url: url,
               type: 'POST',
               data: {
                 indexes: indexes.join(","),
               }
            });
        },
    });
    $('#content-main table tbody').find('.order_link').parent('td').hide();
    /* 
       :contains(value) — value here must be the same as in model's 
       order_link.short_description 
    */
    $('#content-main table thead').find('th:contains("Order")').hide();
    $("#content-main table tbody").disableSelection();
});

$(document).ready(function(){
//alert('loading');
//    if(confirm('Click on ok.')){
//        alert('Django Class');
//    }else{
//        alert('Django Class Else');
//    }

// var falane = new Classname(); ~~  $('#falane');
// var country = new Country();
// country.value;
    $('#country').attr('disabled', true);
    $('#state').attr('disabled', true);

    $(document).on('keyup', '#city', function(){
        $('#country').removeAttr('disabled', true);
        $('#state').removeAttr('disabled', true);
    });

    $(document).on('change', '#country', function(){
//        $.ajax({
//            url: '/back/ajax/?action=countrychange&countryid=' + $('#country').val(),
//        })
//        .done(function(data){
//            alert(data);
//        })
//        .fail(function(){
//            alert('Something went wrong.');
//        });


        $.ajax({
            url: '/back/ajax/',
            type: 'POST',
            beforeSend: function(xhr, settings) {
                 function getCookie(name) {
                     var cookieValue = null;
                     if (document.cookie && document.cookie != '') {
                         var cookies = document.cookie.split(';');
                         for (var i = 0; i < cookies.length; i++) {
                             var cookie = $.trim(cookies[i]);
                             // Does this cookie string begin with the name we want?
                             if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                 break;
                             }
                         }
                     }
                     return cookieValue;
                 }
                 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                     // Only send the token to relative URLs i.e. locally.
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 }
             },
            data:{
                'action':'countrychange',
                'countryid':$('#country').val()
            },
        })
        .done(function(data){
            alert(data);
        })
        .fail(function(){
            alert('Something went wrong.');
        });
    });

    $(document).on('dblclick', '#country', function(){
        alert('Double Click');
    });

    $(document).on('mousedown', '#country', function(e){
        if( e.button == 2 ) {
          alert('Right mouse button!');
          return false;
        }
    });

//    $(document).on('click', '#country', function(){
//        alert('Single Click');
//    });//jquery style

//    var conob = document.getElementById('country');
//    conob.addEventListener('click', function(){
//        alert('Single Click');
//    });//native js style

    $.ajax({

    });

//    $(document).on('click','.ourbutton', function(){
//        alert('See this alert.');
//        if( $(this).text() == 'You Clicked'){
//            $(this).text('Link To Button');
//            $(this).css('background-color', '#337ab7');
//        }else{
//            $(this).text('You Clicked');
//            $(this).css('background-color', 'green');
//        }
//        $(this).html('<input type="text" class="form-control" placeholder="Type Something" />');
//    });

//        $('.ourbutton').one('click', function(){
//            alert('Only one time alert.');
//        });

//    var a = 0;
//    $(document).on('click', '.ourbutton', function(){
//        a = a + 1;
//        $('.counter').text(a);
//    });

    $(document).on('click', '.ourbutton', function(){
        if($('body').hasClass('bodytagcss')){
            $('body').removeClass('bodytagcss');
        }else{
            $('body').addClass('bodytagcss');
        }
    });
});
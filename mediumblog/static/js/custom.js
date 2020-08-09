$(document).ready(function(){
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
        $.ajax({
            url: '/back/ajax/?action=countrychange&countryid=' + $('#country').val(),
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

    var conob = document.getElementById('country');
    conob.addEventListener('click', function(){
        alert('Single Click');
    });//native js style

    $.ajax({

    });
});
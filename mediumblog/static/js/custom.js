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
        .done(date){
            alert(data);
        }
        .fail(){
            alert('Something went wrong.');
        };
    });
});
$( document ).ready(function() {

    $( "#subForm" ).submit(function( event ) {
        var data = {email: $("#subEmail").val() };
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/subscribe",
            data: data,
            success: function(data){
            }
          });
        $("#subForm").hide();
        $("#subscribe-success").show();
        event.preventDefault();
    });
});
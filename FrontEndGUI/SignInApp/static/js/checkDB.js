$(function(){
        $('#btnCheckDB').click(function(){
                console.log("HTML Button pressed- .js now running. Attempting AJAX POST on javascript file");
                $.ajax({
                        url: '/checkDB',
                        data: $('form').serialize(),
                        type: 'POST',
                        success: function(response){
                                console.log(response);
                        },
                        error: function(error){
                                console.log(error);
                        }
                });
        });
});


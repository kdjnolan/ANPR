$(function(){
        $('#btnSignIn').click(function(){
                console.log("Button(btn- signIn from HTML) activated the javascript code");
                $.ajax({
                        url: '/signIn',
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



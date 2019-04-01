$(function(){
        $('#btnSignIn').click(function(){
                console.log("Button pressed. 'signin.js' now running. Attempting AJAX POST on javascript file");
                $.ajax({
                        url: '/signIn',
                        data: $('form').serialize(),
                        type: 'POST',
                        success: function(response){
                                //console.log(response);                                
                        },
                        error: function(error){
                                console.log(error);
                        }
                });
        });
});



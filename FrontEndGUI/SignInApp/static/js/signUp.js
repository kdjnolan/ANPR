$(function(){
	$('#btnSignUp').click(function(){
                console.log("Button pressed. 'signUp.js' now running. Attempting AJAX POST on javascript file");
		$.ajax({
			url: '/signUp',
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

$(function(){
	$('#btnCheckDB').click(function(){
		console.log("Button(btnCheckDB from HTML) activated the javascript code");
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

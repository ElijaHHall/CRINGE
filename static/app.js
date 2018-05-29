$(document).ready(function(){
	$('.modal').modal();

		$('#drink-btn').on('click', function(event){
		event.preventDefault();
		console.log('clicked')
		var element = $(this);
			$.ajax({
				url: '/users/drink/',
				method: 'GET',
				data: {message_id: element.attr('data-id')},
				success: function(response){
				console.log(response);
				console.log()
				}
			})
		})
});
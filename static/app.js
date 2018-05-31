
$(document).ready(function(){
	$('.modal').modal();

		$('#drink-btn').on('click', function(event){
		event.preventDefault();
		console.log('clicked')
		var element = $(this);
			$.ajax({
				url: '/users/send_message/',
				method: 'GET',
				data: {username: element.attr('data-id')},
				success: function(response){
					$('#appendMessages').append("<li>" + response + "<hr/>");

				}
			})
		})
});

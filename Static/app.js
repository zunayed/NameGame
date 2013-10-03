$('#checkButton').on('click', function(){

	var dictionary = {}

	$('select').each(function(index, el){
		dictionary[$(el).attr("name")] = $(el).val()
	})

	console.log('button clicked')
	$.post("/check", dictionary,function(response){

		$('#result').text(response)
	})


})


$('select').each(function(index, el) {console.log(index, $(el).val())})
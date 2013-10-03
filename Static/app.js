$('#checkButton').on('click', function(){

	var dictionary = {}

	$('select').each(function(index, el){
		dictionary[$(el).attr("name")] = $(el).val()
	})

	$.post("/check", dictionary,function(response){
		//$('#result').text(response)

		$('img').each(function(index, el){
			if(response['answers'][index]){
				$(el).addClass('correct')
			}else{
				$(el).addClass('incorrect')
			}
		})

	})
})

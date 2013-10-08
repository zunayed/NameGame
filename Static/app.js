$('#checkButton').on('click', function(){

	var dictionary = {}
	$('#checkButton').hide();

	$('select').each(function(index, el){
		dictionary[$(el).attr("name")] = $(el).val()
	})

	$.post("/check", dictionary,function(response){

		$('img').each(function(index, el){
			if(response['answers'][index]){
				$(el).addClass('correct')
			}else{
				$(el).addClass('incorrect')
			}
		})
	})
})

$('#morePeople').on('click', function(){
	location.reload();
})


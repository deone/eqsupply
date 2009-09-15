function createQuote()	{
    var data = "user=" + $("#user-id").val() + "&title=" + $("#title").val();
    var url = "/quote/create/";

    ajaxPost(data, url);
}

function ajaxPost(data, url) {

    $.ajax({
	url: url,
	type: "POST",
	data: data,
	dataType: "json",

	success: function(response) {
	    alert(response);
	},

	error: function(response)   {
	    alert(response);
	}
    });

}

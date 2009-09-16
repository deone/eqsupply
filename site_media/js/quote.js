$(function()	{

});

function createQuote()	{
    var data = "user=" + $("#user-id").val() + "&title=" + $("#title").val();
    var url = "/quote/create/";

    ajaxPost(data, url);
}

function ajaxGet()  {
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

function get_pending_quote(url)	{
}

$(function()	{

});

function createQuote()	{
    var data = "user=" + $("#user-id").val() + "&title=" + $("#title").val();
    var url = "/quote/create/";

    ajaxPost(data, url);
}

function ajaxGet(url)	{

    $.ajax({
	url: url,
	type: "GET",
	dataType: "json",

	success: function(response) {
	    showQuotes(response.data.body);
	},

	error: function(response)   {
	    alert(response);
	}
    });

}

function ajaxPost(data, url) {

    $.ajax({
	url: url,
	type: "POST",
	data: data,
	dataType: "json",

	success: function(response) {
	    if (response.data.type != "ok") {
	    } else  {
		document.location = "/quote/" + response.data.body["id"] + "/add_item/";
	    }
	},

	error: function(response)   {
	    alert(response);
	}
    });

}

function showQuotes(data)   {
    var quoteList = "<ul>";

    for (var i=0; i<data.length; i++)	{
	quoteList += "<li><a href='#'>" + data[i].id + " " + data[i].title + " " + data[i].time_created + "</a></li>";
    }

    quoteList += "</ul>";

    $("#p-quotes").append(quoteList);

}

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
	    if (response.data.body != "") {
		showQuotes(response.data.body);
	    } else  {
		$("#p-quotes").append("<p>You have no pending quotes.</p>");
	    }
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
		document.location = "/product_groups/?quote_id=" + response.data.body["id"];
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

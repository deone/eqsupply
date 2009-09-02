$(function()	{

    $("#tabs").tabs();

});

function ajaxGet(url)	{

    $.ajax({
	url: url,
	type: "GET",
	dataType: "json",

	success: function(response) {
	    if (response[0]["model"] == "quote_generator.manufacturer") {
		showManufacturers(response);
	    }
	    if (response[0]["model"] == "quote_generator.category") {
		showCategories(response);
	    }
	},

	error: function(response)   {
	    alert(response);
	}
    });

}

function showManufacturers(data)	{
    var lst = "";

    for (var i = 0; i < data.length; i++)   {
	lst += "<dt><a href=''>" + data[i].fields.name + "</a></dt>" + 
		"<dd>" + data[i].fields.city + ", " + data[i].fields.country + "</dd>";
    }
    $("#manuf_list").html(lst);
}

function showCategories(data)	{
    var lst = "";

    for (var i = 0; i < data.length; i++)   {
	lst += "<dt><a href=''>" + data[i].fields.name + "</a></dt>" + 
		"<dd>" + data[i].fields.short_description + "</dd>";
    }
    $("#category_list").html(lst);
}

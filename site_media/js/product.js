$(function()	{

    $("#tabs").tabs();

});

function ajaxGet(url)	{

    $.ajax({
	url: url,
	type: "GET",
	dataType: "json",

	success: function(response) {
	    showManufacturers(response);
	},

	error: function(response)   {
	    alert(response);
	}
    });

}

function showManufacturers(data)	{
    var lst = "";

    for (var i = 0; i < data.length; i++)   {
	lst += "<dt><a href='http://" + data[i].fields.website + "'>" + data[i].fields.name + "</a></dt>" + 
		"<dd>" + data[i].fields.city + ", " + data[i].fields.country + "</dd>";
    }
    $("#manuf_list").append(lst);
}

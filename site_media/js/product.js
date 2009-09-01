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
	lst += "<li><a href=''>" + data[i].fields.name + "</a></li>";
    }
    $("#manuf_list").append(lst);
}

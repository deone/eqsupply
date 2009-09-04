$(function()	{

    $("#tabs").tabs();

    $(".biller").hide();

    $(".product-detail").hover(
	function()  {
	    $(this).find(".biller").show();
	},
	function()  {
	    $(this).find(".biller").hide();
	}
    );

});


function ajaxPost(data, url)  {//{{{

    $.ajax({
        url: url,
        type: "POST",
        data: data,
        dataType: "json",

        success: function(response) {
            if (response.code != 0) {
                alert(response.data.body);
            } else  {
		if (response.data.type != "ok")	{
		} else	{
		    showMessage(response.data.type, response.data.body);
		}
            }
        },

        error: function(response)   {
            alert(response);
        }
    });

}//}}}

function ajaxGet(url)	{//{{{

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

}//}}}

function showManufacturers(data)	{//{{{
    var lst = "";

    for (var i = 0; i < data.length; i++)   {
	lst += "<dt><a href='/products/manufacturer/" + data[i].pk + "/'>" + data[i].fields.name + "</a></dt>" + 
		"<dd>" + data[i].fields.city + ", " + data[i].fields.country + "</dd>";
    }
    $("#manuf_list").html(lst);
}//}}}

function showCategories(data)	{//{{{
    var lst = "";

    for (var i = 0; i < data.length; i++)   {
	lst += "<li><a href='/products/category/" + data[i].pk + "/'>" + data[i].fields.name + "</a></li>";
    }
    $("#category_list").html(lst);
}//}}}

function setQuote() {
    if ($("#quantity").val() == "")	{
	showMessage("error", "Please tell us the quantity you need");
    } else  {
	var userId = $("#user-id").val();    
	var productId = $("#product-id").val();
	var quantity = $("#bill" + productId + " " + "#quantity").val();

	var data = "user=" + userId + "&product=" + productId + "&quantity=" + quantity;
	var url = "/products/setquote/";

	ajaxPost(data, url);
    }
}

function showMessage(msgType, msg)	{
    if (msgType != "error") {
	$("#msger").html("<p>" + msg + "</p>");
	$("#msger").slideDown(500);
	$("#msger").slideUp(2000);
    } else  {
	$("#msger").html("<p class='err'>" + msg + "</p>");
	$("#msger").slideDown(500);
    }
}

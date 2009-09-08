$(function()	{

    $("#tabs").tabs();

    $(".product-detail").hover(
	function()  {
	    $(this).find(".add-quote").show();
	},
	function()  {
	    $(this).find(".add-quote").hide();
	}
    );

});

// We can construct a url->action(s) mapping because ajaxPost() would be handling all post requests in this module.
function ajaxPost(data, url, options)  {//{{{

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
		    $("#cell" + options["product_id"]).find(".add-quote").remove();
		    $("#cell" + options["product_id"]).find(".remove-quote").show();
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
	var quantity = $("#cell" + productId + " " + "form" + " " + "#quantity").val();

	var data = "user=" + userId + "&product=" + productId + "&quantity=" + quantity;
	var url = "/products/setquote/";
	var options = {"product_id": productId};

	ajaxPost(data, url, options);
    }
}

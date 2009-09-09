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
		    if (url == "/products/setquote/")	{
			showMessage(response.data.body);
			$("#cell" + options["product"]).find(".add-quote").hide();
			$("#cell" + options["product"]).parent().hover(
			    function()	{
				$(this).find(".add-quote").hide();
			    },
			    function()	{
				$(this).find(".add-quote").hide();
			    }
			);
			$("#cell" + options["product"]).find(".remove-quote").show();
		    } else  {
			showMessage(response.data.body);
			$("#cell" + options["product"]).find(".remove-quote").hide();
			$("#cell" + options["product"]).find(".add-quote").show();
			$("#cell" + options["product"]).parent().hover(
			    function()	{
				$(this).find(".add-quote").show();
			    },
			    function()	{
				$(this).find(".add-quote").hide();
			    }
			);
		    }
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

function getQuoteData(form, productId)	{

    var userId = $("#user-id").val();

    if (form == ".add-quote")	{
	if ($("#quantity" + productId).val() != "")	{

	    return  {
		"user": userId, 
		"product": productId, 
		"quantity": $("#quantity" + productId).val()
	    };

	} else	{
	    showMessage("Please tell us the quantity you need");
	    return null;
	}

    } else  {
	return	{
	    "user": userId, 
	    "product": productId
	}
    }
}

// These two functions are the same!!
function setQuote(productId) {
    var params = getQuoteData(".add-quote", productId);

    if (params)	{
	var data = "user=" + params["user"] + "&product=" + params["product"] + "&quantity=" + params["quantity"];
	var url = "/products/setquote/";

	ajaxPost(data, url, params);
    }
}

function unsetQuote(productId)	{
    var params = getQuoteData(".remove-quote", productId);

    var data = "user=" + params["user"] + "&product=" + params["product"];
    var url = "/products/unsetquote/";

    ajaxPost(data, url, params);
}

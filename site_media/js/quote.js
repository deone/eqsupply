var options = {
    url: null,
    type: "POST",
    data: null,
    dataType: "json",
    success: null,
    error: function(response)   {
	showMessage("Internal Server Error");
    }
}

function displayLst(url)	{

    // A special case: we have to re-initialize the options variable, will take a closer look sometime.
    var options = {};

    options["url"] = url;
    options["type"] = "GET";
    options["dataType"] = "json";
    options["success"] = function(response) {
	if (url == "/manufacturer_list/")   {
	    showManufacturers(response);
	}
	if (url == "/category_list/")   {
	    showCategories(response);
	}
    }
    options["error"] = function(response)   {
	showMessage("Internal Server Error");
    }

    $.ajax(options);

}

function createQuote()	{
    options["data"] = "user=" + $("#user-id").val() + "&company=" + $("#user-company").val();
    options["url"] = "/quote/create/";
    options["success"] = function(response) {
	document.location = "/product_groups/?quote_id=" + response.data.body["id"];
    }

    $.ajax(options);
}

function emailQuote(quoteId, userId)	{
    options["url"] = "/quote/" + quoteId + "/email/";
    options["data"] = "user_id=" + userId;
    options["success"] = function(response) {
	showMessage(response.data.body);
    }

    $.ajax(options);
}

function getQuoteData(action, productId)    {

    var quoteId = $("#quote-id").val();

    if (action == "Add")    {
	if ($("#quantity" + productId).val() != "")	{

	    return  {
		"quote": quoteId, 
		"product": productId, 
		"quantity": $("#quantity" + productId).val()
	    };

	} else	{
	    $("#msger").slideDown("fast");
	    showMessage("Please tell us the quantity you need");
	    return null;
	}

    }

    if (action == "Remove") {
	return	{
	    "quote": quoteId, 
	    "product": productId
	}
    }
}

function showAddQuoteForm(params) {
    $("#cell" + params["product"]).find(".rem-quote-item").hide();
    $("#cell" + params["product"]).find("#add-quote-item").show();
    $("#cell" + params["product"]).parent().hover(
	function()	{
	    $(this).find("#add-quote-item").show();
	},
	function()	{
	    $(this).find("#add-quote-item").hide();
	}
    );
}

function showRemoveQuoteForm(params)	{
    $("#cell" + params["product"]).find("#add-quote-item").hide();
    $("#cell" + params["product"]).parent().hover(
	function()	{
	    $(this).find("#add-quote-item").hide();
	},
	function()	{
	    $(this).find("#add-quote-item").hide();
	}
    );
    $("#cell" + params["product"]).find(".rem-quote-item").show();
}

function displayErrorsOrDoAction(msg, url, params)	{
    showMessage(msg);
    
    if (url == "/quote/set_quote_item/")    {
	showRemoveQuoteForm(params);
    }
    if (url == "/quote/unset_quote_item/")  {
	showAddQuoteForm(params);
    }
}

function quote(action, productId) {
    var params = getQuoteData(action, productId);

    if (params)	{
	if (params["quantity"])	{
	    options["data"] = "quote=" + params["quote"] + "&product=" + params["product"] + "&quantity=" + params["quantity"];
	    options["url"] = "/quote/set_quote_item/";
	    options["success"] = function(response)  {
		displayErrorsOrDoAction(response.data.body, options["url"], params);
	    }
	} else	{
	    options["data"] = "quote=" + params["quote"] + "&product=" + params["product"];
	    options["url"] = "/quote/unset_quote_item/";
	    options["success"] = function(response) {
		displayErrorsOrDoAction(response.data.body, options["url"], params);
	    }
	}
    }

    $.ajax(options);
}

function getUserCompany(id) {
    options["url"] = "/account/" + id + "/company/";
    options["success"] = function(response) {
	$("#user-company").attr("value", response.data.body);
    }
    $.ajax(options);
}

function displayQtyFeedback(referrer)	{
    var quoteId = referrer[4];

    if (referrer[5] == "add_product")	{
	options["type"] = "GET";
	options["url"] = "/quote/" + quoteId + "/count_items/";
	options["success"] = function(response)	{
	    var count = response.data.body;
	    if (count != 0)	{
		if (count == 1)	{
		    $("#quote-info p").html("You have added " + response.data.body + " product to your quote. <a href='#'>Preview</a>");
		} else if (count > 1)	{
		    $("#quote-info p").html("You have added " + response.data.body + " products to your quote. <a href='#'>Preview</a>");
		}
		$("#quote-info").show();
	    }
	}

	$.ajax(options);
    }
}

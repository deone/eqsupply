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

function ajaxGet(url)	{

    $.ajax({
	url: url,
	type: "GET",
	dataType: "json",

	success: function(response) {
	    if (url == "/manufacturer_list/")	{
		showManufacturers(response);
	    }
	    if (url == "/category_list/")   {
		showCategories(response);
	    }
	    if (url.split("/")[3] == "count_items") {
		var count = response.data.body;
		if (count != 0)	{
		    if (count == 1)	{
			$("#quote-info p").html("You have added " + response.data.body + " product to your quote.");
		    } else if (count > 1)	{
			$("#quote-info p").html("You have added " + response.data.body + " products to your quote.");
		    }
		    $("#quote-info").show();
		}
	    }
	},

	error: function(response)   {
	    alert(response);
	}
    });

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

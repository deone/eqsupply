var getOptions = {
    url: null,
    type: "GET",
    data: null,
    dataType: "json",
    success: null,
    error: function(response)   {
	showMessage("Internal Server Error");
    }
}

var postOptions = {
    url: null,
    type: "POST",
    data: null,
    dataType: "json",
    success: null,
    error: function(response)   {
	showMessage("Internal Server Error");
    }
};

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
    postOptions["data"] = "user=" + $("#user-id").val() + "&company=" + $("#user-company").val();
    postOptions["url"] = "/quote/create/";
    postOptions["success"] = function(response) {
	document.location = "/product_groups/?quote_id=" + response.data.body["id"];
    }

    $.ajax(postOptions);
}

function emailQuote(quoteId, userId)	{
    postOptions["url"] = "/quote/" + quoteId + "/email/";
    postOptions["data"] = "user_id=" + userId;
    postOptions["success"] = function(response) {
	showMessage(response.data.body);
    }

    $.ajax(postOptions);
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
	    postOptions["data"] = "quote=" + params["quote"] + "&product=" + params["product"] + "&quantity=" + params["quantity"];
	    postOptions["url"] = "/quote/set_quote_item/";
	    postOptions["success"] = function(response)  {
		displayErrorsOrDoAction(response.data.body, postOptions["url"], params);
	    }
	} else	{
	    postOptions["data"] = "quote=" + params["quote"] + "&product=" + params["product"];
	    postOptions["url"] = "/quote/unset_quote_item/";
	    postOptions["success"] = function(response) {
		displayErrorsOrDoAction(response.data.body, postOptions["url"], params);
	    }
	}
    }

    $.ajax(postOptions);
}
    
function getUserCompany(id) {
    getOptions["url"] = "/account/" + id + "/company/";
    getOptions["success"] = function(response) {
	$("#user-company").attr("value", response.data.body);
    }
    $.ajax(getOptions);
}

function displayQtyFeedback(referrer)	{
    var quoteId = referrer[4];

    if (referrer[5] == "add_product")	{
	getOptions["url"] = "/quote/" + quoteId + "/count_items/";
	getOptions["success"] = function(response)	{
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

	$.ajax(getOptions);
    }
}

function submitMoreDetails(userId, quoteId)	{
    var quote = $("#quote-id").val();
    var phone = $("#phone").val();
    var company = $("#company").val();
    var position = $("#position").val();
    var company_address = $("#company_address").val();
    var city = $("#city").val();
    var state = $("#state").val();
    var country = $("#country").val();

    postOptions["url"] = "/account/" + userId + "/add_details/";
    postOptions["data"] = "quote_id=" + quote + "&phone=" + phone + "&company=" + company + 
			    "&position=" + position + "&company_address=" + company_address + 
			    "&city=" + city + "&state=" + state + "&country=" + country;

    postOptions["success"] = function(response) {
	document.location = "/quote/" + quoteId + "/preview/";
    }

    $.ajax(postOptions);
}

function quoteHasItem(quoteId, userId)	{
    getOptions["url"] = "/quote/" + quoteId + "/check/";
    getOptions["success"] = function(response) {
	if (response.data.type != "ok")	{
	    showMessage("Please add at least 1 item to your quote");
	} else	{
	    userHasDetails(quoteId, userId);
	}
    }
    $.ajax(getOptions);
}

function userHasDetails(quoteId, userId)	{
    getOptions["url"] = "/account/" + userId + "/has_details/";
    getOptions["success"] = function(response)	{
	if (response.data.type != "ok")	{
	    $("#user-details").dialog('open');
	    return false;
	} else	{
	    document.location = "/quote/" + quoteId + "/preview/";
	}
    }
    $.ajax(getOptions);
}

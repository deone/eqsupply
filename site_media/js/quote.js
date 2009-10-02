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

function ajaxPost(data, url, options)  {

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
		    var urlBits = url.split("/")
		    
		    if (urlBits[urlBits.length - 2] == "create")	{
			document.location = "/product_groups/?quote_id=" + response.data.body["id"];
		    }

		    if (urlBits[urlBits.length - 2] == "email") {
			showMessage(response.data.body);
		    }

		    if (url == "/quote/set_quote_item/")	{
			showMessage(response.data.body);
			$("#cell" + options["product"]).find("#add-quote-item").hide();
			$("#cell" + options["product"]).parent().hover(
			    function()	{
				$(this).find("#add-quote-item").hide();
			    },
			    function()	{
				$(this).find("#add-quote-item").hide();
			    }
			);
			$("#cell" + options["product"]).find(".rem-quote-item").show();
		    } else  {
			showMessage(response.data.body);
			$("#cell" + options["product"]).find(".rem-quote-item").hide();
			$("#cell" + options["product"]).find("#add-quote-item").show();
			$("#cell" + options["product"]).parent().hover(
			    function()	{
				$(this).find("#add-quote-item").show();
			    },
			    function()	{
				$(this).find("#add-quote-item").hide();
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

}

function createQuote()	{
    var data = "user=" + $("#user-id").val() + "&company=" + $("#user-company").val();
    var url = "/quote/create/";

    ajaxPost(data, url);
}



function emailQuote(quoteId, userId)	{
    var url = "/quote/" + quoteId + "/email/";
    var data = "user_id=" + userId;

    ajaxPost(data, url);
}

function showQuotes(data)   {
    var quoteList = "<table><thead></thead><tbody>";

    for (var i=0; i<data.length; i++)	{
	quoteList += "<tr>" + 
			"<td><a href=''>" + data[i].title + "</a></td>" + 
			"<td>" + data[i].time_created + "</td>" + 
			"</tr>";
    }

    quoteList += "</tbody></table>";

    $("#p-quotes").append(quoteList);

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

function quote(action, productId) {
    var params = getQuoteData(action, productId);

    if (params)	{
	if (params["quantity"])	{
	    var data = "quote=" + params["quote"] + "&product=" + params["product"] + "&quantity=" + params["quantity"];
	    var url = "/quote/set_quote_item/";
	} else	{
	    var data = "quote=" + params["quote"] + "&product=" + params["product"];
	    var url = "/quote/unset_quote_item/";
	}

	ajaxPost(data, url, params);
    }
}

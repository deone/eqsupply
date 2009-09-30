$(function()	{

    $("#tabs").tabs();

    $(".product-detail").hover(
	function()  {
	    $(this).find("#add-quote-item").show();
	},
	function()  {
	    $(this).find("#add-quote-item").hide();
	}
    );

});

/* We can construct a url->action(s) mapping 
 * because ajaxPost() would be handling 
 * all post requests in this module.*/

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

}//}}}

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

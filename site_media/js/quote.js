var options = {
    url: null,
    type: "POST",
    data: null,
    dataType: "json",
    success: null,
    error: function(response)   {
	showMessage("Internal Server Error");
    }
};

function showQuoteForm(id) {
    $("#cell" + id).find(".quote_btn").hide();
    var form = $("#cell" + id).find(".quote_form");
    form.show();
    form.find("#id_quantity").focus();
}

function quote(pvId)  {
    var quoteForm = $("#quote_" + pvId + "_form");

    var quantity = quoteForm.find("#id_quantity").val();
    var user = $("#id_user").val();

    options["url"] = "/products/" + pvId + "/quote";
    options["data"] = "user=" + user + "&quantity=" + quantity;
    options["success"] = function(response)	{
	showItemQtyAndDateLink(response.data.body);
    }

    $.ajax(options);
}

function showItemQtyAndDateLink(quoteDetail)	{
    var detail = quoteDetail.line_item_qty;

    if (quoteDetail.line_item_qty != 1)	{
	detail += " lines ";
    } else  {
	detail += " line ";
    }

    if (quoteDetail.date_created != null)   {
	detail += quoteDetail.date_created;
    }

    $("#quote_link").html(detail);
}

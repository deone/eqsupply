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
    $("#cell" + id).find("#quote_btn").hide();
    $("#cell" + id).find("#quote_form").show();
}

function quote(pvId)  {
    var user = $("#user").val();
    var qty = $("#qty" + pvId).val();

    options["url"] = "/products/" + pvId + "/quote";
    options["data"] = "user=" + user + "&quantity=" + qty;
    options["success"] = function(response)	{
	alert(response);
    }

    $.ajax(options);
}

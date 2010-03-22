$(function()	{

    $("#ajax_msg").ajaxStart(function() {
	$(this).show();
    }).ajaxStop(function()  {
	$(this).hide();
    });

});

function showErrors(errors)   {
    $('.errorlist').remove();

    if (!errors.keys)	{
	showMessage(errors);
    } else  {
	for (var i=0; i<errors.keys.length; i++) {
	    if (errors.keys[i] == "__all__")    {
		msg = errors.__all__.split("<li>")[1];
		errMsg = msg.split(".")[0];
		showMessage(errMsg);
	    } else  {
		var error_html = errors[errors.keys[i]];
		$("#id_" + errors.keys[i]).parent().before(error_html);
	    }
	}
    }
}

function showMessage(msg)   {
    $("#error_msg").html("<p>" + msg + "</p>");
    $("#error_msg").show();
    setTimeout("$('#error_msg').fadeOut('fast')", 7000);
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

    if (quoteDetail.line_item_qty > 0)   {
	$("#quote_link").attr("href", "/quotation/" + quoteDetail.id);
    }
    $("#quote_link").html(detail);
}

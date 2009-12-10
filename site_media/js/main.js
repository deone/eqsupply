$(function()	{

    $(".ajax").ajaxStart(function() {
	$(this).show();
    }).ajaxStop(function()  {
	$(this).hide();
    });

});

function highlightErrorFields(errors)   {
    $('.error').remove();

    for (var i=0; i<errors.keys.length; i++) {
	if (errors.keys[i] == "__all__")    {
	    showMessage(errors.__all__);
	} else	{
	    var error_html = "<li class='error'>" + errors[errors.keys[i]] + "</li>";
	    $("#id_" + errors.keys[i]).before(error_html);
	    document.getElementById("id_" + errors.keys[i]).style.background = "#ffa";
	}
    }
}

function showMessage(msg)	{
    $("#msger").html("<p>" + msg + "</p>");
    $("#msger").slideDown("fast");
    setTimeout("$('#msger').slideUp('fast')", 7000);
}

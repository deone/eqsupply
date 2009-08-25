function displayErrors(errors)   {
    if (errors.keys)    {
        for (var i=0; i<errors.keys.length; i++) {
            $("#id_" + errors.keys[i]).before("<ul class='errorlist'><li>" + errors[errors.keys[i]] + "</li></ul>");
        }
    } else  {
        $("#err").html("<ul class='errorlist'><li>" + errors["__all__"] + "</li></ul>");
    }
}

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

function displayErrors(errorObj)    {
    /* Classes of Errors
     * * Connection error: also in sliding div, but longer than usual. We should pass milliseconds into showMessage()
     * so that we would be able to make some display longer than others.
     * * Validation errors: display them with the sliding div, normal duration.
     * * Username-taken errors.
     * * Field omission errors.
     */
    highlightErrorFields(errorObj.data.body);

}

function logIn()    {
    var username = $("#id_username").val();
    var password = $("#id_password").val()

    options["url"] = "/account/";
    options["data"] = "username=" + username + "&password=" + password;
    options["success"] = function(response) {
	displayErrorsOrRedirect(response, "/products/");
    }

    $.ajax(options);
}

function displayErrorsOrRedirect(respObj, dLocation)	{
    if (respObj.data.type != "ok")  {
	displayErrors(respObj);
    } else  {
	document.location = dLocation;
    }
}

function signUp()   {
    var firstname = $("#id_first_name").val();
    var lastname = $("#id_last_name").val();
    var username = $("#id_username").val();
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();
    var email = $("#id_email").val();

    options["url"] = "/account/signup/";
    options["data"] = "first_name=" + firstname + 
			"&last_name=" + lastname + 
			"&email=" + email + 
			"&username=" + username + 
			"&password1=" + password1 + 
			"&password2=" + password2;

    options["success"] = function(response) {
	displayErrorsOrRedirect(response, "/account/");
    }

    $.ajax(options);
}

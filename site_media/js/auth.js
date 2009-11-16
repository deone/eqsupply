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
    if (!errorObj.keys)   {
	showMessage(errorObj["__all__"]);
    } else  {
	highlightErrorFields(errorObj);
	showMessage("Please fill out required fields");
    }
}

function logIn()    {
    var username = $("#id_username").val();
    var password = $("#id_password").val()

    options["url"] = "/account/";
    options["data"] = "username=" + username + "&password=" + password;
    options["success"] = function(response) {
	displayErrorsOrRedirect(response, "/quote/");
    }

    $.ajax(options);
}

function displayErrorsOrRedirect(respObj, dLocation)	{
    if (respObj.data.type != "ok")  {
	displayErrors(respObj.data.body);
    } else  {
	document.location = dLocation;
    }
}

function signUp()   {
    var firstname = $("#id_first_name").val();
    var lastname = $("#id_last_name").val();
    var email = $("#id_email").val();
    var username = $("#id_username").val();
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();

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

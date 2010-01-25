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

function logIn()    {
    var username = $("#id_username").val();
    var password = $("#id_password").val()

    options["url"] = "/";
    options["data"] = "username=" + username + "&password=" + password;
    options["success"] = function(response) {
	displayErrorsOrRedirect(response, "/products");
    }

    $.ajax(options);
}

function signUp()   {
    var firstname = $("#id_first_name").val();
    var lastname = $("#id_last_name").val();
    var username = $("#id_username").val();
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();
    var email = $("#id_email").val();

    options["url"] = "/signup";
    options["data"] = "first_name=" + firstname + 
			"&last_name=" + lastname + 
			"&email=" + email + 
			"&username=" + username + 
			"&password1=" + password1 + 
			"&password2=" + password2;

    options["success"] = function(response) {
	displayErrorsOrRedirect(response, "/signup");
    }

    $.ajax(options);
}

function displayErrorsOrRedirect(respObj, dLocation)	{
    if (respObj.data.type != "ok")  {
	showErrors(respObj.data.body);	/* main.js */
    } else  {
	document.location = dLocation;
    }
}

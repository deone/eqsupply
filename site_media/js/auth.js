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

function authCallback(response, dLocation)    {

    if (response.data.type == "error")  {
	if (!response.data.body.keys)   {
	    showMessage(response.data.body["__all__"]);
	} else  {
	    highlightErrorFields(response.data.body);
	    showMessage("Please fill out required fields");
	}
    } else  {
	document.location = dLocation;
    }

}

function login()    {

    var username = $("#id_username").val();
    var password = $("#id_password").val()

    options["url"] = "/account/";
    options["data"] = "username=" + username + "&password=" + password;
    options["success"] = function(response) {
	authCallback(response, "/quote/");
    }

    $.ajax(options);

}

function signup()   {
    var firstname = $("#id_first_name").val();
    var lastname = $("#id_last_name").val();
    var email = $("#id_email").val();
    var phone = $("#id_phone").val();
    var username = $("#id_username").val();
    var password1 = $("#id_password1").val();
    var password2 = $("#id_password2").val();
    var company = $("#id_company").val();
    var position = $("#id_position").val();
    var companyStreetAddress = $("#id_company_street_address").val();
    var state = $("#id_state").val();
    var city = $("#id_city").val();
    var country = $("#id_country").val();

    options["url"] = "/account/signup/";
    options["data"] = "first_name=" + firstname + "&last_name=" + lastname + "&email=" + email + "&phone=" + phone + 
                "&username=" + username + "&password1=" + password1 + "&password2=" + password2 + "&company=" + company + 
                "&position=" + position + "&company_street_address=" + companyStreetAddress + "&city=" + city + "&state=" + state + "&country=" + country;
    options["success"] = function(response) {
	authCallback(response, "/account/");
    }

    $.ajax(options);

}

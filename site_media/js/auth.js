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
	displayErrorsOrRedirect(response);
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
	displayErrorsOrRedirect(response);
    }

    $.ajax(options);
}

function displayErrorsOrRedirect(respObj)   {
    if (respObj.data.type != true) {
	showErrors(respObj.data.body);
    } else  {
	document.location = respObj.data.body;
    }
}

function checkDetail(userId)	{
    company = $("#id_company").val();

    if (company != "")	{
	// Call quote-processing function here.
    } else  {
	// Fill out user detail form
	document.location = "/user/" + userId + "/add_details";
    }
}

// We should write a generic data gathering function
// instead of repeating this process everywhere!
function insertUserDetails(userId)	{
    var phone = $("#id_phone").val();
    var company = $("#id_company").val();
    var position = $("#id_position").val();
    var company_street_address = $("#id_company_street_address").val();
    var country = $("#id_country").val();
    var city = $("#id_city").val();
    var dLocation = $("#id_location").val();

    options["url"] = "/user/" + userId + "/add_details";
    options["data"] = "phone=" + phone + 
			"&company=" + company + 
			"&position=" + position + 
			"&company_street_address=" + company_street_address + 
			"&country=" + country + 
			"&city=" + city + 
			"&location=" + dLocation;

    options["success"] = function(response) {
	// Call quote-processing function here.
	alert(response);
    }

    $.ajax(options);
}

function validateName(name) {

	var reg = /^[a-zA-Z ]*$/;

	if (!reg.test(name.value)) {

		alert("Please enter a valid name...");
		return false;
	}
	return true;
}

function validateEmail(email) {

	var reg = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

	if (!reg.test(email.value)) {

		alert("Please enter a valid email...");
		return false;
	}
	return true;
}

function validateFormPersonSignup() {

	var first = document.forms["myForm"]["first"];
	var last = document.forms["myForm"]["last"];
	var phone = document.forms["myForm"]["phone"];
	var email = document.forms["myForm"]["email"];

	if (!validateName(first)) {

		return false;
	}

	if (!validateName(last)) {

		return false;
	}

	if (!validatePhone(phone)) {

		return false;
	}

	if (!validateEmail(email)) {

		return false;
	}

	return true;
}

function validateFormDoctorSignup() {

	var first = document.forms["myForm"]["first"];
	var last = document.forms["myForm"]["last"];
	var phone = document.forms["myForm"]["phone"];
	var experience = document.forms["myForm"]["experience"];
	var fee = document.forms["myForm"]["fee"];
	var email = document.forms["myForm"]["email"];

	if (!validateName(first)) {

		return false;
	}

	if (!validateName(last)) {

		return false;
	}

	if (!validatePhone(phone)) {

		return false;
	}

	if (!validateExperience(experience)) {

		return false;
	}

	if (!validateFee(fee)) {

		return false;
	}

	if (!validateEmail(email)) {

		return false;
	}

	return true;
}

function validateFormEmail() {

	var email = document.forms["myForm"]["email"];

	if (!validateEmail(email)) {

		return false;
	}

	return true;
}

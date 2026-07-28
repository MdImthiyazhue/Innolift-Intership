// ===============================
// DOM Elements
// ===============================

const form = document.getElementById("registrationForm");

const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const phoneInput = document.getElementById("phone");
const dobInput = document.getElementById("dob");
const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");

const strength = document.getElementById("strength");
const successMessage = document.getElementById("successMessage");

const togglePassword = document.getElementById("togglePassword");


// ===============================
// Regular Expressions
// ===============================

const nameRegex = /^[A-Za-z ]{3,30}$/;

const emailRegex =
/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$/;

const phoneRegex =
/^[6-9]\d{9}$/;

const passwordRegex =
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$/;

togglePassword.addEventListener("click", () => {

    if(passwordInput.type === "password"){

        passwordInput.type = "text";
        togglePassword.textContent = "🙈";

    }

    else{

        passwordInput.type = "password";
        togglePassword.textContent = "👁";

    }

});

function showError(input, message){

    const formGroup = input.parentElement.classList.contains("password-box")
        ? input.parentElement.parentElement
        : input.parentElement;

    formGroup.querySelector(".error").textContent = message;

    input.classList.remove("valid");
    input.classList.add("invalid");

}

function showSuccess(input){

    const formGroup = input.parentElement.classList.contains("password-box")
        ? input.parentElement.parentElement
        : input.parentElement;

    formGroup.querySelector(".error").textContent = "";

    input.classList.remove("invalid");
    input.classList.add("valid");

}

function validateName(){

    const value = nameInput.value.trim();

    if(value===""){

        showError(nameInput,"Name is required");
        return false;

    }

    if(!nameRegex.test(value)){

        showError(
            nameInput,
            "Only alphabets and spaces (3-30 chars)"
        );

        return false;

    }

    showSuccess(nameInput);

    return true;

}

function validateEmail(){

    const value = emailInput.value.trim();

    if(value===""){

        showError(emailInput,"Email is required");
        return false;

    }

    if(!emailRegex.test(value)){

        showError(emailInput,"Invalid email address");
        return false;

    }

    showSuccess(emailInput);

    return true;

}

function validatePhone(){

    const value = phoneInput.value.trim();

    if(value===""){

        showError(phoneInput,"Phone number required");
        return false;

    }

    if(!phoneRegex.test(value)){

        showError(phoneInput,"Enter valid Indian mobile");

        return false;

    }

    showSuccess(phoneInput);

    return true;

}

// ===============================
// Date of Birth Validation
// ===============================

function validateDOB(){

    if(dobInput.value===""){

        showError(dobInput,"Date of Birth is required");
        return false;

    }

    const dob=new Date(dobInput.value);
    const today=new Date();

    let age=today.getFullYear()-dob.getFullYear();

    const month=today.getMonth()-dob.getMonth();

    if(month<0 || (month===0 && today.getDate()<dob.getDate())){

        age--;

    }

    if(age<18){

        showError(dobInput,"You must be at least 18 years old");

        return false;

    }

    showSuccess(dobInput);

    return true;

}

// ===============================
// Password Validation
// ===============================

function validatePassword(){

    const password=passwordInput.value;

    if(password===""){

        showError(passwordInput,"Password is required");

        strength.textContent="";

        return false;

    }

    if(password.length<8){

        showError(passwordInput,"Minimum 8 characters");

        strength.textContent="Weak";
        strength.className="weak";

        return false;

    }

    let score=0;

    if(/[a-z]/.test(password)) score++;
    if(/[A-Z]/.test(password)) score++;
    if(/\d/.test(password)) score++;
    if(/[!@#$%^&*]/.test(password)) score++;

    if(score<=2){

        strength.textContent="Weak";
        strength.className="weak";

    }

    else if(score===3){

        strength.textContent="Medium";
        strength.className="medium";

    }

    else{

        strength.textContent="Strong";
        strength.className="strong";

    }

    if(!passwordRegex.test(password)){

        showError(
            passwordInput,
            "Include uppercase, lowercase, number & special character"
        );

        return false;

    }

    showSuccess(passwordInput);

    return true;

}

// ===============================
// Confirm Password
// ===============================

function validateConfirmPassword(){

    if(confirmPasswordInput.value===""){

        showError(
            confirmPasswordInput,
            "Confirm your password"
        );

        return false;

    }

    if(passwordInput.value!==confirmPasswordInput.value){

        showError(
            confirmPasswordInput,
            "Passwords do not match"
        );

        return false;

    }

    showSuccess(confirmPasswordInput);

    return true;

}

// ===============================
// Live Validation
// ===============================

nameInput.addEventListener("input",validateName);

emailInput.addEventListener("input",validateEmail);

phoneInput.addEventListener("input",validatePhone);

dobInput.addEventListener("change",validateDOB);

passwordInput.addEventListener("input",()=>{

    validatePassword();

    if(confirmPasswordInput.value!==""){

        validateConfirmPassword();

    }

});

confirmPasswordInput.addEventListener(
    "input",
    validateConfirmPassword
);

// ===============================
// Form Submission
// ===============================

form.addEventListener("submit",function(e){

    e.preventDefault();

    const isValid=

        validateName() &&
        validateEmail() &&
        validatePhone() &&
        validateDOB() &&
        validatePassword() &&
        validateConfirmPassword();

    if(isValid){

        successMessage.style.display="block";

        form.reset();

        strength.textContent="";

        document
            .querySelectorAll(".valid")
            .forEach(input=>{

                input.classList.remove("valid");

            });

        setTimeout(()=>{

            successMessage.style.display="none";

        },4000);

    }

});

const register = async() => {
    var usernameElement = document.getElementById('username')
    var emailElement = document.getElementById('email')
    var passwordElement = document.getElementById('password')
    var group = document.querySelector('input[name="group"]:checked').value
    console.log(usernameElement.value, emailElement.value, passwordElement.value, group)
    var myResponse = await fetch("https://motidivya.pythonanywhere.com/users/register", {
        method: "POST", 
        body: JSON.stringify({
            username: usernameElement.value,
            password: passwordElement.value,
            email: emailElement.value,
            group: group,
        }),
        headers: {
        "Content-type": "application/json; charset=UTF-8"
        }
    })
    var myJSON = await myResponse.json();
    window.location.href = "./login.html";
    alert("User Registered Successfully");
    console.log(myJSON);
}
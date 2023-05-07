const login = async() => {
    var userUsername = document.getElementById('username').value;
    var userPassword = document.getElementById('password').value;
    var myResponse = await fetch("http://localhost:8000/users/login", {
            method: "POST",
            
            body: JSON.stringify({
                username: userUsername,
                password: userPassword
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        });
    var myJSON = await myResponse.json();
    sessionStorage.setItem('jwt', myJSON.jwt);
    window.location.href = './index.html'
    console.log(myJSON)
}

function parseJWT(){
    token = sessionStorage.getItem('jwt');
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    var jsonData = console.log(JSON.parse(jsonPayload));
    localStorage.setItem('jsonData', jsonData);
}


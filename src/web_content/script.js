// script.js

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var loginButton = document.getElementById("loginButton");
    var lockIconContainer = document.getElementById("lock-icon-container");

    if (username === "admin" && password === "@Madara@1") {
        window.location.href = "vpn_status.html";
    } else {
        document.getElementById("error-msg").innerText = "Invalid credentials. Please try again.";
        loginButton.setAttribute("disabled", "disabled");
        loginButton.classList.add("disabled");
        lockIconContainer.innerHTML = '<i class="material-icons lock-icon">lock</i>';
    }
});

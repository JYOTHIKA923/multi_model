

// Open dashboard after login
function openDashboard() {
    document.getElementById("loginPage").style.display = "none";
    document.getElementById("dashboard").style.display = "block";
}

// Logout
function logout() {
    document.getElementById("loginPage").style.display = "flex";
    document.getElementById("dashboard").style.display = "none";
}

// Sidebar toggle
function toggleSidebar() {
    let sidebar = document.getElementById("sidebar");

    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-250px";
    } else {
        sidebar.style.left = "0px";
    }
}

// Show pages
function showPage(pageId) {

    let pages = document.querySelectorAll(".page");

    pages.forEach(function(page) {
        page.style.display = "none";
    });

    document.getElementById(pageId).style.display = "block";
}

// Preview image
function previewImage(event) {

    let file = event.target.files[0];
    let preview = document.getElementById("preview");

    preview.src = URL.createObjectURL(file);
    preview.style.display = "block";
}

// Loading
function showLoading() {
    document.getElementById("loading").style.display = "block";
}


function saveTheme() {
    let theme = document.getElementById("themeSelect").value;

    if (theme === "dark") {
        document.body.classList.add("dark-mode");
        localStorage.setItem("theme", "dark");
    } else {
        document.body.classList.remove("dark-mode");
        localStorage.setItem("theme", "light");
    }
}

window.onload = function () {

    let savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark-mode");
        document.getElementById("themeSelect").value = "dark";
    }
}
function feedback(button, product, vote){

    fetch("/feedback", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            product: product,
            vote: vote
        })
    })
    .then(response => response.text())
    .then(data => {

        let box = button.parentElement;
        let buttons = box.querySelectorAll("button");

        buttons.forEach(btn => btn.classList.remove("active"));

        button.classList.add("active");

        let msg = box.nextElementSibling;
        msg.innerHTML = "Thanks for your feedback!";
    });
}


function deleteProduct(){

    let id = document.getElementById("deleteId").value;

    fetch("/delete_product/" + id)
    .then(response => response.text())
    .then(data => alert(data));
}
/* ===================================== */
/* DELETE PRODUCT JS */
/* ===================================== */

function deleteProduct(){

    let id = document.getElementById("deleteId").value;

    if(id == ""){
        alert("Enter Product ID");
        return;
    }

    fetch("/delete_product/" + id)
    .then(response => response.text())
    .then(data => {
        alert(data);
        document.getElementById("deleteId").value = "";
    });
}


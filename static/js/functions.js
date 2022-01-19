function enable_signin()
{
    document.getElementById("signup_part").style.visibility = "visible";
    document.getElementById("signup_btn").style.visibility = "hidden";
}
function call_welcome_screen()
{
    location.href = "Welcome_page.html";
}
function home()
{
    location.href = "Home_page.html";
}

function show_file()
{
    var fname = document.getElementById("file_book").files[0].name;
    document.getElementById("f_name").innerHTML = fname;
}

function message_close(){
    document.getElementById('message_div').setAttribute("style", "display:none");
}
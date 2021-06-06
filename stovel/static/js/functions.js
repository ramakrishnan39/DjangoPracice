function enable_signin()
{
    document.getElementById("signup_part").style.visibility = "visible";
    document.getElementById("signup_btn").style.visibility = "hidden";
}
function call_welcome_screen()
{
    location.href = "Welcome_page.html";
}
function call_home()
{
    location.href = "Home_page.html";
}

function show_file()
{
    var fname = document.getElementById("file_book").files[0].name;
    document.getElementById("f_name").innerHTML = fname;
}
function show_edit()
{
    var ch_cnt = document.getElementById("profile_name").childElementCount;
    if (ch_cnt < 1)
    {
        var node = document.createElement("p");
        node.setAttribute("id", "profile_tag");
        node.appendChild(document.createTextNode("Your profile is here "));
        document.getElementById("profile_name").appendChild(node);
        node.appendChild(document.createTextNode(ch_cnt));

    }
}
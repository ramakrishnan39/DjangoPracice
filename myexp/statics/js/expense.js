function js_setdate()
{
    //document.getElementById("appdate").valueAsDate = new Date()
}

function js_addrow()
{
    var numrows = document.getElementById("exptable").rows.length;

    var btnsub = document.createElement("BUTTON");
    var t1 = document.createTextNode("Submit");
    btnsub.appendChild(t1);
    btnsub.onclick = "js_addrow()";
    var btndel = document.createElement("BUTTON");
    var t2 = document.createTextNode("Delete");
    btndel.appendChild(t2);


    var inpdate = document.createElement("INPUT");
    inpdate.setAttribute("type", "Date");
    
    var inpexpname = document.createElement("INPUT");
    inpexpname.setAttribute("type", "Text")

    var inpamount = document.createElement("INPUT");
    inpamount.setAttribute("type", "Number")
    
    var table = document.getElementById("exptable");
    var row = table.insertRow();
    var cell1 = row.insertCell(0);
    cell1.appendChild(inpexpname);
    var cell2 = row.insertCell(1);
    cell2.appendChild(inpamount);
}

function addexpense() {
    var expense_name = prompt("Please enter the expense name ");
    var amount = prompt("Please enter the amount ")
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    if (amount === null || typeof amount ==="") { amount = 0 }
    else { amount = Number(amount) }
    window.location.href ="/add/" + expense_name + "/" + amount + "/" + sdate;
    
}

function deleteexpense(expid) {
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    window.location.href = "/delete/"+expid+"/"+sdate;
}

function viewall()
{
    var ddate = document.getElementById('appdate').value;
    var sdate = ddate.toString();
    window.location.href = "/home/" + sdate;
   // document.getElementById('appdate').value=ddate;
}

function logout()
{
    window.location.href = "/logout/";
}
function js_addrow()
{
    var btnsub = document.createElement("BUTTON");
    var t = document.createTextNode("Submit");
    btnsub.appendChild(t);

    var table = document.getElementById("exptable");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var numrows = document.getElementById("exptable").rows.length;
    if(numrows == 0){
        cell1.innerHTML = "1";
    }
    else {
        cell1.innerHTML = numrows + 1;
    }
    cell2.innerHTML = " ";
    cell3.innerHTML = " ";
    cell4.innerHTML = " ";
    cell5.appendChild(btnsub);
}
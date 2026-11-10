
let students = [];

let form = document.getElementById("studentForm");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value.toUpperCase();
    let usn = document.getElementById("usn").value.toUpperCase();
    let dept = document.getElementById("dept").value.toUpperCase();

    let sub1 = document.getElementById("sub1").value;
    let sub2 = document.getElementById("sub2").value;
    let sub3 = document.getElementById("sub3").value;

    let student = [name, usn, dept, sub1, sub2, sub3];

    students.push(student);

    displayStudents();

    form.reset();

});


function displayStudents() {

    let table = document.getElementById("studentList");

    table.innerHTML = "";

    for (let i = 0; i < students.length; i++) {

        let row = document.createElement("tr");

        for (let j = 0; j < students[i].length; j++) {

            let cell = document.createElement("td");

            cell.textContent = students[i][j];

            row.appendChild(cell);

        }

        let action = document.createElement("td");

        let btn = document.createElement("button");

        btn.innerText = "Delete";
        btn.className = "delete-btn";

        btn.onclick = function() {

            students.splice(i, 1);

            displayStudents();

        };

        action.appendChild(btn);

        row.appendChild(action);

        table.appendChild(row);

    }

}

function cleanTable(table){
    var n = table.children.length;
    for(var i=0; i<n-1; i++){
        table.children[1].remove();
    }
}

function generateCourseTable(courses){
    var table = document.getElementById('course-table');
    cleanTable(table);
    for (var i = 0; i < courses.length; i++){
        var tr = document.createElement('tr');   

        var td1 = document.createElement('td');
        var td2 = document.createElement('td');
        var td3 = document.createElement('td');
        var td4 = document.createElement('td');

        var text1 = document.createTextNode(courses[i][0]);
        var text2 = document.createTextNode(courses[i][1]);
        var text3 = document.createTextNode(courses[i][2]);
        var text4 = document.createTextNode(courses[i][3]);

        td1.appendChild(text1);
        td2.appendChild(text2);
        td3.appendChild(text3);
        td4.appendChild(text4);
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        tr.appendChild(td4);

        table.appendChild(tr);
    }
}

function generateStudentTable(students){
    var table = document.getElementById('student-table');
    cleanTable(table);
    for (var i = 0; i < students.length; i++){
        var tr = document.createElement('tr');   

        var td1 = document.createElement('td');
        var td2 = document.createElement('td');
        var td3 = document.createElement('td');
       

        var text1 = document.createTextNode(students[i][0]);
        var text2 = document.createTextNode(students[i][1]);
        var text3 = document.createTextNode(students[i][2]);
        

        td1.appendChild(text1);
        td2.appendChild(text2);
        td3.appendChild(text3);
        
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
        

        table.appendChild(tr);
    }
    
}
// let teacher = document.getElementById("teachers");
// let dept = document.getElementById("depts");
// let college = document.getElementById("colleges");

// data = document.getElementsByClassName("data-container");

function setCollegeVisiblity() {
  teacher = document.getElementById("teachers");
  dept = document.getElementById("depts");
  college = document.getElementById("colleges");

  if (college.style.display === "none") {
    college.style.display = "block";
    dept.style.display = "none";
    teacher.style.display = "none";
  } else {
    college.style.display = "none";
  }
}
function setDepartmentVisiblity() {
  teacher = document.getElementById("teachers");
  dept = document.getElementById("depts");
  college = document.getElementById("colleges");

  if (dept.style.display === "none") {
    dept.style.display = "block";
    teacher.style.display = "none";
    college.style.display = "none";
  } else {
    dept.style.display = "none";
  }
}

function setTeacherVisiblity() {
  teacher = document.getElementById("teachers");
  dept = document.getElementById("depts");
  college = document.getElementById("colleges");

  if (teacher.style.display === "none") {
    teacher.style.display = "block";
    dept.style.display = "none";
    college.style.display = "none";
  } else {
    teacher.style.display = "none";
  }
  console.log(data);
}

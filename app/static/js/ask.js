question = document.getElementsByClassName("question");

for (let i = 0; i < question.length; i++) {
  question[i].addEventListener("click", setVisible);
}

function setVisible(event) {
  for (let i = 0; i < question.length; i++) {
    document.getElementById("#" + question[i].id).classList.add("hidden");
  }
  id = "#" + event.target.id;
  document.getElementById(id).classList.remove("hidden");
}

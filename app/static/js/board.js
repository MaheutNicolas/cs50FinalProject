deck = document.getElementsByClassName("deckHolder")[0].children;
cards = document.getElementsByClassName("cardHolder")[0].children;

for (let i = 0; i < deck.length; i++) {
  deck[i].addEventListener("click", setSelected);
}
for (let i = 0; i < cards.length; i++) {
  cards[i].addEventListener("click", check);
}

function check(event) {
  for (let i = 0; i < deck.length; i++) {
    if (deck[i].classList.contains("selected")) {
      cardID = String(event.target.id);
      if (cardID.charAt(0) == "#") {
        cardID = cardID.slice(1);
      }
      post(cardID, deck[i].id);
    }
  }
}

function post(cardID, deckID) {
  fetch("/game/index", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      deck: deckID,
      card: cardID,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      data = data.response;
      if (data == 0 || data == 1) {
        reloadPage();
        return;
      }
      console.log(data);
      document.getElementById("messageHolder").innerHTML = data;
      console.log(document.getElementsByClassName("messageHolder"));
      document
        .getElementsByClassName("messageHolder")[0]
        .classList.remove("hidden");
    });
}

function setSelected(event) {
  for (let i = 0; i < deck.length; i++) {
    deck[i].classList.remove("selected");

    id = event.target.id;
    if (id) deck[i].id == String(event.target.id).slice(1);
    if (id.charAt(0) == "#") {
      id = id.slice(1);
    }

    if (deck[i].id == id) {
      deck[i].classList.add("selected");
    }
  }
}

function reloadPage() {
  location.reload();
}

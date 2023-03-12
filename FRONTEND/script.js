var lastPlay = [];
var lastHandPlayed = [];
var intendedHandToPlay = [];
var current_player = null;
var player1 = [];
var player2 = [];
var player3 = [];
var player4 = [];

const values = {
  Two: 12,
  Three: 0,
  Four: 1,
  Five: 2,
  Six: 3,
  Seven: 4,
  Eight: 5,
  Nine: 6,
  Ten: 7,
  Jack: 8,
  Queen: 9,
  King: 10,
  Ace: 11,
};

// API calls ------------------------------------
const startGame = async () => {
  try {
    const url = "http://127.0.0.1:8000/new-game";
    const data = await fetch(url).then((data) => data.json());
    return data;
  } catch (err) {
    console.log(err);
  }
};

const submit_play = async () => {
  try {
    _body = {
      intended_play: intendedHandToPlay,
      last_play: lastPlay,
    };

    const url = "http://127.0.0.1:8000/submit-play";
    const data = await fetch(url, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(_body),
    });
    return data;
  } catch (err) {
    console.log(err);
  }
};

const bot_turn = async () => {
  _bot = {
    1: player2,
    2: player3,
    3: player4,
  };

  try {
    _body = {
      bot_hand: _bot[current_player],
      last_play: lastHandPlayed,
    };
    const url = "http://127.0.0.1:8000/bot";
    const data = await fetch(url, {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(_body),
    });
    return data.json()
  } catch (err) {
    console.log(err);
  }
};

// Game functions -------------------------------
const createPlayers = async () => {
  try {
    visibilityOn(".play-btn");
    hideElement(".start-btn");
    let data = await startGame();
    current_player = data.current_player;
    data = data.players;
    player1 = data.player1;
    player2 = data.player2;
    player3 = data.player3;
    player4 = data.player4;
    sortHand(player1);
    sortHand(player2);
    sortHand(player3);
    sortHand(player4);

    renderHand(player1, ".playerOne");
    renderBot(player2, ".botOne");
    renderBot(player3, ".botTwo");
    renderBot(player4, ".botThree");

    // BOT TURN
    highlightCurrentPlayer(current_player);
    if (current_player != 0) {
      console.log(current_player)
      let bot_data = await bot_turn();
      console.log(bot_data)
    }
  } catch (err) {
    console.log(err);
  }
};

// DOM element functions ----------------------------
const hideElement = (className) => {
  const element = document.querySelector(className);
  element.style.display = "none";
};

const showElement = (className) => {
  const startBtn = document.querySelector(className);
  startBtn.style.display = "";
};

const visibilityOn = (className) => {
  const element = document.querySelector(className);
  element.style.visibility = "visible";
};

const visibilityOff = (className) => {
  const element = document.querySelector(className);
  element.style.visibility = "hidden";
};

const enableBtn = (className) => {
  const element = document.querySelector(className);
  element.disabled = false;
};

const disableBtn = (className) => {
  const element = document.querySelector(className);
  element.disabled = true;
};

// Render player1 hand
const displayCard = (rank, suit) => {
  return `
	<div class="${suit == "Diamonds" || suit == "Hearts" ? "card red" : "card"}">
	<p>${rank}</p>
	<p>${suit}</p>
	</div>`;
};

const renderHand = (hand, parentDiv) => {
  const tempHand = hand
    .map((card) => {
      return displayCard(card.rank, card.suit);
    })
    .join("");
  document.querySelector(parentDiv).insertAdjacentHTML("afterbegin", tempHand);
};

// render bot's hands
const displayBots = (botHand, botName) => {
  return `
	<div class=botHand>
	<p class=botCardCount>${botHand.length}</p>
	<p class=botName>${botName}</p>
	</div>
	`;
};

const renderBot = (botHand, botName) => {
  const bot = displayBots(botHand, botName);
  document.querySelector(botName).insertAdjacentHTML("afterbegin", bot);
};

// sort hand tien len style
// 3, 4, 5 -> K, A, 2
// spades > clubs > diamonds > hearts
const suitValues = {
  Spades: 0,
  Clubs: 1,
  Diamonds: 2,
  Hearts: 3,
};

const sortRanks = (hand) => {
  return hand.sort((a, b) => a["value"] - b["value"]);
};

const sortSuits = (hand) => {
  return hand.sort((a, b) => {
    if (a["value"] == b["value"]) {
      return suitValues[a["suit"]] - suitValues[b["suit"]];
    } else return;
  });
};

const sortHand = (hand) => {
  sortSuits(sortRanks(hand));
};

// logic for selecting cards ---------------------------
const removeFromPlayer = (rank, suit) => {
  let result = [];

  for (let i = 0; i < player1.length; i++) {
    if (player1[i]["rank"] == rank && player1[i]["suit"] == suit) {
    } else {
      result.push(player1[i]);
    }
  }
  player1 = result;
};

const removeFromIntended = (rank, suit) => {
  let result = [];

  for (let i = 0; i < intendedHandToPlay.length; i++) {
    if (
      intendedHandToPlay[i]["rank"] == rank &&
      intendedHandToPlay[i]["suit"] == suit
    ) {
    } else {
      result.push(intendedHandToPlay[i]);
    }
  }
  intendedHandToPlay = result;
};

const addToIntendedHandToPlay = (rank, suit) => {
  const tempCard = {
    rank: rank,
    suit: suit,
    value: values[rank],
  };
  intendedHandToPlay.push(tempCard);
  sortHand(intendedHandToPlay);
};

const addToPlayerHand = (rank, suit) => {
  const tempCard = {
    rank: rank,
    suit: suit,
    value: values[rank],
  };
  player1.push(tempCard);
  sortHand(player1);
};

const canPlayIntendedHand = () => {
  if (intendedHandToPlay.length > 0 && current_player == 0) {
    enableBtn(".play-btn");
  } else {
    disableBtn(".play-btn");
  }
};

const selectCard = (event) => {
  let rank;
  let suit;
  const target = event.target;
  const parent = target.parentNode;

  if (parent.classList == "playerOne") {
    rank = target.children[0].innerText;
    suit = target.children[1].innerText;

    removeFromPlayer(rank, suit);
    addToIntendedHandToPlay(rank, suit);
    displayIntendedHand(rank, suit);

    target.style.display = "none"; // hide card
  } else if (parent.parentNode.classList == "playerOne") {
    rank = parent.children[0].innerText;
    suit = parent.children[1].innerText;

    removeFromPlayer(rank, suit);
    addToIntendedHandToPlay(rank, suit);
    displayIntendedHand(rank, suit);

    parent.style.display = "none"; // hide card
  } else if (parent.classList == "intendedHandToPlay") {
    rank = target.children[0].innerText;
    suit = target.children[1].innerText;

    removeFromIntended(rank, suit);
    addToPlayerHand(rank, suit);
    displayPlayerHand(rank, suit);

    target.style.display = "none"; // hide card
  } else if (parent.parentNode.classList == "intendedHandToPlay") {
    rank = parent.children[0].innerText;
    suit = parent.children[1].innerText;

    removeFromIntended(rank, suit);
    addToPlayerHand(rank, suit);
    displayPlayerHand(rank, suit);

    parent.style.display = "none"; // hide card
  }
  canPlayIntendedHand();
};

// clear / refresh DOM to prevent duplicates
const displayIntendedHand = (rank, suit) => {
  const target = document.querySelector(".intendedHandToPlay");
  target.innerHTML = "";
  renderHand(intendedHandToPlay, ".intendedHandToPlay");
};

const displayPlayerHand = (rank, suit) => {
  const target = document.querySelector(".playerOne");
  target.innerHTML = "";
  renderHand(player1, ".playerOne");
};

const first_play_of_game = () => {
  console.log("first play")
};

// Highlight current player ------------------------------
const highlightCurrentPlayer = (current_player) => {
  _botOneHand = document.querySelector(".botOne").children[0];
  _botTwoHand = document.querySelector(".botTwo").children[0];
  _botThreeHand = document.querySelector(".botThree").children[0];

  _black = "1px solid black";
  _red = "2.5px solid red";
  _botOneHand.style.border = _black;
  _botTwoHand.style.border = _black;
  _botThreeHand.style.border = _black;

  switch (current_player) {
    case 1:
      _botOneHand.style.border = _red;
      break;
    case 2:
      _botTwoHand.style.border = _red;
      break;
    case 3:
      _botThreeHand.style.border = _red;
      break;
  }
};

// BIND EVENT LISTENERS ----------------------------------
// helper bind function
const bind = (el, evt, func) => {
  if (el.addEventListener) {
    el.addEventListener(evt, func, false);
  } else if (el.attachEvent) {
    el.attachEvent("on" + evt, func);
  }
};

// start button
const _start_button = document.querySelector(".start-btn");
bind(_start_button, "click", startGame);
bind(_start_button, "click", createPlayers);
bind(_start_button, "click", first_play_of_game);

// selecting player1 hand
const _player1_card = document.querySelector(".playerOne");
bind(_player1_card, "click", selectCard);

// selecting intendedHandToPlay hand
const _intended_hand = document.querySelector(".intendedHandToPlay");
bind(_intended_hand, "click", selectCard);

// hit play button
const _play_button = document.querySelector(".play-btn");
bind(_play_button, "click", submit_play);

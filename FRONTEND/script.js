let lastPlay = []
let lastHandPlayed = []
var intendedHandToPlay = []
var player1 = []
var player2 = []
var player3 = []
var player4 = []

const values = { 
	"Two": 12,
	"Three": 0,
	"Four": 1,
	"Five": 2,
	"Six": 3,
	"Seven": 4,
	"Eight": 5,
	"Nine": 6,
	"Ten": 7,
	"Jack": 8,
	"Queen": 9,
	"King": 10,
	"Ace": 11
}

const startGame = async () => {
	try {
		const url = "http://127.0.0.1:8000/deal-cards"
		const data = await fetch(url).then(data => data.json())
		return data
	} catch (err) {
		console.log(err)
	}
}

const createPlayers = async () => {
	try {
		hideElement(".start-btn")
		const data =await startGame()
		player1 = data.player1
		player2 = data.player2
		player3 = data.player3
		player4 = data.player4
		sortHand(player1)
		sortHand(player2)
		sortHand(player3)
		sortHand(player4)

		renderHand(player1, '.playerOne')
		renderBot(player2, '.botOne')
		renderBot(player3, '.botTwo')
		renderBot(player4, '.botThree')
	} catch (err) {
		console.log(err)
	}
}

// we can possibly set up a toggle to hide/show display
const hideElement = (className) => {
	const element = document.querySelector(className)
	element.style.display = "none"
}

const showElement = (className) => {
	const startBtn = document.querySelector(className)
	startBtn.style.display = ""
}

// Render player1 hand
const displayCard = (rank, suit) => {
	return `
	<div class="${suit == 'Diamonds' || suit == 'Hearts' ? 'card red' : 'card'}">
	<p>${rank}</p>
	<p>${suit}</p>
	</div>`
}

const renderHand = (hand, parentDiv) => {
	const tempHand = hand.map(card => {
		return displayCard(card.rank, card.suit)
	}).join("")
	document.querySelector(parentDiv).insertAdjacentHTML("afterbegin", tempHand)
}

// render bot's hands
const displayBots = (botHand) => {
	const name = 'player'
	return `
	<div class=botHand>
	<p class=botCardCount>${botHand.length}</p>
	<p class=botName>${name}</p>
	</div>
	`
}

const renderBot = (botHand, parentDiv) => {
	const bot = displayBots(botHand)
	document.querySelector(parentDiv).insertAdjacentHTML("afterbegin", bot)
}

// sort hand tien len style 
// 3, 4, 5 -> K, A, 2
// spades > clubs > diamonds > hearts
const suitValues = {
	"Spades": 0,
	"Clubs": 1,
	"Diamonds": 2,
	"Hearts": 3
}

const sortRanks = (hand) => {
	return hand.sort((a,b) => a["value"] - b["value"])
}

const sortSuits = (hand) => {
	return hand.sort((a,b) => {
		if (a["value"] == b["value"]) {
			return suitValues[a['suit']] - suitValues[b['suit']]
		} else return ;
	})
}

const sortHand = (hand) => {
	sortSuits(sortRanks(hand))
}

// logic for selecting cards
const findIndx = (rank, suit) => {
	for (let i = 0; i < playerOne.length; i++) {
		if (playerOne[i]['rank'] == rank && playerOne[i]['suit'] == suit) {
			return i
		}
	}
}

// logic for selecting cards
const addToIntendedHandToPlay = (rank, suit) => {
	const tempCard = {
		"rank": rank,
		"suit": suit,
		"value": values[rank]
	}
	intendedHandToPlay.push(tempCard)
	sortHand(intendedHandToPlay)
}

const selectCard = (event) => {
	let rank
	let suit
	const target = event.target
	const parent = target.parentNode

	if (parent.classList == "playerOne") {
		rank = target.children[0].innerText
		suit = target.children[1].innerText

		addToIntendedHandToPlay(rank, suit)
		sortHand(intendedHandToPlay)
		displayIntendedHand(rank, suit)

		target.style.display = "none"

	} else if (parent.parentNode.classList == "playerOne") {
		rank = parent.children[0].innerText
		suit = parent.children[1].innerText

		addToIntendedHandToPlay(rank, suit)
		sortHand(intendedHandToPlay)
		displayIntendedHand(rank, suit)

		parent.style.display = "none"

	} else {
		return
	}
}

// clear / refresh DOM to prevent duplicates

const displayIntendedHand = (rank, suit) => {
	const target = document.querySelector(".intendedHandToPlay")
	target.innerHTML = ""
	renderHand(intendedHandToPlay, ".intendedHandToPlay")
}

// BIND EVENT LISTENERS

// helper bind function
const bind = (el, evt, func) => {
	if (el.addEventListener){
		el.addEventListener(evt, func, false);
	} else if (el.attachEvent) {
		el.attachEvent('on' + evt, func);
	}
}

// start button
const _start_button = document.querySelector(".start-btn")
bind(_start_button, "click", startGame)
bind(_start_button, "click", createPlayers)


// selecting player1 hand
const _player1_card = document.querySelector(".playerOne")
bind(_player1_card, "click", selectCard)
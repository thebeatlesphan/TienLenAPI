let players = []
let lastPlay = []
let playerOne = []
let botOne = []
let botTwo = []
let botThree = []
let lastHandPlayed = []

async function startGameBtn() {
	let url = "http://127.0.0.1:8000/deck"

	// hide button onclick
	const hideStartBtn = document.querySelector(".start-btn")
	hideStartBtn.style.display = 'none'

	fetch(url)
	.then(response => response.json())
	.then(data => {
		players = data;
		playerOne = sortSuits(sortRanks(players.player1))
		botOne = sortSuits(sortRanks(players.player2))
		botTwo = sortSuits(sortRanks(players.player3))
		botThree = sortSuits(sortRanks(players.player4))

		const html = playerOne.map(card => {
			return `
			<div class="${card.suit == 'Diamonds' || card.suit == 'Hearts' ? 'card red' : 'card'}">
			<p>${card.rank}</p>
			<p>${card.suit}</p>
			</div>`
		}).join("")
		document.querySelector(".playerOne").insertAdjacentHTML("afterbegin", html)

		const botOneHTML = displayBots(botOne)
		document.querySelector(".botOne").insertAdjacentHTML("afterbegin", botOneHTML)

		const botTwoHTML = displayBots(botTwo)
		document.querySelector(".botTwo").insertAdjacentHTML("afterbegin", botTwoHTML)

		const botThreeHTML = displayBots(botOne)
		document.querySelector(".botThree").insertAdjacentHTML("afterbegin", botThreeHTML)

		console.log(botOne)
	})
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
		} else return 0;
	})
}


// render bot's hands
const displayBots = (botHand) => {
	const name = 'botName'
	return `
	<div class=botHand>
	<p class=botCardCount>${botHand.length}</p>
	<p class=botName>${name}</p>
	</div>
	`
}


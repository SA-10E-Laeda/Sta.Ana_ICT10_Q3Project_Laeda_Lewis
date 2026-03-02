from pyscript import document, window
from urllib.parse import parse_qs

teams = {

    "Green Hornets": [
        "Opdesh Brar",
        "Lewis Laeda",
        "Aion Ramirez",
        "Benjamin Gale",
        "Cen Mar Chavez",
        "Matt Sky Razonable",
        "Joshua Gracia",
        "David Alwit",
        "Wilwen Omnes",
        "Alyza Lusica",
        "Hanna Musor",
        "Lucilind Sileza",
        "CJ Estabilio",
        "Samuel De Los Santos",
        "Kushdeep Tiwari",
        "Simrat Kaur",
        "Sophia Macala",
        "Lesvie Fernandez",
        "Ekamnoor Gill",
        "Shean Aquino",
        "Rochel Oreiro",
        "Padme Montemayor",
        "Kaitlin Maranan",
        "Margaux Alotaya",
        "Janinna Faner",
        "Zaia Macas",
        "Reese Chua",
        "Travis Platon",
        "Toni Salvador",
        "Eris Salvador",
        "Leona Villanueva"
    ],

    "Red Bulldogs": [
        "Marcus Dizon",
        "Nathan Flores",
        "Paolo Garcia",
        "Kyle Torres"
    ],

    "Blue Bears": [
        "Daniel Lopez",
        "Miguel Ramirez",
        "Kevin Cruz",
        "Carlos Mendoza"
    ],

    "Yellow Tigers": [
        "John Rivera",
        "Gabriel Santos",
        "Noah Tan",
        "Andrei Villanueva"
    ]
}

def load_team():

    query = window.location.search
    params = parse_qs(query[1:])

    team = params.get("team", [None])[0]

    title = document.getElementById("teamTitle")
    output = document.getElementById("playerList")

    if team in teams:

        title.innerHTML = f"{team} Team Members"

        for player in teams[team]:
            output.innerHTML += f"""
            <div class="list-group-item">
                {player}
            </div>
            """

    else:
        title.innerHTML = "No Team Found"

load_team()
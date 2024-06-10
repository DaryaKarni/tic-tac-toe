import json

class GameSaveManager:
    @staticmethod
    def save_game(gameGrid, file_path):
        game_state = {
            "currentPlayer": gameGrid.currentPlayer,
            "nextGrid": gameGrid.nextGrid,
            "subGridStatus": gameGrid.subGridStatus,
            "buttons": [[button.text() for button in row] for row in gameGrid.buttons]
        }
        with open(file_path, 'w') as file:
            json.dump(game_state, file)

    @staticmethod
    def load_game(gameGrid, file_path):
        try:
            with open(file_path, 'r') as file:
                game_state = json.load(file)
                gameGrid.currentPlayer = game_state["currentPlayer"]
                gameGrid.nextGrid = tuple(game_state["nextGrid"]) if game_state["nextGrid"] else None
                gameGrid.subGridStatus = game_state["subGridStatus"]
                for i in range(9):
                    for j in range(9):
                        gameGrid.buttons[i][j].setText(game_state["buttons"][i][j])
                gameGrid.updateButtonStyles()
        except (FileNotFoundError, json.JSONDecodeError):
            print("Failed to load game state.")

from colorama import Fore, Style


class Connect4:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = [[' ' for i in range(width)] for j in range(height)]
        self.players_colors = {
            'GREEN': Fore.GREEN,
            'RED': Fore.RED,
        }
        self.players = ['GREEN', 'RED']

    def draw_board(self):
        for i in range(self.width):
            print(' ', str(i + 1), end='')

        print()
        for i in range(self.height):
            for j in range(self.width):
                print('|', self.board[i][j], end='')
            print('|' + '\n' + '-' * 3 * self.width)

    def take_player(self, player_turn):
        turn_not_ended = True
        while turn_not_ended:
            print("Select column to drop")
            player_input = input()
            try:
                player_input = int(player_input)
            except:
                print('Incorrect input, use number from 1 to ' + str(self.width))
                continue
            if 1 <= player_input <= self.width:
                pos = self.height - 1
                found_space = False
                while pos >= 0 and turn_not_ended:
                    if self.board[pos][player_input - 1] != ' ':
                        pos -= 1
                    else:
                        self.board[pos][player_input - 1] = f'{self.players_colors[player_turn]}*{Style.RESET_ALL}'
                        found_space = True
                        turn_not_ended = False

                if not found_space:
                    print('Column is filled, try another')

            else:
                print('Make sure you entered number from 1 to ' + str(self.width))

    def winning_move(self, color):
        color = f'{self.players_colors[color]}*{Style.RESET_ALL}'
        for i in range(self.width - 3):
            for j in range(self.height):
                if self.board[j][i] == color and self.board[j][i + 1] == color \
                        and self.board[j][i + 2] == color and self.board[j][i + 3] == color:
                    return True
        for i in range(self.width):
            for j in range(self.height - 3):
                if self.board[j][i] == color and self.board[j + 1][i] == color \
                        and self.board[j + 2][i] == color and self.board[j + 3][i] == color:
                    return True
        for i in range(self.width - 3):
            for j in range(self.height - 3):
                if self.board[j][i] == color and self.board[j + 1][i + 1] == color \
                        and self.board[j + 2][i + 2] == color and self.board[j + 3][i + 3] == color:
                    return True
        for i in range(self.width - 3):
            for j in range(3, self.height):
                if self.board[j][i] == color and self.board[j - 1][i + 1] == color \
                        and self.board[j - 2][i + 2] == color and self.board[j - 3][i + 3] == color:
                    return True

    def game_on(self):
        run_game = True

        current_player = 0
        while run_game:
            self.draw_board()
            print('Players ' + self.players[current_player] + ' turn')
            self.take_player(self.players[current_player])
            if self.winning_move(self.players[current_player]):
                self.draw_board()
                print('Player ' + self.players[current_player] + ' has won, congratulations!')
                run_game = False
            else:
                current_player = (current_player + 1) % len(self.players)


game = Connect4()
game.game_on()

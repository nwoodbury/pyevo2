from pyevo2.custom_board_50_50 import CustomBoard
from pyevo2.agents import (TitForTatAgent, NotTitForTatAgent,
                          AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo2.payoffs import load_payoffs
from pyevo2.imitation_game import ImitationGame

if __name__ == '__main__':

    # Select the payoffs used in this game
    payoffs1 = load_payoffs('prisoners_dilemma', 0.95)
    payoffs2 = load_payoffs('stag_hunt', 0.95)
    payoffs3 = load_payoffs('battle_of_the_sexes', 0.95)
    
    # Define the agents to be in each quad
    # AD_AC
    quads = [
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'},
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AD_AC/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AD_AC/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AD_AC/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)


    # AD_TFT
    quads = [
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'},
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AD_TFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AD_TFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AD_TFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # AD_NTFT
    quads = [
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'},
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AD_NTFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AD_NTFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AD_NTFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # AC_AD
    quads = [
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AC_AD/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AC_AD/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AC_AD/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)


    # AC_TFT
    quads = [
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AC_TFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AC_TFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AC_TFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # AC_NTFT
    quads = [
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'},
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/AC_NTFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/AC_NTFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/AC_NTFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # TFT_AD
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/TFT_AD/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/TFT_AD/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/TFT_AD/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)

    # TFT_AC
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/TFT_AC/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/TFT_AC/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/TFT_AC/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # TFT_NTFT
    quads = [
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'},
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/TFT_NTFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/TFT_NTFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/TFT_NTFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
        # NTFT_AD
    quads = [
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},
		{'name': 'Always Defect', 'class': AlwaysDefectAgent,
         'color': 'r'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/NTFT_AD/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/NTFT_AD/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/NTFT_AD/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)


    # NTFT_AC
    quads = [
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},
        {'name': 'Always Cooperate', 'class': AlwaysCooperateAgent,
         'color': 'g'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/NTFT_AC/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/NTFT_AC/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/NTFT_AC/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
    
    # NTFT_TFT
    quads = [
        {'name': 'Not-Tit-for-Tat', 'class': NotTitForTatAgent,
         'color': 'm'},
        {'name': 'Tit-for-Tat', 'class': TitForTatAgent,
         'color': 'b'}
    ]

    # Initialize the board
    board1 = CustomBoard(quads)
    board2 = CustomBoard(quads)
    board3 = CustomBoard(quads)

    # Initialize the game
    game1 = ImitationGame(board1, payoffs1, 'gamma_95/50_50/NTFT_TFT/PD')
    game2 = ImitationGame(board2, payoffs2, 'gamma_95/50_50/NTFT_TFT/Stag_Hunt')
    game3 = ImitationGame(board3, payoffs3, 'gamma_95/50_50/NTFT_TFT/Battle')

    # Run the game over 100 time steps, results will be saved in out/custom_01/
    game1.run(100)
    game2.run(100)
    game3.run(100)
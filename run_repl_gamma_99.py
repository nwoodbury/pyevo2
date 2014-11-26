# !! Don't forget to switch to pyevo2
from pyevo2.population import Population
from pyevo2.agents import (TitForTatAgent, NotTitForTatAgent,
                           AlwaysCooperateAgent, AlwaysDefectAgent)
from pyevo2.payoffs import load_payoffs
from pyevo2.replication_game import ReplicationGame

if __name__ == '__main__':

    # Select the payoffs used in this game
    payoffs1 = load_payoffs('prisoners_dilemma', 0.99)
    payoffs2 = load_payoffs('stag_hunt', 0.99)
    payoffs3 = load_payoffs('battle_of_the_sexes', 0.99)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 225
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 225
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 225
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 225
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/equal_pop')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/equal_pop')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/equal_pop')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 325
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 325
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 249
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 1
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/AD_1')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/AD_1')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/AD_1')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 300
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 300
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 300
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_Other_equal_pop')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_Other_equal_pop')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_Other_equal_pop')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 450
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 450
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 0
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_AC_equal_pop_TFT_NTFT')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_AC_equal_pop_TFT_NTFT')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_AC_equal_pop_TFT_NTFT')
            
    game1.run(20, fps=0.5)
    game1.run(20, fps=0.5)
    game1.run(20, fps=0.5)

    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 0
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 450
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 450
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_TfT_equal_pop_AC_NTFT')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_TfT_equal_pop_AC_NTFT')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_TfT_equal_pop_AC_NTFT')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 450
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 0
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 450
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_NTfT_equal_pop_AC_TFT')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_TfT_equal_pop_AC_TFT')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_TfT_equal_pop_AC_TFT')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 800
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 100
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 0
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_AC_TFT_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_AC_TFT_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_AC_TFT_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 100
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 800
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 0
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_AC_NTFT_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_AC_NTFT_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_AC_NTFT_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 0
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 800
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 100
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_TFT_NTFT_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_TFT_NTFT_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_TFT_NTFT_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 0
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 100
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 800
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_TFT_AC_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_TFT_AC_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_TFT_AC_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 100
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 0
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 800
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_NTFT_AC_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_NTFT_AC_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_NTFT_AC_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)
    
    agents = {
        'Tit-for-Tat': {
            'class': TitForTatAgent,
            'color': 'b',
            'number': 800
        },
        'Not-Tit-for-Tat': {
            'class': NotTitForTatAgent,
            'color': 'm',
            'number': 0
        },
        'Always Cooperate': {
            'class': AlwaysCooperateAgent,
            'color': 'g',
            'number': 100
        },
        'Always Defect': {
            'class': AlwaysDefectAgent,
            'color': 'r',
            'number': 0
        }
    }
    pop1 = Population(agents)
    pop2 = Population(agents)
    pop3 = Population(agents)

    game1 = ReplicationGame(pop1, payoffs1, 'gamma_99/repl/PD/No_AD_No_NTFT_TFT_Dominates')
    game2 = ReplicationGame(pop2, payoffs2, 'gamma_99/repl/Stag_Hunt/No_AD_No_NTFT_TFT_Dominates')
    game3 = ReplicationGame(pop2, payoffs3, 'gamma_99/repl/Battle/No_AD_No_NTFT_TFT_Dominates')
            
    game1.run(20, fps=0.5)
    game2.run(20, fps=0.5)
    game3.run(20, fps=0.5)    
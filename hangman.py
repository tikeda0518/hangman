def hangman(word):
    wrong = 0
    stages = ["",
                "__________              ",
                "|                       ",
                "|         |             ",
                "|         O             ",
                "|        /|\            ",
                "|        / \            ",
                "|                       "
            ]
    # wordを1文字ずつのリストへ
    rletters = list(word)
    # wordの文字数分アンダースコアを格納
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        # 入力値が答えの中にあるかチェック
        if char in rletters:
            cind = rletters.index(char)
            # アンダースコアと文字を入れ替える
            board[cind] = char
            # 1回ヒットした文字を消す
            rletters[cind] = "$"
        else:
            wrong += 1
        # スペースで問題を繋いで表示
        print(" ".join(board))
        e = wrong + 1
        # hangmanを改行で繋げる
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        # format関数で置換
        print("あなたの負け!正解は {}.".format(word))


hangman("cat")

#coding = utf-8
m = {
        '0': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        '1': "XXXXOXXX\nXXXOOXXX\nXXOOOXXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXOOOOXX\nXXXXXXXX\n",
        '2': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXXXXOOXX\nXXXOOXXX\nXXOOXXXX\nXOOOOOOX\nXXXXXXXX\n",
        '3': "XXOOOOXX\nXOOXXOOX\nXXXXXOOX\nXXXOOOXX\nXXXXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        '4': "XXXXOOXX\nXXXOOOXX\nXXOXOOXX\nXOXXOOXX\nXOOOOOOX\nXXXXOOXX\nXXXOOOOX\nXXXXXXXX\n",
        '5': "XOOOOOOX\nXOOOOOOX\nXOXXXXXX\nXOOOOOXX\nXXXXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        '6': "XXOOOOXX\nXOOXXOOX\nXOOXXXXX\nXOOOOOXX\nXOOXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        '7': "XOOOOOOX\nXOXXXOOX\nXXXXXOOX\nXXXXOOXX\nXXXXOOXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\n",
        '8': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        '9': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXXOOOOOX\nXXXXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        "-": "XXXXXXXX\n",
        'a': "XXOOOXXX\nXXXOOOXX\nXXOXOOXX\nXXOXXOOX\nXOOOOOOX\nXOXXXOOO\nOOOXOOOO\nXXXXXXXX\n",
        'b': "XOOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOOOOXX\nXXXXXXXX\n",
        'c': "XXOOOOOX\nXOOXXOOX\nXOOXXXOX\nXOOXXXXX\nXOOXXXOX\nXOOXXXOX\nXXOOOOXX\nXXXXXXXX\n",
        'd': "OOOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nOOOOOOXX\nXXXXXXXX\n",
        'e': "XOOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOOXX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
        'f': "OOOOOOOX\nXOOXXXOX\nXOOXOXOX\nXOOOOXXX\nXOOXOXXX\nXOOXXXXX\nOOOOOXXX\nXXXXXXXX\n",
        'g': "XXOOOOOX\nXOOXXOOX\nXOOXXXOX\nXOOXXXXX\nXOOXOOOO\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        'h': "OOOOXOOO\nXOOXXOOX\nXOOXXOOX\nXOOOOOOX\nXOOXXOOX\nXOOXXOOX\nOOOXOOOO\nXXXXXXXX\n",
        'i': "XXOOOOXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXOOOOXX\nXXXXXXXX\n",
        'j': "XXXOOOOX\nXXXXOOXX\nXXXXOOXX\nXXXXOOXX\nXXXXOOXX\nXOOXOOXX\nXXOOOXXX\nXXXXXXXX\n",
        'k': "OOOOXOOO\nXOOXXOOX\nXOOXOOXX\nXOOOOXXX\nXOOXOOXX\nXOOXXOOX\nOOOOXOOO\nXXXXXXXX\n",
        'l': "XOOOOXXX\nXXOOXXXX\nXXOOXXXX\nXXOOXXXX\nXXOOXXOX\nXXOOXOOX\nXOOOOOOX\nXXXXXXXX\n",
        'm': "OOXXXOOO\nXOOXXOOX\nXOOXOOOX\nXOOOOOOX\nXOXOXOOX\nXOXXXOOX\nOOOXOOOO\nXXXXXXXX\n",
        'n': "OOOXXOOO\nXOOOXXOX\nXOOOXXOX\nXOXOOXOX\nXOXOOXOX\nXOXXOOOX\nOOOXOOOX\nXXXXXXXX\n",
        'o': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXXOOOOXX\nXXXXXXXX\n",
        'p': "XOOOOOXX\nXXOOXOOX\nXXOOXOOX\nXXOOXOOX\nXXOOOOXX\nXXOOXXXX\nXOOOOXXX\nXXXXXXXX\n",
        'q': "XXOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOXXOOX\nXOOXOOOX\nXOOXXOOX\nXXOOOOXO\nXXXXXXXX\n",
        'r': "OOOOOOXX\nXOOXXOOX\nXOOXXOOX\nXOOOOOXX\nXOOXXOOX\nXOOXXOOX\nOOOOXXOO\nXXXXXXXX\n",
        's': "XXOOOOOX\nXOOXXOOX\nXOOOXXXX\nXXOOOOXX\nXXXXOOOX\nXOOXXOOX\nXOOOOOXX\nXXXXXXXX\n",
        't': "OOOOOOOO\nOOXOOXOO\nOXXOOXXO\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXOOOOXX\nXXXXXXXX\n",
        'u': "OOOOXOOO\nXOOXXXOX\nXOOXXXOX\nXOOXXXOX\nXOOXXXOX\nXOOXXXOX\nXXOOOOXX\nXXXXXXXX\n",
        'v': "OOOOXOOO\nXOOXXXOX\nXOOXXXOX\nXXOOXOXX\nXXOOXOXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\n",
        'w': "OOOXOXOO\nOOXXOXXO\nOOXOOOXO\nOOXOOOXO\nXOOOXOOX\nXOOXXOOX\nXOOXXOOX\nXXXXXXXX\n",
        'x': "OOOOXOOO\nXOOXXXOX\nXXOOXOXX\nXXXOOXXX\nXXOXOOXX\nXOXXXOOX\nOOOXOOOO\nXXXXXXXX\n",
        'y': "OOOOXOOO\nXOOXXXOX\nXXOOXOXX\nXXOOXOXX\nXXXOOXXX\nXXXOOXXX\nXXOOOOXX\nXXXXXXXX\n",
        'z': "XOOOOOOX\nXOXXXOOX\nXXXXOOXX\nXXXOOXXX\nXXOOXXXX\nXOOXXXOX\nXOOOOOOX\nXXXXXXXX\n",
        ".": "XXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\nXXXXXXXX\n",
        ",": "XXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXOXXX\nXXXOXXXX\nXXXXXXXX\n",
        "!": "XXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\n",
        "?": "XXOOOOXX\nXOOXXOOX\nXXXXXOOX\nXXXOOXXX\nXXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\n",
        "@": "XOOOOOOX\nOXXXXXXO\nOXXOOOXO\nOXOXXOXO\nOXXOOXOX\nOXXXXXXX\nXOOOOOOX\nXXXXXXXX\n",
        "#": "XOOXXOOX\nXOOXXOOX\nOOOOOOOO\nXOOXXOOX\nOOOOOOOO\nXOOXXOOX\nXOOXXOOX\nXXXXXXXX\n",
        '$': "XXXOOXXX\nXXOOOOOX\nXOOXXXXX\nXXOOOOXX\nXXXXXOOX\nXOOOOOXX\nXXXOOXXX\nXXXXXXXX\n",
        "&": "XXOOOOXX\nXOOXXOOX\nXXOOXOXX\nXXOOOXXO\nOOXXOOXO\nOOXXXOOX\nXOOOOXOO\nXXXXXXXX\n",
        "*": "XXXOOXXX\nXOXOOXOX\nXXOOOOXX\nXOXOOXOX\nXXXOOXXX\nXXXXXXXX\n",
        "+": "XXXOOXXX\nXXXOOXXX\nXOOOOOOX\nXOOOOOOX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\n",
        ":": "XXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\nXXXXXXXX\n",
        ";": "XXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXXXXXX\nXXXOOXXX\nXXXOOXXX\nXXXOXXXX\nXXXXXXXX\n",
        "/": "XXXXOOXX\nXXXXOOXX\nXXXOOXXX\nXXXOOXXX\nXXXOOXXX\nXXOOXXXX\nXXOOXXXX\nXXXXXXXX\n"
    }

m = {"0": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\n\n",
"1": "XOOOOOXXX\nXOOOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
"2": "XOOOOOOXX\nXOOOOOOOX\nXXXXXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
"3": "XOOOOOOXX\nXOOOOOOOX\nXXXXXOOOX\nXXOOOOOXX\nXXOOOOOOX\nXXXXXOOOX\nXOOOOOOOX\nXOOOOOOXX\nXXXXXXXXX\n",
"4": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXXOOOOOOX\nXXXXXOOOX\nXXXXXOOOX\nXXXXXXXXX\n",
"5": "XOOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXOOOX\nXOOOOOOOX\nXOOOOOOXX\nXXXXXXXXX\n",
"6": "XXOOOOOXX\nXOOOOOOXX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXXXXXXX\n",
"7": "XOOOOOOOX\nXOOOOOOOX\nXXXXOOOOX\nXXXOOOOXX\nXXOOOOXXX\nXXOOOXXXX\nXXOOOXXXX\nXXOOOXXXX\nXXXXXXXXX\n",
"8": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXXXXXXX\n",
"9": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXOOOX\nXXOOOOOOX\nXXOOOOOXX\nXXXXXXXXXX\n",
"-": "XXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\n\n",
"a": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"b": "XOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOXX\nXXXXXXXXX\n",
"c": "XXOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOOOOOX\nXXOOOOOOX\nXXXXXXXXX\n",
"d": "XOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOXX\nXXXXXXXXX\n",
"e": "XOOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOXXX\nXOOOOOXXX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
"f": "XOOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOXXX\nXOOOOOXXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXXXXX\nXXXXXXXXX\n",
"g": "XXOOOOOXX\nXOOOOOOXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOOX\nXXXXXXXXX\n",
"h": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"i": "XOOOOOOOX\nXOOOOOOOX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
"j": "XXXXXOOOX\nXXXXXOOOX\nXXXXXOOOX\nXXXXXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXXXXXXX\n",
"k": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"l": "XOOOXXXXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXXXXX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
"m": "XOOXXXOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"n": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"o": "XXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXXXXXXX\n",
"p": "XOOOOOOXXX\nXOOOOOOOXX\nXOOOXOOOXX\nXOOOXOOOXX\nXOOOOOOOXX\nXOOOOOOXXX\nXOOOXXXXXX\nXOOOXXXXXX\n\n",
"q": "XXOOOOOXXX\nXOOOOOOOXX\nXOOOXOOOXX\nXOOOXOOOXX\nXOOOXOOOXX\nXOOOXOOXXX\nXOOOOOOOXX\nXXOOOOOOXX\nXXXXXXXXXX\n",
"r": "XOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"s": "XXOOOOOOX\nXOOOOOOOX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXOOOX\nXOOOOOOOX\nXOOOOOOXX\nXXXXXXXXX\n",
"t": "XOOOOOOOX\nXOOOOOOOX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\n",
"u": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXX\n",
"v": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXOOOXXX\n\n",
"w": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOOOOOX\nXOOOXOOOX\nXOOXXXOOX\nXXXXXXXXX\n",
"x": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXOOOOOXX\nXOOOOOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXXXXXXXXX\n",
"y": "XOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOXOOOX\nXOOOOOOOX\nXXOOOOOXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\n",
"z": "XOOOOOOOX\nXOOOOOOOX\nXXXXOOOOX\nXXXOOOOXX\nXXOOOOXXX\nXOOOOXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXXXXX\n",
";": "XXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXOOXXX\nXXXXOOXXX\nXXXXXXXXX\n",
"!": "XXXOOOXXX\nXXOOOOOXX\nXXOOOOOXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\nXXXOOOXXX\nXXXOOOXXX\nXXX\n",
"?": "XOOOOOOXX\nXOOOOOOOX\nXXXXXOOOX\nXXOOOOOOX\nXXOOOOOXX\nXXXXXXXXX\nXXOOOXXXX\nXXOOOXXXX\nXXXXXXXXX\n",
"@": "XXOOOOOXX\nXOXXXXXOX\nXOXOOOXOX\nXOXOOOXOX\nXOXOOOXOX\nXOXOOOOXX\nXOXXXXXXX\nXXOOOOOXX\nXXXXXXXXX\n",
"#": "XXOOXOOXX\nXXOOXOOXX\nXOOOOOOOX\nXXOOXOOXX\nXXOOXOOXX\nXOOOOOOOX\nXXOOXOOXX\nXXOOXOOXX\nXXXXXXXXX\n",
"$": "XXXXOXXXX\nXXOOOOOOX\nXOOOXXXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXXXOOOX\nXOOOOOOXX\nXXXXOXXXX\nXXXXX\n",
"&": "XXOOOOOXX\nXOOOOOOXX\nXOOOXXXXX\nXXOOOXOOO\nXOOOOXOOO\nXOOOXXOOX\nXOOOOOOOX\nXXOOOOOOX\nXXXXXXXXX\n",
"*": "XXOXOXOXX\nXXXOOOXXX\nXXOOOOOXX\nXXXOOOXXX\nXXOXOXOXX\nXXXXXXXXXX\n",
"+": "XXXOOOXXX\nXXXOOOXXX\nXOOOOOOOX\nXOOOOOOOX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXXXXX\n",
":": "XXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\n\n",
";": "XXXOOOXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXXXXXX\nXXXOOOXXX\nXXXOOOXXX\nXXXXOOXXX\nXXXXOOXXX\n\n",
"/": "XXXXXOOOX\nXXXXXOOOX\nXXXXOOOXX\nXXXOOOXXX\nXXXOOOXXX\nXXOOOXXXX\nXOOOXXXXX\nXOOOXXXXX\nXXXXXXXXXXXXXXXXXX",
}


for char in 'abcdefg':
    x = m[char]
    x = x.replace('X', u'·').replace('O', u'█')
    print x
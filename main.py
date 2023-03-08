"""
    Author: Michael Fessler
    Date: 2023/03/08
    Version: 0.1
    Description:
            Primitive version of the snake phone game.
"""

import PlayingField

for i in range(len(PlayingField.fields)):
    for j in range(len(PlayingField.fields[i])):
        print(PlayingField.fields[i][j], end="")
    print()
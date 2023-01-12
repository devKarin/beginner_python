"""
EX09.3 and EX09.4 - Meta-trees and meta-dragons.

This program draws recursively using python turtle module.

Available functions:
tree(length); Draws a binary tree using turtle.

"""

from turtle import Turtle
from sys import setrecursionlimit
setrecursionlimit(10000)


def tree(length):
    """
    A turtle program to draw a binary tree.

    Starts with a trunk 200px tall.
    Each new branch is 3/5 as big as its trunk.
    Minimum branch size is 5px.

    Move turtle with: t.forward(), t.left(), t.right(), tree()

    :param length: height of the trunk or leaf
    """
    if length < 5:
        return
    # Start drawing.
    t.pendown()
    # Draw the left side of the tree.
    t.forward(length)
    t.left(60)
    # Every next tree branch is 3/5 in length of the previous.
    tree(length * 3 / 5)
    # Change colour for better visibility during visual review (lightblue).
    # Draw the right side of the branch.
    t.color("#4d94ff")
    # The angle between the left and the right branch must be 120 degrees.
    t.right(120)
    tree(length * 3 / 5)
    # Change colour for better visibility during visual review (white).
    # Turn back.
    t.color("#fff")
    # Since the last command ordered the turtle to turn right 120 degrees, but if the tree length was shorter or
    # equal to 5 the next loop was not executed and the turtle is at angle 60 degrees right (left 60 + right 120).
    # In order to turn around the turtle it must be turned 240 degrees left (right 60 + left 240 = left 180) or
    # 120 degrees right (right 60 + right 120 = right 180).
    t.right(120)
    # Go back.
    t.forward(length)
    # Turn around again.
    t.right(180)


def apply_dragon_rules(string):
    """
    Write a recursive function that replaces characters in string.

    Like so:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    pass


def curve(string, depth):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instructionset for drawing the dragon at iteration 'depth'
    """
    pass


def format_curve(string):
    """
    Use recursions to remove  a  and  b  symbols from the instruction string.

    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    pass


def draw_dragon(string, length):
    """Draws the dragon by reading the string recursively.

    Use t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    pass


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("#96004f")
    t.speed(0)
    t.pensize(3)
    # Move the tree a bit down, otherwise it will grow out of the window.
    t.setpos(0, -200)
    t.left(90)
    tree(200)

    '''
    s = curve("Fa", 8)
    s = format_curve(s)
    l = get_line_length(100, 8)
    draw_dragon(s, l)
    '''
    save(t)
    t.getscreen().exitonclick()
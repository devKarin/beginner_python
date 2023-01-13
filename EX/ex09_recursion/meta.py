"""
EX09.3 and EX09.4 - Meta-trees and meta-dragons.

This program draws recursively using python turtle module.

Available functions:
tree(length); Draws a binary tree using turtle.
apply_dragon_rules(string); Writes a recursive function which replaces characters in string.
curve(string, depth); Recursively generates the next depth of rules.
format_curve(string); Removes a and b symbols from the instruction string using recursion.
draw_dragon(string, length); Draws the dragon by using turtle and by reading the string recursively.

Helper functions:
get_line_length(dragon_width, depth); Returns one Turtle step length if the width and depth are known.
save(t: Turtle); Saves the turtle graphic to file which can be opened with an image editor like GIMP.

"""

from turtle import Turtle
from sys import setrecursionlimit
setrecursionlimit(10000)


def tree(length):
    """
    Draw a binary tree using turtle.

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
    Write a recursive function which replaces characters in string.

    Examples:
        "a" -> "aRbFR"
        "b" -> "LFaLb"
    apply_dragon_rules("a") -> "aRbFR"
    apply_dragon_rules("aa") -> "aRbFRaRbFR"
    apply_dragon_rules("FRaFRb") -> "FRaRbFRFRLFaLb"

    :param string: sentence with "a" and "b" characters that need to be replaced
    :return: new sentence with "a" and "b" characters replaced
    """
    sentence = ""
    if len(string) <= 0:
        return ""
    if string[-1] == "a":
        sentence += apply_dragon_rules(string[:-1]) + "aRbFR"
    elif string[-1] == "b":
        sentence += apply_dragon_rules(string[:-1]) + "LFaLb"
    else:
        sentence += apply_dragon_rules(string[:-1]) + string[-1]
    return sentence


def curve(string, depth):
    """
    Recursively generate the next depth of rules.

    Calls apply_dragon_rules() function `depth` times.

    Example:
    curve("Fa", 2) -> "FaRbFRRLFaLbFR"

    :param string: current instruction string
    :param depth: how many times the rules are applied
    :return: instruction set for drawing the dragon at iteration 'depth'
    """
    if depth <= 0:
        return string
    else:
        instruction_set = apply_dragon_rules(string)
    # Saving the new depth value into a variable speeds up the recursion.
    depth -= 1
    # Call again with new values.
    return curve(instruction_set, depth)


def format_curve(string):
    """
    Remove a and b symbols from the instruction string using recursion.

    Example:
    format_curve("Fa") -> "F"
    format_curve("FaRbFR") -> "FRFR"

    :param string: instruction string
    :return: clean instructions with only "F", "R", and "L" characters
    """
    sentence = ""
    if len(string) <= 0:
        return ""
    if string[-1] in ["a", "b"]:
        sentence += format_curve(string[:-1])
    else:
        sentence += format_curve(string[:-1]) + string[-1]
    return sentence


def draw_dragon(string, length):
    """
    Draw the dragon by using turtle and by reading the string recursively.

    Uses t.right(), t.left(), t.forward() and draw_dragon() to move turtle.
        L - means turn 90 degrees to left and go forward
        R - means turn 90 degrees to right and go forward
        F - means don't turn just go forward

    :param string: instructions left to process
    :param length: how many pixels to move forward, left or right
    """
    if len(string) <= 0:
        return
    if string[0] == "L":
        t.left(90)
        t.forward(length)
        draw_dragon(string[1:], length)
    elif string[0] == "R":
        t.right(90)
        t.forward(length)
        draw_dragon(string[1:], length)
    elif string[0] == "F":
        t.forward(length)
        draw_dragon(string[1:], length)


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with an image editor like GIMP."""
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')


if __name__ == '__main__':
    t = Turtle()
    t.getscreen().bgcolor("#1c262b")
    t.color("#96004f")
    t.speed(0)
    t.pensize(3)

    # Move the tree a bit down, otherwise it will grow out of the window.
    # t.setpos(0, -200)
    t.left(90)
    # tree(200)

    s = curve("Fa", 8)
    s = format_curve(s)
    line_length = get_line_length(100, 8)
    draw_dragon(s, line_length)

    print("apply_dragon_rules", apply_dragon_rules("a"))  # -> "aRbFR"
    print("apply_dragon_rules", apply_dragon_rules("b"))  # -> "LFaLb"
    print("apply_dragon_rules", apply_dragon_rules("aa"))  # -> "aRbFRaRbFR"
    print("apply_dragon_rules", apply_dragon_rules("FRaFRb"))  # -> "FRaRbFRFRLFaLb"
    print("curve", curve("Fa", 2))  # -> "FaRbFRRLFaLbFR"
    print("curve", curve("FaRbFR", 1))  # -> "FaRbFRRLFaLbFR"
    print("curve", curve("Fa", 4))  # -> "FaRbFRRLFaLbFRRLFaRbFRLLFaLbFRRLFaRbFRRLFaLbFRLLFaRbFRLLFaLbFR"
    print("format_curve", format_curve("Fa"))  # -> "F"
    print("format_curve", format_curve("FaRbFR"))  # -> "FRFR"

    save(t)
    t.getscreen().exitonclick()

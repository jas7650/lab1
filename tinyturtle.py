"""
CSapx Lab 1: Tiny Turtle
A program that interprets commands for the turtle and makes the turtle do it.

author: Justin Shaytar
"""

import turtle as t
import sys


def main():
    cmd_str = str(input('Enter a list of commands: '))
    print('Close the graphic window when done.')
    evaluate(cmd_str)

    t.done()


def evaluate(cmd_str):
    cmd_str = expand_polygon(cmd_str)
    cmd_str = expand_iterate(cmd_str)

    cmd_list = cmd_str.split()

    for i in range(len(cmd_list)):
        if cmd_list[i][:1] == "F":
            length = cmd_list[i][1:]
            print(cmd_list[i] + " forward(" + length + ")")
            t.forward(int(length))
        elif cmd_list[i][:1] == "B":
            length = cmd_list[i][1:]
            print(cmd_list[i] + " backward(" + length + ")")
            t.backward(int(length))
        elif cmd_list[i][:1] == "L":
            angle = cmd_list[i][1:]
            print(cmd_list[i] + " left(" + angle + ")")
            t.left(int(angle))
        elif cmd_list[i][:1] == "R":
            angle = cmd_list[i][1:]
            print(cmd_list[i] + " right(" + angle + ")")
            t.right(int(angle))
        elif cmd_list[i][:1] == "C":
            radius = cmd_list[i][1:]
            print(cmd_list[i] + " circle(" + radius + ")")
            t.circle(int(radius))
        elif cmd_list[i][:1] == "U":
            print(cmd_list[i] + " up()")
            t.penup()
        elif cmd_list[i][:1] == "D":
            print(cmd_list[i] + " down()")
            t.pendown()


def expand_iterate(cmd_str):
    out_str = ""
    cmd_list = cmd_str.split()
    i = 0
    while i < len(cmd_list):
        if cmd_list[i][0] == "I":
            j = int(cmd_list[i][1:])
            i += 1
            iter_str = ""

            while cmd_list[i] != "@":
                iter_str += cmd_list[i]
                iter_str += " "
                i += 1
            out_str += iter_str * j
        else:
            out_str += cmd_list[i]
            out_str += " "

        i += 1
    return out_str


def expand_polygon(cmd_str):
    cmd_list = cmd_str.split()
    out_str = ""
    i = 0
    while i < len(cmd_list):
        if cmd_list[i][0] == "P":
            num_sides = int(cmd_list[i][1:])
            i += 1
            side_length = int(cmd_list[i])
            out_str += "I%s F%s L%s @ " % (num_sides, side_length, round(360 / num_sides))
        else:
            out_str += cmd_list[i] + " "
        i += 1
    return out_str


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()

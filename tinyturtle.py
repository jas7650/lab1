"""
CSapx Lab 1: Tiny Turtle
A program that interprets commands for the turtle and makes the turtle do it.

author: Justin Shaytar
"""

import turtle
cmds = {"F": (turtle.forward, True),
        "L": (turtle.left, True),
        "U": (turtle.up, False),
        "D": (turtle.down, False)}
def main():
    cmd_str=str(input('Enter a list of commands: '))
    evaluate(cmd_str)
def evaluate(cmd_str):
    cmd_str=expand_iterate(cmd_str)
    cmd_str=expand_polygon(cmd_str)
    for cmd in cmd_str.split(""):
        func, args = cmds[cmd[0]]
        if args:
            func(float(cmd[1:]))
        else:
            func()
def expand_iterate(cmd_str):
    out_str=""
    cmd_list=cmd_str.split("")
    i=0
    while i < len(cmd_list):
        if cmd_list[i][0]=="I":
            j=int(cmd_list[i][1:])
            i+=1
            while cmd_list[i] != "@":
                iter_str += cmd_list[i]
                iter_str += ""
                i+=1
            out_str+=iter_str
        else:
            out_str += cmd_list[i]
            out_str += ""
            i+=1
    return out_str
def expand_polygon(cmd_str):
    cmd_list = cmd_str.split("")
    out_str=""
    i=0
    while i < len(cmd_list):
        if cmd_list[i][0]=="P":
            num_sides=int(cmd_list[i][1:])
            i+=1
            side_length = int(cmd_list[i])
            out_str += "I%s F%s L%s @"%(side_length,side_length,360/num_sides)
        else:
            out_str+=cmd_list[i] + ""
        i+=1
    return out_str
main()
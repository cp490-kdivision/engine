import pyodbc
import uuid
import json
import re
import cmd
from config import *
from pathlib import Path

ATTRS_FILE = Path(__file__).parent / "primitives.json"


#create PYOBDC connection object
cnxn: pyodbc.Connection = pyodbc.connect(coalEngineDBCon.con)
#cursor object from connection
crsr: pyodbc.Cursor = cnxn.cursor()

def getEvent(eventID):
    #select query
    select_sql = "SELECT event_Condition From Events WHERE event_ID = '{}'".format(eventID)
    #execute select query
    crsr.execute(select_sql)
    rows = crsr.fetchall()
    # Close db connetion
    cnxn.close()

    #conver to JSON serializable
    data=[]
    data.append([x for x in rows])
    return data

eventResult = getEvent('2c0unr2ntl')

str1 = ''.join(str(e) for e in eventResult)
m = re.findall('{(?:[^{}])*}',str1)
for item in m:
    print(item)
my_lst_string = ','.join(map(str,m))
print(my_lst_string)

primitive = []
arguments = []
UUID = None
game_id = None

class condition:
    primitive: str
    arguments: list[str]

    def __init__(self,primitive: str, arguments: list[str]) -> None:
        self.primitive = primitive
        self.arguments = arguments

class cmdMushroom():
    command: 'eat mushroom'
    condition : {'primitive': "obj-loc-is-equal", 'arguments': ["item","mushroom","character"]}
    true_part: {'primitive': "You have been poisoned, you might feel sick", 'arguments': ["character", "#", "poisoned", "2"]}
    {'primitive': "You are getting worse", 'arguments': ["game", "#", "poisoned"]},
    {'primitive': "GAME OVER!!! YOU DIED", 'arguments': ["", "mushroom"]}
    false_part: {'primitive': "Invalid Input", 'arguments': ["game", "#", "cannot-eat-mushroom"]}
    game_id: UUID
    id: UUID

    def __init__(self, command: 'eat mushroom', condition:list[condition], 
    true_part: list[condition], false_part: list[condition]) -> None:
        self.command = command
        self.condition = condition
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdblacboard():
    command: 'read blackboard'
    condition : {'primitive': "obj-loc-is-equal", 'arguments': ["item", "blackboard", "#"]}
    true_part:  {"primitive": "Blackboard says you are Beautiful", "arguments": ["game", "#", "blackboard"]}
    false_part: {'primitive': "Invalid Input", 'arguments': ["game", "#", "item-not-here"]}
    game_id: UUID
    id: UUID

    def __init__(self, command: 'read blackboard', condition:list[condition], 
    true_part: list[condition], false_part: list[condition]) -> None:
        self.command = command
        self.condition = condition
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdDrop():
    command: 'drop !item'
    condition : {'primitive': "obj-loc-is-equal", 'arguments': ["item", "!item", "character"]}
    true_part:  {"primitive": "I think you dropped something","arguments": ["game", "#", "drop-item"]}
    {"primitive": "mv-item-to-room", "arguments": ["#", "!item"]}
    false_part: {'primitive': "Invalid Input", 'arguments': ["game", "#", "cannot-drop-there"]}
    game_ID: UUID
    id: UUID

    def __init__(self, command: 'drop !item', condition:list[condition], 
    true_part: list[condition], false_part: list[condition]) -> None:
        self.command = command
        self.condition = condition
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdget():
    command: 'get !item'
    condition : {"primitive": "is-equal", "arguments": ["item", "!item", "takeable", "true"]}
    {"primitive": "obj-loc-is-equal", "arguments": ["item", "!item", "#"]} 
    true_part : {"primitive": "want to get something", "arguments": ["game", "#", "took-item"]}
    {"primitive": "mv-item-to-char", "arguments": ["!item"]}
    false_part : {"primitive": "invalid input", "arguments": ["game", "#", "cannot-take-that"]}
    game_id:UUID
    id: UUID
        
    def __init__(self, command: 'get !item', condition:list[condition], 
    true_part: list[condition], false_part: list[condition]) -> None:
            self.command = command
            self.condition = condition
            self.true_part = true_part
            self.false_part = false_part
            self.id = id
            self.game_id = game_id

class cmdDir():
    command: 'go !direction'
    condition : {}
    true_part : {"primitive" : "go", "arguments" : ["room", "#", "!direction"]}
    false_part : {}
    game_id : UUID
    id : UUID

    def __init__(self, command: 'go !direction', condition:list[condition], 
    true_part: list[condition], false_part: list[condition]) -> None: 
        self.command = command
        self.condition = condition
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdLook():
    command : 'look'
    condition : {}
    true_part : {"primitive" : "look", "arguments" : []}
    false_part : {}
    game_id : UUID
    id: UUID

    def __init__(self, command: 'look', condition:list[condition],
        true_part: list[condition], false_part:list[condition]) -> None:
        self.command = command
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdInventory():
    command : 'inventory'
    condition : {}
    true_part : {"primitive" : "inventory", "arguments" : []}
    false_part : []
    game_id : UUID
    id = UUID

    def __init__(self, command: 'inventory', condition:list[condition],
    true_part: list[condition], false_part: list[condition]) -> None:
        self.command = command
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class cmdBlank():
    command : ''
    condition : {"primitive" : "is-gt", "arguments" : ["character", "#", "poisoned", "0"]}
    true_part : {"primitive" : "message", "arguments" : ["game", "#", "poisioned-more"]}
    {"primitive" : "dec", "arguments" : ["character", "#", "poisioned"]}
    false_part : []
    game_id : UUID
    id = UUID

    def __init__(self, command: '', condition:list[condition],
        true_part: list[condition], false_part: list[condition]) -> None:
        self.command = command
        self.true_part = true_part
        self.false_part = false_part
        self.id = id
        self.game_id = game_id

class TextAdventureCmd(cmd.Cmd):
    print('Welcome to MUD!')
    print('====================')
    print()
    player_name = input("Hello there, what is your name?\n :>")
    print("Well then, " + player_name + ".\n");
    
    print("================================")

    print('To Play enter the Commands: ')
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True
    

if __name__ == '__main__':
    TextAdventureCmd().cmdloop()
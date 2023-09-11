import sys, time, threading, cursor, msvcrt, time
from Input import Input
from TerminalPosition import TerminalPosition
from TerminalTemplates import TerminalTemplates

class Loading:
    def __init__(self):
        self.TerminalTemplate = TerminalTemplates.Return("Loading")
        self.ToggleBlink = True
    
    def Animation(self):
        while self.ToggleBlink:
            TerminalPosition.UpdatePosition()
    
    def Threading(self):
        pass
    
    def Return_Loading_Screen(self):
        pass
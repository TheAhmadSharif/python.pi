#!/usr/bin/python
import argparse
import sys


class CLI:
    def __init__(self, command):
        getattr(self, command)()
        print(command, '___________ Command ___________')

    def find(self):
        print("Hi")
    
    def stream(self):
        for x in range(10):
            print(x)
#!/usr/bin/env python3
"""
A boot-script to start the bot without installing as package
"""
import sys
import os

# Ensure 'src' is in the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from bot import start_bot

if __name__ == '__main__':
    start_bot()

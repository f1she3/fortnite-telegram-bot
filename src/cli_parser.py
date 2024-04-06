"""
    This module handles CLI args.
"""

import argparse

parser = argparse.ArgumentParser(
    description='CLI options'
)

parser.add_argument(
    "-u", 
    "--username", 
    type=str,
    help="Fortnite username",
    default=""
)
parser.add_argument(
    "-i", 
    "--id", 
    type=int,
    help="Telegram user id",
    default=0
)
parser.add_argument(
    "-s", 
    "--stats", 
    action="store_true",
    help="Fetch and display the stats of the user specified by --username"
)
parser.add_argument(
    "-a", 
    "--add",
    action="store_true",
    help="Add the user specified by --username to the ranking"
)
parser.add_argument(
    "-r", 
    "--rank", 
    help="Publish the ranking",
    action="store_true",
)

args = parser.parse_args()

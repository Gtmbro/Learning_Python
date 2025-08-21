# # !/usr/bin/ env python3
# # ^ A "Shebang" to tell terminal to use python3

# import sys
# # print (sys.argv) #Returns a list of arguments I pass..
# name = sys.argv[1] #Takes 2nd argument to make it name..
# print(f"Hello {name}, how are you?")

import argparse

# parsers and subparsers object
parser = argparse.ArgumentParser(description="Multicommand greeting")
subparsers = parser.add_subparsers(dest="command", required=True)

#Greet subcommand
greet_parser = subparsers.add_parser("greet", help="Greet someone")
greet_parser.add_argument("name", help="Name of the person")
greet_parser.add_argument("--shout", action="store_true", help="Shout the name in uppercase")
greet_parser.add_argument("--repeat", type=int, default=1, help="Repeat the name for required times")

#Bye subcommand
bye_parser = subparsers.add_parser("bye", help="Say goodbye")
bye_parser.add_argument("name", help="Name of the person")
bye_parser.add_argument("--shout", action="store_true", help="Shout the name in uppercase")
bye_parser.add_argument("--repeat", type=int, default=1, help="Repeat the name")

#Parsing the added arguments.
args = parser.parse_args()

#The logic
if args.command == "greet":
  name = args.name.upper() if args.shout else args.name
  for _ in range(1,args.repeat+1):
    print(f"Hello, {name}!")

if args.command == "bye":
  name = args.name.upper() if args.shout else args.name
  for _ in range(1,args.repeat+1):
    print(f"Good bye,{name}!")
  

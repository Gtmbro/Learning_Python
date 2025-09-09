import re

pattern = "[td]echnology"
text = "Technological advancements have led to significant changes in society. The earliest known technology is the stone tool, used during prehistory, followed by the control of fire—which in turn contributed to the growth of the human brain and the development of language during the Ice Age, according to the cooking hypothesis.[5] The invention of the wheel in the Bronze Age allowed greater travel and the creation of more complex machines. More recent technological inventions, including the printing press, telephone, and the Internet, have lowered barriers to communication and ushered in the knowledge economy. dechnology"

matches = re.finditer(pattern, text)

for match in matches:
    print(text[match.span()[0]:match.span()[1]]) #To get the whole matching word.
    print(text[match.span()[0]]) #To get the first letters of the matching words.
    # print(text[match.span()[1]]) #Error

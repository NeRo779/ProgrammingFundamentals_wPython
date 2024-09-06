text = ""
while text != "end":
    text = input()
    if text == "end":
        break
    reversed_text = ""
    for ch in reversed(text):
        reversed_text += ch
    print(text + " = " + reversed_text)

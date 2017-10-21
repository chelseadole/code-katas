"""Kata: Create Phone Number - format phone number input.

#1 Best Practices Solution by kalmat2

def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

"""


def create_phone_number(n):
    new_n = ""
    for i in n:
        new_n += str(i)
    return "(" + new_n[:3] + ") " + new_n[3:6] + "-" + new_n[6:]

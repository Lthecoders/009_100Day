"----------------day 9 challenge----------------"

print("GENERATION INDENTIFIER")
print("----------------------\n")

name = input("What is your name?🤔 ")
year = int(input("Which year were you born?🤔 "))

if year >= 1883 and year <= 1900:
  print()
  print("\033[32m", name, "you are part of the Lost Generation 💀☠️", "\033[0m")

elif year >= 1901 and year <= 1927:
  print()
  print("\033[32m", name, "you are part of the Greatest Generation 🫡🫡",
        "\033[0m")

elif year >= 1928 and year <= 1945:
  print()
  print("\033[32m", name, "you are part of the Silent Generation🤫🤫", "\033[0m")

elif year >= 1946 and year <= 1964:
  print()
  print("\033[32m", name, "you are part of the Baby Boomers 👶👶", "\033[0m")

elif year >= 1965 and year <= 1980:
  print()
  print("\033[32m", name, "you are part of the Generation X 😎🧐", "\033[0m")

elif year >= 1981 and year <= 1996:
  print()
  print("\033[32m", name, "you are part of the Millenials 🤓🤓", "\033[0m")

elif year >= 1997 and year <= 2012:
  print()
  print("\033[32m", name, "you are part of the Generation Z 🤑🤑", "\033[0m")

elif year >= 2012 and year <= 2023:
  print()
  print("\033[32m", name, "you are part of the Generation Alpha 🤖🤖", "\033[0m")

else:
  print()
  print(
      "\033[31m", "ERROR",
      "you have entered an invalid year or number\n make sure you enter year from 1883 to 2023 ONLY",
      "\033[0m")

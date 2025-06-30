# Suspects: Anna, Brian, Carla
# Rule: 1 guilty, 1 truth-teller

# Statements:
# Anna says: "Brian is guilty."
# Brian says: "Anna is lying."
# Carla says: "I am innocent."

names = ["Anna", "Brian", "Carla"]

for guilty in names:
  truth_count = 0
  truth_teller = ""
  if guilty == "Brian":
    truth_count += 1
    truth_teller = "Anna"
  if guilty != "Brian":
    truth_count += 1
    truth_teller = "Brian"
  if guilty != "Carla":
    truth_count += 1
    truth_teller = "Carla"

  if truth_count == 1:
    print(f"{guilty} is guilty and\n{truth_teller} is telling truth")
    break

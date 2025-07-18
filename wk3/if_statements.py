# temperture = float(input("How high is your temperature? "))
# if temperture > 40.5:
#   print("You are to go to the hospital.")
# elif temperture > 39.4:
#   print("Call a Doctor.")
# else:
#   print("Consider rest or medicine.")
# print("Have a nice day.")

animal = input("What is your favourite animal? ").lower()
sound =""

if animal == "cat":
  sound = "meow"
elif animal == "dog":
  sound = "bark"
else:
  sound = "unknown"

print(f"The {animal} makes the sound {sound}")

name = input("Type your name: ")
print(f"\nWelcome, {name}, to the Lost Kingdom Adventure!")

answer = input(
    "\nYou wake up in a mysterious forest. Ahead of you are two paths.\n"
    "Do you go LEFT or RIGHT? "
).lower()

if answer == "left":
    answer = input(
        "\nYou discover an ancient castle. The gate is open.\n"
        "Do you ENTER the castle or WALK away? "
    ).lower()

    if answer == "enter":
        print(
            "\nInside the castle, you find a magical crown."
            "\nYou become the ruler of the Lost Kingdom! "
            "\n YOU WIN!"
        )
    elif answer == "walk":
        print(
            "\nYou leave the castle behind and get lost in the forest."
            "\n GAME OVER!"
        )
    else:
        print("\nInvalid choice. GAME OVER!")

elif answer == "right":
    answer = input(
        "\nYou reach a river where a boat is waiting.\n"
        "Do you TAKE the boat or SWIM across? "
    ).lower()

    if answer == "take":
        print(
            "\nThe boat carries you to a hidden island filled with treasure."
            "\n YOU WIN!"
        )
    elif answer == "swim":
        print(
            "\nA strong current pulls you away."
            "\n GAME OVER!"
        )
    else:
        print("\nInvalid choice. GAME OVER!")

else:
    print("\nInvalid choice. GAME OVER!")
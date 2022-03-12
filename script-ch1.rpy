# The script for events that repeat throughout part 1 but with subtle variation

# make sure only to call this label, not jump
label ch1_bus:

    scene bg bus

    "[name] walks to the bus stop and gets on the next bus."

    "There are three open seats left."

    if ryan == 0 and day > 2:
        jump ch1_bus_ryan

    else:

        if ryan == 0:
            $ temp1 = "[n_pos] classmate, [ally]"
        else:
            $ temp1 = "[ally]"

        menu:
            "Sit with [temp1]":
                jump ch1_bus_ryan
            "Sit with a stranger":
                jump ch1_bus_stranger
            "Sit alone":
                jump ch1_bus_alone

label ch1_bus_ryan:

label ch1_bus_stranger:

    if ryan > 1:
        $ renpy.say("[name] decided not to bother [ally] with [n_pos] problems today.")

    n norm smile ""

    $ 

label ch1_bus_alone:

    $ temp1 = renpy.random.choice(["English", "biology", "art", "math", "history"])

    if ryan > 1:
        $ renpy.say("[name] decided not to bother [ally] with [n_pos] problems today.")

    "[name] stares out the window as [n_sbj] thinks about [n_pos] [temp1] homework."

    n_self "Another day, another lonely day."

    $ happy-=

    jump ch1_school

label ch1_school:



    return

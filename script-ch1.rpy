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
            $ temp1 = "classmate"
        else:
            $ temp1 = "friend"

        menu:
            "Sit with [n_pos] [temp1] [ally]":
                $ bus = True
                jump ch1_bus_ryan
            "Sit with a stranger":
                jump ch1_bus_stranger
            "Sit alone":
                jump ch1_bus_alone

label ch1_bus_ryan:

    if ryan > 0:
        $ temp1 = "friend"
    else:
        $ temp1 = "classmate"

    "[name] sits with [n_pos] [temp1], [ally]."

    if ryan > 0:
        call ch1_bus_ryan_friend
    else:
        call ch1_bus_ryan_classmate

    if ryan > 2:
        $ temp3 = "sit with a friend"
    else:
        $temp3 = "have company"

    "It's nice to [temp3] on the bus."

    jump ch1_school

label ch1_bus_ryan_friend:

    if ryan > 2:
        $ temp2 = renpy.random.choose(["cat", "math", "art", "insight"])
        if temp2 == "cat":
            call ch1_bus_ryan_cat
        elif temp2 == "math":
            call ch1_bus_ryan_math
        elif temp2 == "art":
            call ch1_bus_ryan_art
        else:
            call ch1_bus_ryan_insight
    else:
        call ch1_bus_ryan_new

        return

label ch1_bus_ryan_classmate:

    "The two make small talk as the bus begins its way towards the middle school."

    "Sicne [ally] thinks [name]'s name is \"[d_name]\", [a_sbj] thinks [name]'s a [d_noun] and [name] doesn't bother to correct [ally]."

    "[ally] seems like a cool person otherwise."

    return

label ch1_bus_ryan_new:

    "[name] and [ally] make small talk on the way to school."

    return

label ch1_bus_ryan_cat:

    "[name] laughs as [ally] talks about [a_pos] adorable cat, Randle."

    return

label ch1_bus_ryan_math:

    "[ally] jokes about [mathTeach]'s homework."

    "[name] agrees that it's ridiculous."

    return

label ch1_bus_ryan_art:

    "[name] and [ally] talk about their favorite art projects."

    return

label ch1_bus_ryan_insight:

    "[ally] gives some insightful introspection."

    return

label ch1_bus_stranger:

    if ryan > 1:
        $ renpy.say("[name] decided not to bother [ally] with [n_pos] problems today.")

    n norm smile "Hey."

    show extra norm

    "The stranger looks at [name] and nods back without saying anything more."

    "[name] stares out the window as [n_sbj] thinks about [n_pos] homework."

    n_self "Another day, another awkward day."

    jump ch1_school

label ch1_bus_alone:

    $ temp1 = renpy.random.choice(["English", "biology", "art", "math", "history"])

    if ryan > 1:
        $ renpy.say("[name] decided not to bother [ally] with [n_pos] problems today.")

    "[name] stares out the window as [n_sbj] thinks about [n_pos] [temp1] homework."

    n_self "Another day, another lonely day."

    $ happy -= 1

    jump ch1_school

label ch1_school:

    if bus:
        $ temp1 = " " + ally
        if ryan > 2:
            $ temp2 = " along side"
        else:
            $ temp2 = " with"
    else:
        $ temp1 = ""
        $ temp2 = ""

    if self > 1:
        $ temp3 = "notices that flowers of multiple colors and varieties are in bloom"
    elif self < 0:
        $ temp3 = "is annoyed to be at school again but whatever"
    else:
        $ temp3 = "worries about the upcoming hay fever season"

    "As [name] walks to middle school[temp2][temp1], [n_sbj] [temp3]."

    return

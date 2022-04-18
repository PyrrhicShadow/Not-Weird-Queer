# The script for part 1 day 9 (technically loop 9)

label ch2_09:

    $ loop = 9
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# history class day 9

    show bg classroom history

    $ happy -= 1

    "[name] gets bullied.  Details coming soon."

    menu:
        "What should [name] do?"

        "Defend [n_obj]self calmly":
            jump ch2_08_history_calm

        "Defend [n_obj]self angrily":
            jump ch2_08_history_angry

        "Do nothing":
            jump ch2_08_history_nothing

    jump ch2_club

label ch2_08_history_calm:

    $ defHist = "calm"
    $ happy += 1

    if outfit == "g":
        $ actn += 1

    elif outfit == "d":
        $ actn += 0.5

    else:
        $ actn += 1

    "The peaceful option gives [name] the best outcome."

    jump ch2_08_lunch

label ch2_08_history_angry:

    $ defHist = "angry"

    if outfit == "g":
        $ actn += 0.5

    elif outfit == "d":
        $ actn -= 0.5

    "$name becomes angry at the bully, and the two almost get violent."

    "At the end, the bully gives up, avoiding a physical confrontation."

    "$name doesn't feel worse than before, but this doesn't feel like the right reaction."

    jump ch2_08_lunch

label ch2_08_history_nothing:

    $ defHist = "none"
    $ happy -= 1

    if outfit == "n":
        $ actn -= 0.5

    elif outfit == "d":
        $actn -= 1

    "$name sits there silently as the bully berates $obj."

    "This is a shitty experience."

    "Why didn't $name fight back? {w}Why?"

    jump ch2_08_lunch

label ch2_08_lunch:

    if defHist == "calm":
        n "I composed myself and told him why he was wrong."

        a "Nice. How'd it go?"

        n "It went pretty well."

        n "I mean, he didn't appologize, or anything, but it got him to shut up without making a big fuss in front of the teacher."

        a "That sounds like it worked out. Nice."

    elif defHist == "angry":
        n "He was getting allup into my face so I got really upset at him and then we almost fought."

        a "Oh."

        n "I mean, I don't thknk he wanted to get the teacher's attention so he backed down in the end, but it still didn't feel good."

        n "I don't like fighting people."

        a "Yeah, I'm glad you didn't get into a fight."

        a "That guy's a real dick, huh?"

    elif defHist == "none":
        n "I didn't feel like doing anything so I just sat there and let him go on."

        a "What?"

        n "I didn't want to get into a fight with him. I didn't know what else to do."

        a "That's how it is, sometimes.  I wish that hadn't happened."

    else:
        call dirty_hacker

        play music school

    n "Anyway, let's talk about something more lighthearted."

    n "I've had enough of him for the day."

    if book == "manga":
        $ temp1 = ""
        $ temp2 = "manga"

    else:
        $ temp1 = " novel"
        $ temp2 = "novel"

    a "Sure. I started a new [book][temp1] last night."

    n "Oh, what's it about?"

    "[ally] laughs before describing the plot of [a_pos] [temp2]."

    "Chilling with [name]'s friend is a good break from the events of history class."

# PE class day 9

    show bg field pe

    "$name goes to $pos PE class with $ally."

    "Today's just a fitness day, so they run the mile together."

    "The weather isn't too warm yet for running, yet, which $name is grateful for."

    "$ally goes on and on about something while $name just listens along and chimes in when $sbj feels like it."

    "It wasn't $name's best mile, but $ally's silly antics sure made up for it."

    jump ch2_club

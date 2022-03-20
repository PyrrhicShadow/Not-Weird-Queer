# test script - to be removed in the final game
# uses assets not created for this game,
# such as Monika sprites and (my) Kris fanart

label ch0_00:

    $ part = 0
    $ day = 0
    $ loop = 0
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

    $ redEyes = False

    scene bg classroom gen

    show monika norm

    # These display lines of dialogue.

    "[name] wakes up in a classroom with Monika in front of [n_obj]."

    $ verb = v("have")

    "[N_sbj] [verb] no idea how [n_sbj] got there."

    $ verb = v("think")

    "[N_sbj] [verb] this is very strange."

    n norm "Whaaa?"

    a "Hello, [name]. Welcome to the classroom."

    n "Who are you?"

    a "I'm [ally], your classmate. Don't mind my appearance, it's just a placeholder used by the programmer currently."

    n "Please don't kill me. I'm sorry I couldn't want to date you."

    show monika sly

    a "No need to worry. I'm [ally], not Monika."

    show monika norm

    a "As I said, this is just a placeholder for my real appearance."

    a "Think of it as an online avatar."

    n "I still don't trust you."

    show monika sly

    a "Hehe."

    scene bg start day

    "[name] is transported to another place."

    scene bg classroom gen

    n norm "What? But I'm still here?"

    show kris norm eyeless

    a "How's this for a better avatar, huh?"

    n "AHHHHH! YOU HAVE NO EYES!"

    a "There's nothing to be afraid of. Like I said earlier, these are all just placeholders."

    a "I'm still me, [ally]."

    a "And yeah, I do regret the lack of eyes in this avatar."

    a "Though I suppose red eyes would've been even creepier than hidden eyes."

    a "What do you think?"

    menu:
        "Would red eyes have been creepier than hidden eyes?"

        "Yeah, you're right.":
            jump redEyes_creepy

        "No, red eyes look cool.":
            jump redEyes_cool

label redEyes_creepy:
    $ redEyes = True

    n_self "Yeah, red eyes would be really creepy."

    a "Ah, I knew you'd agree with me"

    jump mathBud

label redEyes_cool:
    $ redEyes = False

    n_self "I think red eyes are actually pretty cool."

    a "I'll keep that in mind for next time, then."

    jump mathBud

label mathBud:

    n "How did you know what I was thinking."

    hide kris
    show monika sly

    a "I have my ways."

    show monika norm

    a "Anyway."

    $ renpy.show("extra " + a_gender + " norm", at_list=[left])

    m "I think red eyes look sick!"

    n "Who are you?"

    a "This is one of our classmates. Looks like [a_sbj]'s in your math class."

    n "Oh my God, please, everyone, get out of here!"

    hide extra

    a "I'm sad to see you go."

    a "Bye!"

    hide monika

    n "Good riddance."

    "[name] leaves the classroom and heads back into the void of the game."

label charas_test:

    scene bg end day

    "Now time to test that all the characters work."

    scene bg club front

    $ renpy.show("ally " + a_gender + " norm")

    a "Hi, I'm [ally], and I use [a_sbj]/[a_obj] pronouns. Nice to meet you."

    hide ally
    show sophia norm

    s """Hi, I'm Sophia, and I use she/her pronouns.

    I'm the classmate in [name]'s art class. Nice to meet you."""

    hide sophia
    show bioteam 1

    b """Hi, I'm [bioteam], and I use he/him pronouns.

    I'm of one [name]'s biology classmates. We do a group project together.

    Nice to meet you."""

    hide bioteam
    show cami norm

    c """Hi, I'm Cami Newton, and I use she/her pronouns.

    I'm in [name]'s book club. Nice to meet you."""

    hide cami
    $ renpy.show("mathbud " + a_gender + " norm")

    m """Hi, I'm [mathBud], and I use [a_sbj]/[a_obj] pronouns.

    [name] and I went to the same elementary school. Nice to meet you."""

    hide mathbud
    $ renpy.show("popkid " + d_gender + " norm")

    p "Hi, I'm [popKid]. Nice to meet you."

    show popkid at right
    $ renpy.show("ally " + a_gender + " norm", at_list=[left])

    a "You need to give your pronouns."

    p "Why would I need to give my pronouns?"

    a "Well, [popKid], everyone's has been doing it."

    p "Fine.  I use [d_sbj]/[d_obj] pronouns."

    p "There, are you happy?"

    hide popkid
    show ally at center

    a "Thank you. Next!"

    hide popkid
    hide ally
    show extra male norm

    cp """Hi, I'm the Club President of the middle school book club.

    I use he/him pronouns. Nice to meet you."""

    hide extra
    $ renpy.show("extra " + d_gender + " norm")

    $ classmate = "Classmate 1"

    x "Hi, I'm a generic classmate. I use [d_sbj]/[d_obj] pronouns."

    hide extra
    show extra female norm

    $ classmate = "Classmate 2"

    xf """Hi, I'm a generic classmate. I use she/her pronouns.

    Nice to meet you!"""

    show extra male norm

    $ classmate = "Classmate 3"

    xm """Hi, I'm another generic classmate.

    I use he/him pronouns."""

    hide extra

    mom norm "Hi, I'm [name]'s mom. Nice to meet you!"

    show teacher pe

    pe """I'm [peTeach].

    Teachers should have a different color than students."""

    hide teacher
    show teacher math

    math "And I'm [mathTeach], a female teacher."

    hide teacher

    "Now let's test the fail-safe message: "

    # call instead of jump if you don't want the game to end at the end of the message

    call dirty_hacker

    "That's all for now. Thank you for playing."

    "Now let's get on with the actual game."

    jump ch1

# for testing the game on a specific day
label test_game:

    menu:
        "Select which part you'd like to test:"

        "Debug":
            jump charas_test

        "Part 1":
            jump test_ch1

        "Part 2":
            jump test_ch2

        "Ending":
            jump tbc

label test_ch1:

    $ part = 1

    call test_variables

    menu:

        "Select which chapter you'd like to begin at:"

        "Part 1":
            jump ch1

        "Day 1":
            jump ch1_01

        "Day 2":
            jump ch1_02

        "Day 3":

            jump ch1_03
        "Day 4":
            jump ch1_04

        "Day 5":
            jump ch1_05

        "Day 6: Weekend":
            jump ch1_06

label test_ch2:

    $ part = 2

    call test_variables

    menu:
        "Select which chapter you'd like to begin at:"

        "Part 2":
            jump ch2

        "Day 7":
            jump tbc

        "Day 8":
            jump tbc

        "Day 9":
            jump tbc

        "Day 10":
            jump tbc

        "Day 11":
            jump tbc

        "Day 12: Weekend":
            jump tbc

label test_variables:

    "Input your day number (not loop) to test specific scenarios."

    $ temp2 = renpy.input("Input your day number:", length=2, allow="{0123456789}")
    $ temp2 = temp2.strip()
    if temp2 == "":
        $ day = 0
    else:
        $ day = int(temp2)

    "Input your point values ahead of time to test specific scenarios."

    $ temp2 = renpy.input("Input your self points:", length=2, allow="{0123456789}")
    $ temp2 = temp2.strip()
    if temp2 == "":
        $ self = 0
    else:
        $ self = int(temp2)

    if part == 1:
        $ temp2 = renpy.input("Input your ally-action points:", length=2, allow="{0123456789}")
        $ temp2 = temp2.strip()
        if temp2 == "":
            $ ryan = 0
        else:
            $ ryan = int(temp2)
    elif part == 2:
        $ temp2 = renpy.input("Input your action points:", length=2, allow="{0123456789}")
        $ temp2 = temp2.strip()
        if temp2 == "":
            $ actn = 0
        else:
            $ actn = int(temp2)

    "Set certain boolean variables."

    menu:
        "Talk true":
            $ talk = True
        "Talk false":
            $ talk = False

    return

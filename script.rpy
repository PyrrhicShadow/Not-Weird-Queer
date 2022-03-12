# The script of the game
# Events that reccur regardless of part or loop are written here
# Calls other script pages for specific parts and loops for human readability

# Declare characters used by this game.

call def_charas

# The game starts here.

label start:

    $ game = "Not Weird. Queer"

    # names of people
    $ name = ""
    $ ally = ""
    $ bioteam = renpy.random.choice(["Issac", "Evan", "Luke"])

    # variables
    $ part = 0
    $ loop = 0
    $ day = 0
    $ self = 0
    $ happy = 0
    $ deaths = 0
    $ ryan = 0
    $ bus = False
    $ club = False
    $ talk = False
    $ complete = False
    $ actn = 0
    $ temp1 = "" 

    scene bg start game

    $ name = renpy.input("What is your name?", length=14, allow="{ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789}")
    $ name = name.strip()

    if name == "":
        $ name = "Jake"

label choose_pronouns:

    "What pronouns does [name] use?"

    menu:
        "he/him":
            jump gender_male
        "she/her":
            jump gender_female
        "xe/xem":
            jump gender_enby
        "other":
            jump gender_custom

label bad_ending:

    scene bg end dead

    "This world is a cruel and unforgiving one."

    "The world crumbles around [name] and [n_pos] vision turns black."

    "[name] has died. \n[ally] misses [n_sbj] dearly."

    "Game over."

    $ deaths += 1

    jump restart

label restart:

    # reset relevant variables
    $ ryan = 0
    $ happy = 0
    $ self = 0
    $ bus = False
    $ club = False
    $ talk = False
    $ day = 0
    $ part = 0
    $ loop = 0
    $ actn = 0

    scene bg start game

    jump ch1_01

label dirty_hacker:

    scene bg end day

    """The programmer's not sure how you got here, but you're not supposed to be here.

    Odds are, you're just a dirty little hacker, aren't you?"""

    return

label tbc:

    scene bg end game

    """For the special player who played this special game:

    Thank you for making it through this game. No, seriously.

    I know it's very unfinished,
    but it means a lot to me that you took the time to click through the text,
    read through all the dialogue,
    and deal with all my nasty bugs and grammar problems.

    I hope you enjoyed playing [game] as much as I enjoyed making it.
    [name] also thanks you eternally for helping [n_obj] get through [n_pos] journey.

    You completed [n_pos] adventure with [self] self-esteem points over [day] days.
    Hopefully, through this adventure, we've all learned a little more about ourselves and the people around us.

    With hope, \n
    Pyrrhic Silva"""

    $ complete = True

    # This ends the game.

    return

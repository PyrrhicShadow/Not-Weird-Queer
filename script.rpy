# The script of the game
# Events that recur regardless of part or loop are written here
# Calls other script pages for specific parts and loops for human readability
# More definitions at definitions.rpy

# The game starts here.

label start:

    # Give a default save name
    $ save_name = name + ", Day " + "%s" %day

    # names of people
    $ bioteam = "Issac"
    $ peTeach = "Coach Paul"
    $ bioTeach = "Mr. Kinsey"
    $ histTeach = "Mr. Coulter"
    $ engTeach = "Mr. Francis"
    $ mathTeach = "Mrs. Pendle"
    $ artTeach = "Ms. Tedders"

    # game variables
    $ part = 0
    $ loop = 0
    $ day = 0
    $ self = 0
    $ happy = 0
    $ deaths = 0
    $ ryan = 0
    $ last_happy = 0
    $ actn = 0.0

    $ plur = False
    $ bus = False
    $ club = False
    $ share = False
    $ talk = False
    $ death = False

    # temp variables
    $ verb = ""
    $ verb1 = ""
    $ temp1 = ""
    $ temp2 = ""
    $ temp3 = ""

    # get the main character's name and pronouns
    scene bg start game

    "Welcome to {i}[config.name]{/i}!"

    call choose_name
    jump choose_pronouns

label choose_name:

    $ name = renpy.input("What is your name?", length=14, allow="{ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789}")
    $ name = name.strip()

    if name == "":
        $ name = "Jake"

    return

label choose_pronouns:

    "What pronouns does [name] use?"

    menu:
        "he/him":
            jump gender_male
        "she/her":
            jump gender_female
        "xe/xem":
            jump gender_enby_xe
        "they/them":
            jump gender_enby_they
        "other":
            jump gender_enby_custom

label pronouns_complete:

    # capitalized subject pronouns for ease of access
    $ N_sbj = n_sbj.capitalize()
    $ A_sbj = a_sbj.capitalize()
    $ D_sbj = d_sbj.capitalize()

    # make sure npc names are not the same as the player name

    if popKid.lower() == name.lower():
        $ popKid = popKid + " H"
    if mathBud.lower() == name.lower():
        $ mathBud = mathBud + " K"

    # name the save file name after the player's name and pronouns
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day
    $ initialized = True

    "Are you happy with your choice?"

    # The programmer (or modders) can start the game at any day (or part) by only changing this menu
    menu:
        "[name] ([n_sbj]/[n_obj])"

        "I'm ready":
            jump ch1

        "I want to test the game" if persistent.debug:
            jump test_game

        "I want to change my name":
            call choose_name

        "I want to change my pronouns":
            jump choose_pronouns

    jump pronouns_complete

label bad_ending:

    scene bg end dead

    "This world is a cruel and unforgiving one."

    "The world crumbles around [name] and [n_pos] vision turns black."

    "[name] has died. \n[ally] misses [n_sbj] dearly."

    "Game over."

    $ death = True
    $ deaths += 1

    jump restart

label restart:

    # reset relevant variables
    $ ryan = 0
    $ happy = 0
    $ self = 0
    $ last_happy = 0
    $ bus = False
    $ club = False
    $ share = False
    $ talk = False
    $ day = 0
    $ part = 0
    $ loop = 0
    $ actn = 0

    jump ch1

# if you don't want the game to end on reaching this screen, use call instead of jump
label dirty_hacker:

    scene bg end day

    """The programmer's not sure how you got here, but you're not supposed to be here.

    Odds are, you're just a dirty little hacker, aren't you?"""

    return

# a temporary ending for the game before it's fully completed
# always use jump in order to properly end the game
label tbc:

    scene bg end game

    if persistent.complete:
        $ temp1 = " again"
    else:
        $ temp1 = ""
    if persistent.debug:
        $ temp2 = "You've even stumbled upon the debug mode somehow. Good on ya ;)"
    else:
        $ temp2 = ""
    if death:
        $ temp3 = "perservered to get [name] to a better place, "
    else:
        $ temp3 = ""

    """For the special player who played this special game:

    Thank you for making it through this game[temp1]. No, seriously.

    I know it's very unfinished,
    but it means a lot to me that you took the time to click through the text,
    read through all the dialogue,
    [temp3]
    and deal with all my nasty bugs and grammar problems. [temp2]

    I hope you enjoyed playing {i}[config.name]{/i} as much as I enjoyed making it.
    [name] also thanks you eternally for helping [ n_obj] get through [n_pos] journey.

    You completed [n_pos] adventure with [self] self-esteem points over [day] days.
    Hopefully, through this adventure, we've all learned a little more about ourselves and the people around us.

    With hope, \n
    Pyrrhic Silva"""

    $ persistent.complete = True

    # This ends the game.

    return

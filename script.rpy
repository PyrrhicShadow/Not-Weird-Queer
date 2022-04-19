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

    # play music start

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

    menu:
        "{noalt}What pronouns does [name] use?{/noalt}{alt}Hello, [name]. What pronouns do you use?{/alt}"

        "{noalt}[he_him[pn]]{/noalt}{alt}he him{/alt}":
            jump pronouns_he_him

        "{noalt}[she_her[pn]]{/noalt}{alt}she her{/alt}":
            jump pronouns_she_her

        "{noalt}[xe_xem[pn]]{/noalt}{alt}xee xem{/alt}":
            jump pronouns_xe_xem

        "{noalt}[they_them[pn]]{/noalt}{alt}they them{/alt}":
            jump pronouns_they_them

        "other{alt} pronouns{/alt}":
            jump pronouns_custom

label pronouns_he_him:

    $ gender = "male"
    $ noun = "boy"
    $ adj = "boyish"
    $ pn = he_him
    $ plur = False

    jump transmasc

label pronouns_she_her:

    $ gender = "female"
    $ noun = "girl"
    $ adj = "girly"
    $ pn = she_her
    $ plur = False

    jump transfemme

label pronouns_xe_xem:

    $ pn = xe_xem
    $ plur = False

    jump gender_enby

label pronouns_they_them:

    $ pn = they_them
    $ plur = True

    jump gender_enby

label pronouns_custom:

    "Currently, custom pronouns are not supported."

    "Support for custom pronouns will be added when the programmer figures out how to display multiple text boxes at once."

    "Thank you for your patience."

    menu:
        "choose {noalt}[xe_xem[pn]]{/noalt}{alt}xee xem{/alt} pronouns":
            jump pronouns_xe_xem
        "choose {noalt}[they_them[pn]]{/noalt}{alt}they them{/alt} pronouns":
            jump pronouns_they_them
        "return to pronoun choice screen":
            jump choose_pronouns

label gender_enby:

    $ gender = "enby"
    $ noun = "nonbinary person"
    $ adj = "gender-neutral"

    jump sex_assigned_at_birth

label sex_assigned_at_birth:

    menu:
        "Pick a sex assigned at birth."
        
        "female":
            jump transmasc

        "male":
            jump transfemme

        "random":
            $ coin = renpy.random.choice(["H", "T"])

            if coin == "H":
                "Congrats! [name] is transfemme."

                jump transfemme

            if coin == "T":
                "Congrats! [name] is transmasc."

                jump transmasc

label transmasc:

    # main chara names
    $ d_name = renpy.random.choice(f_names)
    if d_name.lower() == name.lower():
        $ d_name = "Macie"
    $ d_gender = "female"
    $ d_noun = "girl"
    $ d_adj = "girly"
    $ pd = she_her

    $ ally = renpy.random.choice(m_names)
    if ally.lower() == name.lower():
        $ally = "Owen"
    $ a_gender = "male"
    $ a_noun = "boy"
    $ a_adj = "boyish"
    $ pa = he_him

    $ popKid = "Elise"
    $ mathBud = "Jaina"

label transfemme:

    # main chara names
    $ d_name = renpy.random.choice(m_names)
    if d_name.lower() == name.lower():
        $ d_name = "Brian"
    $ d_gender = "male"
    $ d_noun = "boy"
    $ d_adj = "boyish"
    $ pd = he_him

    $ ally = renpy.random.choice(f_names)
    if ally.lower() == name.lower():
        $ ally = "Megan"
    $ a_gender = "female"
    $ a_noun = "girl"
    $ a_adj = "girly"
    $ pa = she_her

    $ popKid = "Jeremy"
    $ mathBud = "Dylan"

label pronouns_complete:

    # make sure npc names are not the same as the player name

    if popKid.lower() == name.lower():
        $ popKid = popKid + " H"
    if mathBud.lower() == name.lower():
        $ mathBud = mathBud + " K"

    # name the save file name after the player's name and pronouns
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    # The programmer (or modders) can start the game at any day (or part) by only changing this menu
    menu:
        "Are you happy with your choice? {p}[name]{noalt} ([pn[pn]]){/noalt}{alt}, [pn[sbj]] [pn[obj]] pronouns{/alt}"

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

    play music death

    end "This world is a cruel and unforgiving one."

    end "The world crumbles around [name] and [pn[psv]] vision turns black."

    end "[name] has died. \n[ally] misses [pn[sbj]] dearly."

    end "Game over."

    $ persistent.death = True
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

    play music death

    end """The programmer's not sure how you got here, but you're not supposed to be here.

    Odds are, you're just a dirty little hacker, aren't you?"""

    return

# a temporary ending for the game before it's fully completed
# always use jump in order to properly end the game
label tbc:

    scene bg end game

    play music end

    if persistent.complete:
        $ temp1 = " again"
    else:
        $ temp1 = ""

    if death:
        $ temp2 = ", even perservering to get " + name + " to a better place"
    else:
        $ temp2 = ""

    end "For the special player who played this special game:"

    end "Thank you for making it through this game[temp1]."

    end "No, seriously."

    end "I know it's very unfinished,
    {w}but it means a lot to me that you took the time to click through the text,
    {w}read through all the dialogue,
    {w}and deal with all my nasty bugs and grammar problems."

    if persistent.debug:
        end "You've even stumbled upon the debug mode somehow. Good on ya {noalt};){/noalt}{alt}winking smiley face{/alt}"

    nvl clear

    end "I hope you enjoyed playing {i}[config.name]{/i} as much as I enjoyed making it."

    end "[name] also thanks you eternally for helping [pn[obj]] get through [pn[psv]] journey[temp2]."

    end "You completed [pn[psv]] adventure with [self] self-esteem points over [day] days."

    end "Hopefully, through this adventure, we've all learned a little more about ourselves and the people around us."

    end "With hope, {p}Pyrrhic Silva"

    $ persistent.complete = True

    # This ends the game.

    return

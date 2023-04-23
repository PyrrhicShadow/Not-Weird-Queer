# The script for events that repeat throughout part 2 but with subtle variation

label ch2:

    $ part = 2
    $ day1 = day

    scene bg start day

    play music start

    "Part 2: Choice"

    jump ch2_07

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

# make sure only to call this label, not jump
# when the game gets further along, I might replace the morning loop with unique mornings per day
# but for the time being, every morning in the part 2 "loop" is the same.
label ch2_morning:

    scene bg bedroom

    play music name

    "Morning, day [day]."

    if self > 5:
        "Life is looking up."

        "[name] wonders what adventures life will bring next."

    elif self < 3:
        "So, this is dummy text. Enjoy!"

    else:
        "So, this is dummy text. Enjoy!"

    if loop == 7:
        if gender == "male":
            $ temp0 = "some boys'"

        elif gender == "female":
            $ temp0 = "some girls'"

        else:
            $ temp0 = "both girls' and boys'"

        "[pn[sbj]!c] has [temp0] clothes that [pn[sbj]] had bough on [pn[psv]] own with [pn[psv]] Christmas money."

        "On the other hand, [pn[sbj]] could it safe and just wear a [d_noun]s' outfit."

    menu:
        "[name] looks in [pn[psv]] wardrobe. What should [pn[sbj]] wear today?"

        "[adj] outfit":
            $ outfit = "g"

            jump ch2_morning_gender

        "[d_adj] outfit":
            $ outfit = "d"

            jump ch2_morning_notGender

        "gender neutral outfit" if gender != "enby":
            $ outfit = "n"

            jump ch2_morning_neutral

label ch2_morning_gender:
    $ happy += 1

    $ renpy.show("main " + gender + " " + outfit + " norm")

    if gender == "male":
        if loop == 7:
            $ temp0 = "graphic t-shirt and sweat pants"
        elif loop == 8:
            $ temp0 = "blue t-shirt and basketball shorts"
        elif loop == 9:
            $ temp0 = "long-sleeved polo and jeans"
        else:
            $ temp0 = "black t-shirt and jeans"

    elif gender == "female":
        if loop == 7:
            $ temp0 = "v-neck sweater and red skirt"
        elif loop == 8:
            $ temp0 = "lacy top and skinny jeans"
        elif loop == 9:
            $ temp0 = "denim dress with a flower pin"
        else:
            $ temp0 = "flowy sky-blue dress with pink leggings"

    else:
        $ temp0 = "gender neutral outfit idea"

    "[name] looks in the mirror at [pn[psv]] [temp0]."

    "It's emboldening to be able to dress the way [pn[sbj]] feels on the inside."

    return

label ch2_morning_notGender:
    $ happy -= 1

    $ renpy.show("main " + gender + " " + outfit + " norm")

    if d_gender == "female":
        if loop == 7:
            $ temp0 = "v-neck sweater and red skirt"
        elif loop == 8:
            $ temp0 = "flower-print shirt and skinny jeans"
        elif loop == 9:
            $ temp0 = "denim dress"
        else:
            $ temp0 = "plain white shirt and skirt"

    elif d_gender == "male":
        if loop == 7:
            $ temp0 = "boyish graphic t-shirt"
        elif loop == 8:
            $ temp0 = "long-sleeved polo"
        elif loop == 9:
            $ temp0 = "t-shirt and basketball shorts"
        else:
            $ temp0 = "outfit 4"

    else:
        $ temp0 = dirty_hacker

    "[name] quickly throws on a [temp0] and hurries out to the kitchen."

    "[name] is embarrassed that [pn[sbj]] didn't have to courage to express [pn[psv]] true self."

    return

label ch2_morning_neutral:

    $ renpy.show("main " + gender + " " + outfit + " norm")

    if loop == 7:
        $ temp0 = "gender neutral outfit 1"
    elif loop == 8:
        $ temp0 = "gender neutral outfit 2"
    elif loop == 9:
        $ temp0 = "gender neutral outfit 3"
    else:
        $ temp0 = "gender neutral outfit 4"

    $ verb0 = v(pn, "do", "does")
    "[name] decides that [pn[sbj]] doesn't feel like taking risks today, but [pn[sbj]] also [verb0]n't want to hide [pn[obj]]self."

    $ verb0 = v(pn, "put")
    "[pn[sbj]!c] [verb0] on a [temp0]."

    "[name] figures [pn[sbj]] can always fight another day."

    return

label ch2_bus:

    $ happy += 1
    $ ryan += 1

    scene bg bus

    play music outside

    "[name] gets on the bus and sits with [pn[psv]] friend, [ally]."

    if outfit == "g":
        "[ally] has a supportive reaction to [name]'s outfit."

    elif outfit == "d":
        "[ally] tells [name] to take [pn[psv]] time with things."
    else:
        "[ally] reminds [name] that [pn[sbj]] will always support [name]'s choices."

    "[name] and [ally] talk about stuff on the bus ride."

    scene bg school front

    "The weather's been warming up, and it's a beautiful day outside."

    "Birds are singing, flowers are blooming."

    """On days like these, {w}kids like you {w}should be arriving at school."""

    return

# Cry in the hallway part 2
label  ch2_hallway_cry:

    scene bg school hallway

    stop music

    "[name] stops in the hallway and checks to see that no one else is there."

    if self < 2:
        jump bad_ending

    else:
        $ happy += 1

        "The day's been rough but [name] calms down and makes it through the school day."

        play music school

        if loop == 8:
            jump ch2_08_art

        elif loop == 10:
            jump ch2_club

        else:
            call dirty_hacker
            jump ch2_home

# club part 2
label ch2_club:

    scene bg club front

    "[name] and [ally] go to the afterschool book club."

    if loop == 7:
        $ temp0 = "day 1 topic"
    elif loop == 8:
        $ temp0 = "day 2 topic"
    elif loop == 9:
        $ temp0 = "day 3 topic"
    else:
        $ temp0 = "day 4 topic"

    "[name] writes a story about [temp0]."

    "When [pn[sbj]] showes [ally], [pn[sbj]] tells [name] that it's really good and that other people will like it."

    "Soon, it's time for everyone to share their writing."

    if loop == 7 and (day == day1 + 1):
        jump ch2_07_club_story

    elif loop == 8 and (day == day1 + 2):
        jump ch2_08_club_story

    elif actn > 5:
        jump ch2_10_club_story

    else:
        jump ch2_club_share

label ch2_club_share:

    $ renpy.show("name " + gender + " " + outfit + " norm")

    "[name] shares [pn[psv]] story with the club. The other club memebers loved [pn[psv]] story."

    jump ch2_home

label ch2_home:

    scene bg school front

    play music outside

    if loop == 7:
        $ temp0 = "chat topic 1"
    elif loop == 8:
        $ temp0 = "chat topic 2"
    elif loop == 9:
        $ temp0 = "chat topic 3"
    else:
        $ temp0 = "chat topic 4"

    "After the club meeting, [name] and [ally] chat a little about [temp0] while walking home."

    if happy < 0:
        $ self -= 1

    elif happy > 1:
        $ self += 1

    $ last_happy = happy
    $ happy = 0
    $ share = False

    if self < 2:
        jump bad_ending

    else:
        if last_happy > 2:
            "The day was pretty good."

            "Hopefully, tomorrow will go well, too."

        elif last_happy < 0:
            $ verb0 = v(pn, "have", "has")
            "The day was a rough one, but nothing [pn[sbj]] [verb0]n't seen before."

        else:
            "The day was an okay one."

            "There was more that [name] wanted to do, but there will be another chance tomorrow."

    "[name] is ready to start a new day."

    if actn > 5:
        jump ch2_11
    else:
        if loop == 7:
            jump ch2_08

        elif loop == 8:
            jump ch2_09

        elif loop == 9:
            jump ch2_10

        elif loop == 10:
            jump ch2_07

        else:
            call dirty_hacker
            jump restart

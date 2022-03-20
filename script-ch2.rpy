# The script for events that repeat throughout part 2 but with subtle variation

label ch2:

    $ part = 2
    $ day1 = day

    scene bg start day

    "Part 2: Choice"

    jump ch2_07

# make sure only to call this label, not jump
# when the game gets further along, I might replace the morning loop with unique mornings per day
# but for the time being, every morning in the part 2 "loop" is the same.
label ch2_morning:

    scene bg bedroom

    "Morning, day [day]."

    if self > 5:
        "Life is looking up. [name] wonders what adventures life will bring next."

    if loop == 7:
        if gender == "male":
            $ temp1 = "some boys'"

        elif gender == "female":
            $ temp1 = "some girls'"

        else:
            $ temp1 = "both girls' and boys'"

        "[N_sbj] has [temp1] clothes that [n_sbj] had bough on [n_pos] own with [n_pos] Christmas money."

        "On the other hand, [n_sbj] could it safe and just wear a [d_noun]s' outfit."

    menu:
        "[name] looks in [n_pos] wardrobe. What should [n_sbj] wear today?"

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
            $ temp1 = "graphic t-shirt and sweat pants"
        elif loop == 8:
            $ temp1 = "blue t-shirt and basketball shorts"
        elif loop == 9:
            $ temp1 = "long-sleeved polo and jeans"
        else:
            $ temp1 = "black t-shirt and jeans"

    elif gender == "female":
        if loop == 7:
            $ temp1 = "v-neck sweater and red skirt"
        elif loop == 8:
            $ temp1 = "lacy top and skinny jeans"
        elif loop == 9:
            $ temp1 = "denim dress with a flower pin"
        else:
            $ temp1 = "flowy sky-blue dress with pink leggings"

    else:
        $ temp1 = "gender neutral outfit idea"

    "$name looks in the mirror at $pos [temp1]."

    "It's emboldening to be able to dress the way $sbj feels on the inside."

    return

label ch2_morning_notGender:
    $ happy -= 1

    $ renpy.show("main " + gender + " " + outfit + " norm")

    if d_gender == "female":
        if loop == 7:
            $ temp1 = "v-neck sweater and red skirt"
        elif loop == 8:
            $ temp1 = "flower-print shirt and skinny jeans"
        elif loop == 9:
            $ temp1 = "denim dress"
        else:
            $ temp1 = "plain white shirt and skirt"

    elif d_gender == "male":
        if loop == 7:
            $ temp1 = "boyish graphic t-shirt"
        elif loop == 8:
            $ temp1 = "long-sleeved polo"
        elif loop == 9:
            $ temp1 = "t-shirt and basketball shorts"
        else:
            $ temp1 = "outfit 4"

    else:
        $ temp1 = dirty_hacker

    "[name] quickly throws on a [temp1] and hurries out to the kitchen."

    "[name] is embarrassed that [n_sbj] didn't have to courage to express [n_pos] true self."

    return

label ch2_morning_neutral:

    $ renpy.show("main " + gender + " " + outfit + " norm")

    if loop == 7:
        $ temp1 = "gender neutral outfit 1"
    elif loop == 8:
        $ temp1 = "gender neutral outfit 2"
    elif loop == 9:
        $ temp1 = "gender neutral outfit 3"
    else:
        $ temp1 = "gender neutral outfit 4"

    $ verb = v("do", "does")

    "[name] decides that [n_sbj] doesn't feel like taking risks today, but [n_sbj] also [verb]n't want to hide [n_obj]self."

    $ verb = v("put")

    "[N_sbj] [verb] on a [temp1]."

    "[name] figures [n_sbj] can always fight another day."

    return

label ch2_bus:

    $ happy += 1
    $ ryan += 1

    scene bg bus

    "[name] gets on the bus and sits with [n_pos] friend, [ally]."

    if outfit == "g":
        "[ally] has a supportive reaction to [name]'s outfit."

    elif outfit == "d":
        "[ally] tells [name] to take [n_pos] time with things."
    else:
        "[ally] reminds [name] that [n_sbj] will always support [name]'s choices."

    "[name] and [ally] talk about stuff on the bus ride."

    scene bg school front

    "The weather's been warming up, and it's a beautiful day outside."

    "Birds are singing, flowers are blooming."

    """On days like these,

    kids like you

    should be arriving at school."""

    return

label ch2_club:

    scene bg club front

    "$name and $ally go to the afterschool book club."

    if loop == 7:
        $ temp1 = "day 1 topic"
    elif loop == 8:
        $ temp1 = "day 2 topic"
    elif loop == 9:
        $ temp1 = "day 3 topic"
    else:
        $ temp1 = "day 4 topic"


    "[name] writes a story about [temp1]."

    "When [n_sbj] showes [ally], $sbj tells $name that it's really good and that other people will like it."

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

    "[name] shares [n_pos] story with the club. The other club memebers loved [n_pos] story."

    jump ch2_home

label ch2_home:

    scene bg school street

    if loop == 7:
        $ temp1 = "chat topic 1"
    elif loop == 8:
        $ temp1 = "chat topic 2"
    elif loop == 9:
        $ temp1 = "chat topic 3"
    else:
        $ temp1 = "chat topic 4"

    "After the club meeting, $name and $ally chat a little about [temp1] while walking home."

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

        elif lasthappy < 0:
            $ verb = v("have", "has")

            "The day was a rough one, but nothing [n_sbj] [verb]n't seen before."

        else:
            "The day was an okay one."

            "There was more that [name] wanted to do, but there will be another chance tomorrow."

    "[name] is ready to start a new day."

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    if action > 5:
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

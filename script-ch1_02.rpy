# The script for part 1 day 2 (technically loop 2)

label ch1_02:

    $ loop = 2
    $ day += 1

    scene bg start day

    "Morning, day [day]."

    scene bg bedroom

    "The next morning rolls around."

    if self < 0:
        jump ch1_02_morning_sad
    elif self > 0:
        jump ch1_02_morning_happy
    else:
        jump ch1_02_morning_neutral

label ch1_02_morning_happy:

    "[name] was awake before [n_pos] alarm rang so [n_sbj] had time to make [n_obj]self breakfast without being late for the bus."

    "[name] picked a vaguely [adj] outfit and made a sandwich for lunch."

    scene bg kitchen

    jump ch1_02_kitchen

label ch1_02_morning_neutral:

    "[name] hit snooze on [n_pos] alarm clock twice before jumping out of bed."

    "[name] picked out a gender-neutral outfit and made it out the door on time, but only because [n_sbj] skipped breakfast."

    scene bg kitchen

    jump ch1_02_kitchen

label ch1_02_morning_sad:

    "[name] had overselpt again. Hastily, [n_sbj] throws on a [d_adj] outfit and combs through [n_pos] unruly hair."

    scene bg kitchen

    "While rushing through the door, [n_pos] mom chides [n_obj] about oversleeping all the time."

    jump ch1_02_kitchen

label ch1_02_kitchen:

    show mom norm

    mom norm "Have a good day at school, [d_name]."

    "Of course, [n_pos] mom called [n_obj] \"[d_name]\" again."

    "Even though it was annoying, [name] isn't really sure there's anything [n_sbj] could do about it."

    n norm smile "Thanks, Mom. Love you."

    mom "Love you, too, sweetie."

    call ch1_bus

# biology class part 1

    scene bg classroom biology

    if day > 2:
        $ temp1 = "still "
    else:
        $ temp1 = ""

    "[name] goes to [n_pos] biology class.  The teacher, [bioTeach] is[temp1] lecturing about parts of flowers."

    n_self "Flower genders are weird."

    $ temp2 = renpy.random.choice(["anthers", "pistils", "sepals"])

    show teacher boy

    "[bioTeach] asks a question about flower [temp2]."

    "[name] knows the answer. What should [n_sbj] do?"

    if ryan > 1:
        $ temp1 = "friend"
    else:
        $ temp1 = "classmate"

    menu:
        "Raise [n_pos] hand":
            jump ch1_02_bio_answer
        "Whisper to [n_pos] [temp1], [ally]":
            jump ch1_02_bio_ryan
        "Do nothing":
            jump ch1_02_bio_nothing

label ch1_02_bio_answer:

    bio boy "[d_name]?"

    "Cringing, [name] answers the question about [temp2]."

    bio "Correct."

    "[name] zones out for the rest of the class period."

    jump ch1_02_bio

label ch1_02_bio_ryan:

    $ ryan += 1

    hide teacher

    "[name] whispers to [n_pos] [temp1], [ally]."

    n norm smile "Don't you think it's weird that flowers can be both genders at the same time?"

    show ally norm smile

    if ryan > 0:
        $ happy += 1
        $ renpy.say(a, "Yeah, definitely.")
        $ renpy.say(n, "Sometimes, I wish people could be flexible like that, too.")
        $ renpy.say("[ally] smiles.")
        $ renpy.say(n_self, "Maybe I've made a friend.")
    else:
        $ renpy.say("[ally] nods mildly.")
        $ renpy.say("[name] feels awkward, looks away, and drops the subject.")

    jump ch1_02_bio

label ch1_02_bio_nothing:

    if day == 2:
        $ temp3 = "[ally]"
    else:
        $ temp3 = renpy.random.choice(["Becky", "Peter", "Josh", "Chara"])

    "[name] stares out the window as [temp3] answers the question."

    "Although [name] knew the answer, [n_sbj] was too embarrassed to answer."

    "Maybe next time."

    jump ch1_02_bio

label ch1_02_bio:

    "Soon, it's time for lunch."

    scene bg lunchroom lunch

    "Lunchtime."

    jump tbc

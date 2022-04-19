# The script for events that repeat throughout part 1 but with subtle variation

label ch1:

    $ part = 1
    $ loop = 0
    $ day = 0

    scene bg start day

    "Part 1: Discovery"

    jump ch1_01

# make sure only to call this label, not jump
# when the game gets further along, I might replace the morning loop with unique mornings per day
# but for the time being, every morning in the part 1 "loop" is the same.
label ch1_morning:

    scene bg bedroom

    play music name

    "Morning, day [day]."

    if self < 0:
        $ outfit = "d"

        jump ch1_morning_sad

    elif self > 0:
        $ outfit = "g"

        jump ch1_morning_happy

    else:
        if gender == "enby":
            $ outfit = "d"
        else:
            $ outfit = "n"

        jump ch1_morning_neutral

label ch1_morning_happy:

    $ renpy.show("main " + gender + " " + outfit + " norm")
    $ verb = v(pn, "has")

    "[name] is awake before [pn[psv]] alarm rang so [pn[sbj]] [verb] time to make [pn[obj]]self breakfast without being late for the bus."

    $ verb = v(pn, "pick")

    "[pn[sbj]!c] picks a vaguely [adj] outfit and makes a sandwich for lunch."

    scene bg kitchen

    jump ch1_kitchen

label ch1_morning_neutral:

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] hits snooze on [pn[psv]] alarm clock twice before jumping out of bed."

    $ verb = v(pn, "pick")
    $ verb1 = v(pn, "make")

    "[pn[sbj]!c] [verb] out a gender neutral outfit and [verb1] it out the door on time, but only because [pn[sbj]] skipped breakfast."

    scene bg kitchen

    jump ch1_kitchen

label ch1_morning_sad:

    $ renpy.show("main " + gender + " " + outfit + " norm")
    $ verb = v(pn, "throw")
    $ verb1 = v(pn, "comb")

    "[name] had overselpt again. Hastily, [pn[sbj]] [verb] on a [d_adj] outfit and [verb] through [pn[psv]] unruly hair."

    scene bg kitchen

    "While rushing through the door, [pn[psv]] mom chides [pn[obj]] about oversleeping all the time."

    jump ch1_kitchen

label ch1_kitchen:

    show mom norm

    mom "Have a good day at school, [d_name]."

    n norm "Thanks, Mom. Love you."

    mom "Love you, too, sweetie."

    hide mom

    "Of course, [pn[psv]] mom called [pn[obj]] \"[d_name]\" again."

    "Even though it was annoying, [name] isn't really sure there's anything [pn[sbj]] could do about it."

    return

# make sure only to call this label, not jump
label ch1_bus:

    scene bg bus

    play music outside

    "[name] walks to the bus stop and gets on the next bus."

    if ryan == 0 and day > 2:
        jump ch1_bus_ryan

    else:

        if ryan == 0:
            $ temp1 = "classmate"
        else:
            $ temp1 = "friend"

        menu:
            "There are three open seats left."

            "Sit with [pn[psv]] [temp1], [ally]":
                $ happy += 1
                $ ryan += 1
                $ bus = True
                jump ch1_bus_ryan

            "Sit with a stranger":
                jump ch1_bus_stranger

            "Sit alone":
                $ happy -= 1
                jump ch1_bus_alone

label ch1_bus_ryan:

    if ryan > 1:
        $ temp1 = "friend"
    else:
        $ temp1 = "classmate"

    "[name] sits with [pn[psv]] [temp1], [ally]."

    if ryan > 1:
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
        if loop == 2:
            call ch1_bus_ryan_art

        elif loop == 3:
            call ch1_bus_ryan_cat

        elif loop == 4:
            call ch1_bus_ryan_insight

        elif loop == 5:
            call ch1_bus_ryan_math

    else:
        call ch1_bus_ryan_new

    return

label ch1_bus_ryan_classmate:

    "The two make small talk as the bus begins its way towards the middle school."

    "Since [ally] thinks [name]'s name is \"[d_name]\", [pa[sbj]] thinks [name]'s a [d_noun]."

    "[name] doesn't bother to correct [pa[obj]]. This happens all the time."

    "[ally] seems like a cool person otherwise."

    return

label ch1_bus_ryan_new:

    "[name] and [ally] make small talk on the way to school."

    return

label ch1_bus_ryan_cat:

    "[name] laughs as [ally] talks about [pa[psv]] adorable cat, Randle."

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
        "[name] decided not to bother [ally] with [pn[psv]] problems today."

    n norm "Hey."

    $ renpy.show("extra " + a_gender + " norm")

    "The stranger looks at [name] and nods back without saying anything more."

    hide extra

    "[name] stares out the window as [pn[sbj]] thinks about [pn[psv]] homework."

    n_self "Another day, another awkward day."

    jump ch1_school

label ch1_bus_alone:

    $ temp1 = renpy.random.choice(["English", "biology", "art", "math", "history"])

    if ryan > 1:
        "[name] decided not to bother [ally] with [pn[psv]] problems today."

    "[name] stares out the window as [pn[sbj]] thinks about [pn[psv]] [temp1] homework."

    n_self "Another day, another lonely day."

    jump ch1_school

label ch1_school:

    scene bg school front

    if bus:

        $ temp1 = " " + ally
        if ryan > 2:
            $ temp2 = " with"
        else:
            $ temp2 = " behind"
    else:

        $ temp1 = ""
        $ temp2 = ""

    if self > 1:
        $ temp3 = "notices that flowers of multiple colors and varieties are in bloom"
    elif self < 0:
        $ temp3 = "is annoyed to be at school again but whatever"
    else:
        $ verb = v(pn, "worry", "worries")
        $ temp3 = verb + " about the upcoming hay fever season"

    "As [name] walks to middle school[temp2][temp1], [pn[sbj]] [temp3]."

    return

# Cry in the hallway part 1
label ch1_hallway_cry:

    scene bg school hallway

    stop music

    "[name] stops in the hallway and checks to see that no one else is there."

    if self < -2:
        jump bad_ending

    else:
        $ happy += 1

        "The day's been rough but [name] calms down and makes it through the school day."

        play music school

        jump ch1_club

label ch1_club:

    if club:
        $ temp1 = " with " + ally
        $ temp2 = " next to " + ally
    else:
        $ temp1 = ""
        $ temp2 = ""

    scene bg club front

    "After school, [name] goes to the middle school book club[temp1]."

    $ verb = v(pn, "begin")

    "[name] sits down[temp2]. As usual, [pn[sbj]] [verb] writing."

    if happy > 2:
        $ temp2 = "a short story about "

        if gender == "male":
            if loop == 2:
                $ temp2 = temp2 + "his favorite taco place downtown"

            elif loop == 3:
                $ temp2 = temp2 + "a PewDiePie Let's Play"

            elif loop == 4:
                $ temp2 = temp2 + "male idea 4"

            else:
                $ temp2 = temp2 + "his Hotwheels collection"

        elif gender == "female":
            if loop == 2:
                $ temp2 = temp2 + "her neighbor's new kittens"

            elif loop == 3:
                $ temp2 = temp2 + "a sentient Pintrest board"

            elif loop == 4:
                $ temp2 = temp2 + "female idea 4"

            else:
                $ temp2 = temp2 + "the color chartreuse"

        else:
            if loop == 2:
                $ temp2 = temp2 + "gender neutral idea 1"

            elif loop == 3:
                $ temp2 = temp2 + "gender neutral idea 2"

            elif loop == 4:
                $ temp2 = temp2 + "gender neutral idea 4"

            else:
                $ temp2 = temp2 + "gender neutral idea 3"
    else:
        $ temp2 = "a poem "

        if happy < 1:
            $ temp2 = temp2 + "about knives"

            if self < -1:
                $ temp2 = temp2 + ". All the knives"
        else:
            $ temp2 = temp2 + "metaphorically describing "

            if loop == 2:
                $ temp2 = temp2 + "a heated argument"

            elif loop == 3:
                $ temp2 = temp2 + "the bottom of a well"

            else:
                $ temp2 = temp2 + "the darkness in space"

    "Today, [name] is writing [temp2]."

    "Soon, it is time for everyone to share their pieces of writing."

    if talk:
        jump ch1_05_club_share
    else:
        jump ch1_club_share

label ch1_club_share:

    menu:
        "The book club president asks if there are any volunteers. [name] looks down at [pn[psv]] story."

        "Share [name]'s story":
            if club:
                jump ch1_club_share_ryan

            else:
                jump ch1_club_share_alone

        "Do nothing":
            if club:
                jump ch1_club_nothing_ryan

            else:
                jump ch1_club_nothing_alone

label ch1_club_share_ryan:

    $ happy += 1

    if share:
        call ch1_club_share_ryan_again
    else:
        call ch1_club_share_ryan_first

    scene bg club front

    if club:
        $ temp1 = " and " + ally
    else:
        $ temp1 = ""

    if loop % 2 == 0:
        show extra male norm
    else:
        show extra female norm

    "Some of the other club members share their stories. [name][temp1] snap after each one."

    hide extra

    "Soon, it's time to go home."

    jump ch1_home

label ch1_club_share_ryan_again:

    scene bg club sharing

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] shares [pn[psv]] story in front of the clubroom and the other club members snap enthusiastically."

    hide main
    $ renpy.show("ally " + a_gender + " smile")

    a "You did a great job!"

    n norm "Thanks."

    hide ally

    return

label ch1_club_share_ryan_first:

    $ share = True

    "[name] quietly shares [pn[psv]] story with just [ally]."

    $ renpy.show("ally " + a_gender + " norm")

    a "That's really good. You should share it with the class."

    "[name] shrugs."

    n norm "Maybe next time."

    return

label ch1_club_nothing_ryan:

    $ renpy.show("ally " + a_gender + " norm")

    a "Are you gonna share?"

    "[name] shrugs."

    n norm "Maybe next time."

    a "Can I see?"

    "[name] hands [pn[psv]] writing to [ally]."

    a "This is really good!"

    n "Thanks."

    a "Why don't you share it with the club?"

    if self < 1:
        $ temp1 = "I guess I'm not that confident."

    n "I don't know. [temp1]"

    a "It's really good. You should share it next time, okay? I think they'll love it."

    n "Okay. Maybe next time."

    "[name] wishes [pn[sbj]] had the courage to share this story with the rest of the club."

    "Maybe the next one."

    "Soon, it's time to go home."

    jump ch1_home

label ch1_club_share_alone:

    $ happy +=1

    scene bg club sharing

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] shares [pn[psv]] poem with the club."

    if self < 0:
        $ temp1 = "start to "
    else:
        $ temp1 = ""
    if happy < 0:
        $ temp2 = " quietly after an awkward silence"
    else:
        $ temp2 = ""
    if (self > -1) and (happy > -1):
        $ temp3 = " for " + pn["obj"]
    else:
        $ temp3 = ""

    "The other members [temp1]snap[temp2][temp3]."

    hide main

    "After a few more club members share their writing, it's time to go home."

    jump ch1_home

label ch1_club_nothing_alone:

    $ happy -= 1

    "[name] stares at [pn[psv]] poem."

    "Embarrassed, [pn[sbj]] feels angry at [pn[obj]]self for not having the courage to share, but it's too late to do anything about it."

    "After a few of the other club members share their stories, it's time to go home."

    jump ch1_home

label ch1_home:

    scene bg school front

    play music outside

    if club:
        call ch1_home_club

    if happy < 0:
        $ self -= 1
    elif (happy > 2) and (self < 5):
        $ self += 1
    else:
        $ self = self
    $ last_happy = happy
    $ happy = 0
    $ bus = False

    if self < -2:
        jump bad_ending
    else:
        jump ch1_home_alive

label ch1_home_club:

    $ happy += 1

    "Before they part ways, [ally] pulls [name] aside."

    $ renpy.show("ally " + a_gender + " norm")

    if ryan > 4:
        a "Remember, you're super awesome, [d_name]."

    else:
        a "Remember, if you ever need to talk, I'm here for you, [d_name]."

    "Although it hurts to hear [pn[psv]] friend call [pn[obj]] by that name, the sentiment is still appreciated."

    "After all, [name] knows [ally] doesn't know any better."

    n norm "Thanks, [ally]."

    hide ally

    return

label ch1_home_alive:

    scene bg day end

    if last_happy > 2:
        "The day surprisingly didn't suck. Hopefully, tomorrow won't suck, either."
    elif last_happy < 0:
        "The day was a rough one, but nothing [pn[sbj]] hasn't seen before."
    else:
        "The day was fine. Nothing noteworthy. Tomorrow will be another."

    "[name] is ready to start a new day."

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    if loop == 2:
        jump ch1_03

    elif loop == 3:
        jump ch1_04

    elif loop == 4:
        jump ch1_05

    elif loop == 5:
        jump ch1_02

    else:
        call dirty_hacker
        jump restart

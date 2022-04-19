# The script for part 1 day 7 (technically loop 7)

label ch2_07:

    $ loop = 7
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# biology class day 7

    scene bg classroom biology

    play music school

    $ defbio = False

    if day == (day1 + 1):
        $ bioteam = "Issac"
        $ temp1 = "a flower anatomy poster"
    elif day == (day + 5):
        $ bioteam = "Evan"
        $ temp1 = "discecting and labeling a flower"
    else:
        $ bioteam = "Luke"
        $ temp1 = "a flower anatomy study guide"

    if bioteam.lower() == name.lower():
        $ bioteam = bioteam + " C"

    "[name] and [ally] head to biology class."

    show teacher bio

    "[bioTeach] announces that today, to finish off flower anatomy, the class will be starting group projects."

    "[name] groans. Group projects are the worst."

    hide teacher

    "[name] and [ally] form a team of 3 with their classmate [bioteam]."

    "The three are working on [temp1]."

    $ renpy.show("ally " + a_gender + " norm")

    "[ally] addresses [name] by [pn[psv]] correct pronouns and [bioteam] gets confused."

    if day == (day1 + 1):
        show bioteam 1 at left

        b "Wait, did you get that wrong?"

    elif day == (day1 + 5):
        show bioteam 2 at left

        b "Wait, did you get that wrong?"

    else:
        show bioteam 3 at left
        b "Wait, did you get that wrong?"

    a "Uh…"

    menu:
        "What should [name] do?"

        "Explain to [bioteam] that [name] uses [pn[pn]] pronouns":
            jump ch2_07_bio_explain

        "Tell [bioteam] not to worry about it":
            jump ch2_07_bio_ignore

label ch2_07_bio_explain:

    $ defbio = True

    "[name] explains to [bioteam] that [pn[sbj]] prefers [pn[pn]] pronouns."

    if outfit == "g":
        $ actn += 1.5

        "[bioteam] thinks that's cool, and uses the correct pronouns for [name] for the rest of the class period."

    elif outfit == "d":
        $ actn += 0.5

        "[bioteam] is a little confused by this, and stumbles over [name]'s pronouns for the rest of the class period."

    else:
        $ actn += 1

        "[bioteam] thinks that's interesting, and mostly uses the correct pronouns for [name] for the rest of the class period."

    jump ch2_07_ryan_apologizes


label ch2_07_bio_ignore:

    "[name] feels awkward about it, so [pn[sbj]] not to explain anything to [bioteam]."

    n norm "Oh, don't worry about it, [bioteam]."

    "[bioteam] frowns but doesn't say anything more."

    "[ally] almost seems disapointed, but [name] can't tell if [pn[sbj]]'s imagining it."

    if outfit == "d":
        $ actn -= 1
        $ happy -= 1

    elif outfit == "n":
        $ actn -= 0.5

    jump ch2_07_ryan_apologizes


label ch2_07_ryan_apologizes:

    $ ryan += 1

    "Regardless, the three continue to work on their poster."

    scene bg school hallway

    "[ally] pulls [name] aside before they have to get to their next class."

    $ renpy.show("ally " + a_gender + " norm")

    a "Hey, [name], I'm sorry about putting you on the spot there."

    n norm "It wasn't your fault, [ally]. It's nice of you to apologize, though."

    a "Well, it just doesn't feel right to expose you like that. I'll try to remember next time."

    if not defbio:
        $ temp1 = "I was just nervous just now, but "
    else:
        $ temp1 = ""

    n "I mean, [temp1]I should be acting more like myself, right?"

    n "If I'm not afraid to be a [noun], then you won't have to watch yourself."

    a "Well, you should do it on your terms. Anyway, see you at lunch!"

    "[name] says goodbye to [ally] and heads to [pn[psv]] next class."

# history class day 7

    scene bg classroom history

    if day == (day1 + 1):
        $ temp1 = "playing a movie about the American Revolution"

    else:
        $ temp1 = "lecturing about the Articles of Confederation"

    "Today in history class, [histTeach] is [temp1]."

    if gender == "male":
        $ temp1 = "the perfect fps arsenal"

    elif gender == "female":
        $ temp1 = "finding the perfect shade of purple"

    else:
        $ temp1 = "cheddar cheese and frozen mice"

    "[name] writes a poem about [temp1] in [pn[psv]] notebook."

    n_self "History class is so boring."

    "Lunch can't come soon enough."

# lunch day 7

    scene bg gym lunch

    "[name] hangs out with [ally] at lunch."

    "As [ally] takes a bite of [pn[psv]] cafeteria sloppy joe, [name] hesitantly decides to ask [pn[obj]] a question."

    play music ally

    n norm "Hey, [ally]. Why did you, um, want to be my friend?"

    "[ally] sets down [pa[psv]] messy sandwich."

    a"When I moved here, I left everything behind. Sure, the kids at my old school were pricks, but I had friends, too."

    a "I didn't have anything here."

    n "Oh."

    a """But then I saw you on the bus, the quiet kid from art class with those deep, introspective sculptures. You reminded me of my old friends.

    I thought if I could just get you to talk to me, you'd see that I was an interesting person.

    Then, maybe, I wouldn't be so lonely anymore."""

    n "You are an interesting person, [ally]."

    $ renpy.show("ally " + a_gender + " smile")

    a "Yeah, but you're like way cooler. You're so good at writing. And don't get me started on your art!"

    n "Stop teasing me!"

    a "I'm not teasing you! You've got to show me some of your other writing sometime."

    n "Okay, I will, but only if you don't make such a big fuss about it."

    a "I only say it's good because it is good."

    n "Well, I think your writing is really good, and you don't believe me."

    a "Touché, [name]. Touché."

    play music school

    jump ch2_club

label ch2_07_club_story:

    show extra male norm

    cp "Hello, club. Writing time is over."

    cp "Have we got any brave volunteers for sharing today?"

    "[name] looks down at [pn[psv]] story."

    menu:
        "What should [name] do?"

        "Share [pn[psv]] story":
            jump ch2_07_club_share

        "Do nothing":
            jump ch2_07_club_nothing

label ch2_07_club_share:

    $ happy += 1
    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] shares [pn[psv]] story and the other club members snap enthusiastically."

    hide main
    show extra male norm

    cp "That was really good, [d_name]."

    cp "Who wants to go next?"

    hide extra
    $ renpy.show("ally " + a_gender + " smile", at_list=[right])

    a "[name], you did great. That was amazing!"

    n "Thanks."

    jump ch2_home

label ch2_07_club_nothing:

    $ happy -= 1

    "[ally] asks [name] what [pn[sbj]] wrote, so [name] shares [pn[psv]] story with just [ally]."

    "[ally] tells [name] that [pn[psv]] writing is really good."

    a "Why don't you share it with the club?"

    n "I don't know. I guess I could."

    a "It's really good. You should share it next time, okay? I think they'll love it."

    n "Okay. Maybe next time."

    "[name] decides that next time, [pn[sbj]] has to share [pn[psv]] story, if only for [ally]'s sake."

    jump ch2_home

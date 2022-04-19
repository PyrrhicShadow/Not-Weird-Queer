# The script for part 1 day 10 (technically loop 10)

label ch2_10:

    $ loop = 10
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# math class day 10

    scene bg classroom math

    "[name] heads to math class."

    "Today, they're just catching up on past assignments. [name] decides to do tonight's homework."

    "[name]'s sitting next to [mathBud], a [noun] that [name] had gone to elementary school with."

    "Though they don't know each other that well, [name] has always had a fairly positive opinion of [mathBud]."

    if day == (day1 + 4):
        jump ch2_10_math_art

    else:
        jump ch2_10_math_chat

label ch2_10_math_art:

    m "Hey, [d_name]"

    "[name] turns to look at them."

    n norm"Yeah?"

    m "I saw your last sculpture on [artTeach]'s new art display. I thought your sculpture looked really amazing."

    m "Oh, I have her for drawing class. That's how I saw it. Quite eyecatching, I'd say."

    n "Oh, thank you, [mathBud]."

    if gender == "male":
        $ temp1 = "shapes"

    elif gender == "female":
        $ temp1 = "colors"

    else:
        $ temp1 = "shapes and colors"

    m "Oh, no need to thank me. You capture this feeling of darkness really well, even though the [temp1] you used weren't dark at all."

    menu:
        "[name] feels proud of [pn[psv]] sculpture. Should [pn[psv]] explain their art to [mathBud]"

        "Explain [name]'s personal connection to [pn[psv]] sculpture":
            jump ch2_10_math_explain

        "Play off [name]'s scuplture as inspired by a good book":
            jump ch2_10_math_notExplain

label ch2_10_math_explain:

    $ happy += 1

    if gender == "male":
        $ temp1 = "masculine"

    elif gender == "female":
        $ temp1 = "feminine"

    else:
        $ temp1 = "gender-ambiguous"

    "[name] decides to explain to [mathBud] the personal significance of the [temp1] pain depicted in [pn[psv]] sculpture."

    n "And that's why I've decided to go as '[name]' now."

    if outfit == "g":
        $ actn += 1.5

        m "Oh, that makes a lot of sense. It's pretty cool that you see yourself as a [noun]."

        n "Oh, yeah?"

        m "Well, keep being you, [name]. Everyone else is taken, right?"

        "[name] smiles."

        n "Yeah."

    elif outfit == "d":
        $ actn += 0.5

        m "So, you see yourself as a [noun]?"

        n "Yeah."

        m "Well, I guess that's cool. You do you."

        n "Yeah."

    else:
        $ actn += 1

        m "Oh, that's really cool. I didn't know that you saw yourself as a [noun]."

        n "Oh, yeah."

        m "Well, keep being you, [name]. If you're not you, then who is?"

        "[name] smiles."

        n "Yeah."

    m "Anyway, don't ever stop making art. You've got a good eye."

    n "Thanks, [mathBud]."

    "[name] is surprised at how [mathBud] reacts to [pn[psv]] art. [mathBud] is actually a pretty cool person."

    jump ch2_10_lunch

label ch2_10_math_notExplain:

    "[name] tells [mathBud] that [pn[sbj]] was inspired by this book that [pn[sbj]] recently read. [mathBud] isn't really into books, but [pa[sbj]] agrees that that book sounds cool."

    m "Anyway, don't ever stop making art. You've got a good eye."

    n "Thanks, [mathBud]."

    "[name] wonders how [mathBud] would've reacted to [name]'s gender, but quickly dismisses the thought."

    "Not every interaction is a challenge to one's gender, and sometimes, it's okay to take a break and just live."

    jump ch2_10_lunch

label ch2_10_math_chat:

    "[mathBud] and [name] talk about the apparent weirdness of [artTeach]."

    "It turns out [mathBud] is actually a pretty funny person."

    jump ch2_10_lunch

# lunch day 10

label ch2_10_lunch:

    scene bg gym lunch

    "[name] starts out lunch with [ally] and they hang out as much as they can while eating as [ally] has to work on [pa[psv]] group project during the lunch period."

    n "Good luck."

    "[ally] laughs."

    a "I'm gonna need it."

    "[ally] throws their lunch tray away and leaves to work on [pa[psv]] project."

    scene bg field lunch

    "[name] heads out to the field and wanders alone in the quiet landscape, thinking."

    if day == (day1 + 4):
        jump ch2_10_lunch_popkid

    else:
        jump ch2_10_lunch_wander

label ch2_10_lunch_popkid:

    $ happy -= 1

    "After a bit, [pn[sbj]] runs into [pn[psv]] classmate [popKid]."

    "They had gone to the same elementary school, but rarely talked since [popKid] mostly hung out with the \"popular\" kids."

    "It was strange to see [pd[sbj]] out in the field, alone."

    if outfit == "d":
        $ happy -= 1

        if d_gender == "female":
            $ temp1 = "really pretty"

        elif d_gender == "male":
            $ temp1 = "badass and manly"

        "[popKid] compliments [name]'s outfit for being [temp1]."

        "[name] tries to take [popKid]'s words as a compliment the best [pn[sbj]] can even though it makes [pn[obj]] feel angry about [pn[obj]]self."

    else:
        "[popKid] asks [name] about [pn[psv]] odd outfit."

        "Before [name] can reply, [popKid] asks why [name] can't just pretend to be a [d_noun]."

        "[name] genuinely thinks about it for a moment and plainly tells [popKid] that [pn[sbj]] can't because [pn[sbj]]'s a [noun]."

        p "Interesting."

        "[popKid] walks away."

        jump ch2_10_english

label ch2_10_lunch_wander:

    "The weather is nice and [pn[sbj]] brainstorms an idea for the book club before the bell rings for the end of lunch period."

    jump ch2_10_english

# English class day 10

label ch2_10_english:

    scene bg classroom english

    "[name] heads to English class."

    if defEng:
        $ temp1 = "still "

    else:
        $ temp1 = ""

    "[engTeach] [temp1]refers to [pn[obj]] as a [d_noun]."

    if defEng:
        menu:
            "Should [name] correct him again?"

            "Yes, and get angry":
                jump ch2_10_english_angry

            "Yes, but stay calm":
                jump ch2_10_english_calm

            "No, do nothing":
                jump ch2_10_english_nothing

    else:
        menu:
            "Should [name] correct him?"

            "Defend [name]'s gender":
                jump ch2_10_english_calm

            "Do nothing":
                jump ch2_10_english_nothing

label ch2_10_english_calm:

    $ happy += 1

    if outfit == "g":
        $ actn += 1.5

    elif outfit == "d":
        $ actn += 0.5

    else:
        $ actn += 1

    if defEng:
        $ temp1 = " once again"

    else:
        $ temp1 = ""

    "[name] explains[temp1] that [pn[psv]] is a [noun] and uses {noalt}[pn[pn]]{/noalt}{alt}[pn[sbj]] [pn[obj]]{/alt} pronouns."

    "Getting people to repsepct [name]'s gender is an uphill battle, but calm and collected is the way to win the war."

    jump ch2_club

label ch2_10_english_angry:

    if outfit == "g":
        $ actn += 0.5
        $ happy += 1

    elif outfit = "d":
        $ actn -= 0.5

    n "I told you that I'm a $noun. Do you even bother to listen, [engTeach]?"

    eng "Oh, there you go on again with that irrelivent gender stuff."

    n "It's-{w} It's not irrelivent, it's about respect, {w}just like all that respect stuff you've been talking about all year!"

    if gender == "male":
        $ temp1 = "Mister"

    elif gender == "female":
        $ temp1 = "Miss"

    else:
        $ temp1 = ""

    eng "Oh, really, [temp1]?"

    n "Yes. {w}Yes, it is."

    "Though [name] seems to have won that encounter, agitating [engTeach] doesn't seem like the right choice of action."

    jump ch2_club

label ch2_10_english_nothing:

    if outfit == "d":
        $ actn -= 1
        $ happy -= 1

    elif outfit == "n":
        $ actn -= 0.5

    if defEng:
        "Even though [name] has already told [engTeach] about $psv gender, $sbj decides that [engTeach] is too stubborn to bother correcting."

    else:
        if outfit == "d":
            $ temp1 = ", and other days to fight them.  This is not [name]'s day"

        "[name] decides to let it go. There are other battles $sbj can fight[temp1]."

    if self < 4:
        jump ch2_hallway_cry

    else:
        jump ch2_club

# story sharing day 10
label ch2_10_club_story:

    cp "Any volunteers for sharing today?"

    "[name] looks at [pn[psv]] story."

    menu:
        "What should [name] do?"

        "Share [pn[psv]] story":
            jump ch2_10_club_share

        "Do nothing":
            jump ch2_10_club_nothing

label ch2_10_club_share:

    $ happy += 1
    $ share = True

    "[name] shares [pn[psv]] story with the club."

    "They appreciate the odd humor that [pn[sbj]] put into day 4 topic."

    a "That one was really cool. I told you people would like it."

    n "I'm sure they're only snapping because it's polite."

    a "I'll go after Cami to prove to you that they like your stuff more than mine."

    "[name] rolls [pn[psv]] eyes, but Cami starts reading before [pn[sbj]] can reply."

    jump ch2_10_club_ryan

label ch2_10_club_nothing:

    $ happy -= 1
    $ share = False

    "Of course, [ally] notices when [name] doesn't raise [pn[psv]] hand to share."

    a "You're not sharing today?"

    n "I don't think so."

    a "I really do think people are going to like your thing today."

    n "Nah. I don't really feel like it today."

    a "Well, okay, then I'm going to share."

    n "What?"

    "Before [pn[sbj]] can say anything more, [ally] is already in front of the classroom with [psv] notebook."

    jump ch2_10_club_ryan

label ch2_10_club_ryan:

    if share:
        $ temp1 = "Once it's " + a_psv + " turn, "

    else:
        $ temp1 = ""

    play music ally

    "[temp1][ally] reads [pa[psv]] short poem in front of class."

    if day == (day1 + 2):
        $ temp1 = "strangely bouncy " + book + " poem"

    elif day == (day1 + 6):
        $ temp1 = "philisophical piece about climate change"

    else:
        $ temp1 = "few repeating lines about the life of a cat"

    "It's a [temp1]. [ally]'s voice shakes slightly as [pa[sbj]] reads, something that surprises [name] as [ally] is usually such a fearless, outgoing person."

    "[name] snaps enthusiastically for [pn[psv]] friend, but notices that [ally] is right about the other club members."

    "Even though [name] thought that [ally]'s poem was great, the other club members just aren't snapping as loudly for $ally."

    play music school

    if not share:
        "[name] regrets not sharing [pn[psv]] story, if only for [ally]'s sake."

    "[ally] sits back down next to [name] looking exhasted."

    a "So, what did you think?"

    n "I think that was an amazing poem."

    a "Well, nowhere near as good as your stuff. And the audience's snaps agreed, wouldn't you say so?"

    n "Well, I think you did great."

    a "Thanks, but no, I'm just not that good at writing."

    "And that's okay I'm more of a visual artist, anyway."

    "[name] frowns. [ally] has really great ideas for stories, but it was just that [pa[psv]] pacing and delivery was a little off."

    "What if there was a way to help [ally] solve [pa[psv]] reading confidence problems?"

    "The other club members are dispersing. It's time to head home."

    jump ch2_home

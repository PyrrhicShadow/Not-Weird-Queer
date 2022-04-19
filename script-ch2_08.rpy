# The script for part 1 day 8 (technically loop 8)

label ch2_08:

    $ loop = 8
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# english class day 8
label ch2_08_english:

    scene bg classroom english

    play music school

    show teacher eng

    "In English class, [name]'s teacher gets fed up that only one [d_noun] is answering all the questions, so he decides to pick on a [a_noun] next."

    "As usual, [name] knows the answer."

    "Since [ally] isn't in [name]'s English class, [pn[sbj]] can't ask [ally] for advice."

    menu:
        "What should [pn[sbj]] do?"

        "Raise [pn[psv]] hand":
            jump ch2_08_english_answer

        "Do nothing":
            jump ch2_08_english_nothing

label ch2_08_english_answer:

    $ happy += 1
    $ defEng = True

    "[engTeach] frowns at [name]."

    eng "[d_name], I'm only picking on [a_noun]s, so you can put your hand down."

    "[name] takes a deep breath."

    n norm "Well, I am a [noun], and I know the answer."

    if outfit == "g":
        $ actn += 1.5

        "[engTeach] shrugs and looks around the room before calling on [name]."

    elif outfit == "d":
        $ actn += 0.5

        eng "I'm in no mood to joke around, [d_name]."

        "[engTeach] calls on two other [noun]s, who both get the question wrong, before finally calling on [name]."

    else:
        $ actn += 1

        "Mr. Francis is visibly confused. He sighs deeply before calling on [name]."

    "Of course, [name] answers the question correctly."

    if outfit == "d":
        "Even though [engTeach] was a bit of an ass about it, at least [name] got to answer the question in the end."

    scene bg school hallway

    "[name] meets up with $ally after English class and tells $obj what happened."

    jump ch2_08_lunch

label ch2_08_english_nothing:



label ch2_08_lunch:



label ch2_08_art:



# story inspiration
label ch2_08_club_story:

    show extra male norm

    cp "Anyone wanna volunteer today?"

    $ verb = v(pn, "re", "s")

    "[name] raises [pn[psv]] hand. The club president tell [pn[obj]] that [pn[sbj]]'[verb] fourth."

    hide extra

    $ verb = v(pn, "read")

    "Finally, it's time for [name] to share. [pn[sbj]!c] [verb] [pn[psv]] story with a calm, clear voice."

    "After everyone's done snapping, Cami Newton raises her hand."

    cp "Yeah, Cami?"

    c "I have a question for the writer. So, what inspired this story?"

    n "It's a little bit complicated. Why don't I tell you after the meeting?"

    c "Sure. That sounds good."

    $ verb = v(pn, "wonder")

    "After [name] sits down, [pn[sbj]] [verb] what [pn[sbj]] should tell Cami."

    menu:
        "Should [name] share [pn[psv]] inspiration?"

        "Share the true inspiration":
            call ch2_08_club_inspiration
        "Say something vaugely related":
            call ch2_08_club_related

    a_myst "I told you your writing is good!"

    "Sure enough, [ally] sneaks up on [name] as soon as [pn[psv]] conversation is done."

    n "I'm sure she's just being nice."

    a "No, I think she really liked it, too!"

    if not share:
        "I understand why you didn't share your gender with her, though."

        "That kinda thing's gotta be scary."

    n "I mean, what if she was just saying all that to be nice to me? My writing can't be {i}that{/i} good."

    a "How am I ever going to convince you that you're a good writer?"

    n "Well, don't worry, [ally]. Even if I'm not as good as you say, I'm not going to stop anytime soon."

    a "Now, that's truly good news."

    jump ch2_home

label ch2_08_club_inspiration:

    $ happy += 1
    $ share = True

    "After the club meeting, [name] explains to Cami the inspiration behind the day 2 topic story, including some of [pn[psv]] struggles with implicit gender biases."

    c "Wow, that's actually pretty cool. Keep up the good work!"

    n "Thanks."

    c "Well, see you tomorrow?"

    n "Yeah."

    hide cami

    return

label ch2_08_club_related:

    $ share = False

    "After the club meeting, [name] tells Cami that [pn[sbj]] was inspired by a book [pn[sbj]] read once."

    c "Oh, cool! What book?"

    "[name] laughs nervously."

    n "You know, it's been so long, I can't remeber what it's called anymore."

    c "Well, it sure seems to have left an impression on you."

    c "Anywya, keep up the good work!"

    hide cami

    n_self "That didn't go as well as I would've liked. It wouldn't hurt to just tell people, would it?"

    return

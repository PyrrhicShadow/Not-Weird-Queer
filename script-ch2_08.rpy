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

    a "Yeah, that Mr. Francis guy is a dick. I'm sorry you have to put up with him."

    n "Well, he let me answer (cond: $outfit is "gender", "anyway,", $outfit is "not gender", "only because no one else knew the answer,", $outfit is "neutral", "eventually,") so it was okay in the end."

    a "That was really brave of you to stand up to him."

    "[name] frowns for a moment."

    n "Yeah, I guess it was. It was a little scary, but in the end, I'm glad that I did it."

    "It feels nice to stand up for myself."

    a "Yeah. It is."

    jump ch2_08_english_after

label ch2_08_english_nothing:

    if outfit == "d":
        $ actn -= 1
        $ happy -= 1

    elif outfit == "n":
        $ actn -= 0.5

    "[engTeach] calls on three different [noun]s before one of them answers the question correctly."

    $ verb = v("feel")

    "[name] knew the answer, so [pn[sbj]] [verb] bad that [pn[sbj]] just let it go so easily." j

    if outfit == "g":
        n_self "Well, I know [engTeach] is a sexist and besides, [ally] isn't here."

        $ temp1 = "Still, "

    else:
        $ temp1 = ""

    n_self "[temp1]I should probably stand up for myself next time."

    scene bg school hallway

    "[name] meets up with $ally after English class and tells $obj what happened."

    a "That Mr. Francis guy is a dick. I'm sorry you have to put up with him."

    n "Yeah. He's really scary. I'm not sure what would've happened if I had actually tried to answer his question."

    a "I guess you'll never know if you never try."

    n "I guess so. Maybe next time, I'll take the chance."

    a "Well, only if you're comfortable, [name]."

    jump ch2_08_english_after

label ch2_08_english_after:

    "[name] smiles at [ally]."

    n "Hey, [ally]. Thanks."

    a "Thanks? For what?"

    n "For believing in me."

    a "Of course. Thanks for being my friend, too."

# lunch day 8
    scene bg gym lunch

    $ happy -= 1

    "During lunch, some creep hits on [name], thinking [pn[sbj]]'s a [d_noun]."

    "[name] tells [pa[obj]] that [pn[sbj]] isn't interested and asks the creep if [pa[sbj] knew that [name]'s a [noun]."

    "[ally] defends [name] against [pa[obj]], telling the creep to piss off."

    $ classmate = "Creepy " + a_noun.capitalize()
    if outfit == "g":
        y "Oh. You're one of those weird gay people. Miss me with that shit."

        "Before either [name] or [ally] could snap back at [pa[obj]], the creep leaves and joins [pa[pos] friends sitting by the door."

    elif outfit == "d":
        y "Really?"

        "The creep looks [name] up and down."

        y "You're way too cute to be a [d_noun], darling."

        "Giggling, the creep walks back to [pa[psv]] friends sitting by the door."

    else:
        y "Oh, really? Yeah, right. I'll give you some time to reconsider, darling."

        "After lingering for a few seconds, the creep leaves and joins [pa[pos]] friends by the door."

    "[name] shakes [pn[psv]] head."

    if a_gender == "male":
        $ temp1 = "guy"

    else:
        $ temp1 = "chick"

    n "Is it just me, or was that [temp1] kind of a creep?"

    a "And an asshole at that. If [pa[sbj]] was really interested, [pa[sbj]] wouldn't have been so rude just because you told [pa[obj]] that you're a [noun]."

    n "Yeah, [pa[sbj]]'s not worth my time if [pa[sbj]]'s going to be so disrespectful."

    if: outfit == "g":
        a "Besides, being trans has nothing to do with being gay."

        "[name] thinks if over for a seccond."

        n "Yeah. Exactly!"

    "Even though the weirdo ended up leaving $name alone, $sbj still shivers slightly at the memory."

    if happy > -1:
        a "Hey, $name, forget about that prick. Your next sculpture isn't going to build itself!"

        if day1 == day + 1:
            n "I'm actually not sure what to make next. The next project is like recycled art?"

            a "Maybe? I'm sure whatever it is, you'll do great."

        else:
            n "Yeah, making art from recycled materials is an interesting idea."

            a "Yeah. Enviornmentally respectful."

        jump ch2_08_art

    else:
        a "Hey, [name], you okay?"

        n "Huh?"

        n "Yeah, just give me a moment. I want to think."

        jump ch2_hallway_cry

label ch2_08_art:

    "$name heads to $pos art class with $ally."

    if day > day1 + 7:
        $ temp1 = "finishing up"

    else:
        $ temp1 = "working on"

    "Today, the class is [temp1] sculptures made from recycled materials."

    if gender == "male":
        $ temp1 = "masculine sculpture idea"

    elif gender == "female":
        $ temp1 = "feminine sculpture idea"

    else:
        $ temp1 = "nonbinary sculpture idea"

    "$name is making a [temp1]."

    "[ally] is also working on a sculpture of [pa[psv]] own with some sort of recycled materials."

    jump ch2_club

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

# The script for part 1 day 8 (technically loop 8)

label ch2_08:

    $ loop = 8
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# story inspiration
label ch2_08_club_story:

    show extra male norm

    cp "Anyone wanna volunteer today?"

    $ verb = v("re", "s")

    "[name] raises [n_pos] hand. The club president tell [n_obj] that [n_sbj]'[verb] fourth."

    hide extra

    $ verb = v("read") 

    "Finally, it's time for [name] to share. [N_sbj] [verb] [n_pos] story with a calm, clear voice."

    "After everyone's done snapping, Cami Newton raises her hand."

    cp "Yeah, Cami?"

    c "I have a question for the writer. So, what inspired this story?"

    n "It's a little bit complicated. Why don't I tell you after the meeting?"

    c "Sure. That sounds good."

    $ verb = v("wonder")

    "After [name] sits down, [n_sbj] [verb] what [n_sbj] should tell Cami."

    menu:
        "Should [name] share [n_pos] inspiration?"

        "Share the true inspiration":
            call ch2_08_club_inspiration
        "Say something vaugely related":
            call ch2_08_club_related

    a_myst "I told you your writing is good!"

    "Sure enough, [ally] sneaks up on [name] as soon as [n_pos] conversation is done."

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

    "After the club meeting, [name] explains to Cami the inspiration behind the day 2 topic story, including some of [n_pos] struggles with implicit gender biases."

    c "Wow, that's actually pretty cool. Keep up the good work!"

    n "Thanks."

    c "Well, see you tomorrow?"

    n "Yeah."

    hide cami

    return

label ch2_08_club_related:

    $ share = False

    "After the club meeting, [name] tells Cami that [n_sbj] was inspired by a book [n_sbj] read once."

    c "Oh, cool! What book?"

    "[name] laughs nervously."

    n "You know, it's been so long, I can't remeber what it's called anymore."

    c "Well, it sure seems to have left an impression on you."

    c "Anywya, keep up the good work!"

    hide cami

    n_self "That didn't go as well as I would've liked. It wouldn't hurt to just tell people, would it?"

    return

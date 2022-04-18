# The script for part 1 day 5 (technically loop 5)

label ch1_05:

    $ loop = 5
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch1_morning

# bus part 1

    call ch1_bus

# art class day 5

    scene bg classroom art

    play music school

    "[name] goes to [n_pos] art class with [ally]."

    if day == 5:
        $ temp1 = "working on"
    else:
        $ temp1 = "finishing up"

    "Today, the class is [temp1] their paper-mâché sculptures."

    if day == 5:
        if gender == "male":
            $ temp1 = "pain, covered with sharp corners and dark, jarring colors"
        elif gender == "female":
            $ temp1 = "pain, curvacious and gracefully helpless, spotted with bright, popping complementary colors"
        else:
            $ temp1 = "pain, with contradictory sharpness and smooth edges"
    else:
        if gender == "male":
            $ temp1 = "masculine pain"
        elif gender == "female":
            $ temp1 = "feminine pain"
        else:
            $ temp1 = "gender-ambiguous pain"

    # show main's sculpture

    "[name]'s sculpture is a stylized depiction of [temp1]."

    $ renpy.show("ally " + a_gender + " norm")

    "[ally] stares quizzically at [name]'s sculpture."

    a "What's your sculpture about?"

    "[name] frowns at [n_pos] sculpture."

    menu:
        "Should [name] let [ally] in on the inspiration?"

        "Talk about [name]'s hardships" if (self > 1) and (ryan > 4):
            jump ch1_05_ryan_talk

        "Evade [ally]'s question":
            jump ch1_05_ryan_evade

label ch1_05_ryan_talk:

    $ ryan += 1
    $ happy += 1
    $ talk = True

    play music ally

    "[name] looks up at [ally]."

    n norm "Well, there's something I want to tell you."

    a "Cool."

    n "I… don't think I'm normal."

    $ renpy.show("ally " + a_gender + " smile")

    a "What do you mean by that? No one's actually 'normal,' silly."

    $ renpy.show("ally " + a_gender + " norm")

    n "I don't know. It's just that, I've always felt different."

    $ renpy.show("ally " + a_gender + " frown")

    a "Different how…?"

    n "You know how everyone thinks I'm a [d_noun]?"

    $ renpy.show("ally " + a_gender + " norm")

    a "Oh. Yeah? What about it?"

    n "Well, I don't think I'm actually a [d_noun]."

    "[name] takes a deep breath."

    if d_gender == "male":
        $ temp1 = "boyish"
    elif d_gender == "female":
        $ temp1 = "girly"

    n "I mean, I've always felt weird when people called me '[d_sbj]' or '[d_obj]' or tried to associate me with [temp1] things."

    a "I see."

    "[name] looks down at [n_pos] shoes."

    # show cg ryan accepts you (depending on how you got here)

    $ renpy.show("ally " + a_gender + " smile")

    "[ally] cracks a smile."

    a "That's actually really cool!"

    n "Oh. You think so?"

    if gender == "enby":
        $ temp1 = ""
    else:
        $ temp1 = ", like me"

    a "Yeah!  I think so. You're saying that you're actually a [a_noun][temp1]."

    if gender == "enby":
        "[name] chuckles quietly to [n_obj]self."

        n "Um, no. Actually, I don't think I'm a [d_noun] or a [a_noun]."

        a "Oh, so like nonbinary?"

        n "Yeah. I think that's the term for it."

    else:
        n "Um, yeah. Kind of, I guess. Yeah."

    "[name] shuffles from foot to foot."

    $ renpy.show("ally " + a_gender + " norm")

    a "Hey, [d_name]. You okay?"

    n "Um, I don't actually being called '[d_name]'."

    $ renpy.show("ally " + a_gender + " frown")

    a "Oh. I'm sorry."

    n "It's okay. You didn't know."

    $ renpy.show("ally " + a_gender + " norm")

    a "Well, is there something else I could call you?"

    n "Um, is it okay if you call me '[name]' instead?"

    $ renpy.show("ally " + a_gender + " smile")

    a "\'[name]\'. That's a cool name. I like it."

    n "Yeah. I like it, too."

    $ renpy.show("ally " + a_gender + " laugh")

    a "[name], a cool name for a cool [noun]."

    n "Yeah! Thanks. I'm so glad you agree."

    "[name] laughs along with [n_pos] friend."

    $ renpy.show("ally " + a_gender + " norm")

    "[name] hasn't felt this good about [n_obj]self since… [n_sbj] can't remember when."

    play music school

    if not club:
        call ch1_05_ryan_invite

    if day == 4:
        $ self += 1

    if loop == 2:
        jump ch1_club
    elif (loop == 4) or (loop == 5):
        jump ch1_05_lunch
    else:
        call dirty_hacker
        jump ch1_home

label ch1_05_ryan_evade:

    n "It's nothing. Don't worry about it."

    a "Okay."

    "Still, [ally] looks unconvinced."

    if day > 5:
        $ happy -= 1
        $ verb = v("do", "does")

        "[name] wants to tell [ally] what's going on, but [n_sbj] [verb]n't know how to find the right words."

        n_self "Maybe next time."

    if loop == 4:
        jump ch1_04_lunch
    elif loop == 5:
        jump ch1_05_lunch
    else:
        call dirty_hacker
        jump ch1_home

label ch1_05_ryan_invite:

    $ club = True

    a "So, what you're doing after school?"

    if self < 0:
        $ temp1 = "  I don't even know why I keep going."
    else:
        $ temp1 = ""

    n "Not much.  Just my book club.[temp1]"

    $ renpy.show("ally " + a_gender + " smile")

    a "Can I come with?"

    n "Um, of course!"

    "[name] smiles, excited to see [ally] at the book club."

    return

label ch1_05_lunch:

    $ ryan += 1

    scene bg gym lunch

    "[name] hangs out with [ally] during the lunch period."

    if talk:
        jump ch1_05_lunch_thanks

    if a_gender == "male":
        $ temp1 = "tacos or pizza"
    else:
        $ temp1 = "chocolate or rice krispies"

    "They debate whether [temp1] is the superior midnight snack."

    if loop == 4:
        jump ch1_04_art
    elif loop == 5:
        jump ch1_club
    else:
        jump dirty_hacker

label ch1_05_lunch_thanks:

    $ happy += 1

    n norm "Hey, thanks for understanding."

    $ renpy.show("ally " + a_gender + " norm")

    a "Of course. You're my friend, [name]. That's what friends are for."

    "[ally] called [name] by the correct name. [N_sbj] had no idea it'd feel this good to be validated."

    if loop == 4:
        jump ch1_04_art
    elif loop == 5:
        jump ch1_club
    else:
        jump dirty_hacker

label ch1_05_club_share:

    "The book club president asks if there are any volunteers."

    $ renpy.show("ally " + a_gender + " norm")

    a "You going to share today?"

    n norm "I don't know. Maybe."

    a "Oh, come on. Your stuff is awesome!"

    n "Okay, I'll present."

    a "I mean, I don't want to force you or anything…"

    hide ally

    menu:
        "[name] looks down at [n_pos] story."

        "Share [n_pos] story":
            jump ch1_05_club_talk_share
        "Do nothing":
            jump ch1_05_club_talk_nothing

label ch1_05_club_talk_share:

    $ happy += 1

    scene bg club sharing

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] shares [n_pos] story and the other club members snap enthusiastically."

    hide main
    $ renpy.show("ally " + a_gender + " smile")

    a "Told you they'd love it."

    n norm "Haha. Whatever."

    a "Why won't you just believe me, [name]?"

    n "Shh, the next kid's reading!"

    hide ally
    $ renpy.show("extra " + d_gender + " norm")

    "[name] and [ally] watch the other club members present their writing. All too soon, it's time to go home."

    jump ch1_05_home

label ch1_05_club_talk_nothing:

    "[ally] asks [name] what [n_sbj] wrote, so [name] shares [n_pos] story with just [ally]."

    a "Hey, that was really good."

    n "You think so?"

    a "Of course! Still, you don't have to share your writing if you don't want to. I mean, sharing isn't for everyone."

    n "No, I'll probably share next time."

    a "Really? I think they'll love it."

    jump ch1_05_home

label ch1_05_home:

    $ happy += 1

    scene bg school front

    play music outside

    "[ally] stops [name] before they part ways for the day."

    $ renpy.show("ally " + a_gender + " norm")

    a "Hey, [name]. Want to hang out this weekend?"

    n norm "Yeah, that sounds fun."

    a "Saturday afternoon at the park?"

    n "Okay."

    a "Sounds good. See you then!"

    hide ally

    "It's really cool to hear [ally] call [n_obj] \"[name]\" instead of \"[d_name].\""

    scene bg day end

    "The day has gone surprisingly well. [name] is feeling hopeful for tomorrow."

    "[name] is ready to start [n_pos] weekend."

    if happy < 0:
        $ self -= 1
    elif happy > 2 and self < 5:
        $ self += 1
    $ last_happy = happy
    $ happy = 0
    $ bus = False

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    jump ch1_06

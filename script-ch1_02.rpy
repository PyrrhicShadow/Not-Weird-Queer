# The script for part 1 day 2 (technically loop 2)

label ch1_02:

    $ loop = 2
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch1_morning

# bus part 1

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

    show teacher bio

    "[bioTeach] asks a question about flower [temp2]."

    if ryan > 1:
        $ temp1 = "friend"
    else:
        $ temp1 = "classmate"

    menu:
        "[name] knows the answer. What should [n_sbj] do?"

        "Raise [n_pos] hand":
            call ch1_02_bio_answer

        "Whisper to [n_pos] [temp1], [ally]":
            call ch1_02_bio_ryan

        "Do nothing":
            call ch1_02_bio_nothing

    "Soon, it's time for lunch."

    jump ch1_02_lunch

label ch1_02_bio_answer:

    bio "[d_name]?"

    "Cringing upon being refered to with {i}that{/i} name, [name] answers the question about [temp2]."

    bio "Correct."

    "[name] zones out for the rest of the class period."

    return

label ch1_02_bio_ryan:

    $ ryan += 1

    hide teacher

    n norm "Hey, [ally], don't you think it's weird that flowers can be both genders at the same time?"

    $ renpy.show("ally " + a_gender + " norm")

    if ryan > 0:
        $ happy += 1

        a "Yeah, definitely."

        n "Sometimes, I wish people could be flexible like that, too."

        $ renpy.show("ally " + a_gender + " smile")

        "[ally] laughs quietly, trying not to alert [bioTeach]."

        hide ally

        n_self "Maybe I've made a friend."

    else:

        "[ally] nods mildly."

        hide ally

        "[name] feels awkward, looks away, and drops the subject."

    return

label ch1_02_bio_nothing:

    $ happy -= 1

    if day == 2:
        $ temp3 = ally
    else:
        $ temp3 = renpy.random.choice(["Becky", "Peter", "Josh", "Chara"])

    "[name] stares out the window as [temp3] answers the question."

    $ verb = v("were", "was")

    "Although [name] knew the answer, [n_sbj] [verb] too embarrassed to answer."

    "Maybe next time."

    return

label ch1_02_lunch:

    scene bg gym lunch


    "It's lunch now. [name] sits down at a table and starts eating the sandwich [n_pos] mom made for [n_obj]."

    "Someone sitting at the other end of the table looks at [n_obj] sideways."

    n norm "What?"

    show extra male norm
    $ classmate = "Lunchroom bully"

    xm  "Why you always dressed so funny?"

    "[name] looks down and frowns."

    n "What do you mean…?"

    if d_gender == "male":
        $ temp1 = "freaking sissy"
    elif d_gender == "female":
        $ temp1 = "crazy feminazi"

    xm "You a [temp1] or something?"

    "The bully laughs too loudly to be comfortable."

    hide extra

    if ryan > 0:
        jump ch1_02_lunch_ryan
    else:
        jump ch1_02_lunch_alone

label ch1_02_lunch_ryan:

    a_myst "What the fuck are you doing, asshole? Don't you have anything better to do?"

    n_self "Wait, is that [ally]? What is [a_sbj] doing here?"

    "[name] turns around and indeed, [ally]'s standing behind [n_obj]."

    $ renpy.show("ally " + a_gender + " norm")

    a "Come on, [d_name], let's get out of here."

    "Grateful for the help, [name] follows [ally] out of the lunchroom."

    jump ch1_02_lunch_field

label ch1_02_lunch_alone:

    "[name] buries [n_pos] attention into [n_pos] sandwich."

    "When the roaring in [n_pos] ears becomes unbearable, [n_sbj] storms out of the cafeteria."

    jump ch1_hallway_cry

label ch1_02_lunch_field:

    scene bg field lunch

    "[ally] leads [name] out to the field."

    $ renpy.show("ally " + a_gender + " frown")

    a "Hey, you okay?"

    "[name] stares at [n_pos] shoes and shrugs."

    menu:
        "Should [name] tell [ally] what's bothering [n_obj]?"

        "Talk about [name]'s problems.":
            if (self > 1) and (ryan > 4):
                jump ch1_05_ryan_talk
            else:
                jump ch1_02_ryan_talk
        "Tell [ally] that everything's fine.":
            jump ch1_02_ryan_not

label ch1_02_ryan_talk:

    $ ryan += 1
    $ happy += 1

    "[name] looks up at [ally]."

    n norm "I just hate that people keep doing that."

    a "Yeah. That guy was a real jerk."

    "[name] stares back at [n_pos] shoes."

    n "Uh, thanks for standing up for me. Not a lot of people do that."

    $ renpy.show("ally " + a_gender + " smile")

    a "No problem, [d_name]. If that guy ever bothers you again, just let me know, okay?"

    n "Okay. I will."

    jump ch1_02_club_eligible

label ch1_02_ryan_not:

    "[name] continues staring at [n_pos] shoes."

    n norm "I'm doing fine."

    "[ally] nods."

    a norm "If you ever want to talk…"

    "[name] looks up and smiles weakly."

    n "Thanks, [ally]."

    jump ch1_02_club_eligible

label ch1_02_club_eligible:

    if ryan > 2:
        jump ch1_02_ryan_invite
    else:
        jump ch1_club

label ch1_02_ryan_invite:

    $ club = True

    if (day > 2) and (self < 2):
        $ temp1 = " I don't even know why I keep going."
    else:
        $temp1 = ""

    a "So, what you're doing after school?"

    n "Not much. Just my book club.[temp1]"

    a "Can I come with?"

    n "Of course."

    "[name] smiles."

    jump ch1_club

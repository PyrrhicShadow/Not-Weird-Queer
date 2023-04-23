# The script for part 1 day 4 (technically loop 4)

label ch1_04:

    $ loop = 4
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

# for now, each morning in the "loop" is the same

    call ch1_morning

# bus part 1

    call ch1_bus

# PE class part 1

    scene bg gym pe

    play music school

    "[name] heads to [pn[psv]] first class, PE."

    "[peTeach] splits the class into boys and girls teams to play dodgeball."

    if ryan > 4:
        $ temp0 = " with " + ally
    else:
        $ temp0 = ""

    "[name] walks over to the [a_noun]'s team[temp0]."

    $ renpy.show("ally " + a_gender + " norm")

    a "You're playing on the [a_noun]'s team today?"

    if self > 1:
        n norm "Yeah. You've got a problem with that?"

        $ renpy.show("ally " + a_gender + " smile")

        "[ally] laughs."

        a "Of course not! Come and play with us."

        $ renpy.show("ally " + a_gender + " norm")

    else:
        "[name] shrugs weakly."

        a "Don't worry about it, I won't tell."

    show teacher pe at right

    "Suddenly, [peTeach] walks over to the [a_noun]'s team."

    pe "[d_name], stop wasting time and get on your team already."

    "[name] shivers upon hearing {i}that{/i} name."

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True)

    menu:
        "What should [name] do?"

        "Stay on the [a_noun]'s team" if self > 1:
            jump ch1_04_pe_gender

        "Play on the [d_noun]'s team":
            jump ch1_04_pe_notGender

label ch1_04_pe_gender:

    $ verb0 = v(pn, "want")
    n "Sorry, [peTeach], I'm playing on the [a_noun]'s team today!"

    if ryan > 4:
        $ ryan += 1
        $ happy += 1

        if talk:
            $ temp0 = ""
            $ temp1 = pn["obj"]

        else:
            $ temp0 = "Despite not fully understanding why, "
            $ temp1 = pd["obj"]

        "[temp0][ally] supports [pn[obj]], too."

        a "Yeah. Maybe one of the other [a_noun]s can switch places with [temp1]?"

        "[peTeach] takes a moment to think over [ally]'s suggestion."

        pe "Fine, whatever. Any volunteers?"

        "A [a_noun] walks over to the [d_noun]'s team, snickering."

        "[peTeach] is satisfied."

        hide teacher

    else:
        if self < 2:
            $ happy += 1

            hide ally

            n "Sorry, [peTeach], I'm playing on the [a_noun]'s team today!"

            show teacher pe at center

            pe "Then the teams would be uneven."

            n "Maybe one of the other [a_noun]s can switch places with me?"

            "[peTeach] takes a moment to think over [name]'s suggestion."

            pe "Fine, whatever. Any volunteers?"

            "A [a_noun] walks over to the [d_noun]'s team, snickering. [peTeach] is satisfied."

        else:
            $ verb0 = v(pn, "stare")
            "[pn[sbj]] [verb0] at the ground for a moment before walking to the [d_noun]'s team."

    hide teacher
    hide ally

    "[name] isn't particularly good at sports, but dodgeball is easy enough."

    if ryan < 6 and self < 3:
        $ temp0 = "is tolerable"
    else:
        $ temp0 = "goes without a hitch"

    "The class period [temp0]."

    if ryan > 6 and self > 1:
        jump ch1_04_ryan_talk
    else:
        jump ch1_04_lunch

label ch1_04_pe_notGender:

    $ happy -= 1

    "[name] decides it's easier if [pn[sbj]] plays on the [d_noun]'s team."

    if ryan > 4:
        "[ally] notices [name]'s discomfort but doesn't say anything."

        n_self "I probably shouldn't have let it go so easily. Oh, well."

    else:
        "[name] feels shitty about playing on the [d_noun]'s team but whatever."

        n_self "This is just how my life is, anyway."

    hide teacher

    "[name] isn't particularly good at sports, but dodgeball is easy enough."

    "The class period is tolerable."

    jump ch1_04_lunch

label ch1_04_ryan_talk:

    $ renpy.show("ally " + a_gender + " norm")

    if talk:
        $ temp0 = name
    else:
        $ temp0 = d_name

    "Near the end of the class period, [ally] pulls [name] aside."

    a "Hey, [temp0], let's talk after class."

    n "Oh? Um, sure."

    scene bg school hallway

    "[name] finds [ally] outside the locker rooms."

    $ renpy.show("ally " + a_gender + " norm")

    a "So, I was just wondering."

    a "Why did you insist on playing on the [a_noun]'s team with me today?"

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True)

    menu:
        "[name] can tell that [pa[sbj]] is truly curious and just trying to understand."

        "Explain [name]'s reasons":
            jump ch1_05_ryan_talk

        "Evade [ally]'s question":
            jump ch1_05_ryan_evade

label ch1_04_lunch:

    $ happy -= 1

    scene bg gym lunch

    if ryan > 3:
        "[ally] has homework to get done, so [pn[sbj]] doesn't have time to eat lunch with [name]"

    if gender == "male":
        $ temp0 = renpy.random.choice(["male topic 1", "male topic 2", "male topic 3"])
    elif gender == "female":
        $ temp0 = renpy.random.choice(["female topic 1", "female topic 2", "female topic 3"])
    else:
        $ temp0 = renpy.random.choice(["topic 1", "topic 2", "topic 3"])

    $ verb0 = v(pn, "get")
    "[name] eats [pn[psv]] sandwich in peace, thinking about [temp0], when [pn[sbj]] [verb0] bullied by this girl sitting across from [pn[obj]]."

    show extra female norm

    $ classmate = "Lunchroom bully"

    xf "Why do you dress so weird, you gay bitch?"

    if self < 0:
        "[name] gets angry and wonders if there's another way to live."
        jump ch1_04_lunch_confront
    else:
        "[name] burries [pn[psv]] head in [pn[psv]] sandwich and ignors her."
        jump ch1_04_lunch_after

label ch1_04_lunch_confront:

    "[name] stands up from the table and stares down the bully."

    n norm "Why? Why do you say these things?"

    "The bully looked at her hand and then at [name] again."

    if gender == "female":
        $ temp0 = "girl"
    else:
        $ temp0 = "dude"

    xf "Chill out, [temp0], I was just joking. Can't you take a joke?"

    if self < 0:
        "Stunned, [name] backed up and ran out of the cafeteria."
        jump ch1_hallway_cry
    else:
        "[name] frowned, balling [pn[psv]] fists."

        n "It's not funny, jerk."

        xf "Whatever, weirdo."

        xf "Amazingly, the bully left [pn[obj]] alone for the rest of the lunch period."

        jump ch1_04_lunch_after

label ch1_04_lunch_after:

    $ happy += 1
    $ ryan += 1

    scene bg school hallway

    "After lunch but before [pn[psv]] next class, [name] meets up with [ally] and tells [pa[obj]] about what just happened."

    $ renpy.show("ally " + a_gender + " shocked")

    a "She had no right to harass you like that!"

    n norm "…"

    a "She didn't. I won't let you or anyone else tell me otherwise."

    "[name] smiles for the first time since the bully showed up at lunch."

    n "Thanks."

    a "No problem."

    if club:
        a "See you at the book club."
        n "Yeah!"

    jump ch1_club

# art class day 4

label ch1_04_art:

    scene bg classroom art

    "[name] goes to [pn[psv]] art class with [ally]."

    if day == 4:
        $ temp0 = "working on"
    else:
        $ temp0 = "finishing up"

    "Today, the class is [temp0] their paper-mâché sculptures."

    if gender == "male":
        $ temp0 = "covered with sharp corners and dark, jarring colors"
    elif gender == "female":
        $ temp0 = "curvacious and gracefully helpless, spotted with bright, popping complementary colors"
    else:
        $ temp0 = "with contradictory sharpness and smooth edges, "

    $ renpy.show("art main " + gender)

    "[name]'s sculpture is a stylized depiction of pain, [temp0]."

    $ renpy.show("ally " + a_gender + " norm", at_list=[right])

    a "I like how your sculpture's turning out."

    n norm "Huh?"

    if talk:
        if gender == "male":
            $ temp0 = "deep, masculine"
        elif gender == "female":
            $ temp0 = "deep, feminine"
        else:
            $ temp0 = "mixture of both masculine and feminine"
    else:
        $ temp0 = ""

    a "I like how the colors and shapes come together to express this [temp0] pain."

    n "Thanks."

    hide art
    show art ally

    "[name] studies [ally]'s sculpture."

    "It's a fairly tall structure comprised of complex hubs stacked atop one another, each bearing its own theme."

    "Some hubs are monochromatic while others are speckled with rough textures. One even has parts of the inner copper frame intentionally left bare."

    n "Your sculpture is really cool, too. So diverse and abstract."

    "[ally] studies [pa[psv]] own sculpture for a second."

    if talk:
        $ temp0 = name + ". Yours feels like you"
    else:
        $ temp0 = deadname

    a "Sure, but it's nowhere near as cool as yours, [temp0]."

    "[name] smiles."

    if talk:
        $ temp0 = ", " + ally
    else:
        $ temp0 = ""

    n "Thank you[temp0]."

    jump ch1_club

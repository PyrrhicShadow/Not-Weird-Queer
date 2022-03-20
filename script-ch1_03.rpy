# The script for part 1 day 3 (technically loop 3)

label ch1_03:

    $ loop = 3
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch1_morning

# bus part 1

    call ch1_bus

# math class part 1

    scene bg classroom math

    "During math class, [name] needs to go to the bathroom."

    scene bg school hallway

    "[name] walks out into the hallway and has to make a choice."

    menu:
        "Which bathroom should [n_sbj] use?"

        "[a_noun]'s":
            call ch1_03_math_gender

        "[d_noun]'s":
            call ch1_03_math_notGender

        "other":
            call ch1_03_math_missing

    scene bg classroom math

    show teacher math

    $ temp1 = renpy.random.choice(["lowest common denominators", "basic inequalities", "exponent rules"])

    "Back in math class, [name] zones out as [mathTeach] goes over [temp1]."

    "Eventually, it's time for lunch."

    jump ch1_03_lunch

label ch1_03_math_gender:

    $ happy += 1

    scene bg school bathroom

    $ verb = v("need")

    "[name] goes to the bathroom and does what [n_sbj] [verb] to do."

    $ verb = v("walk")

    "As [n_sbj] [verb] out, [n_pos] art teacher, [artTeach], walks by."

    show teacher art

    art "What were you doing in the [a_noun]'s bathroom?"

    n norm "Um, using the bathroom…?"

    art "You can't use the [a_noun]'s bathroom, [d_name]. You're a [d_noun]."

    n "You're right. I'm sorry."

    hide teacher

    "[name] whispers this before heading back to math class."

    "Despite the confrontation, [name] still feels like [n_sbj] did the right thing."

    "If only other people understood [n_obj]."

    return

label ch1_03_math_notGender:

    $ happy -= 1

    scene bg school bathroom

    $ verb = v("is")

    "[name] goes into the [d_noun]'s bathroom. It bothers [n_obj] to need to hide who [n_sbj] [verb] but the fear keeps [n_obj] from doing differently."

    "Afterward, [name] heads back to math class."

    return

label ch1_03_math_missing:

    "Unfortunately, [name]'s school doesn't have a gender neutral bathroom."

    $ verb = v("has")
    $ verb1 = v("make")

    menu:
        "[name] frowns but [n_sbj] really [verb] to pee, so [n_sbj] [verb1] a choice."

        "[a_noun]'s":
            jump ch1_03_math_gender

        "[d_noun]'s":
            jump ch1_03_math_notGender

label ch1_03_lunch:

    $ ryan += 1
    $ happy += 1

    scene bg gym lunch

    if ryan > 1:
        $ temp1 = "with " + ally + " "
    else:
        $ temp1 = ""

    "[name] picks a table [temp1]and starts eating [n_pos] sandwich."

    if club:
        call ch1_03_lunch_club
    elif ryan > 1:
        call ch1_03_lunch_ryan
    else:
        call ch1_03_lunch_company

    "Today, no one bullies [name] during the lunch period."

    if day == 3:
        "[N_sbj] can't remember the last time that happened."

    else:
        "It's a pleasant surprise."

    "All too soon, it's time to go to [n_pos] next class."

    jump ch1_03_english

label ch1_03_lunch_club:

    "They talk about reading, writing, and the book club. [ally] encourages [name] to share [n_pos] writing with the other club members because it's good."

    return

label ch1_03_lunch_ryan:

    $ club = True

    "They talk about their favorite books."

    "Seeing [ally]'s interest in books, [name] decides to invite [a_sbj] to [n_pos] afterschool book club."

    a norm "Oh, I didn't know we had a book club!"

    a "I'd love to come. I'm free most days after school, anyway."

    n "Awesome."

    return

label ch1_03_lunch_company:

    "[ally] sees [name] sitting alone in the cafeteria and decides to join [n_obj]."

    "Though they're mostly silent while eating, it's still nice to have company during lunch."

    return

label ch1_03_english:

    scene bg classroom english
    show teacher eng

    "The last class of the day is English class. [engTeach] is lecturing about misplaced and dangling modifiers."

    if happy > 1:
        if gender == "male":
            $ temp1 = "sexy sports cars"
        elif gender == "female":
            $ temp1 = "cats with party hats"
        else:
            $ temp1 = "popping, abstract shapes"
    elif self < 0:
        $ temp1 = "a way to leave this world behind"
    else:
        $ temp1 = "nothing of particular importance"

    $ verb = v("doodle")

    "As [name]'s taking notes, [n_sbj] [verb] [temp1] in the margins of [n_pos] notes."

    "Eventually, the bell rings."

    if self > -1:
        jump ch1_club

    else:
        "[name] slowly packs [n_pos] things and heads into a quiet hallway."

        jump ch1_hallway_cry

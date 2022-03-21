# The script for setting up all the variables that varry based on gender

label gender_male:

    $ gender = "male"
    $ noun = "boy"
    $ adj = "boyish"

    # pronouns
    $ plur = False
    $ n_sbj = "he"
    $ n_obj = "him"
    $ n_pos = "his"
    $ n_robj = "his"

    jump transmasc

label gender_female:

    $ gender = "female"
    $ noun = "girl"
    $ adj = "girly"

    # pronouns
    $ plur = False
    $ n_sbj = "she"
    $ n_obj = "her"
    $ n_pos = "her"
    $ n_robj = "hers"

    jump transfemme

label gender_enby:

    $ gender = "enby"
    $ noun = "nonbinary person"
    $ adj = "gender-neutral"

    jump sex_assigned_at_birth

label gender_enby_xe:

    # pronouns
    $ plur = False
    $ n_sbj = "xe"
    $ n_obj = "xem"
    $ n_pos = "xyr"
    $ n_robj = "xyrs"

    jump gender_enby

label gender_enby_they:

    # pronouns
    $ plur = True
    $ n_sbj = "they"
    $ n_obj = "them"
    $ n_pos = "their"
    $ n_robj = "theirs"

    jump gender_enby

label gender_enby_custom:

    $ gender = "enby"
    $ noun = "nonbinary person"
    $ adj = "gender-neutral"

    "Currently, custom pronouns are not supported."

    "Support for custom pronouns will be added when the programmer figures out how to display multiple text boxes at once."

    "Thank you for your patience."

    menu:
        "choose xe/xem pronouns":
            jump gender_enby_xe
        "choose they/them pronouns":
            jump gender_enby_they
        "return to pronoun choice screen":
            jump choose_pronouns

    jump sex_assigned_at_birth

label sex_assigned_at_birth:

    "Pick a sex assigned at birth."

    menu:
        "female":
            jump transmasc

        "male":
            jump transfemme

        "random":
            $ coin = renpy.random.choice(["H", "T"])

            if coin == "H":
                jump transfemme

            if coin == "T":
                jump transmasc

label transmasc:

    # main chara names
    $ d_name = renpy.random.choice(["Jessica", "Allison", "Zoë"])
    if d_name.lower() == name.lower():
        $ d_name = "Macie" 

    $ ally = renpy.random.choice(["Sean", "Kyle", "Ryan"])
    if ally.lower() == name.lower():
        $ally = "Owen"

    $ popKid = "Elise"
    $ mathBud = "Jaina"

    # ally pronouns
    $ a_gender = "male"
    $ a_noun = "boy"
    $ a_adj = "boyish"

    $ a_sbj = "he"
    $ a_obj = "him"
    $ a_pos = "his"
    $ a_robj = "his"

    # dead pronouns
    $ d_gender = "female"
    $ d_noun = "girl"
    $ d_adj = "girly"

    $ d_sbj = "she"
    $ d_obj = "her"
    $ d_pos = "her"
    $ d_robj = "hers"

    jump pronouns_complete

label transfemme:

    # main chara names
    $ d_name = renpy.random.choice(["Owen", "Peter", "Kyle"])
    if d_name.lower() == name.lower():
        $ d_name = "Brian"

    $ ally = renpy.random.choice(["Allison", "Jessica", "Zoë"])
    if ally.lower() == name.lower():
        $ ally = "Megan"

    $ popKid = "Jeremy"
    $ mathBud = "Dylan"

    # ally pronouns
    $ a_gender = "female"
    $ a_noun = "girl"
    $ a_adj = "girly"

    $ a_sbj = "she"
    $ a_obj = "her"
    $ a_pos = "her"
    $ a_robj = "hers"

    # dead pronouns
    $ d_gender = "male"
    $ d_noun = "boy"
    $ d_adj = "boyish"

    $ d_sbj = "he"
    $ d_obj = "him"
    $ d_pos = "his"
    $ d_robj = "his"

    jump pronouns_complete

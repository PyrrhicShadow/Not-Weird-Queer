# The script for setting up all the variables that varry based on gender

label gender_male:

    $ gender = "male"
    $ noun = "boy"
    $ adj = "boyish"

    # pronouns
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
    $ n_sbj = "she"
    $ n_obj = "her"
    $ n_pos = "her"
    $ n_robj = "hers"

    jump transfemme

label gender_enby:

    $ gender = "enby"
    $ noun = "kid"
    $ adj = "neutral"

    # pronouns
    $ n_sbj = "xe"
    $ n_obj = "xem"
    $ n_pos = "xyr"
    $ n_robj = "xyrs"

    jump sex_assigned_at_birth

label gender_custom:

    $ gender = "enby"
    $ noun = "kid"

    "Currently, custom pronouns are not supported."

    "Support for custom pronouns will be added when the programmer figures out how to display multiple text boxes at once."

    "Thank you for your patience."

    menu:
        "choose xe/xem pronouns":
            jump gender_enby
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
    $ ally = renpy.random.choice(["Sean", "Kyle", "Ryan"])
    if ally.lower() == name.lower():
        $ally = "Owen"

    # ally pronouns
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
    $ ally = renpy.random.choice(["Allison", "Jessica", "Zoë"])

    if ally.lower() == name.lower():
        $ ally = "Megan"

    # ally pronouns
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

label pronouns_complete:

    "Are you happy with your choice? \n[name] ([n_sbj]/[n_obj])"

    # The programmer (or modders) can start the game at any day (or part) by only changing this menu
    menu:
        "I'm ready":
            jump ch1_01
        "I want to test the game":
            jump ch0_00
        "I want to change my name":
            jump start
        "I want to change my pronouns":
            jump choose_pronouns

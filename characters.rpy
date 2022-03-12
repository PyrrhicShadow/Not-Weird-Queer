# The script to declare all characters used by the game.

label def_charas:

    # main characters
    define n = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main")
    define n_self = Character("[name]", color="44DD22", what_prefix="{i}", what_suffix="{/i}")
    define a = Character("[ally]", color="22AAEE", what_prefix="\"", what_suffix="\"", image="ally")

    # unnamed classmate characters
    # define x = Character("[classmate]", color="999999", what_prefix="\"", what_suffix="\"", image="boy")
    define xm = Character("[m_classmate]", color="9999AA", what_prefix="\"", what_suffix="\"", image="boy")
    define xf = Character("[f_classmate]", color="AA9999" ,what_prefix="\"", what_suffix="\"", image="girl")

    # named classmate characters
    define s = Character("Sophia", kind=xf)
    define b = Character("[bioteam]", kind=xm)
    define c = Character("Cami", kind=xf)
    define m = Character("Dylan", kind=xm)
    define p = Character("Elise", kind=xf)
    define cp = Character("Club President", kind=xm)
    define e = Character("Eigth Grader", kind=xf)

    # teacher characters
    define t = Character("[teacher]", color="555555", what_prefix="\"", what_suffix="\"", image="teacher")
    define pe = Character("Coach Paul", kind=t)
    define bio = Character("Mr. Kinsey", kind=t)
    define hist = Character("Mr. Coulter", kind=t)
    define eng = Character("Mr. Francis", kind=t)
    define math = Character("Mrs. Pendle", kind=t)
    define art = Character("Ms. Tedders", kind=t)

    # other characters
    define mom = Character("Mom", type=t, image="mom")

    return

################################################################################
## Characters
################################################################################

## main character
define name_girl_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_g", callback=n_voice, who_alt="[name] says,")
define name_girl_n = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_n", callback=n_voice, who_alt="[name] says,")
define name_girl_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_d", callback=n_voice, who_alt="[name] says,")
define name_boy_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_g", callback=n_voice, who_alt="[name] says,")
define name_boy_n = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_n", callback=n_voice, who_alt="[name] says,")
define name_boy_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_d", callback=n_voice, who_alt="[name] says,")
define name_enby_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_e_g", callback=n_voice, who_alt="[name] says,")
define name_enby_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_e_d", callback=n_voice, who_alt="[name] says,")
define n_self = Character("[name]", color="44DD22", what_italic=True, who_alt="[name] thinks,")

## ally character
define ally_girl = Character("[ally]", color="22AAEE", what_prefix="\"", what_suffix="\"", callback=a_voice, who_alt="[ally] says,")
define ally_boy = Character("[ally]", color="22AAEE", what_prefix="\"", what_suffix="\"", callback=a_voice, who_alt="[ally] says,")
define a_myst = Character("???", color="22AAEE", what_prefix="\"", what_suffix="\"", callback=a_voice, who_alt="A familiar voice says,")

## unnamed classmate characters
define xm = Character("[classmate]", color="9999AA", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[classmate] says,")
define xf = Character("[classmate]", color="AA9999" ,what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[classmate] says,")

## named classmate characters
define s = Character("Sophia", color="AA9999" ,what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Sophia says,")
define b = Character("[bioteam]", color="9999AA", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[bioteam] says,")
define c = Character("Cami", color="AA9999" ,what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Cami says,")
define cp = Character("Club President", color="9999AA", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="The Club President says,")

## gender-dependent classmate characters
define m_mathBud = Character("Dylan", color="9999AA", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Dylan says,")
define f_mathBud = Character("Jaina", color="AA9999" ,what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Jaina says,")
define f_popKid = Character("Elise", color="AA9999" ,what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Elise says,")
define m_popKid = Character("Jeremy", color="9999AA", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Jeremy says,")

## teacher characters
define pe = Character("[peTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[peTeach] says,")
define bio = Character("[bioTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[bioTeach] says,")
define hist = Character("[histTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[histTeach] says,")
define eng = Character("[engTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[engTeach] says,")
define math = Character("[mathTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[mathTeach] says,")
define art = Character("[artTeach]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[artTeach] says,")

## other characters
define mom = Character("Mom", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="Mom says,")
define adult = Character("[adult]", color="555555", what_prefix="\"", what_suffix="\"", callback=x_voice, who_alt="[adult] says,")
define note = Character("[note]", kind=nvl, who_alt="The page reads,")
define end = Character(None, kind=nvl)

################################################################################
## Variable Characters
################################################################################

init python:

    ## main character
    def n(what, **kwargs):
        if gender == "female":
            if outfit == "g":
                name_girl_g(what, **kwargs)
            elif outfit == "d":
                name_girl_d(what, **kwargs)
            else:
                name_girl_n(what, **kwargs)
        elif gender == "male":
            if outfit == "g":
                name_boy_g(what, **kwargs)
            elif outfit == "d":
                name_boy_d(what, **kwargs)
            else:
                name_boy_n(what, **kwargs)
        else:
            if outfit == "d":
                name_enby_d(what, **kwargs)
            else:
                name_enby_g(what, **kwargs)

    ## ally character
    def a(what, **kwargs):
        if a_gender == "female":
            ally_girl(what, **kwargs)
        else:
            ally_boy(what, **kwargs)

    ## main's named math classmate
    def m(what, **kwargs):
        if a_gender == "male":
            m_mathBud(what, **kwargs)
        else:
            f_mathBud(what, **kwargs)

    ## popular kid from main's elementary school days
    def p(what, **kwargs):
        if a_gender == "male":
            f_popKid(what, **kwargs)
        else:
            m_popKid(what, **kwargs)

    ## unnamed classmate
    def x(what, **kwargs):
        if d_gender == "male":
            xm(what, **kwargs)
        else:
            xf(what, **kwargs)

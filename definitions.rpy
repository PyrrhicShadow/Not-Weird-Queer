# Declare characters used by this game.

# main character
define name_girl_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_g")
define name_girl_n = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_n")
define name_girl_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_f_d")
define name_boy_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_g")
define name_boy_n = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_n")
define name_boy_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_m_d")
define name_enby_g = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_e_g")
define name_enby_d = Character("[name]", color="44DD22", what_prefix="\"", what_suffix="\"", image="main_e_d")
define n_self = Character("[name]", color="44DD22", what_prefix="{i}", what_suffix="{/i}")

# ally character
define ally_girl = Character("[ally]", color="22AAEE", what_prefix="\"", what_suffix="\"")
define ally_boy = Character("[ally]", color="22AAEE", what_prefix="\"", what_suffix="\"")
define a_myst = Character("???", color="22AAEE", what_prefix="\"", what_suffix="\"")

# unnamed classmate characters
define xm = Character("[classmate]", color="9999AA", what_prefix="\"", what_suffix="\"")
define xf = Character("[classmate]", color="AA9999" ,what_prefix="\"", what_suffix="\"")

# named classmate characters
define s = Character("Sophia", kind=xf)
define b = Character("[bioteam]", kind=xm)
define c = Character("Cami", kind=xf)
define cp = Character("Club President", kind=xm)

# gender-dependent classmate characters
define m_mathBud = Character("Dylan", kind=xm)
define f_mathBud = Character("Jaina", kind=xf)
define f_popKid = Character("Elise", kind=xf)
define m_popKid = Character("Jeremy", kind=xm)

# teacher characters
define pe = Character("[peTeach]", color="555555", what_prefix="\"", what_suffix="\"")
define bio = Character("[bioTeach]", color="555555", what_prefix="\"", what_suffix="\"")
define hist = Character("[histTeach]", color="555555", what_prefix="\"", what_suffix="\"")
define eng = Character("[engTeach]", color="555555", what_prefix="\"", what_suffix="\"")
define math = Character("[mathTeach]", color="555555", what_prefix="\"", what_suffix="\"")
define art = Character("[artTeach]", color="555555", what_prefix="\"", what_suffix="\"")

# other characters
define mom = Character("Mom", color="555555", what_prefix="\"", what_suffix="\"")
define adult = Character("[adult]", color="555555", what_prefix="\"", what_suffix="\"")
define note = Character("[note]", kind=nvl)

# Persistent and startup variables

default persistent.debug = False
default persistent.complete = False
define config.has_autosave = False
# define config.autosave_on_choice = False
# define config.autosave_on_quit = True

default dirty_hacker = "The programmer's not sure how you got here, but you're not supposed to be here. Odds are, you're just a dirty little hacker, aren't you?"
default save_name = "New game"

default name = "New game"
default n_sbj = "sbj"
default n_obj = "obj"
default ally = "Ally"
default outfit = "g"

default part = 0
default loop = 0
default day = 0
default self = 0
default happy = 0
default deaths = 0
default ryan = 0
default last_happy = 0
default actn = 0.0

default plur = False
default bus = False
default club = False
default share = False
default talk = False
default death = False

# Custom screens

# create debug screen for showing happy, self, ally, and action points
screen debug():
    style_prefix "say"

    window:
        id "window"
        vbox:
            id "namebox"
            style "namebox"
            text "[name] ([n_sbj]/[n_obj])" id "who"

        vbox:
            style "say_dialogue"

            text "Days: [day] (Part [part] day [loop])" id "what"
            text "Self: [self] | Happy: [happy] ([last_happy]) | [ally]: [ryan] | Action: [actn] ([outfit])" id "what"
            if death:
                text "Deaths: [deaths]" id "what"
            text "bus: [bus] | club: [share] | share: [share] | talk: [talk]" id "what"
            if persistent.complete:
                text "Completed" id "what"

# create chapter select screen for debug mode
screen chapter():
    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style debug_vbox:
    background "#000000"

init python:

# variable characters
    # main character
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

    # ally character
    def a(what, **kwargs):
        if a_gender == "female":
            ally_girl(what, **kwargs)
        else:
            ally_boy(what, **kwargs)

    # main's named math classmate
    def m(what, **kwargs):
        if a_gender == "male":
            m_mathBud(what, **kwargs)
        else:
            f_mathBud(what, **kwargs)

    # popular kid from main's elementary school days
    def p(what, **kwargs):
        if a_gender == "male":
            f_popKid(what, **kwargs)
        else:
            m_popKid(what, **kwargs)

    # unnamed classmate
    def x(what, **kwargs):
        if d_gender == "male":
            xm(what, **kwargs)
        else:
            xf(what, **kwargs)

    # function to switch the number agreement for the verbs
    # syntax: v(plural, singular) or v(plural)
    # example: v(have, has) or v(think)
    # will return "They have", "She has" or "They think", "She thinks"
    def v(*verbs):
        common = v_common(verbs[0])
        if common != "":
            verbs = common
        if plur:
            return verbs[0]
        else:
            if len(verbs) == 2:
                return verbs[1]
            else:
                return verbs[0] + "s"

    def v_common(vc):
        if vc == "are" or vc == "is":
            return ("are", "is")
        elif vc == "have" or vc == "has":
            return ("have", "has")
        elif vc == "do" or vc == "does":
            return ("do", "does")
        else:
            return ""

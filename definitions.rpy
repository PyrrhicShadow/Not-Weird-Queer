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
# define config.has_autosave = False
define config.autosave_on_choice = False
define config.autosave_on_input = False
define config.autosave_on_quit = False

default dirty_hacker = "The programmer's not sure how you got here, but you're not supposed to be here. Odds are, you're just a dirty little hacker, aren't you?"
default save_name = "New game"
default initialized = False

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
            style "say_dialogue"

            label "[name] ([n_sbj]/[n_obj])" id "who"

            text "Days: [day] (Part [part] day [loop])" id "what"
            text "Self: [self] | Happy: [happy] ([last_happy]) | [ally]: [ryan] | Action: [actn] ([outfit])" id "what"
            if death:
                text "Deaths: [deaths]" id "what"
            text "bus: [bus] | club: [share] | share: [share] | talk: [talk]" id "what"
            if persistent.complete:
                text "Completed" id "what"

style debug_window:
    xalign 0
    yalign 0.05
    background Image("gui/debugbox.png", xalign=0.0, yalign=0.25)

style debug_vbox:
    xalign 0.03
    yalign 0.05

# create chapter select screen for debug mode
screen chapter():
    tag menu

    default chapter = 1


    use game_menu(_("Chapter Select"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:
                textbutton _("Chapter 1") action SetScreenVariable("chapter", 1)
                textbutton _("Chapter 2") action SetScreenVariable("chapter", 2)

            if chapter == 1:
                use chapter1

            elif chapter == 2:
                use chapter2

screen chapter1():

    hbox:
        label _("Chapter 1")
        textbutton _("Jump to day 1") action Jump("ch1_01")

    hbox:
        label _("Chapter 2")
        textbutton _("Jump to day 2") action Jump("ch1_02")

    hbox:
        label _("Chapter 3")
        textbutton _("Jump to day 3") action Jump("ch1_03")

    hbox:
        label _("Chapter 4")
        textbutton _("Jump to day 4") action Jump("ch1_04")

    hbox:
        label _("Chapter 5")
        textbutton _("Jump to day 5") action Jump("ch1_05")

    hbox:
        label _("Chapter 6")
        textbutton _("Jump to day 6") action Jump("ch1_06")



screen chapter2():

    hbox:
        label _("Chapter 7")
        textbutton _("Jump to day 7") action Jump("ch2_07")

    hbox:
        label _("Chapter 8")
        textbutton _("Jump to day 8") action Jump("ch2_08")

    hbox:
        label _("Chapter 9")
        textbutton _("Jump to day 9") action Jump("ch2_09")

    hbox:
        label _("Chapter 10")
        textbutton _("Jump to day 10") action Jump("ch2_10")

    hbox:
        label _("Chapter 11")
        textbutton _("Jump to day 11") action Jump("ch2_11")

    hbox:
        label _("Chapter 12")
        textbutton _("Jump to day 12") action Jump("ch2_12")

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

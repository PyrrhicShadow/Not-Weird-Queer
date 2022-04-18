################################################################################
## Variables
################################################################################

## Persistent and startup variables
default persistent.debug = False
default persistent.complete = False
default persistent.death = False

## autosave at specific points
define config.has_quicksave = False
define config.autosave_on_choice = False
define config.autosave_on_input = False
define config.autosave_on_quit = False

## common variables
default dirty_hacker = "The programmer's not sure how you got here, but you're not supposed to be here. {p}Odds are, you're just a dirty little hacker, aren't you?"
default save_name = "New game"

default name = "New game"
default n_sbj = "sbj"
default n_obj = "obj"
default ally = "Ally"

default part = 0
default loop = 0
default day = 0
default self = 0
default happy = 0
default deaths = 0
default ryan = 0
default last_happy = 0
default death = False

## part 1 vars
default plur = False
default bus = False
default club = False
default share = False
default talk = False

# part 2 vars
default day1 = 0
default actn = 0.0
default outfit = "g"
default defHist = "none"
default defEng = False

## random name bank for deadnames and ally's names
default m_names = ["Owen", "Peter", "Kyle", "Sean", "Kevin", "Ryan", "Cole", "Andrew", "Jason"]
default f_names = ["Allison", "Jessica", "Zoë", "Abby", "Gabby", "Emily", "Katie", "Peyton", "Ciara"]

################################################################################
## Custom Functions
################################################################################

## function to switch the number agreement for the verbs
## syntax: v(plural, singular) or v(plural)
## example: v(have, has) or v(think)
## returns "They have", "She has" or "They think", "She thinks"
init python:
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

    ## helper function for common, irregular verbs
    def v_common(vc):
        if vc == "are" or vc == "is":
            return ("are", "is")
        elif vc == "have" or vc == "has":
            return ("have", "has")
        elif vc == "do" or vc == "does":
            return ("do", "does")
        else:
            return ""

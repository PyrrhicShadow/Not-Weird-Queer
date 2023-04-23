################################################################################
## Pronouns
################################################################################

## For variable pronouns, assign your character a pronoun
#  $ p_main = he_him
## Then use in "say" statement
#  "I'll give [p_main[obj]] some money later."
define he_him = {
    "pn": "he/him",
    "plur": False,
    "sbj": "he",
    "obj": "him",
    "psv": "his",
    "rfx": "his"
}

define she_her = {
    "pn": "she/her",
    "plur": False,
    "sbj": "she",
    "obj": "her",
    "psv": "her",
    "rfx": "hers"
}

define they_them = {
    "pn": "they/them",
    "plur": True,
    "sbj": "they",
    "obj": "them",
    "psv": "their",
    "rfx": "theirs"
}

define xe_xem = {
    "pn": "xe/xem",
    "plur": False,
    "sbj": "xe",
    "obj": "xem",
    "psv": "xyr",
    "rfx": "xyrs"
}

################################################################################
## Functions
################################################################################

init python:

## function to populate a custom set of pronouns
## syntax
    def pn_custom(plur, sbj, obj, psv, rfv):
        pn = sbj + "/" + obj
        custom = {
            "pn": pn,
            "plur": plur,
            "sbj": sbj,
            "obj": obj,
            "psv": psv,
            "rfv": rfv
        }

        return custom

## function to switch the number agreement for the verbs
## syntax: v(pronoun, plural, singular) or v(pronoun, plural)
## pronoun defaults to he/him, or singular
## common irregulars include is/are, have/has, do/does
## let's say `px` contains the user-player's pronouns
#  $ verb0 = v(px, have)
#  $ verb1 = v(px, think)
## verb0 returns "They have" or "She has"
## verb1 returns "They think" or "She thinks"
    def v(pronoun = he_him, *verbs):
        common = v_common(verbs[0])

        if common != "":
            verbs = common

        if pronoun["plur"]:
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

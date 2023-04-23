# The script for part 1 day 12 (technically loop 12)

label ch2_12:

    $ loop = 12
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    scene bg bedroom

    play music name

    $ outfit = "g"

    "Afternoon, day [day]."

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "Once again, it's finally Saturday afternoon."

    "After a morning of lounging in bed and watching Cartoon Network, it's time to go relax at the pier with [ally]."

# head to the pier

    jump tbc

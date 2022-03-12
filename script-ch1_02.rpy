# The script for part 1 day 2 (technically loop 2)

label ch1_02:

    $ loop = 2
    $ day += 1

    scene bg start day

    "Morning, day [day]."

    scene bg bedroom

    "The next morning rolls around."

    if self < 0:
        jump ch1_02_morning_sad
    elif self > 0:
        jump ch1_02_morning_happy
    else:
        jump ch1_02_morning_neutral

label ch1_02_morning_happy:

    "[name] was awake before [n_pos] alarm rang so [n_sbj] had time to make [n_obj]self breakfast without being late for the bus."

    "[name] picked a vaguely [adj] outfit and made a sandwich for lunch."

    scene bg kitchen

    jump ch1_02_kitchen

label ch1_02_morning_neutral:

    "[name] hit snooze on [n_pos] alarm clock twice before jumping out of bed."

    "[name] picked out a gender-neutral outfit and made it out the door on time, but only because [n_sbj] skipped breakfast."

    scene bg kitchen

    jump ch1_02_kitchen

label ch1_02_morning_sad:

    "[name] had overselpt again. Hastily, [n_sbj] throws on a [d_adj] outfit and combs through [n_pos] unruly hair."

    scene bg kitchen

    "While rushing through the door, [n_pos] mom chides [n_obj] about oversleeping all the time."

    jump ch1_02_kitchen

label ch1_02_kitchen:

    show mom norm

    mom norm "Have a good day at school, [d_name]."

    "Of course, [n_pos] mom called [n_obj] \"[d_name]\" again."

    "Even though it was annoying, [name] isn't really sure there's anything [n_sbj] could do about it."

    n norm smile "Thanks, Mom. Love you."

    mom "Love you, too, sweetie."

    call ch1_bus

    jump tbc

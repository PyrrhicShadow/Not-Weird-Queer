# The script for part 1 day 9 (technically loop 9)

label ch2_09:

    $ loop = 9
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

    jump ch2_home

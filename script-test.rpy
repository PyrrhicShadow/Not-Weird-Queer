# test script - to be removed in final game
# uses assests not created for this game,
# such as Monika sprites and (my) Kris fanart

label ch0_00:

    $ redEyes = False

    scene bg classroom gen

    show monika norm smile

    # These display lines of dialogue.

    "[name] wakes up in a classroom with Monika in front of [n_obj]."

    n norm smile "Whaaa?"

    a norm smile "Hello, [name]. Welcome to the classroom."

    n "Who are you?"

    a "I'm [ally], your classmate. Don't mind my appearance, it's just a placeholder used by the programmer currently."

    n "Please don't kill me. I'm sorry I couldn't want to date you."

    show monika sly smile

    a norm smile "No need to worry. I'm [ally], not Monika."

    show monika norm smile

    a norm smile "Like I said, this is just a placeholder for my real appearance."

    a "Think of it as an online avatar."

    n "I still don't trust you."

    show monika sly smile

    a norm smile "Hehe."

    scene bg start day

    "[name] is transported to another place."

    scene bg classroom gen

    n norm smile "What? But I'm still here?"

    show kris norm eyeless

    a norm smile "How's this for a better avatar, huh?"

    n "AHHHHH! YOU HAVE NO EYES!"

    a "There's nothing to be afraid of. Like I said earlier, these are all just placeholders."

    a "I'm still me, [ally]."

    a "And yeah, I do regret the lack of eyes in this avatar."

    a "Though I suppose red eyes would've been even creepier than hidden eyes."

    a "What do you think?"

    menu:
        "Yeah, you're right.":
            jump redEyes_creepy
        "No, red eyes look cool.":
            jump redEyes_cool

label redEyes_creepy:
    $ redEyes = True

    n_self "Yeah, red eyes would be really creepy."

    a "Ah, I knew you'd agree with me"

    jump mathBud

label redEyes_cool:
    $ redEyes = False

    n_self "I think red eyes are actually pretty cool."

    a "I'll keep that in mind for next time, then."

    jump mathBud

label mathBud:

    n "How did you know what I was thinking."

    hide kris
    show monika sly smile

    a norm smile "I have my ways."

    show monika norm smile
    a "Anyway."

    show boy norm at left

    m norm "I think red eyes look sick!"

    n norm smile "Who are you?"

    a "This is one of our classmates. Looks like he's in your math class."

    hide boy

    n "Oh my God, please, everyone, get out of here!"

    hide kris
    show monika norm smile

    a norm smile "I'm sad to see you go."

    a "Bye!"

    hide monika

    n "Good riddence."

    "[name] leaves the classroom and heads back into the void of the game."

    scene bg start

    "Now time to test that all the characters work."

    scene bg club front

    show ally norm smile

    a norm smile "Hi, I'm [ally], and I use [a_sbj]/[a_obj] pronouns. Nice to meet you."

    hide ally
    show girl norm

    s norm """Hi, I'm Sophia, and I use she/her pronouns.

    I'm the classmate in [name]'s art class. Nice to meet you."""

    hide girl
    show boy norm

    b norm """Hi, I'm [bioteam], and I use he/him pronouns.

    I'm the classmate in [name]'s biology class. We do a group project together.

    Nice to meet you."""

    hide boy
    show girl norm

    c norm """Hi, I'm Cami Newton, and I use she/her pronouns.

    I'm in [name]'s book club. Nice to meet you."""

    hide girl
    show boy norm

    m norm """Hi, I'm Dylan, and I use he/him pronouns.

    [name] and I went to the same elementary school. Nice to meet you."""

    hide boy
    show girl norm

    p norm "Hi, I'm Elise. Nice to meet you."

    a norm smile "You need to give your pronouns."

    p "Why would I need to give my pronouns?"

    a "Well, Elise, everyone's has been doing it."

    p "Fine.  I use she/her pronouns."

    p "There, are you happy?"

    a "Thank you. Next!"

    hide girl
    show boy norm

    cp norm """Hi, I'm the Club President of the middle school book club.

    I use he/him pronouns. Nice to meet you."""

    hide boy
    show girl norm

    e norm """Hi, I'm the eight grader in [name]'s book club.

    I use she/her pronouns.  Nice to meet you."""

    show girl norm

    $ f_classmate = "Classmate 1"

    xf norm """Hi, I'm a generic classmate. I use she/her pronouns.

    Nice to meet you!"""

    hide girl
    show boy norm

    $ m_classmate = "Classmate 2"

    xm norm """Hi, I'm another generic classmate.

    I use he/him pronouns."""

    hide boy
    show mom norm

    mom norm "Hi, I'm [name]'s mom. Nice to meet you!"

    hide mom
    show teacher boy

    pe boy """I'm Coach Paul.

    Teachers should have a different color than students."""

    show teacher girl

    math girl "And I'm Mrs. Pendle, a female teacher."

    hide teacher

    "Now let's test the fail-safe message: "

    call dirty_hacker

    "That's all for now. Thank you for playing."

    "Now let's get on with the actual game."

    jump ch1_01

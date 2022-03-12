# The script for part 1 day 1

label ch1_01:

    $ part = 1
    $ loop = 1
    $ day += 1

    scene bg start day

    "Part 1: Discovery"

    scene bg bedroom

    "Morning, day [day]."

    "[name] finally wakes up after [n_pos] alarm rings four times."

    "[name] quickly throws on a vaugly [adj] outfit and rushes to the kitchen to grab some breakfast, inevitably running into [n_pos] mom."

    scene bg kitchen

    mom norm "[d_name], if you don't hurry up, you're going to be late, again."

    "[name] cringes at the mention of {i}that{/i} name."

    n norm smile "Okay, Mom. I'm going."

    n "Love you."

    mom "Love you, too. Have a good day!"

    "[name] doesn't like being called [d_name], but that's the name [n_sbj] was given."

    "With a heavy sigh, [name] grabs [n_pos] backpack and heads out the door."

    scene bg bus

    "[name] walks to the bus stop and gets on the next bus."

    "There are three open seats left."

    "[name] is shy so [n_sbj] sits alone."

    "[name] see [n_pos] classmate, [ally], sitting a few rows away and wonders if [a_sbj] would like to have company."

    "Before [name] gets the courage to sit with [ally], the bus doors close and it's too late for [name] to get up and switch seats."

    n_self "It's fine, I chose to be lonely today, that's all."

    "But a part of [n_obj] wishes [n_sbj] hadn't chosen to sit alone."

    scene bg school front

    "[name] arrives at school, wearing [n_pos] jacket around [n_pos] waist."

    "The morning is surprisingly warm compared to last week. Spring must be on it's way."

    scene bg classroom history

    "[name] goes to [n_pos] first class of the day, history."

    "Doodling in [n_pos] notebook, [name] tries [n_obj] to pay attention to the classwork without falling asleep."

    "One of [name]'s classmates comes up and picks on the way [n_sbj] is acting."

    if d_gender == "male":
        jump ch1_01_history_boy
    elif d_gender == "female":
        jump ch1_01_history_girl

label ch1_01_history_boy:

    show boy norm at left
    show boy norm as boy2 at right

    $ m_classmate = "Classmate 1"

    xm norm "Look at what [d_name]'s doing right now."

    $ m_classmate = "Classmate 2"

    xm "Yeah, what a freaking pussy-ass."

    hide boy
    hide boy2

    jump ch1_01_lunch

label ch1_01_history_girl:

    show girl norm at right
    show girl norm as girl2 at left

    $ f_classmate = "Classmate 1"

    xf norm "Look at what [d_name]'s doing right now."

    $ f_classmate = "Classmate 2"

    xf "Yeah, who does [d_sbj] think [d_sbj] is, acting all cocky like that."

    hide girl
    hide girl2

    jump ch1_01_lunch

label ch1_01_lunch:

    "[name] shrinks into [n_pos] desk and tries to ignore [n_pos] classmates by burying [n_pos] head in [n_pos] classwork."

    "Thankfully, it's soon lunch time."

    scene bg lunchroom lunch

    "[name] eats [n_pos] sandwich alone at lunch, watching the other kids laugh and talk."

    "At any moment, one of them could refocus their attention at laughing at [n_obj]."

    "Lunch is fairly stressful most days."

    "A group of older classmates notices [name] sitting alone at the end of the lunch table"

    if d_gender == "male":
        jump ch1_01_lunch_boy
    elif d_gender == "female":
        jump ch1_01_lunch_girl

label ch1_01_lunch_boy:

    jump ch1_01_art

label ch1_01_lunch_girl:

    jump ch1_01_art

label ch1_01_art:

    scene bg field lunch

    "Even though [name]'s not quite done with [n_pos] sandwich, [n_sbj] gets up and leaves the lunchroom to finish [n_pos] sandwich on the field."

    "At least the next class is one [name] enjoys, art."

    scene bg classroom art

    "Today in art class, [name]'s class is finishing up their charcoal self-portraits."

    "Since [n_sbj] has already finished [n_pos] portrait last class, [n_sbj] is writing in [n_pos] notebook."

    "A few other classmates are also finishing up. [name] isn't sure if [n_sbj] wants to talk to one of them or not."

    menu:
        "Talk to a classmate":
            jump ch1_01_art_talk
        "Not talk to a classmate":
            jump ch1_01_art_not

label ch1_01_art_talk:

    n norm smile "Hey, Sophia."

    show girl norm

    s norm "Hello, [d_name]. What's up?"

    "[name] stares at [n_pos] notebook."

    n "Not much."

    "Sophia nods slowly."

    s "\'Kay. Cool."

    hide girl norm

    "Sighing, [name] returns to writing in [n_pos] notebook."

    jump ch1_01_notebook

label ch1_01_art_not:

    "After a moment of thought, [name] decides not to bother [n_pos] classmates."

    n_self "Sigh."

    jump ch1_01_notebook

label ch1_01_notebook:

    "[name] wishes [n_sbj] could express [n_obj]self better."

    "Back to the notebook, [name] continues crafting [n_pos] latest story."

    """[name] loves to write short stories and poems. It's the only way [n_sbj] can really express [n_obj]self.

    [name] likes writing so much, [n_sbj] joined the middle school book club.

    Though [n_sbj] doesn't know anyone in the book club, [name] enjoys the oportunity to write and listen to the others stories."""

    scene bg club front

    "After class, [name] heads to the afterschool book club."

    "As soon as [n_sbj] sits down, [n_sbj] start writing."

    """Today, [name] is writing a poem about the struggle of looking like a [d_noun] when [n_sbj] hates most [d_adj] things
    through the metaphor of a film written in a language no one understands."""

    "It's a really personal piece, and [name] is really proud of how it turned out."

    "Soon, it is time for everyone to share their pieces of writing."

    scene bg club sharing

    "Every day, the book club president asks if there are nay volunteers. The same few kids who always share volunteer immediately."

    "[name] listens as the other club members, mostly kids older than [n_obj], share their fun, wacky sotries and freeform poetry."

    "[name] usually doesn't share, but [n_sbj] wishes [n_sbj] had the courage to."

    "After every person who shares, all the club members polietly snap their fingers in encouragement."

    "[name] always claps along, wondering if [n_sbj] should go next, but [n_sbj] rarely gains the courage to."

    "Soon, it's time to head home."

    scene bg school street

    "After the book club, [name] walks home by [n_obj]self."

    """During the colder months, [n_sbj]'d often skip the book club in order to catch the bus home,
    especially when it rained, but the weather was finally nice enough for [name] to risk missing the bus."""

    "While the day was a rough one, but nothing [name] hasn't seen before."

    "[name] is ready to start a new day."

    scene bg end day

    "End of day [day]."

    jump ch1_02

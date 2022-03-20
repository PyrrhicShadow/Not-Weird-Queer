# The script for part 1 day 1

label ch1_01:

    $ loop = 1
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

    scene bg bedroom

    "Morning, day [day]."

    $ outfit = "g"

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] finally wakes up after [n_pos] alarm rings four times."

    $ verb = v("throw")
    $ verb1 = v("rush", "rushes")

    "[N_sbj] quickly [verb] on a vaguely [adj] outfit and [verb1] to the kitchen to grab some breakfast, inevitably running into [n_pos] mom."

    scene bg kitchen
    show mom norm

    mom "[d_name], if you don't hurry up, you're going to be late, again."

    "[name] cringes at the mention of {i}that{/i} name."

    n norm "Okay, Mom. I'm going."

    n "Love you."

    mom "Love you, too, sweetie. Have a good day!"

    $ verb = v("were", "was")

    "[name] doesn't like being called \"[d_name]\", but that's the name [n_sbj] [verb] given."

    "With a heavy sigh, [name] grabs [n_pos] backpack and heads out the door."

# catch the bus day 1

    scene bg bus

    "[name] walks to the bus stop and gets on the next bus."

    "There are three open seats left."

    $ verb = v("sit")

    "[name] is shy so [n_sbj] [verb] alone."

    "[name] sees [n_pos] classmate, [ally], sitting a few rows away and wonders if [a_sbj] would like to have company."

    "Before [name] gets the courage to sit with [ally], the bus doors close and it's too late for [n_obj] to get up and switch seats."

    n_self "It's fine, I chose to be lonely today, that's all."

    "But a part of [n_obj] wishes [n_sbj] hadn't chosen to sit alone."

    scene bg school front

    "[name] arrives at school, wearing [n_pos] jacket around [n_pos] waist."

    "The morning is surprisingly warm compared to last week. Spring must be on its way."

# history class day 1

    scene bg classroom history

    "[name] goes to [n_pos] first class of the day, history."

    "Doodling in [n_pos] notebook, [name] tries [n_obj] to pay attention to the classwork without falling asleep."

    $ verb = v("is")

    "One of [name]'s classmates comes up and picks on the way [n_sbj] [verb] acting."

    $ renpy.show("extra " + d_gender + " norm", at_list=[left])
    $ renpy.show("extra " + d_gender + " norm", at_list=[right], tag="extra2")

    $ classmate = "Classmate 1"

    x "Look at what [d_name]'s doing right now."

    $ classmate = "Classmate 2"

    if d_gender == "male":
        x "Yeah, what a freaking pussy-ass."
    elif d_gender == "female":
        x "Yeah, who does she think she is, sitting there all cocky like that?"

    hide extra
    # hide extra2

# lunch day 1

    "[name] shrinks into [n_pos] desk and tries to ignore [n_pos] classmates by burying [n_pos] head in [n_pos] classwork."

    "Thankfully, it's soon lunchtime."

    scene bg gym lunch

    "[name] eats [n_pos] sandwich alone at lunch, watching the other kids laugh and talk."

    "At any moment, one of them could refocus their attention at laughing at [n_obj]."

    "Lunch is fairly stressful most days."

    "A group of older classmates notices [name] sitting alone at the end of the lunch table."

    if d_gender == "female":
        $ temp1 = "a man-hater"
    elif d_gender == "male":
        $ temp1 = "gay"
    else:
        $ temp1 = "insert insult here"

    $ classmate = "Classmate 1"
    $ renpy.show("extra " + d_gender + " norm")

    x "Hey, look at that weirdo over there."

    $ classmate = "Classmate 2"
    $ renpy.show("extra " + d_gender + " norm", at_list=[right], tag="extra1")

    x "What kind of [d_noun] dresses like that?"

    $ classmate = "Classmate 3"
    $ renpy.show("extra " + d_gender + " norm", at_list=[left], tag="extra2")

    x "Gotta be [temp1] or something."

    $ classmate = "Classmate 1"

    x "Haha, definitely."

    scene bg field lunch

    $ verb = v("get")
    $ verb1 = v("leave")

    "Even though [name]'s not quite done with [n_pos] sandwich, [n_sbj] [verb] up and [verb1] the lunchroom to finish [n_pos] sandwich on the field."

    "At least the next class is one [name] enjoys, art."

# art class day 1

    scene bg classroom art

    "Today in art class, [name]'s class is finishing up their charcoal self-portraits."

    $ verb = v("has")
    $ verb1 = v("are")

    "Since [n_sbj] [verb] already finished [n_pos] portrait last class, [n_sbj] [verb1] writing in [n_pos] notebook."

    $ verb = v("want")

    menu:
        "A few other classmates are also finishing up. [name] isn't sure if [n_sbj] [verb] to talk to one of them or not."

        "Talk to a classmate":
            jump ch1_01_art_talk

        "Not talk to a classmate":
            jump ch1_01_art_not

label ch1_01_art_talk:

    n norm "Hey, Sophia."

    show sophia norm

    s "Hello, [d_name]. What's up?"

    "[name] stares at [n_pos] notebook."

    n "Not much."

    "Sophia nods slowly."

    s "\'Kay. Cool."

    hide sophia

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

    [name] likes writing so much, [n_sbj] joined the middle school book club."""

    $ verb = v("do")

    "Though [n_sbj] [verb]n't know anyone in the book club, [name] enjoys the opportunity to write and listen to the other's stories."

# book club day 1

    scene bg club front

    "After class, [name] heads to the afterschool book club."

    $ verb = v("sit")
    $ verb1 = v("start")

    "As soon as [n_sbj] [verb] down, [n_sbj] [verb1] writing."

    $ verb = v("hate")

    "Today, [name] is writing a poem about the struggle of looking like a [d_noun] when [n_sbj] [verb] most [d_adj] things."

    $ verb = v("choose")

    "[N_sbj] [verb] to express this through a metaphor of a deep, artsy film written in a language no one understands."

    "It's a really personal piece, and [name] is really proud of how it turned out."

    "Soon, it is time for everyone to share their pieces of writing."

    scene bg club sharing

    "Every day, the book club president asks if there are any volunteers. The same few kids who always share volunteer immediately."

    "[name] listens as the other club members, mostly kids older than [n_obj], share their fun, wacky stories and freeform poetry."

    $ verb = v("wish", "wishes")

    "[name] usually doesn't share, but [n_sbj] [verb] [n_sbj] had the courage to."

    "After every person who shares, all the club members politely snap their fingers in encouragement."

    $ verb = v("gain")

    "[name] always snaps along, wondering if [n_sbj] should go next, but [n_sbj] rarely [verb] the courage to."

    "Soon, it's time to head home."

# go home day 1

    scene bg school street

    "After the book club, [name] walks home by [n_obj]self."

    """During the colder months, [n_sbj]'d often skip the book club in order to catch the bus home,
    especially when it rained, but the weather was finally nice enough for [name] to risk missing the bus."""

    scene bg day end

    "While the day was a rough one, it was nothing [name] hasn't seen before."

    "[name] is ready to start a new day."

    jump ch1_02

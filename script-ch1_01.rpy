# The script for part 1 day 1

label ch1_01:

    $ loop = 1
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    scene bg bedroom

    play music name

    "Morning, day [day]."

    $ outfit = "g"

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] finally wakes up after [pn[psv]] alarm rings four times."

    $ verb = v(pn, "throw")
    $ verb1 = v(pn, "rush", "rushes")

    "[pn[sbj]!c] quickly [verb] on a vaguely [adj] outfit and [verb1] to the kitchen to grab some breakfast, inevitably running into [pn[psv]] mom."

    scene bg kitchen
    show mom norm

    mom "[d_name], if you don't hurry up, you're going to be late, again."

    "[name] cringes at the mention of {i}that{/i} name."

    n norm "Okay, Mom. I'm going."

    n "Love you."

    mom "Love you, too, sweetie. Have a good day!"

    $ verb = v(pn, "were", "was")

    "[name] doesn't like being called \"[d_name]\", but that's the name [pn[sbj]] [verb] given."

    "With a heavy sigh, [name] grabs [pn[psv]] backpack and heads out the door."

# catch the bus day 1

    scene bg bus

    play music outside

    "[name] walks to the bus stop and gets on the next bus."
    "There are three open seats left."

    $ verb = v(pn, "sit")

    "[name] is shy so [pn[sbj]] [verb] alone."

    $ verb = v(pn, "see")

    "[pn[sbj]!cl] [verb] [pn[psv]] classmate, [ally], sitting a few rows away and wonders if [pa[sbj]] would like to have company."

    "Before [name] gets the courage to sit with [ally], the bus doors close and it's too late for [pn[obj]] to get up and switch seats."

    n_self "It's fine, I chose to be lonely today, that's all."

    "But a part of [pn[obj]] wishes [pn[sbj]] hadn't chosen to sit alone."

    scene bg school front

    "[name] arrives at school, wearing [pn[psv]] jacket around [pn[psv]] waist."

    "The morning is surprisingly warm compared to last week. Spring must be on its way."

# history class day 1

    scene bg classroom history

    play music school

    "[name] goes to [pn[psv]] first class of the day, history."

    "Doodling in [pn[psv]] notebook, [name] tries [pn[psv]] best to pay attention to the classwork without falling asleep."

    $ verb = v(pn, "is")

    "One of [name]'s classmates comes up and picks on the way [pn[sbj]] [verb] acting."

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
    hide extra2

    "[name] shrinks into [pn[psv]] desk and tries to ignore [pn[psv]] classmates by burying [pn[psv]] head in [pn[psv]] classwork."

    "Thankfully, it's soon lunchtime."

# lunch day 1

    scene bg gym lunch

    "[name] eats [pn[psv]] sandwich alone at lunch, watching the other kids laugh and talk."

    "At any moment, one of them could refocus their attention at laughing at [pn[obj]]."

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

    play music school

    $ verb = v(pn, "get")
    $ verb1 = v(pn, "leave")

    "Even though [name]'s not quite done with [pn[psv]] sandwich, [pn[sbj]] [verb] up and [verb1] the lunchroom to finish [pn[psv]] lunch on the field."

    "At least the next class is one [name] enjoys, art."

# art class day 1

    scene bg classroom art

    "Today in art class, [name]'s class is finishing up their charcoal self-portraits."

    $ verb = v(pn, "are")

    "Since [name] already finished [pn[psv]] portrait last class, [pn[sbj]] [verb] writing in [pn[psv]] notebook."

    $ verb = v(pn, "want")

    menu:
        "A few other classmates are also finishing up. [name] isn't sure if [pn[sbj]] [verb] to talk to one of them or not."

        "Talk to a classmate":
            jump ch1_01_art_talk

        "Write some more":
            jump ch1_01_art_not

label ch1_01_art_talk:

    n norm "Hey, Sophia."

    show sophia norm

    s "Hello, [d_name]. What's up?"

    "[name] stares at [pn[psv]] notebook, barely flinching at {i}that{/i} name."

    n "Not much."

    "Sophia nods slowly."

    s "\'Kay. Cool."

    hide sophia

    "Sighing, [name] returns to writing in [pn[psv]] notebook."

    jump ch1_01_notebook

label ch1_01_art_not:

    "After a moment of thought, [name] decides not to bother [pn[psv]] classmates."

    n_self "Sigh."

    jump ch1_01_notebook

label ch1_01_notebook:

    $ verb = v(pn, "wish", "wishes")

    "[pn[sbj]!cl] [verb] [pn[sbj]] could express [pn[obj]]self better."

    "Back to [pn[psv]] notebook, [name] continues crafting [pn[psv]] latest story."

    "[name] loves to write short stories and poems. It's the only way [pn[sbj]] can really express [pn[obj]]self."

    "[pn[sbj]!cl] also adds little doodles to [pn[psv] stories."

    "With [pn[psv]] head stuck in [pn[psv]] journal, art class is soon over."

    "[name] quickly packs up and heads to [pn[psv]] next class."

# book club day 1

    scene bg club front

    "It doesn't look like it's going to rain today, so [pn[sbj]] heads to the book club after school."

    $ verb = v(pn, "do")
    $ verb1 = v(pn, "enjoy")

    "Though [pn[sbj]] [verb]n't really know anyone there, [pn[sbj]] [verb1] the opportunity to write and listen to the other's stories."

    "Every day, the club officers decide on a prompt to help get the creative juices going."

    $ verb = v(pn, "come")

    "Sometimes, [name] uses them, but other times, [pn[sbj]] [verb] up with [pn[psv]] own idea."

    "Today's prompt is [writing_prompt[0]]."

    $ verb = v(pn, "start")

    "As soon as [name] sits down, [pn[sbj]] [verb] writing."

    $ verb = v(pn, "decide")
    $ verb1 = v(pn, "hate")
    if gender == "enby":
        $ temp1 = "a lot of"
    else:
        $ temp1 = "most"

    "[pn[sbj]!cl] [verb] to write a poem about the struggle of looking like a [d_noun] when [pn[sbj]] [verb1] being associated with [temp1] [d_adj] things."

    $ verb = v(pn, "choose")

    "[pn[sbj]!c] [verb] to express this through a metaphor of a deep, artsy film written in a language no one understands."

    $ verb = v(pn, "is")

    "It's a really personal piece, and [pn[sbj]] [verb] really proud of how it turned out."

    "Soon, it is time for the club members to share their pieces of writing."

    scene bg club sharing

    show extra male norm

    cp "Hello, everyone! I hope you all enjoyed today's prompt."

    cp "Or ignoring today's prompt. Looking at you, Trevor."

    "Everyone laughs. Trevor's pretty famous for flipping the prompt on its head or flat out ignoring it whenever he shares."

    cp "Okay, any volunteers?"

    "As usual, the same few kids who always share volunteer immediately."

    "[name] listens as the other club members, mostly kids older than [pn[obj]], share their fun, wacky stories and freeform poetry."

    $ verb = v(pn, "wish", "wishes")

    "[name] usually doesn't share, but [pn[sbj]] [verb] [pn[sbj]] had the courage to."

    "After every person who shares, all the club members politely snap their fingers in encouragement."

    $ verb = v(pn, "gain")

    "[name] always snaps along, wondering if [pn[sbj]] should go next, but [pn[sbj]] rarely [verb] the courage to."

    "Soon, it's time to head home."

# go home day 1

    scene bg school front

    play music outside

    "After the book club, [name] walks home by [pn[obj]]self."

    """During the colder months, [pn[sbj]]'d often skip the book club in order to catch the bus home,
    especially when it rained, but the weather's actually pretty nice today."""

    $ verb = v(pn, "have")
    "While the day was a rough one, it was nothing [pn[sbj]] [verb]n't seen before."

    "[name] is ready to start a new day."

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    jump ch1_02

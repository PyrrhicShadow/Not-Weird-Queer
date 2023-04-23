# The script for part 1 day 11 (technically loop 11)

label ch2_11:

    $ loop = 11
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    scene bg bedroom

    play music name

    "Morning, day [day]."

    $ outfit = "g"

    if self > 5:
        "Life is looking up."

        "[name] wonders what adventures life will bring next."

    elif self < 3:
        "So, this is dummy text. Enjoy!"

    else:
        "So, this is dummy text. Enjoy!"

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "[name] looks in [pn[psv]] wardrobe and decides to put on a [adj] outfit today."

    "[name] is pleased with the way [pn[psv]] outfit turned out."

# bus part 2

    call ch2_bus

# PE class day 11

    scene bg field pe

    "[name] and [ally] go to PE class. Today, the class is playing tennis."

    "Even though neither of them are very good at tennis, [name] and [ally] teamed up and have a lot of fun standing around and chatting, waiting in between games at the \"overflow\" court."

    "They didn't get a chance to play that much tennis, but chilling in the cool morning sun was rewarding in its own way."

# lunch day 11

    scene bg gym lunch

    "Soon, [name] and [ally] go to lunch."

    $ renpy.show("ally " + a_gender + " smile")

    a "Hey, so, I'm curious how you chose your name."

    n norm "Well, it's kind of embarassing."

    a "Oh, yeah? Now you have to tell me."

    n "Okay. But don't complain when it comes out sappy."

    a "I'm listening."

    n "So, when I was in elementary school, I had a really cool friend named [name]. I really looked up to [pn[obj]] and I wanted to be more like [pn[obj]]."

    a "That's not sappy at all. That's actually a cool reason to pick a name."

    n "I guess."

    a "So, what's the other [name] doing right now?"

    n "Oh, you know, [pn[sbj]] moved away when [psv] dad got a different job. It was different, back then."

    n "We were in fourth grade and after a while, we just kinda lost touch."

    a "Oh. That's kinda sad. Do you still miss [pa[obj]]?"

    n "I guess, sometimes. It doesn't really matter. I bet $sbj doesn't even remember me."

    a "How could [pn[sbj]] forget someone as cool as you? Maybe when we grow up, you can go find [pn[obj]] and say hi or something."

    n "That's a silly idea, [ally]."

    a "Yeah. I moved here this year, and sometimes, I still miss the kids from my old school. I mean, most of them were pricks, but some of them were good kids."

    a "I'd like to think that if I remember them, some of them still remember me."

    n "Yeah. Some of them must."

    a "Anyway, '[name]' is a super cool name and I'm sure the other [name] will be super jealous when [pa[sbj]] finds out you stole [pa[psv]] name."

    n "You can't {i}steal{/i} a name. That's not how names work. I know multiple '[ally]s' at this school."

    a "Sure, but it's cooler when you say it like that."

# biology class day 11

    scene bg classroom biology

    $ happy += 1

    "[name] meets up with [ally] during their biology class."

    "They're finally done with flower parts, and today, [bioTeach] is introducing the class to punnet squares with traits of pea plants."

    n_self "Pea plants are even weirder than flower genders."

    "[ally] leans over and whispers to you."

    a norm "Hey, wanna know an easier way to make smooth peas than all this breeding nonsense?"

    n norm "How?"

    a "Just use glossy paint!"

    "Despite the joke being so bad, [name] can't help but smile."

    "[ally] smiles back as [bioTeach] continues lecturing on dominant and recessive traits."

# book club day 11

    scene bg club front

    "[name] and [ally] go to the afterschool book club."

    n "Hey, [ally], wanna write a story together?"

    a "Huh?"

    n "Well, I really like your ideas, and I thought if we wrote a story together, it'd be an even better story than one either of us wrote separately."

    "[ally] takes a moment to think."

    a "Well, I can't promise it won't be better than something you can do, since you're a way better writer than me, but it's worth a shot."

    n "Sweet!"

    if a_gender == "male":
        $ temp0 = "aliens that only eat fingers"

    else:
        $ tmep1 = "something girly, I don't know"

    "The two of them draft a story about [temp0]."

    "By the time it's time to share, both [name] and [ally] agree that the story is really clever and original."

    scene bg club sharing

    "[name] and [ally] share their story in front of the club, alternating reading paragraphs. Their story is fun, exciting, and weird."

    "The club memebers laugh throughout their tale and by the end are clapping enthusiastically. [name] and [ally] beam proudly."

    scene bg club front

    a "I'm so glad you talked me into writing a story with you. That was so much fun!"

    n "Actually, I kind of got the idea when you presented yesterday. You had really cool ideas, and I wanted to work with your ideas."

    a "Aw, thanks, [name]. I'm glad I met you."

    "[name] can't help but smile."

    n "Me, too."

# Go home day 11

    scene bg school front

    play music outside

    "[name] and $ally walk home together as they've been doing for the past few weeks. It's really cool to walk with a friend along the familar path back home."

    n norm "Hey, $ally, the weekend's coming up."

    $ renpy.show("ally " + a_gender + " norm")

    a "Indeed it is."

    n "Wanna, like, hang out on Saturday?"

    a "Ooh, yeah! Let's go to the pier! It's finally warm enough to just sit by the water without freezing your butt off."

    n "Oh, you've been to the pier when it wasn't freezing before?"

    a "I moved here in the summer. Of course I've gone. Everyone loves the pier."

    n "True that. Sounds like a plan."

    a "Yup. See you Saturday, then."

    n "Can't wait."

    if self > 8:
        $ temp0 = " among a string of good days"
    else:
        $ temp0 = ""

    "Today was a surprisingly good day[temp0]. Life sure is looking up."

    "[name] is ready to start [pn[psv]] weekend."

    $ happy += 1

    if happy < 0:
        $ self -= 1

    elif happy > 1:
        $ self += 1

    $ last_happy =  happy
    $ happy = 0
    $ share = false

    jump ch2_12

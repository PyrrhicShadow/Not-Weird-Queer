# The script for part 1 day 6 (technically loop 6)

label ch1_06:

    $ loop = 6
    $ day += 1
    $ save_name = name + " (" + pn["pn"] + "), Day " + "%s" %day

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    scene bg bedroom

    play music name

    $ outfit = "g"

    "Afternoon, day [day]."

    $ renpy.show("main " + gender + " " + outfit + " norm")

    "After a leisurely Saturday morning of lounging in bed and watching Cartoon Network, it's time to go hang out with [ally]."

    $ verb = v(pn, "put")

    "Feeling more confident than usual, [pn[sbj]] [verb] on a mostly [adj] outfit before heading out."

# head to the park

    scene bg park afternoon

    play music outside

    "[name] meets up with [ally] at the park. They start talking about reading and books."

    n norm "Um, what kind of books do you like to read?"

    $ renpy.show("ally " + a_gender + " smile")

    a "Me? Oh, I like all kinds of books."

    a "I love how stories allow you to gain new experiences and new perspectives that you wouldn't otherwise."

    n "Yeah. That is really cool."

    a "What kind of books do you like to read?"

    hide ally

    menu:
        "What is [name]'s favorite genre of books?"

        "Adventure":
            call ch1_06_adv
        "Romance":
            call ch1_06_rom
        "Science fiction":
            call ch1_06_scifi
        "Fantasy":
            call ch1_06_ftsy
        "Horror":
            call ch1_06_ddlc
        "Mysteries":
            call ch1_06_myst
        "Manga and stuff":
            call ch1_06_weeb

    "[name] smiles at the thought."

    $ renpy.show("ally " + a_gender + " smile")

    a "Hey, what're you smiling about?"

    n "It's just nice to find someone who enjoys books, too."

    a "Yeah. That is nice."

    n "It was my love of reading that led me to join the book club."

    if book == "manga":
        $ temp1 = "create"
    else:
        $ temp1 = "write"

    a "Oh, cool! Do you like to [temp1] [book] outside of the club?"

    n "Well, I like to [temp1] all sorts of things, not just [book]."

    n "But, yeah, I do. It's a really rewarding experience, expressing myself on paper."

    $ renpy.show("ally " + a_gender + " norm")

    a "Yeah. Writing is really fun. I'd love to read some of your other stories sometime."

    n "Haha. Maybe."

    a "Hey, have you thought about other ways of expressing yourself?"

    n "Other ways? Like art?"

    $ renpy.show("ally " + a_gender + " laugh")

    a "Writing is art, silly."

    play music ally

    n "Yeah, I guess it is."

# It's not that easy

    $ renpy.show("ally " + a_gender + " norm")

    a "I notice that sometimes, you dress more gender neutral, but other days, you dress more like a [d_noun]."

    a "Why don't you dress [adj] more often?"

    "[name] gestures to [pn[psv]] vaguely [adj] outfit."

    n "I'm wearing a [adj] outfit today!"

    "[ally] points to [name]'s jacket."

    $ renpy.show("ally " + a_gender + " smile")

    a "That's only vaguely [adj]."

    "[name] frowns, poking at [pn[psv]] own jacket."

    $ renpy.show("ally " + a_gender + " norm")

    n "Well, it's not that easy."

    n "When I write a poem or a short story, most of the time, people don't understand it enough to make fun of me."

    n "But when I try dressing like a [noun], like really going all out…"

    "[ally] puts [pa[psv]] hand on [name]'s shoulder."

    if d_gender == "male":
        $ temp1 = "masculine"
    elif d_gender == "female":
        $ temp1 = "feminine"

    $ renpy.show("ally " + a_gender + " frown")

    a "Hey. I don't know very much about what it's like to be you, but if you don't like being associated with [temp1] things, I'm going to guess that you aren't happy dressing like a [d_noun], either."

    n "Yeah, but it's scary sometimes. I can't just dress like a [noun] because I want to."

    n "People make fun of me and treat me like I'm a monster just because I don't dress or act the way they think I should."

    a "I know, some people can be absolute shitheads, bullying you for no good reason."

    "[ally] stares at the clouds for a moment."

    $ renpy.show("ally " + a_gender + " sad")

    a "I got bullied a lot at my other school, for different reasons."

    n "Oh. I didn't know that. That sucks."

    $ renpy.show("ally " + a_gender + " frown")

    a "Ah, whatever. You live and some people are assholes."

    n "Yeah."

    $ renpy.show("ally " + a_gender + " norm")

    a "But not everyone's an asshole, right?"

    a "It doesn't matter to me that you're really a [noun]. You're a cool person, and I'm glad that you're my friend."

    n "Thanks."

    n "It's rare to find a friend like you."

# You have a choice

    $ renpy.show("ally " + a_gender + " laugh")

    a "Hey, that's no reason to be so cynical."

    n "But, like, there is a reason why I'm not {i}super expressive{/i} about myself."

    $ renpy.show("ally " + a_gender + " norm")

    a "I get that. I can't imagine what it'd be like for the world to think that I'm a [d_noun] and for people to ridicule me for acting like a [a_noun]."

    $ renpy.show("ally " + a_gender + " frown")

    a "That must suck a lot."

    "[name] laughs nervously."

    n "I mean, it's just life. I kind of accept it, now."

    if gender == "enby":
        $ temp1 = " act all gender neutral"

    else:
        $ temp1 = ""

    a "Well, that doesn't seem fair. I mean, why can I act like a [a_noun] but you can't[temp1]?"

    n "I don't know. I just know that if I dress [d_adj] and try to act like a [d_noun], the bullies mostly leave me alone."

    $ renpy.show("ally " + a_gender + " sad")

    a "But you're not a [d_noun]. That's not the real you."

    a "If you don't act like yourself, you're always going to be angry, pretending to be someone you aren't."

    $ renpy.show("ally " + a_gender + " frown")

    n "Yeah. You're right about that. But it's just…"

    "[name]'s not exactly sure how to explain."

# lighten up a little

    $ renpy.show("ally " + a_gender + " norm")

    a "Hey, I get that it's not easy. But nothing worth having is ever easy, right?"

    n "I guess that's true. Yeah."

    play music outside

    $ renpy.show("ally " + a_gender + " smile")

    a "And hey, [name], don't sell yourself short. No one ever laughs at your writing because you're a good writer."

    a "Your stories have a lot of depth to them."

    $ renpy.show("ally " + a_gender + " norm")

    "[name] laughs, trying to see if [ally] was joking."

    if gender == "male":
        $ temp1 = "PewDiePie Let's Plays"

    elif gender == "female":
        $ temp1 = "sentient Pinterest boards"

    else:
        $ temp1 = "topic 2"

    n "Now you're just teasing me. I write about [temp1]."

    $ renpy.show("ally " + a_gender + " laugh")

    a "I liked that one! You had a really confident voice throughout that story."

    $ renpy.show("ally " + a_gender + " norm")

    a "Now, if you could be as confident about yourself as you sound in your writing, you'd be unstoppable."

    n "That's silly."

    "But that idea makes [name] feel powerful."

    hide ally

# Watch the sunset with Ryan

    "[name] and [ally] talk about different things as the day goes by."

    "Spring's here, so the weather is nice and the days are starting to get longer."

    scene bg park sunset

    "Eventually, the sun starts to set. It's probably time to head home."

    # show a cg of ally and main enjoying the sunset

    $ renpy.show("ally " + a_gender + " smile")

    a "Believe in yourself, [name]."

    a "I believe in you."

    n norm "Thanks."

    hide ally

    $ happy += 3
    $ ryan += 1

    jump ch1_06_home

label ch1_06_adv:

    $ book = "adventure"

    n "Huh. I enjoy adventure books."

    $ renpy.show("ally " + a_gender + " smile")

    a "The characters in adventure books are so cool. I wish I could go on cool adventures, too."

    return

label ch1_06_rom:

    $ book = "romance"

    n "Huh. I like romance novels."

    $ renpy.show("ally " + a_gender + " smile")

    a "Romance novels always play out so dramatically, but deep down, they show that all love is the same. Human."

    return

label ch1_06_scifi:

    $ book = "science fiction"

    n "Huh. I enjoy a good sci-fi story."

    $ renpy.show("ally " + a_gender + " smile")

    a "Yeah! I love space ships and robots and aliens. It's so fun to imagine what the future will be like."

    return

label ch1_06_ftsy:

    $ book = "fantasy"

    n "Huh. I like high fantasy."

    $ renpy.show("ally " + a_gender + " smile")

    a "Fantasy worlds are breathtaking. Who wouldn't want to live in a world full of magic?"

    return

label ch1_06_ddlc:

    $ book = "horror"

    n "Huh. I enjoy a good horror story."

    $ renpy.show("ally " + a_gender + " smile")

    a "Isn't it so cool when a horror book takes advantage of your lack of imagination and throws you for a loop?"

    return

label ch1_06_myst:

    $ book = "mystery"

    n "Huh. Can't go wrong with a good mystery novel."

    $ renpy.show("ally " + a_gender + " smile")

    a "A good mystery book is like a good puzzle. I can't put it down until I've solved it."

    return

label ch1_06_weeb:

    $ book = "manga"

    n "Huh. I guess I really like manga and stuff."

    $ renpy.show("ally " + a_gender + " laugh")

    a "Manga? I guess manga is literature. But I got to say, those artists are super talented."

    return

label ch1_06_home:

    scene bg day end

    "[name] goes home feeling lighter about [pn[obj]]self."

    $ verb = v(pn, "try", "tries")

    "Maybe if [pn[sbj]] [verb] to express [pn[obj]]self more, things will start getting better."

    "[name] is ready to start a new week."

    if happy < 0:
        $ self -= 1
    elif happy > 1:
        $ self += 1

    $ last_happy = happy
    $ happy = 0
    $ bus = True
    $ actn = 0

    $ renpy.checkpoint()
    $ renpy.force_autosave(take_screenshot=True, block=True)

    jump ch2

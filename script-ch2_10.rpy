# The script for part 1 day 10 (technically loop 10)

label ch2_10:

    $ loop = 10
    $ day += 1
    $ save_name = name + " (" + n_sbj + "/" + n_obj + "), Day " + "%s" %day

# for now, each morning in the "loop" is the same

    call ch2_morning

# bus part 2

    call ch2_bus

# story sharing day 10
label ch2_10_club_story:

    cp "Any volunteers for sharing today?"

    "[name] looks at [n_pos] story."

    menu:
        "What should [name] do?"

        "Share [n_pos] story":
            jump ch2_10_club_share

        "Do nothing":
            jump ch2_10_club_nothing

label ch2_10_club_share:

    $ happy += 1
    $ share = True

    "$name shares $pos story with the club."

    "They appreciate the odd humor that $sbj put into day 4 topic."

    a "That one was really cool. I told you people would like it."

    n "I'm sure they're only snapping because it's polite."

    a "I'll go after Cami to prove to you that they like your stuff more than mine."

    "[name] rolls $pos eyes, but Cami starts reading before $sbj can reply."

    jump ch2_10_club_ryan


label ch2_10_club_nothing:

    $ happy -= 1
    $ share = False

    "Of course, [ally] notices when [name] doesn't raise [n_pos] hand to share."

    a "You're not sharing today?"

    n "I don't think so."

    a "I really do think people are going to like your thing today."

    n "Nah. I don't really feel like it today."

    a "Well, okay, then I'm going to share."

    n "What?"

    "Before $sbj can say anything more, $ally is already in front of the classroom with $pos notebook."

    jump ch2_10_club_ryan

label ch2_10_club_ryan:

    if share:
        $ temp1 = "Once it's " + a_pos + " turn, "

    else:
        $ temp1 = ""

    "[temp1]$ally reads $pos short poem in front of class."

    if day == (day1 + 2):
        $ temp1 = "strangely bouncy " + book + " poem"

    elif day == (day1 + 6):
        $ temp1 = "philisophical piece about climate change"

    else:
        $ temp1 = "few repeating lines about the life of a cat"

    "It's a [temp1]. $ally's voice shakes slightly as $sbj reads, something that surprises $name as $ally is usually such a fearless, outgoing person."

    "$name snaps enthusiastically for $pos friend, but notices that $ally is right about the other club members."

    "Even though $name thought that $ally's poem was great, the other club members just aren't snapping as loudly for $ally."

    if not share:
        "$name regrets not sharing $pos story, if only for $ally's sake."

    "$ally sits back down next to $name looking exhasted."

    a "So, what did you think?"

    n "I think that was an amazing poem."

    a "Well, nowhere near as good as your stuff. And the audience's snaps agreed, wouldn't you say so?"

    n "Well, I think you did great."

    a "Thanks, but no, I'm just not that good at writing."

    "And that's okay I'm more of a visual artist, anyway."

    "$name frowns. $ally has really great ideas for stories, but it was just that $pos pacing and delivery was a little off."

    "What if there was a way to help $ally solve $pos reading confidence problems?"

    "The other club members are dispersing. It's time to head home." 

    jump ch2_home

################################################################################
## Audio
################################################################################

define config.fade_music = 1.0

define audio.start = "audio/music/im_falling.mp3" # the opening theme
define audio.outside = "audio/music/star_swimming.ogg" # a motif for when the scene is outside
define audio.school = "audio/music/growing_up.mp3" # the game's main theme, used in school and elsewhere
define audio.name = "audio/music/elementary.mp3" # the main character's theme, used in their house and after school
define audio.ally = "audio/music/reckoning.mp3" # the ally's theme, used when having important conversations with the ally
define audio.death = "audio/music/prairie_wolfs_view.mp3" # the theme for when you die or when you dogcheck
define audio.end = "audio/music/die_historic.mp3" # ending theme

define audio.name_dia = "audio/voice/hey.ogg"
define audio.ally_dia = "audio/voice/hey.ogg"
define audio.extra_dia = "audio/voice/oh.ogg"
define audio.adult_dia = "audio/voice/oh.ogg"

################################################################################
## Character Voices
################################################################################

init python:

    renpy.music.register_channel("chara", loop=0.01, mixer="voice")

    def n_voice(event, interact=True, **kwargs):
        if not interact or preferences.self_voicing:
            return

        if event == "show":
            renpy.music.play(audio.name_dia, channel="chara")
        elif event == "slow_done":
            renpy.music.stop(channel="chara", fadeout=0.0)

    def a_voice(event, interact=True, **kwargs):
        if not interact or preferences.self_voicing:
            return

        if event == "show":
            renpy.music.play(audio.ally_dia, channel="chara")
        elif event == "slow_done":
            renpy.music.stop(channel="chara", fadeout=0.0)

    def x_voice(event, interact=True, **kwargs):
        if not interact or preferences.self_voicing:
            return

        if event == "show":
            renpy.music.play(audio.extra_dia, channel="chara")
        elif event == "slow_done":
            renpy.music.stop(channel="chara", fadeout=0.0)

    def t_voice(event, interact=True, **kwargs):
        if not interact or preferences.self_voicing:
            return

        if event == "show":
            renpy.music.play(audio.adult_dia, channel="chara")
        elif event == "slow_done":
            renpy.music.stop(channel="chara", fadeout=0.0)

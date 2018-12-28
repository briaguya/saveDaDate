label hilltop_start:
    scene bg hill with fade
    $ setmusic("audio/hilltop.ogg")


    "You head directly out to Moore's Hill, only to find Felicia has gotten there ahead of you."
    "Given that she lives further away, you assume this means she was in a hurry."
    "The hill is peaceful, and the stars are just starting to come out. You can see the whole town spread out in front of you."

    "Felicia doesn't say anything until you approach, and doesn't even seem to be looking at you."
    "Only after you sit down next to her does she finally acknowledge your presence."

    f "All right. I'm here. And you have some explaining to do."

    $ prompt = "Let's start with the big question.  Just what exactly is going on?  Tell me the truth."

    $ cantHandleTruth_enabled = True
label hilltop_firstMenu:

    menu:
        f "[prompt]"
        "You can't handle the truth!" if cantHandleTruth_enabled:
            f "Very funny. Okay now, seriously."
            $ prompt = "What is going on?"
            $ cantHandleTruth_enabled = False
            jump hilltop_firstMenu
        "Well, see, I'm a wizard...":

            pass
        "I'm actually from the future...":
            pass
        "As it turns out, I have psychic powers!":
            pass
        "Everything here, including you, is a video game that I'm playing...":
            jump hilltop_game
    menu:
        f "Really? Honestly?"
        "Absolutely.":
            f "..."
            f "....."
            f "No."
            f "No, I don't know why, but I don't think you're being honest with me."
            f "And... I'm sorry. But my secret dreams and feelings are not something I'm willing to be lied to about."
            f "Good night."
        "No, not really.":
            "She sighs."
            f "This is dumb."
            f "I don't know why I even came out."
            f "I thought... It doesn't matter."
            f "Sorry to drag you all the way out here for nothing."
        "Actually - one moment. Watch out for that statue." if persistent.d_crushedByStatue:
            f "Wait, what? What are you talking about now?"
            f "Which statue, this one?"
    "She walks over to her bike, parked next to the statue on the top of the hill."
    scene bg hill_statuedeath with vpunch
    "Somehow you're not even surprised when the statue starts to lean, and then topples over, directly onto her."
    $ persistent.d_crushedByStatue = True
    jump standardEnd





label hilltop_game:
    f "...Go on."
    menu:
        f "How does that explain you knowing things I've never told anyone?"
        "This isn't the first time I've played.":
            f "You're saying you played before, and I told you in a different... playthrough?"
        "You did tell me, in an earlier playthrough.":
            f "So it was me that told you, and I just don't remember it, because it didn't happen in this session or something?"

    f "I guess that makes sense, in a Twilight-Zone sort of way."

    menu:
        f "So what's all this about? This game, I mean. What are you trying to do in it?"
        "I'm trying to find a good ending. I haven't found one yet.":
            f "Oh. So us going out to dinner, as planned, must have been a bad ending, then?"
            $ prompt = "What exactly happened at that dinner?"
            pass
        "I'm trying to see as much of the game as I can. I haven't explored this path yet.":
            f "Oh. What have you seen so far?"
            $ prompt = "What would have happened if we'd gone out to dinner like we planned?"
        "You keep dying in stupid ways, and then the game ends. I'm trying to figure out how to keep you alive.":
            f "Oh."
            f "That's pretty dark."
            f "So does that mean I wouldn't have survived if we'd gone out to dinner like we planned?"
            $ prompt = "What exactly would have happened at dinner?"

    $ currentThreat = "bad stuff"

    menu:
        f "[prompt]"
        "You died in a lot of stupid ways.":
            f "Oh. That's pretty vague."
            $ currentThreat = "bad stuff"
        "Well, in one of them, you die from eating peanuts." if persistent.d_peanutAllergy:
            f "Yeah, I guess I am allergic."
            $ currentThreat = "peanuts"
        "Once you died from a being caught in a shootout." if persistent.d_gunfire:
            f "Wait, what? Why were we having dinner somewhere where shootouts happen? I was just planning on the Taco Palace or something."
            $ currentThreat = "gunfights"
        "In one of them, you drowned. Like, in the ocean." if persistent.d_fellInOcean:
            f "Oh. That's kind of random."
            $ currentThreat = "the ocean"
        "You got hit by a car whenever we left the restaurant." if persistent.d_leavingEqualsCar:
            f "Uhg."
            $ currentThreat = "cars"
        "Sometimes you died in a gas explosion." if persistent.d_tookTooLong_burgers:
            f "Oh."
            $ currentThreat = "natural gas"
        "Occasionally you got killed by ninjas." if persistent.d_tookTooLong_thai:
            $ currentThreat = "ninjas"
            f "Wait, seriously? This game is kind of campy, isn't it?"
        "Sea monster." if persistent.d_tookTooLong_tacos:
            f "For real? That's kind of hard to take seriously."
            $ currentThreat = "sea monsters"

    f "Wait a minute. From the way you said that..."

    call countDeaths
    menu:
        f "Exactly how many times have you had to watch me die?"
        "Not that many, actually.":
            f "Really?"
            f "Heh. I get the feeling you're trying to spare my feelings."
            f "Don't worry, I'm not going to freak out on you. But thanks for the thought!"
        "A lot.":
            f "I see."
            f "That doesn't sound good."
        "I've lost count, honestly.":
            f "Oh."
            f "That bad, huh?"
            pass
        "So far? [persistent.totalDeathsSeen] times, in [uniqueDeathsSeen] different ways.":
            f "..."
            f "Geez."
            menu:
                f "I had no idea... And you counted each one?"
                "Every single one.":
                    f "I... I had no idea."
                "No, the game just gave me that number, and I'm trusting that it got it right.":
                    f "Oh."
                    f "I can't decide if that makes the whole thing more macabre or less."

    f "So. Let me get this straight. You're playing a game. A game in which I seem destined to die if we go out to dinner."
    f "So this time, you convinced me to come here instead of going to dinner, because if we go to dinner, I'm basically doomed?"
    $ knowsShesDoomed = False
    $ talkAboutMeta = False
    menu:
        f "So... What does that mean now? Since we didn't go to dinner, am I in the clear?"
        "I don't know yet. Let's find out!":
            f "Fair enough!"
            f "Guess we'll see where this one lands us!"
        "I haven't seen this one yet, but I'm hopeful!":
            f "Well, you're apparently the expert in me dying, so that's probably a good sign..."
        "I'm not sure, but honestly, you've died everywhere else, so I wouldn't get your hopes up.":
            $ knowsShesDoomed = True
            f "Oof. Brutal honesty."
            f "It's okay, though. I can take it. But you'll understand if I hold out hope until the end, right?"
        "No, actually you're still kind of doomed." if persistent.d_fallingStar and persistent.d_aliens:
            $ knowsShesDoomed = True
            menu:
                f "Oh. So why did you bother bringing me here, then?"
                "We can talk longer here. You die a lot sooner if we go to dinner.":
                    f "Hmm. I guess incremental improvement is better than none at all."
                "We talk about different things up here than we do down there, and I need your help. I'm hoping you can help me figure out what I'm missing.":
                    f "Well, I certainly have a vested interest."
                    f "I'll obviously do whatever I can."
                    $ talkAboutMeta = True
                "It's prettier up here.":
                    f "Well, that much is certainly true."


    f "So now what?"
    f "I guess we just talk and see what happens?"
    f "This is all... Too big to take in at once, almost."
    f "I'm kind of out of my depth here."
    "She laughs suddenly."
    f "I was going to say that I've never been in this situation before, so I'm not really sure how to react."
    f "But if what you're saying is true, I've been in this situation a lot of times so far."
    f "I still don't know how to react, though. I'm kind of in shock, and going on autopilot."
    f "I really want to not believe you about any of this, but, somehow, I know you're telling me the truth."

    f "Well, here we are. We've successfully cheated my death, even if it's only for a little bit."
    f "What should we talk about?"

    jump hilltopConversationStartup
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

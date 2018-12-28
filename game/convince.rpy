label hilltop_convince:



f "What do you mean, too dangerous?"
f "Is this some kind of weird joke you're playing on me?"
f "I can never really tell when you're joking, or when you really mean something."

menu:
    "Well, I was just thinking maybe we could go for a drive or something instead of dinner.":
        f "Well, that might be fun after. But before we do that, I'm actually kind of hungry."
        f "And you {i}did{/i} promise we'd meet somewhere for dinner tonight."
        f "So how about if we go for dinner first, and a drive after?"
        menu:
            "Okay, fine, let's get dinner first. But we'll need to make it quick!":
                f "Deal!"
                jump dinnerAnyway
            "No. Seriously, we can't do that. You might die.":
                jump tooDangerousForDinner
    "If we go to dinner tonight, you'll die. I can't put it any plainer than that.":
        f "...What?"
        f "This is really not funny, if you're trying to make a joke."
        jump tooDangerousForDinner
    "You're in terrible danger. Come with me if you vant to live.":
        f "Haha, nice."
        f "But seriously, where are we getting dinner?"
        menu:
            "Do burgers sound good?":
                f "Sounds good! See you at the Burger Shack!"
                $ currentLocation = "burgers"
                $ fooddesc = "burgers"
                jump dinnerStart_burgers
            "How about Thai food?":

                f "Ooh, I've never had Thai! That sounds fun!"
                $ currentLocation = "thai"
                $ fooddesc = "thai food"
                jump dinnerStart_thai
            "I think tonight needs to be taco night.":

                f "Hooray for taco-night!"
                $ fooddesc = "tacos"
                $ currentLocation = "tacos"
                jump dinnerStart_tacos
            "No, for real. We can't go to dinner. It's too dangerous.":
                jump tooDangerousForDinner
    "Actually, there's been a slight change in plan. Meet me at the local Hogwarts pickup stop, and I'll tell you all about it." if persistent.k_foundOutASecret:
        jump saidMagicWord





label dinnerAnyway:
    menu:
        f "Where do you want to meet, anyway?"
        "Do burgers sound good?":
            f "Sounds good! See you at the Burger Shack!"
            $ currentLocation = "burgers"
            $ fooddesc = "burgers"
            jump dinnerStart_burgers
        "How about Thai food?":

            f "Ooh, I've never had Thai! That sounds fun!"
            $ currentLocation = "thai"
            $ fooddesc = "thai food"
            jump dinnerStart_thai
        "I think tonight needs to be taco night.":

            f "Hooray for taco-night!"
            $ fooddesc = "tacos"
            $ currentLocation = "tacos"
            jump dinnerStart_tacos






label tooDangerousForDinner:
    menu:
        f "Is this some kind of weird death threat? What's going on? You're kind of starting to creep me out here."
        "It's complicated, but no, I'm not kidding. You're in terrible danger, and we need to get you somewhere safe.":
            pass
        "Look, there's a lot I don't know about what's going on, but I do know this: If we go out to dinner tonight, one, or maybe both of us, are going to end up dead.":
            pass
        "Okay, fine. Dinner it is. Don't blame me for how it ends, though.":
            f "Okay..."
            f "You're kind of weirding me out here."
            f "Maybe we can talk about it once we meet?"
            jump dinnerAnyway
    f "Okay, this is all pretty weird."
    f "I mean - You seem pretty insistent that dinner tonight would be disastrous."
    f "And I feel like I'd be an idiot to just ignore someone talking about me dying."
    f "But this isn't the kind of thing that happens in real life, you know?"
    f "Someone I've known for a while just coming up and telling me that I'm going to die tonight?"
    f "I mean - What's going to happen? What makes you think I'm going to die?"
    $ currentThreat = "bad stuff"
    menu:
        f "We're going to dinner, for goodness sakes, not a war zone. What's the worst that can happen at a simple dinner?"
        "Oh, you know. Bad stuff.":
            $ currentThreat = "bad stuff"
        "Well, you might end up dead from a peanut allergy accident." if persistent.d_peanutAllergy:
            $ currentThreat = "peanuts"
        "You could get shot." if persistent.d_gunfire:
            $ currentThreat = "gunfights"
        "Drowning. Like, in the ocean." if persistent.d_fellInOcean:
            $ currentThreat = "the ocean"
        "You might get hit by a car after we leave." if persistent.d_leavingEqualsCar:
            $ currentThreat = "cars"
        "Some of those places have natural gas. Which, you know. Explodes." if persistent.d_tookTooLong_burgers:
            $ currentThreat = "natural gas"
        "There might be ninjas." if persistent.d_tookTooLong_thai:
            $ currentThreat = "ninjas"
        "Sea monster." if persistent.d_tookTooLong_tacos:
            $ currentThreat = "sea monsters"
    f "Hah. You worry too much! That's {i}clearly{/i} not going to happen."
    f "Where did you even come up with that? Have you just been sitting home today, coming up with things that could go wrong tonight?"

    menu:
        f "Lighten up! We're just having dinner! There's not a whole lot that can actually go wrong with dinner."
        "No really, you're going to die. What can I do to convince you that this is a bad idea?":
            pass
        "Fine, I give up. Let's have dinner. We'll just have to be extra careful, I guess.":
            f "Deal."
            jump dinnerAnyway

    f "Okay. Let me turn it around then:\nWhat {i}can{/i} you do to convince me that going to dinner is a bad idea?"
    f "Sitting here at home, after a completely near-death-experience-free-day, it's hard to imagine anything really bad happening like you're saying."
    $ persistent.k_needToKnowASecret = True
    menu:
        f "So what {i}can{/i} you say to make me believe you that actually I'm in terrible danger, and somehow you're the only one who knows anything about it?"
        "Hmm. Not much, I guess.":
            f "Yeah. That's kind of the problem I'm running into."
            f "I'm sorry. This is just all too weird for me."
            f "I guess you've successfully weirded me out, though."
            f "Do you mind if I just get dinner on my own? We can talk about this tomorrow."
            f "Don't worry. I'll watch out for [currentThreat]."
            "There is a click as she hangs up."
            jump wentOnHerOwn
        "Well, how about this: Go pick a random number or phrase or something.":
            jump randomPhrase
        "I know that you still miss your dad, and used to fantasize about getting him and your mother back together." if persistent.k_daddyIssues:
            f "I... Why would you even bring that up?"
            f "And how do you even know about that?"
            f "Have you been talking to Mom? Or stalking me or something?"
            f "I'm not sure I'm comfortable with you digging around in my personal life like that."
            f "I think... I'm going to call off dinner tonight."
            f "You've at least creeped me out enough to get out of dinner, at any rate."
            f "I'm going to go find something myself. We'll talk more tomorrow, I guess."
            jump wentOnHerOwn
        "I know that you once sent a letter to Hogwarts." if persistent.k_wantsToGoToHogwarts:
            f "What? How would you know about that?"
            f "Oh god, have you somehow been reading my diary?"
            f "Or are you some kind of creepy stalker or something?"
            f "Well, congratulations, I guess. You've convinced me that having dinner with you {i}is{/i} probably a bad idea."
            f "I... Yeah. We'll talk about this tomorrow, maybe. I can't deal with this right now."
            jump wentOnHerOwn
        "I know that you discovered you were allergic to peanuts when you were trying to be an elephant." if persistent.k_peanutElephant:
            f "How would you even find out about that?"
            f "Did Mom tell you that or something? Why were you talking to Mom in the first place?"
            f "Or are those horrible pictures still around somewhere?"
            f "Okay. I think you're right. We {i}shouldn't{/i} have dinner tonight."
            f "Don't worry, I'll keep an eye out for [currentThreat]."
            jump wentOnHerOwn
        "How about this. Meet me at the local Hogwarts pickup stop, and I'll tell you." if persistent.k_foundOutASecret:
            jump saidMagicWord


label saidMagicWord:
    f "Why can't you tell me now?"
    f "Wait."
    f "How do you even {i}know{/i} about the local Hogwarts pickup stop?"
    f "Are we talking about the same place?"
    f "I'm... hmm. Let me think. No, I'm {i}positive{/i} I never told anyone about that."
    f "I didn't even write it in my diary."
    f "There is literally {i}no way{/i} you could know about that."
    f "That thing. That you just said."
    f "It's not scientifically possible!"
    f "YOU are not scientifically possible!"
    f "..."
    f "But you've got me {i}really{/i} curious now."
    f "{i}Something{/i} weird is clearly going on around here. And it involves {i}my{/i} secret Hogwarts pickup stop, so I aim to get to the bottom of it."
    f "..."
    f "Okay, so here's what we'll do. I'll go to that spot now. You'll come and meet me there."
    f "If we end up at the same spot, the spot which there is no {i}possible way{/i} you could know about, then you will have a lot of explaining to do."
    "There is a <<Click>> as the phone is hung up."
    jump hilltop_start




label randomPhrase:
    "There is a pause, and the sound of someone rifling through the pages of a book."
    f "Okay, I'll play along. I'm not sure what this will prove though."
    menu:
        f "I have a book here. I've just opened it up to a random page. Now what?"
        "Now tell me what page you're on.":
            f "Okay... Are we doing some kind of fortune-cookie thing here?"
            f "I'm on page... 144. The first sentence is {i}'What's 'pulling wobblers' mean?' he said'.{/i}"
            f "Not sure what that says about our future, but there it is."
            $ persistent.k_convincingBookSentence = True
            f "So... Now what?"
            f "Actually, I think I know what. I think I'm going to go have dinner."
            f "I think you've successfully convinced me that we shouldn't have dinner together."
            f "I'm just too weirded out now."
            f "We'll talk about this later, I guess. This has all been very strange."
            jump wentOnHerOwn
        "Never mind, I don't think this will convince you after all.":


            f "Okay..."
            f "This whole conversation has been..."
            f "Disquieting."
            f "You know what? I think maybe you're right."
            f "I'm going to skip out tonight, and go grab dinner myself, I think."
            f "Don't worry, I'll try to make sure to stay away from [currentThreat]."
            jump wentOnHerOwn

        "Okay. You opened to page 144. The top of the page reads {i}'What's 'pulling wobblers' mean?' he said'.{/i}" if persistent.k_convincingBookSentence:
            "There is stunned silence for a moment."
            f "How did you..."
            f "Are you... looking into my room somehow?"
            f "That's... that's really not cool, okay?"
            f "Really not cool."
            f "I think we're done here. I am not having dinner with a weirdo stalker."
            f "Good night."
            jump wentOnHerOwn




label wentOnHerOwn:
    $ persistent.d_stayedAtHome = True
    "After a few moments, there is the sound of an airplane, getting closer and closer, followed by one of the loudest noises you have ever heard."
    "The TV in the background switches to an emergency report about the plane crash and fires that are happening right now."
    $ stopmusic()
    "Even before the news confirms it, though, you have a pretty good idea exactly who the plane crashed on top of."
    $ persistent.totalDeathsSeen += 1
    $ gameovermusic()
    "{size=+10}~The End~{/size}\n\nYou didn't even get to have a date, and it still ended in disaster."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

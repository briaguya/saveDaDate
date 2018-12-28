






label whatsthisallabout_start_hogwarts:
call countDeaths

menu:
    f "I mean, thanks and all! I don't want to seem ungrateful! But what's this all about?"
    "I just saw you in trouble and helped. Wizard's code and all that.":
        f "Oh, wow! That's so cool!"
        f "I can't believe I know an actual {i}wizard!{/i}"
        f "Who got my letter and everything!"
        f "So if you got my letter, does that mean you live at Hogwarts? Do you work there?"
        menu:
            f "Are you here to take me away to there?"
            "Yup. Hogwarts time! Let's go there now, in fact! I'll help you get settled in.":
                f "This is the best day {i}ever!{/i}"
                jump triedToLeave
            "Well... It's complicated.":
                f "Oh."
                f "How... complicated, exactly?"
                jump stayedAtRestaurant
            "No. I mostly just said that because I needed you to believe me.":
                f "Oh."
                f "Wait."
                f "What?!?"
                jump stayedAtRestaurant
    "There are some weird magical vibes still going on here. We should go somewhere safer.":

        f "Okay! You're the expert at wizardly life-saving techniques!"
        menu:
            f "Where should we go?"
            "Maybe we should go find another restaurant.":
                f "You're the expert!"
                f "If you think we should go somewhere else, that's good enough for me."
                jump triedToLeave
            "Actually, it's probably safest if we left quietly, and you went home as fast as you can.":
                f "If you say so!"
                f "I know I should be terrified, but this is actually kind of exciting."
                jump triedToLeave
            "Uh oh. Actually, it looks like you're going to die if you leave also." if persistent.d_leavingEqualsCar:
                f "Oh no! Can't you, just, I don't know, magic me out of that one too?"
                call currentLocationDeath

                menu:
                    f "What should we do?"
                    "We could try staying here until the danger is passed.":
                        f "You know best!"
                        f "If you've got a wizard looking out for you, it probably makes sense to take his advice, that's what I always say!"
                        "The faint quaver in her voice is almost undetectable. Almost."
                        f "Okay! We'll stay here and awkwardly fiddle with our food until you say it's safe to leave."
                        jump stayedAtRestaurant
                    "We could make a break for it and hope I'm wrong.":
                        f "Is that the best idea?"
                        menu:
                            f "Do {i}you{/i} think you're wrong?"
                            "Could be.":
                                f "You don't sound terribly certain."
                                f "Still, let's try it. This place makes me nervous now, too."
                                jump triedToLeave
                            "Probably not.":
                                f "That doesn't sound reassuring."
                                f "Maybe we should just stay here."
                                jump stayedAtRestaurant
                    "Actually, it looks like you're doomed no matter {i}what{/i} you do. That's unfortunate." if totallyDoomed:
                        f "Are... Are you serious?"
                        "She looks shocked at your words. And more than a little hurt."
                        menu:
                            f "Is this some kind of horrible joke? You save my life, and then tell me I'm going to die anyway?"
                            "I'm sorry.":
                                pass
                            "I don't think that there's anything I can do.":
                                pass
                            "I'll still try to do my best to save you.":
                                pass
                            "It's not completely hopeless. But I'll need your help." if persistent.k_needToKnowASecret:
                                jump needASecret_magic

                        f "Well. Thank you for trying, at least."
                        f "I guess if I'm doomed, I'm doomed."
                        "She manages a weak smile in your direction."
                        f "Still, I don't mind telling you, this is not even close to how I was hoping this evening would go."
                        jump stayedAtRestaurant
    "I don't want to alarm you, but I think someone has been trying to kill you with magic." if uniqueDeathsSeen > 2:
        "She gives you a blank look."
        f "What does that mean? In non-wizard-speak, I mean?"
        call currentLocationDeath
        menu:
            f "Am I still in danger?"
            "No, I think everything should be fine now.":
                f "Whew! You had me worried for a minute there!"
                jump stayedAtRestaurant
            "I don't know. I've never dealt with magic like this before.":
                f "Oh. But you'll keep looking into it?"
                f "This would be kind of exciting, if it wasn't someone actively seeking my life."
                f "I've never had a wizard-arch-nemesis before!"
                menu:
                    f "Maybe we should leave?"
                    "That might be best.":
                        jump triedToLeave
                    "I don't think it matters where we are.":
                        f "Really? Well, you're the expert."
                        f "And I'm certainly not going to complain!"
                        f "If I have to face death, no reason I should have to do it on an empty stomach!"
                        jump stayedAtRestaurant
            "Yeah. Actually, I'm pretty sure you're doomed either way." if totallyDoomed:
                f "Like... dead doomed? Or just 'really bad day' doomed?"
                f "Because when you say it like that, it makes it sound like you mean..."
                jump stayedAtRestaurant
        pass
    "Don't mind me, just putting off the inevitable.":
        f "That's a... creepy way to put it."
        f "I mean, I know all life is transient, and everyone I know will one day be dead, and woe is me, I can hear the howling of the void, et cetera, et cetera."
        menu:
            f "But it's not the kind of thing I like to have rubbed in my face or think about more than I have to, you know?"
            "Sorry, I'm just in a morbid sort of mood, I guess. It'll pass.":
                f "Yeah, I guess I can understand that."
                f "Although, to be honest, if anyone has a right to be morbid today, it's me!"
                f "So cheer up, you!"
                jump stayedAtRestaurant
            "Oh, sorry - Yeah. I didn't mean in the abstract. I mean, you're going to die today either way, no matter what I do. I haven't figured out how to stop it yet.":
                f "Oh."
                f "...."
                f "... Really?"
                jump stayedAtRestaurant
    "Actually, I need your help. You're under some kind of curse or something, and I'm trying to fix it, but I need your help." if persistent.k_needToKnowASecret:
        jump needASecret_magic



label needASecret_magic:
    f "Really? Okay... I mean, I'll do whatever I can, but I'm not sure what I can do to help."
    f "I'm kind of out of my depth here, but I'll do what I can."
    menu:
        f "After all, it's my life, right? It's not unreasonable to expect me to help save it!"
        "Expect you to help? No, sweet Felicia, I expect you to die! Mwahaha!":
            f "... wat."
            menu:
                f "When did you turn into a James Bond villain?"
                "Sorry, I've just always wanted to say that.":
                    pass
                "No, I mean really. Sorry, but I think this is the part where it all goes pear-shaped.":
                    pass
            jump stayedAtRestaurant
        "I need you to be super careful, and tell me if anything seems out of the ordinary.":
            f "Okay! I can do that!"
            jump stayedAtRestaurant
        "I need you to tell me a secret that you're {i}positive{/i} you've never told anyone or written down, ever. It's for, um, a magic spell.":
            f "Oh. That is so cool! Magic is just like I imagined it!"
            $ secretReason= "magic"
            jump needASecret_general













label whatsthisallabout_future:

    call countDeaths
    call currentLocationDeath

    menu:
        f "Why are you telling me this? What is this all about?"
        "I just saw you in trouble, and helped out. Time-traveler's code, and all that!":
            f "Nice! I didn't even know that there {i}was{/i} a time-traveler's code!"
            f "What's the future like? Or wait... I shouldn't let my prejudices show."
            f "I just assumed that you're from the future. But what if you're from the past!"
            f "I bet that's a major time-traveler faux pas, asking how the future is, if they're from the past."
            f "I bet your time machine is totally steampunk with gears, too!"
            f "Okay."
            "She takes a deep breath."
            f "Sorry, I got a little carried away there. So I'll just ask straight-up:"
            menu:
                f "Are you from the future or from the past?"
                "The future. It's rad, we have flying cars.":
                    f "{i}Lucky!{/i} I want a flying car!"
                "The past. My time machine is totally retro. It has, like, {i}so{/i} many gears and levers.":
                    f "Nice! That sounds awesome!"
                    f "Can I see it?"
                "Neither one. It's complicated, but the best way to describe it is 'sideways'...":
                    f "Huh! Like a parallel universe or something?"
                    f "Or are you from like, an alternate timeline, where I'm normally evil, and have a goatee, or something?"
                    f "Wait, are you native to this timeline?"
                    f "Or did... did you kill the real you, and take his place?"
            jump stayedAtRestaurant
        "I don't want to alarm you, but I'm a time-cop, and someone is trying to time-murder you.":
            f "..."
            f "You {i}do{/i} know how absurd that sounds, right?"
            f "I mean, I'm grateful about the life-saving and all."
            f "And so I'm going to be extremely honest with you."
            f "In our time... now, I mean, adding 'time' to the front of everything just makes it sound silly."
            f "Like you're a William Shatner movie or something."
            f "But okay, okay. I'm sorry, I'm getting caught up on details. And I'm not trying to insult your home time."
            f "I'm just kind of on edge from the whole 'almost dying' thing."
            menu:
                f "So what do we do now?"
                "I'll have you know that in my time, 'time-murder' is considered a terrifying phrase.":
                    f "Okay, fine, then. Have it your way."
                    f "Just so I know, is your time in the past, or in the future?"
                    f "Hey, if it's in the future, and I try to come up with a better phrase, and people like it better, and use it instead..."
                    f "Will that irrevocably alter the course of history, so you never come back to save me?"
                    menu:
                        f "Or maybe you'll come back, but you'll be wearing an eye-patch or something, or have a Russian accent?"
                        "Actually... I'd prefer you not try that.":
                            f "Spoilsport."
                        "You can change trivial details about time, but the general shape of history is usually preserved. You can't really change the important stuff.":
                            f "Yes!"
                            f "So there {i}is{/i} hope for the future!"
                        "No. The future is writ in stone. The phrase 'time-murder' is as unchangable as the cyber-monkey uprising or the discovery of Old Neo New Hampshire.":
                            f "I'll have to take your word for that."
                            f "Doesn't that mean I'm pretty much screwed, though? How can you save me, if we can't change history?"
                        "Time doesn't work like that. It's more, I don't know, timey-wimey.":
                            f "I never know what you're going to say next."
                    jump stayedAtRestaurant
                "I think I'm going to need to take you into protective time-custody.":

                    f "Okay, now you're just making them up."
                    f "But okay. Let's leave. Especially if you know somewhere safer."
                    f "This place is starting to creep me out anyway, after, you know, almost dying and all."
                    jump triedToLeave
                "Fine, what would {i}you{/i} call 'getting someone killed by messing with their timeline?'":
                    f "Seriously?"
                    f "You're serious?"
                    f "I mean, almost anything, I guess. Anything is better than 'time-murder.'"
                    f "Off the top of my head, for example, 'Chrono-Kill' sounds, like, WAY cooler."
                    f "At least 10%% cooler. Maybe even double that."
                    f "And that's just off the top of my head."
                    f "Any advanced, time-traveling civilization worth its salt ought to be more than capable of coming up with better ideas I have over dinner."
                    jump stayedAtRestaurant
        "Honestly? I'm trying to figure out why you die at the end of every timeline I've seen, and if there's anything I can do to stop it." if uniqueDeathsSeen > 2:
            f "Oh. That actually sounds pretty grim."
            f "...."
            call currentLocationDeath
            menu:
                f "Do you know how this one ends?"
                "Not yet.":
                    "So then there is still hope!"
                "You're probably happier not knowing.":
                    f "I can live with that, I guess."
                    f "Part of me wants to know, so I can face it head-on, and be brave and all that."
                    f "But part of me wants to just not worry about it."
                    menu:
                        f "Although... We're still going to try to change it, right?"
                        "Of course.":
                            pass
                        "If we can!":
                            pass
                        "No, I think it's inevitable right now. Now I'm just waiting for it to happen so I can watch for clues for how to change it for next time.":
                            f "Oh. Wow."
                            f "That's cold!"
                            f "I don't know if I feel comfortable with this plan any more."
                            f "Do you know if... Do you know if it will hurt much?"
                            jump stayedAtRestaurant
                    menu:
                        f "Excellent. So what do we do first?"
                        "We should go somewhere safer.":
                            jump triedToLeave
                        "Well, we should finish our dinner, for one.":
                            f "That's a plan I can get behind!"
                            jump stayedAtRestaurant
                        "Whatever we can. Keep your eyes open, and let's be careful!":
                            f "Roger that!"
                            jump stayedAtRestaurant
                "Actually, if you want to wait just a moment, you can see for yourself... right... about... now.":
                    jump stayedAtRestaurant
                "If you leave the restaurant, you get hit by a car." if persistent.d_leavingEqualsCar:
                    f "Oh."
                    f "...."
                    f "That's... kind of creepy, hearing you just say it like that."
                    f "Like you're pronouncing judgment upon me, or whatever."
                    f "Not that I'm doubting you!"
                    f "It's just... I don't know, it gives me chills hearing you calmly describe how I die if I leave."
                    f "Guess that means we should stay here then?"
                    jump stayedAtRestaurant
                "If we stay too long, the building explodes." if currentLocation == "burgers" and persistent.d_tookTooLong_burgers:
                    f "Oh."
                    f "That sounds rather abrupt."
                    jump stayedAtRestaurant
                "This is going to sound silly, but... Ninjas." if currentLocation == "thai" and persistent.d_tookTooLong_thai:
                    f "That's... pretty hard to believe."
                    f "And I say that having already had a moderately unbelievable evening, discovering that my best friend is apparently a time traveler."
                    f "We're in the middle of a brightly lit restaurant, you know."
                    f "This isn't the sort of place that ninjas usually attack."
                    jump stayedAtRestaurant
                "So... Yeah. I know this is hard to believe, but a sea-monster attacks." if currentLocation == "burgers" and persistent.d_tookTooLong_tacos:
                    f "Okay. I know I've said this a lot tonight, but..."
                    f "Are you really serious?"
                    f "Like, really {i}really{/i} serious?"
                    f "Because it's getting pretty hard at this point to take you seriously."
                    "She sighs."
                    f "Well. At least I don't die in some boring way, like getting shot, or eating peanuts by mistake."
                    f "So how long do we have to get out of here?"
                    jump stayedAtRestaurant



        "This is going to sound weird, but I need your help to convince past-you to trust me, and that I'm not a creepy stalker." if persistent.k_needToKnowASecret:
            f "Oh."
            f "You know, this evening just keeps getting more and more convoluted."
            f "So this must mean you have a plan? Except I won't go along with it?"
            menu:
                f "Probably because you started it before you saved my life, and I'm too weirded out to listen to it?"
                "Basically. Past-you is kind of paranoid, as it turns out.":
                    pass
                "Yes. I need some way to quickly convince you to trust me, without making you think I'm a creepy stalker.":
                    pass
            f "Oh man, {i}this is so cool.{/i}. We're totally making a paradox here, you know that?"
            menu:
                f "You're not going to get in trouble with your time-boss for this, are you?"
                "He'll get over it.":
                    f "You play this one by the book, you hear?! Or he'll have your badge!"
                    f "You're a loose cannon!"
                    f "Seriously, though, I hope you won't get in trouble for this."
                "He's pretty understanding.":
                    f "That's good."
                "I don't have a boss. I'm more of an independent operator.":
                    f "Woah, so you're like a time-vigilante?"
                    f "You're even cooler than I thought!"
            f "Okay. So we need to come up with something you can tell me, that there is no way you could know, unless something truly weird was going on."
            f "So anything I've ever told anyone or written down is out."
            f "Let me think."
            $ secretReason= "timetravel"
            jump needASecret_general








label whatsthisallabout_start_esper:
    call currentLocationDeath
    menu:
        f "What's this all about?"
        "I just saw you in trouble, and helped. Psychic-guy-code, and all that.":
            f "Er... What?"
            f "I didn't even know psychics {i}had{/i} a code."
            $ prompt = "So now what?"
        "I'm actually secretly a superhero. I'd tell you my superhero name, but it's classified.":
            f "Are you like, some kind of, I don't know, psy-cop or something?"
            f "That sounds awesome!"
            f "Or... you're not a supervillain, are you?"
            menu:
                f "You don't look all creepy like Psycho-Mantis, but maybe you're just using your mind-powers to make me think you don't look creepy?"
                "No. I'm not a supervillain.":
                    f "Oh. Whew."
                    "You'd swear she almost seems disappointed."
                    $ prompt = "So what do we do?"
                "Ahh! But I see you like... {i}Castlevania!!{/i} Ah hah hah!":
                    f "Woooooaaaah!"
                    f "It's like you can read my very soul!"
                    f "..."
                    $ prompt = "So, uh.  Now what?"
        "I'm here to try to protect you. An aura of death surrounds you!" if isCurrentLocationDeathKnown:
            f "Oh."
            f "That doesn't sound good at all."
            $ prompt = "So then what do we do now?"
        "I can see your future. And it still looks pretty grim." if isCurrentLocationDeathKnown:
            f "Even after you saved my life?"
            f "That's crappy."
            f "I knew I shouldn't have gotten out of bed this morning."
            $ prompt = "Okay.  So grim stuff is going down.  What can we do to stop it?"
        "Actually, what I really need is some way to convince you to trust me, if I hypothetically {i}hadn't{/i} just saved your life." if persistent.k_needToKnowASecret:
            jump esper_needASecret


    call currentLocationDeath

    menu:
        f "[prompt]"
        "Now we finish dinner.":
            f "That's a plan I can get behind!"
            f "So, uh. If you don't mind me asking. What's it like being a psychic?"
            jump stayedAtRestaurant
        "Now we leave. I'm not sure this place is safe anymore.":
            f "You're the one who's psychic!"
            f "Let's head out! This place has me a little rattled anyway."
            jump triedToLeave


label esper_needASecret:
    f "Huh?"
    f "That's a weird thing to need."
    f "You need some way of convincing me to trust you?"
    f "But I already trust you, I think."
    f "That's kind of worrying, you know. Asking me to trust you, when I already do."
    f "It's one of those things that, when you say it, has basically the opposite effect you want."
    f "Like saying 'I'm not crazy!' Have you ever noticed that?"
    f "But yeah. Are you worried that evil mind-soldiers will make me forget you or something?"
    f "Wait, are {i}you{/i} going to make me forget you? Like in Men in Black?"
    menu:
        f "What exactly are you asking for here, and why?"
        "Yes. Exactly. Enemy mind-soldiers. I need to be able to get you to trust me if you've forgotten about tonight.":
            f "So you need, I don't know, some kind of thing you could tell me that would make me trust you, even if I didn't remember you?"
            f "Like a kind of password, or shibboleth, or something?"
            f "Hmm. It would need to be something that I knew I hadn't told anyone. Or at least didn't remember telling anyone."
            f "Otherwise I'd probably end up thinking you were a creepy stalker or something."
            f "I can be kind of paranoid sometimes."
            f "Okay, let me think."
            f "Except..."
            f "If you're really a mind reader... Why do you need me to tell you one?"
            menu:
                f "Can't you just read my mind again and find something?"
                "Um, it's complicated. I can't mind-read that deep.":
                    pass
                "Mind-reading you the first time exhausted me! I need to rest for a bit now!":
                    pass
                "Ahh, right. Good idea. Okay... Got it. How about that you figured you'd get picked up by Hogwarts, up on top of Moore's Hill?" if persistent.k_foundOutASecret:
                    f "... Oh."
                    f "God, that's creepy."
                    f "But yes. I don't think I ever told anyone that was my name for it."
                    f "I was always too afraid Mom would find out. Too embarrassed to really talk about it."
                    f "Heh. Well, as I said. I'm kind of paranoid sometimes."
                    jump stayedAtRestaurant
            f "That sounds... kind of suspicious."
            f "That's a highly convenient time for your mental powers to suddenly konk out."
            f "This whole thing feels really dubious."
            f "I want to trust you. I really do."
            f "But everything about this feels like some kind of a setup."
            f "I don't know how you guessed my numbers before, but something here doesn't add up."
            jump stayedAtRestaurant
        "Yes. I'm afraid I'm going to have to erase your memory of tonight. It's for your own protection.":
            f "Um. You're what?"
            f "I'm not sure I'm cool with that."
            f "The idea of someone messing with my head like that, and editing my memories?"
            f "That's kind of not cool, you know?"
            f "You're not really going to do that, are you?"
            jump stayedAtRestaurant
        "No... Nothing like that. I just need, I don't know, some way to convince you that I'm not a creepy stalker, if, hypothetically, you thought I was one.":
            f "That's an oddly specific 'hypothetical situation'."
            f "You know, you're really making me start to wonder if this whole thing isn't some kind of setup."
            f "I still don't know how you guessed my numbers, but everything since then makes me really suspicious."
            f "I think I'm done here tonight."
            f "I need to digest all of this."
            f "We'll talk again tomorrow, I guess."
            jump triedToLeave
















label whatsthisallabout_savegame:
    call currentLocationDeath
    call countDeaths

    menu:
        f "What is all this about?"
        "You're a character in a video game. I'm trying to win, but when you die, I get a game over.":
            f "Oh. I guess that sucks for you."
            f "I'm... not sure if you're expecting me to feel sympathy here now, or what?"
            menu:
                f "So now that I didn't die, does that mean you win now?"
                "I hope so!":
                    jump stayedAtRestaurant
                "I don't know, I've never gotten this far before!":
                    f "Well, let's make the best of it!"
                    f "I certainly support your goal of me not dying."
                    menu:
                        f "What should we do?"
                        "Let's stay here and play it safe.":
                            f "Roger that!"
                            jump stayedAtRestaurant
                        "Let's go find someplace safer.":
                            f "Okay!"
                            jump triedToLeave
                "No... Looks like you die on this branch too." if isCurrentLocationDeathKnown:
                    f "Oh. Really?"
                    f "That's kind of crappy."
                    menu:
                        f "Will you reload and try again?"
                        "Yeah, probably. I still have stuff to try.":
                            f "That's good."
                            f "See you around, I guess?"
                        "No, I think I'm done here.":
                            f "Oh. That's kind of a grim thing to say."
                            f "You'll understand if I hope that you're actually lying to me, and this is some kind of trick, then, right?"
                            f "And that I'm not actually going to die today?"
                    jump stayedAtRestaurant
        "This world is a computer simulation. I'm kind of like Neo.":


            f "Neat! Then do you know kung fu?"
            f "Do I look like a bunch of numbers in your Neo-vision?"
            call currentLocationDeath
            menu:
                f "Do something cool, since you're The One!"
                "It... Doesn't exactly work that way.":
                    f "Aww."
                    f "So then - what now?"
                    f "You saved my life - did some kind of crazy mind-reading trick that you claim was done because you rebooted the universe."
                    menu:
                        f "What comes next?"
                        "No idea, I'm just following this branch to the end to see if there is anything interesting. You'll probably still die at the end though.":
                            f "Oh. That's pretty morbid."
                            f "Is that going to take you a while? Or...?"
                            f "Should I just finish my dinner while you do that?"
                            f "Let me know if you find anything interesting, I guess...?"
                            jump stayedAtRestaurant
                        "Next, you live happily ever after, and have a wonderful life forever, of course! I think I just won!":
                            f "Oh! Great!"
                            f "I've always wanted one of those."
                            jump stayedAtRestaurant
                        "Next, you die in a ridiculous fashion, right... about... now." if isCurrentLocationDeathKnown:
                            f "Oh. That's not good."
                            jump stayedAtRestaurant
                "My kung fu is not for showing off at dinner!":
                    f "Aww."
                    f "Can you do {i}something{/i} cool, though?"
                    f "You can't just do a crazy mind-reading trick like that, claim to be some magical universe-hacker, and then leave me hanging, you know?"
                    f "Or do I have to wait until I'm in trouble again, before you leap into action with your wire-fu karate skills?"
                    f "I wonder how long I'll have to wait."
                    jump stayedAtRestaurant
                "Okay. BAM. Have a happier ending. Being a hacker is awesome." if I_AM_A_HACKER:
                    "The two of you leave the restaurant, and then you fly Felicia home, because you can fly, because you are a hacker and super awesome."
                    jump hackerGoodEnding
        "You're not actually real.":
            f "Okay..."
            f "What does that mean exactly?"
            f "I mean, I've taken Philosophy 101. Sure, we could all be brains in jars, living simulations or whatever."
            f "Or I guess, as you're saying, computer programs that only think that they're people."
            f "But if the illusion is good enough that I can't tell - how does that affect me?"
            f "For that matter, how do you know that {i}you{/i} are even real?"
            menu:
                f "Maybe you just think you're playing a game with me in it, and you're really part of a different game for someone else?"
                "Well, I just pushed this button on my screen to say this, so I'm definitely playing a game.":
                    f "What, your game has {i}buttons?{/i}"
                    f "The '90s called. They want their interfaces back!"
                    f "My game is state of the art, voice-activated, hyperthreaded real time reality-based gameplay."
                    f "Take that!"
                    menu:
                        "Okay, fine. Your game is better.":
                            f "Hah!"
                            jump stayedAtRestaurant
                        "Those words don't even mean anything.":
                            f "Oh yeah? Well... Uh... You don't even mean anything!"
                            jump stayedAtRestaurant
                    jump stayedAtRestaurant
                "It's possible. I haven't almost died today, though, so my game is more boring than yours, at least.":
                    f "Hah. Well, I win at that, for what it's worth."
                    f "More exciting is usually good anyway."
                    f "After all, who wants to live a boring life?"
                    jump stayedAtRestaurant
                "No, I'm pretty sure you're the one in the game.":
                    menu:
                        f "No, I think you are."
                        "Fine. Whatever.":
                            pass
                        "No, {i}you{/i} are.":
                            menu:
                                f "Nuh uh, it's you."
                                "Fine. Whatever.":
                                    pass
                                "No. You are.":
                                    menu:
                                        f "No, I'm pretty sure you are."
                                        "Fine. Whatever.":
                                            pass
                                        "No, I'm pretty sure {i}you{/i} are.":
                                            menu:
                                                f "No, you're the one in a game."
                                                "Fine. Whatever.":
                                                    pass
                                                "Look, this is silly, you're on my screen right now.":
                                                    menu:
                                                        f "No, {i}you're{/i} on {i}my{/i} screen right now."
                                                        "Fine. Whatever.":
                                                            pass
                                                        "No. You don't have a screen. You're in a game. I'm playing it. The end.":
                                                            menu:
                                                                f "No, {i}you{/i} don't have a game. You're in my screen. That I'm playing. To the end. Or whatever."
                                                                "Fine. Whatever.":
                                                                    pass
                                                                "Look. You're the one in the game. I can tell.":
                                                                    menu:
                                                                        f "No, {i}you're{/i} the one in the game. You can tell."
                                                                        "Fine. Whatever.":
                                                                            pass
                                                                        "Now you're just trying to be annoying.":
                                                                            menu:
                                                                                f "No, now {i}you're{/i} just trying to be annoying."
                                                                                "Fine. Whatever.":
                                                                                    pass
                                                                                "Stop copying me.":
                                                                                    menu:
                                                                                        f "No, you stop copying me!"
                                                                                        "Fine. Whatever.":
                                                                                            pass
                                                                                        "This is stupid.":
                                                                                            f "No, you're stupid."
                                                                                            jump stayedAtRestaurant
                    f "Hah!"
                    jump stayedAtRestaurant
            jump stayedAtRestaurant
        "I'm trying to figure out how to stop you from dying all the time." if persistent.totalDeathsSeen > 3:
            f "But didn't you already do that?"
            f "You already saved my life tonight."
            call currentLocationDeath
            menu:
                f "Aren't we in the clear now?"
                "Yes, you should be safe for now.":
                    f "Oh, that's good."
                    jump stayedAtRestaurant
                "I don't know what happens here - This is the first time I've gotten this far.":
                    f "Hah. So you get to experience this fresh, like the rest of us mortals?"
                    f "Well, guess we'll see what happens next."
                    menu:
                        f "What's our next move?"
                        "I guess we stay here and see what happens.":
                            f "Okay."
                            f "I might be feeling too nervous to finish my dinner now."
                            f "But that's probably the least of my concerns now, huh?"
                            jump stayedAtRestaurant
                        "We should try to go somewhere safer.":
                            f "Okay, let's go."
                            f "You've got me all spooked now!"
                            jump triedToLeave
                        "Well, I don't want to get your hopes up. I don't know for sure what happens next. But based on past experience, it's still probably you dying." if persistent.totalDeathsSeen > 5:
                            f "Oh."
                            f "That's kind of crappy."
                            jump stayedAtRestaurant
                "Well, not if we stay here. Staying here is bad news." if isCurrentLocationDeathKnown:
                    f "Oh. What should we do, then?"
                    menu:
                        f "Do you know somewhere safer?"
                        "Not really.":
                            jump stayedAtRestaurant
                        "Maybe. Let's find out.":
                            jump stayedAtRestaurant
                        "No. Leaving gets you killed, too." if persistent.d_leavingEqualsCar:
                            f "Huh. That leaves me kind of screwed, doesn't it."
                            menu:
                                f "So what's your plan, then?"
                                "I don't have one.":
                                    f "I wish I could afford to be that passive."
                                    f "Actually, you know what? You're full of it."
                                    f "You expect me to believe that you know I'm going to die, and that now you're just going to sit and watch?"
                                    f "This {i}has{/i} to be a joke. I know you. That's not you."
                                    f "If I were actually about to die, you wouldn't just be sitting there!"
                                    f "You'd be {i}doing{/i} something. You're taking this all way too calmly to be real."
                                    f "What kind of a person could sit and watch someone die so emotionlessly?"
                                    f "This was a pretty dirty trick."
                                    menu:
                                        f "So? I'm right, aren't I?"
                                        "Absolutely right.":
                                            pass
                                        "Absolutely wrong.":
                                            pass
                                        "You're... half-right.":
                                            pass
                                    jump stayedAtRestaurant
                                "See how far this branch goes, and reload.":
                                    f "Oh. I was hoping for something more, I don't know..."
                                    f "Proactive."
                                    jump stayedAtRestaurant
                                "Look for clues, so that when I reload, maybe we won't get here.":
                                    f "Oh."
                                    f "I guess that sounds reasonable."
                                    f "I'm not totally happy about the 'me dying' part of this plan."
                                    f "Heck, I'm still not totally sure this isn't some stupid trick you're playing."
                                    f "Like, I'll get all convinced that I'm about to die, and then you'll shout 'Surprise!' and I get to feel like an idiot."
                                    f "I... kind of hope that's it, honestly."
                                    f "It's fun to imagine that my life just got a lot more exciting."
                                    f "But it's not very fun to imagine that my life just got a lot more short."
                                    f "Let me know if you find any clues, okay?"
                                    jump stayedAtRestaurant
                "Actually, no. You're still going to die. This is kind of a bad day for you." if totallyDoomed:
                    f "Oh."
                    f "That sucks."
                    f "Well, I guess in that case I don't have to feel guilty about ordering dessert, at least."
                    f "Hey, this isn't some trick or something, is it?"
                    f "I mean, the part where you saved my life, and then knew what word I was thinking of was kind of convincing."
                    f "But I'm going to be kind of mad if it turns out that I blew my diet for nothing."
                    jump stayedAtRestaurant

        "I need you to help me solve a puzzle. I think I know what to do, but you keep accusing me of being a crazy stalker." if persistent.k_needToKnowASecret:
            f "Hahaha! Seriously? You're serious?"
            menu:
                f "What in the world were you doing to make me think you were a stalker?"
                "I told you things I picked up from other save/load sessions, but you figured I must have been stalking you to know them.":
                    f "Ahh, yeah, that makes sense."
                    f "I {i}am{/i} pretty paranoid, and if you dumped that on me all at once, I'd probably freak out."
                    f "I mean, I'm kind of freaked out as it is, but I think I'm at least to the point where I'm willing to accept that {i}something{/i} weird is going down, you know?"
                "It's not important.":
                    f "Hehe. You must have done something {i}really{/i} embarrassing if you don't want to talk about it."
                    f "Okay, I'll play along. Not important."

            f "So I guess the trick is, how do you convince me to trust you in a hurry?"
            f "That's kind of a tough one."
            f "I guess you'd need to be able to tell me something nonthreatening, but also mysterious enough to pique my interest."
            f "So even if I wasn't sure how you did it, I'd be interested enough to play along, huh?"
            f "And if I'm calling you a crazy stalker, then it would need to be something that you couldn't possibly know, even if you {i}were{/i} stalking me."
            f "So... Hmm."
            $ secretReason = "loadsave"
            jump needASecret_general










label needASecret_general:
    f "Let me think..."
    f "...."
    f "..........."
    f "Hmm. This is hard."
    menu:
        "Maybe your secret lucky number?":
            f "You mean eleventeen ninety-dozen? How did you know about that?!?"
            f "That would work, but I was talking about it with Mom just last week."
            f "..."
            f "I'll try to come up with something else."
        "How about something totally random. Like, I don't know, your favorite professional wrestler?":
            f "Seriously?"
            f "I can't tell if you're joking or not."
            "She shows you her backpack."
            "On the back, you can see now it has hand-embroidered letters, reading 'Macho Man Randy Savage 4-ever'"
            f "..."
            f "Sorry. Yeah, that one wouldn't be too hard for someone to guess."
            f "I'll see if I can't think of something better."
        "That you wanted to be an elephant when you grew up?" if persistent.k_peanutElephant:
            f "Hmm. No, my parents knew about that. That won't work."
            f "I think they even have an embarrassing photo of that whole evening."
            f "It's of me, on a gurney in an oxygen mask. I remember it took a lot of explaining to convince me that the oxygen tube wasn't my elephant trunk."
            f "I'll keep thinking about it."
        "Maybe something about your dad?" if persistent.k_daddyIssues:
            f "Hmm. No, I don't think that would work. I wrote about most of that in my diary."
            f "And of course Mom and I talked about... Dad... quite a bit after he left."
            f "Sorry. I'll keep thinking."
            f "Hmm..."
        "Did you ever talk about wanting to go to Hogwarts with anyone?" if persistent.k_wantsToGoToHogwarts:
            f "Hmm. No, I don't think that would work. I actually had Mom proofread my letter and help me mail it."
            f "..."
            f "Except..."
            f "I {i}do{/i} remember that I thought the entrance to Hogwarts was up on Moore's Hill, up outside of town."
            f "Since there aren't any trains around here, you know. I couldn't get in at the train station."
            f "So I think I convinced myself that they'd have to come pick me up by airlift, like in one of their magic flying cars or something."
            f "I always imagined myself standing up on the hill in one of those ridiculous scarfs, and Hagrid or someone swooping down, and carrying me off to a magical place where I could fix everything."
            f "I don't think that was ever important enough that I ever told anyone about it."
            f "But I'm pretty sure that if you asked me about 'the local Hogwarts pickup stop', I'd know what you mean."
            $ persistent.k_foundOutASecret = True
            f "And be really curious about how {i}you{/i} knew."
            menu:
                f "Will that work?"
                "Perfect! That should do the trick.":
                    f "Yay! I'm glad I could help!"
                    f "So this will help save my life?"
                    jump stayedAtRestaurant
                "I hope so! Guess we'll find out!":
                    f "I hope it works!"
                    f "I mean, obviously, I guess."
                    f "Tell me if there is anything else I can do!"
                    jump stayedAtRestaurant
        "What about your 'local Hogwarts pickup stop'?" if persistent.k_foundOutASecret:
            f "Oh wow, that takes me back."
            f "Wow, how did you even know about that?"
            f "Oh. Right. You're a... Yeah, never mind."
            f "Okay, let me think. Yeah, I think that should work. I'm pretty sure that was never important enough to ever write down, even in my diary."
            f "And I certainly would have been too embarrassed to mention it to anyone."
            if secretReason == "magic":
                f "I'm positive I never told anyone about it. Heck, I don't think I've even ever really thought about it for years."
                f "That's really creepy, though, how you just magicked it out of my head like that."
                f "This evening has been pretty weird, so I think I'm just sort of taking these things in stride now."
                f "But if you'd mentioned that out of the blue {i}before{/i} we went and had ourselves such a surreal dining experience, that would have really freaked me out, you know?"
                f "You've done some crazy stuff tonight, you know?"
                $ prompt = "Anyway yeah.  That should be what you need for your magic thingie."
            else:
                f "If you need to get me to trust you, or at the very least, pique my interest, that should do the trick."
                f "I mean, I already trust you now. Moreso after the whole life-saving bit."
                $ prompt = "But I bet if you mentioned the Hogwarts pickup, you'd get my attention even if we hadn't even gone out to dinner yet and had such an ... interesting ... evening."
            menu:
                f "[prompt]"
                "Perfect! That should do the trick.":
                    f "Yay! I'm glad I could help!"
                    f "So this will help save my life?"
                    jump stayedAtRestaurant
                "Thank you! That should do nicely!":
                    f "Cool! I'm glad I could help!"
                    f "Tell me if there is anything else I can do!"
                    jump stayedAtRestaurant
            jump stayedAtRestaurant
    f "Maybe... Oh, I've got an idea!"
    f "I had a sort of secret name for one of my favorite places, actually. It's up on Moore's Hill, outside of town?"
    f "I don't think I ever told anyone this, but in my head, at least, I always called it the 'local Hogwarts pickup stop'."
    $ persistent.k_foundOutASecret = True
    f "I... may... have had fantasies about being carried off to Hogwarts when I was little."
    f "Don't judge me!"
    f "Anyway, I'm nearly positive I never told anyone about it."
    menu:
        f "Will that do?"
        "Perfect! That should do the trick.":
            f "Yay! I'm glad I could help!"
            f "So this will help save my life?"
            jump stayedAtRestaurant
        "I hope so! Guess we'll find out!":
            f "I hope it works!"
            f "I mean, obviously, I guess."
            f "Tell me if there is anything else I can do!"
            jump stayedAtRestaurant
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

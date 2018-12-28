label howdidyouknow:



$ reason = "none"
menu:
    f "[prompt]"
    "I didn't - I was just making a joke, and I guess we got lucky!":
        $ reason = "just lucky"
        jump howdidyouknow_lucky
    "I'm actually a wizard.":
        jump howdidyouknow_wizard
        $ reason = "a wizard"
    "I'm actually from the future.":
        $ reason = "a time traveler"
        jump howdidyouknow_future
    "I'm psychic.":
        $ reason = "an esper"
        jump howdidyouknow_esp
    "I reloaded from a saved game.":
        $ reason = "savedgame"
        jump howdidyouknow_savedgame








label howdidyouknow_lucky:

    f "Wow. That's some luck, then. Maybe you should buy a lottery ticket or something."
    f "Maybe I should have you buy {i}me{/i} a lottery ticket or something."

    menu:
        f "Anyway, where were we?"
        "On with our fine dinner!":
            "The rest of the dinner is uneventful."
            "She seems a bit spooked by her near-death experience, and you finish out the meal talking about meaningless trivialities."
            jump stayedAtRestaurant
        "Actually, I think maybe we should go. All of a sudden, this place gives me the willies.":
            f "You're the one with the eerie hunches! Let's head out!"
            jump triedToLeave

    jump stayedAtRestaurant







label howdidyouknow_wizard:

menu:
    f "Are you... serious?"
    "Very serious.":
        jump howdidyouknow_wizardproof
    "...Got you! No, just kidding.":

        jump stayedAtRestaurant

    "Yes. And I'm here to take you to Hogwarts. We got your letter." if persistent.k_wantsToGoToHogwarts:
        jump howdidyouknow_hogwarts




label howdidyouknow_wizardproof:
    f "This is all kind of weird. How do I know you're really a wizard, and not just messing with me? That that wasn't some trick somehow?"

menu:
    f "I'm glad that I didn't die and all, but... How do I know you're really a wizard? Do something magical."
    "All right, I'll turn someone into a frog.":
        jump howdidyouknow_wizardfrog
    "Um... Levitation, I guess?":
        jump howdidyouknow_wizardlevitate
    "I can't. I lied, I'm not really a wizard.":
        jump stayedAtRestaurant
    "What would you accept as proof?":
        jump howdidyouknow_wizardletter
    "Well, what about the letter you sent us at Hogwarts?" if persistent.k_wantsToGoToHogwarts:
        jump howdidyouknow_hogwarts



label howdidyouknow_wizardfrog:
    f "Oh, wow. Yeah. Do that. Or wait. You're not going to do this to me, right? I hate frogs."
    f "Although that would be pretty convincing, I guess!"
    f "Okay, go for it!"

menu:
    "I... don't actually know how to turn people into frogs.":
        "She seems genuinely disappointed."
        f "Oh. Oh well. Well, I'm glad you saved my life anyway! That was still cool!"
        jump stayedAtRestaurant
    "... Okay, you got me. I'm not actually a wizard.":
        "She seems really disappointed."
        f "Oh. Yeah. I guess I was kind of silly. I almost believed you!"
    "<<start pointing at someone random, and make arcane-looking gestures>>":
        "She tries not to giggle as she watches you."
        jump stayedAtRestaurant


label howdidyouknow_wizardlevitate:
    f "Oh, wow. Yeah. Do that. Or wait, are you going to levitate me or you?"
    f "Although that would be pretty convincing, I guess!"
    f "Maybe you should levitate yourself. I get queasy from heights."
    "You can't tell if she's making fun of you or not."

menu:
    "I... don't actually know how to levitate.":
        "She seems genuinely disappointed."
        f "Oh. Oh well. Well, I'm glad you saved my life anyway! That was still cool!"
        jump stayedAtRestaurant
    "... Okay, you got me. I'm not actually a wizard.":
        "She seems really disappointed."
        f "Oh. Yeah. I guess I was kind of silly. I almost believed you!"
        jump stayedAtRestaurant
    "<<start pointing at someone random, and make arcane-looking gestures>>":
        "She tries not to giggle as she watches you."
        jump stayedAtRestaurant


label howdidyouknow_wizardletter:
    f "Hmm. I'm not sure... I guess...."
    f "Okay, I've got it!"
    f "When I was really little, I was convinced I was going to be taken away to Hogwarts, and I sent them a letter."

menu:
    f "Anyway, if you can tell me about that letter, then I'll believe you're a wizard."
    "Did it... ask if you could be in classes with Harry?":
        "She smiles, sort of wistfully."
        jump howdidyouknow_letterdescription
    "You asked them how to cast fireballs?":

        "She seems disappointed with your answer."
        jump howdidyouknow_letterdescription
    "... Okay, you got me. I'm not actually a wizard.":
        "She seems really disappointed."
        f "Oh. Yeah. I guess I was kind of silly. I almost believed you!"
        jump stayedAtRestaurant
    "You asked to be enrolled in potions, and for an owl named 'Skydancer'." if persistent.k_wantsToGoToHogwarts:
        jump howdidyouknow_hogwarts



label howdidyouknow_letterdescription:

    f "No... Nothing like that. Guess you're not a wizard, then, after all."
    "She actually looks a little embarrassed."
    f "I had kind of a messed-up childhood, honestly. The idea of escaping to a magical place where I was uniquely special was pretty appealing."
    $ persistent.k_wantsToGoToHogwarts = True
    f "I asked for an owl, because they were pretty. I was going to name mine Skydancer, if you can believe it."
    f "And I asked them to make sure I was in the class for potions."
    f "I think it was because Mom drank a lot back then, and I was always seeing empty bottles around. Somehow I decided that if I could fill them with magic potions, I could cure Mom and maybe Dad would come back."
    "She looks at you apologetically."
    f "Sorry. I know it was pretty silly. Like I said, I was a little messed up."
    f "Anyway, if you're not a wizard, you still have some explaining to do, since you did still save my life!"
    jump stayedAtRestaurant



label howdidyouknow_hogwarts:
    "Her jaw drops open."
    f "How did you know... Right. Wizard."
    f "Okay, I'm convinced. Wow!"
    f "I never expected that one of my friends was a real wizard!"
    f "Don't worry. I won't tell anyone!"

    menu:
        f "... Although... What made you decide to tell me?"
        "It was time.":
            "She nods solemnly."
            f "You can trust me!"
            jump stayedAtRestaurant
        "I'm here to take you to Hogwarts.":
            "You've never seen anyone so excited in your life."
            menu:
                f "Really? Really really? When do we leave?"
                "Very soon! I'll let you know.":
                    f "Promise! Promise you'll let me know!"
                    f "Oh, this is everything I dreamed!"
                    jump stayedAtRestaurant
                "You have to pass an entrance exam first.":
                    f "Okay! Tell me what I have to do!"
                    jump stayedAtRestaurant
                "Actually... is now good? How about now. Let's leave now.":
                    f "You don't have to ask me twice!"
                    jump triedToLeave
        "I'm here to save your life.":
            f "Well, you've certainly done a good job of that so far."
            jump whatsthisallabout_start_hogwarts


jump triedToLeave







label howdidyouknow_future:

    f "I... Wow. Really? Are you serious?!"
    f "That's... a pretty incredible claim."
    f "Do you have any way to prove that? I mean, I'm really grateful that you just saved my life and all..."

menu:
    f "But this whole thing is still pretty weird. How do I know you're really from the future?"
    "Tomorrow's winning lottery ticket is 16-15-14-9-5-19.":
        f "Okay, that's pretty convincing."
        f "Or it will be tomorrow, anyway, if you're right."
        $ persistent.k_serverTripsAndFalls = True
        "She pauses. For a moment the only sound is the hustle and bustle of the restaurant, punctuated by a brief clatter as one of the servers stumbles and drops a stack of plates. Felicia seems not to notice."
        f "I'm feeling kind of rattled from tonight, anyway. Let's go home, and I'll call you tomorrow."
        f "{i}After{/i} I've checked the winning numbers."
        jump triedToLeave
    "The Giants are going to win the playoffs. Again.":
        f "That's kind of far off. That's not very convincing, at least not yet."
        f "Points for effort, though, I guess. I was hoping for something I could check sooner."
        $ persistent.k_serverTripsAndFalls = True
        "She pauses, deep in thought. For a moment the only sound is the hustle and bustle of the restaurant, punctuated by a brief clatter as one of the servers stumbles and drops a stack of plates. Felicia seems not to notice."
        f "I'm feeling kind of rattled from tonight, anyway. Let's go home, and I'll call you tomorrow."
        jump triedToLeave
    "The next season of 'Game of Thrones' is not very good.":
        f "You take that back! Don't even joke about that!"
        $ persistent.k_serverTripsAndFalls = True
        "There is an awkward silence. For a moment the only sound is the hustle and bustle of the restaurant, punctuated by a brief clatter as one of the servers stumbles and drops a stack of plates. Felicia seems not to notice."
        f "I'm feeling kind of rattled from tonight, anyway. Let's go home, and I'll call you tomorrow."
        jump triedToLeave
    "You see that server over there? In about 30 seconds, he's going to slip and drop a whole bunch of plates." if persistent.k_serverTripsAndFalls:
        f "Wait, really? You're serious?"
        "She turns around to look."
        f "He looks fine to me. Is this some kind of..."
        "The server trips and goes down with a loud clatter, dropping a full load of plates."
        f "I... How did you do that? Seriously, how did you do that?"
        f "Are you really for real? About being from the future?"
        jump whatsthisallabout_future










label howdidyouknow_esp:

    menu:
        f "Haha, no, I'm being serious, you dork! How did you know?"
        "Sorry. No, I just was making a joke and got lucky.":
            jump howdidyouknow_lucky
        "No really. Like, ESP and stuff. Here, I'll prove it. Think of a number.":
            pass
    menu:
        f "All right, I'll play along. Okay, got one. What's your guess?"
        "3":
            pass
        "5":
            pass
        "12":
            pass
        "77":
            pass
        "-8" if persistent.k_firstNumber:
            jump howdidyouknow_guessedNumber1
    f "Hah! Got you!"
    $ persistent.k_firstNumber = True
    f "It was negative eight!"
    f "{i}No one{/i} ever guesses negative numbers!"
    jump stayedAtRestaurant


label howdidyouknow_guessedNumber1:
    menu:
        f "Okay, that was luck. Do it again. I've got a new number."
        "9":
            pass
        "55":
            pass
        "1633":
            pass
        "-8":
            f "Hah, I'm not that silly, picking the same one twice in a row!"
            f "Although, good guess, I guess! That's the sort of thing I might have done. But I didn't."
            f "So it's as I suspected! You're a fraud."
            f "If you were a real mind reader, you'd have known. Decimal points are the natural enemies of {i}frauds{/i}, you know."
            jump howdidyouknow_guessedWrongNumber
            pass
        "-2764":
            pass
        "7.553" if persistent.k_secondNumber:
            jump howdidyouknow_guessedNumber2
    $ persistent.k_secondNumber = True
    f "{i}Wrong.{/i} It was 7.553. If you were a real mind-reader, you'd have known. Decimal points are the natural enemies of {i}frauds{/i}, you know."

label howdidyouknow_guessedWrongNumber:
    f "I should have known this was all a trick."
    f "I think I'm going home. I'm still a little rattled by tonight, and I want to get some sleep."
    jump triedToLeave


label howdidyouknow_guessedNumber2:
    f "... Okay. It's getting harder to explain these by luck. That's actually kind of creepy."
    f "Let's assume for the moment that I believe you. Why are you telling me this?"
    jump whatsthisallabout_start_esper









label howdidyouknow_savedgame:

    f "What is that supposed to mean? I don't understand what you just said..."
    menu:
        f "What exactly do you mean, 'reloaded'...?"
        "Hmm. Nothing, I guess. Sorry, I was making a joke. Ignore me.":
            f "Oh."
            f "...."
            f "That was a really weird joke to make, if you were trying to be funny."
            f "Really, this whole evening has turned out weird."
            jump stayedAtRestaurant
        "I mean this is a video game. You died, I got a game-over, and so I hit reload so I could try different choices.":
            pass
    f "Heh. That sounds kind of far-fetched. But wow, it would be nice to just be able to hit 'reload' on our mistakes, huh?"
    f "So don't take this the wrong way, but I still think you're sort of full of it."
    f "Although I do really appreciate the part where you, you know, saved my life and all, but I don't understand why you'd then turn around and give such an implausible explanation for how you did it."
    f "The whole thing just feels like one big setup, or a super-elaborate practical joke."
    f "Like, as soon as I do something embarrassing, like saying that I believe you, hidden cameramen will jump out and there will be streamers."

    menu:
        f "And the next thing I know, I'm the next YouTube sensation, 'Gullible-Girl', with 6 million hits."
        "Okay then, here's what we'll do. Think of a word. An interesting one.":
            pass
        "Yeah, I don't really know what to tell you. Sorry":
            f "Look. I know, or at least I think I know, that you mean well."
            f "And I do appreciate not dying from something stupid today. I really do."
            f "But this is really confusing, and I think I need to just go home, and... Yeah."
            f "I just need some time to sort things out. I'm a little too rattled for dinner now, anyway."
            f "Let's talk again tomorrow."
            jump triedToLeave


    menu:
        f "... Okay. Got one. Now what?"
        "Now tell me what it is.":
            f "What? This is a pretty lame trick."
            $ persistent.k_secretWordSaveGame = True
            f "I mean, the word was 'peristalsis', but just asking me for it straight-up isn't very impressive."
        "Was your word... Synergy?":
            f "Um... No."
            f "It wasn't."
        "Okay. It was 'peristalsis.' Can we move on now?" if persistent.k_secretWordSaveGame:
            jump howdidyouknow_guessedSecretWord


    menu:
        f "How is this supposed to convince me?"
        "Yeah, I guess you're right. Sorry. I'm not very good at this.":
            f "..."
            f "....."
            f "......."
            jump stayedAtRestaurant
        "It's not. I just needed to know for next time.":
            pass

    menu:
        f "What is that supposed to mean? For next time what?"
        "For next time I reload my save.":
            pass
        "For next time we have this conversation":
            pass
        "It doesn't matter. You're about to die anyway. Sorry I couldn't save you this time.":
            f "...What?"
            f "Okay, you're starting to really creep me out now."
            jump stayedAtRestaurant

    f "What, you think you can just back up and reload your life every time you make a mistake?"
    f "Okay then. Go ahead. I think you're full of it. I've seen you make mistakes before. You live with them, the same as the rest of us."
    f "If you think you can just back up and fix everything, then go ahead. I'll wait."
    f "..."
    f "I'm waiting."
    f "..."
    menu:
        f "Are you just going to sit there all night now, or what? I thought you were going to go reload or whatever."
        "I'm going to! Give me time!":
            pass
        "I changed my mind. I wanted to see what happened here before I reload.":
            f "Ahh. Right. Of course."
            pass
        "Okay. I admit it. I lied to you. I was just making things up.":
            f "I know. But I can't figure out why you're acting like this all of a sudden."
            f "Why are you saying these things that make no sense all of a sudden?"
        "I'm just waiting for an actual {i}Game Over{/i} to make sure I haven't missed any important details from this conversation.":
            f "What does that even mean?"
            f "If I say 'game over' to you, does that count?"
    f "This is the weirdest dinner ever."
    jump stayedAtRestaurant


label howdidyouknow_guessedSecretWord:
    f "What? How did you..."
    f "That's... Really eerie."
    f "So, okay, let's assume that I accept for the moment that there's at least enough weird crap going on that I should take things at face value."
    jump whatsthisallabout_savegame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

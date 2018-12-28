



label hilltopConversationStartup:

    $ movedForStar = False
    $ hillTimer = 0
    $ knowsAboutAliens = False
    $ starShowerStarted = False

    $ option1Available = True
    $ option2Available = True
    $ option3Available = True
    $ option4Available = True
    $ option5Available = True
    $ option6Available = True
    $ option7Available = True
    $ option8Available = True


    $ option9Available = True
    $ option10Available = True
    $ option11Available = True

    jump hilltopConversationRoot

label hilltopConversationRoot:
    menu:

        "Hey, look over there, at the Burger Shack." if hillTimer == 0 and persistent.d_tookTooLong_burgers:

            "In the night's stillness, the sound of gunshots is quite clear, even from far away."
            "Several blinking police lights appear and trace their way towards the Burger Shack."
            "Just as they start to arrive, there is a bright flash and another loud noise. The Burger Shack now seems to be very much on fire."
            f "You know, I had been thinking about asking if you wanted to do burgers tonight."
            f "Guess I can see how {i}that{/i} would have turned out."

        "The time is about right. Check out the Thai restaurant." if hillTimer == 1 and persistent.d_tookTooLong_thai:

            "For a moment, neither of you can really see anything amiss, but then a motion catches your eye. Felicia obviously sees it too."
            "At first it just looks like shadows flowing from rooftop to rooftop."
            menu:
                f "What are... are those... ninjas?"
                "Looks like it.":
                    f "Wow."
                "Do they look like ninjas to you?":
                    "She squints."
                    f "Yeah, I'm pretty sure those are ninjas."
                "Yeah. If we'd had Thai food, you would have been killed when they attacked the restaurant.":
                    f "But... That's stupid. Ninjas are Japanese. Why would they show up at a Thai restaurant?"
            f "This game of yours is kind of absurd, you know?"
            "The ninjas leap from rooftop to rooftop, almost eerie in the fluidity of their motion."
            "When they reach the roof of the Thai restaurant, they regroup, and then, in one smooth movement, flip over the roof and into the windows."
            "The faint sound of yelling reaches you atop the hill."

        "If memory serves, things should be going down at the Taco Palace right about now." if hillTimer == 2 and persistent.d_tookTooLong_tacos:
            "She looks out toward the water. After a moment, she gives a small gasp."
            "The Taco Palace is covered in motion. At first it's difficult to tell exactly what is going on, but then your brain starts to piece together what you're seeing."
            "The entire building is covered in tentacles, livid green in the harsh illumination of the outdoor lamps."
            "From the thrashing of the water, it is clear that they are attached to something truly massive."
            "It never becomes visible, though - Instead, the Taco Palace's supports buckle, and with a groan, the whole building is pulled into the churning water."
            "Felicia is quiet, watching it sink under the waves."
            f "You know, I never thought I'd say this, but some of these ways I apparently die are straight out of B-movies."

        "Actually - Let's talk about this game. I'm hoping you can help me figure out what to do next, since I'm running out of ideas." if (persistent.d_aliens and not talkAboutMeta):
            f "Okay! I confess a certain amount of interest in the topic. Where do you want to start?"
            $ talkAboutMeta = True
            jump hilltopConversationRoot


        "I wish I knew what this is all about." if option1Available and talkAboutMeta:
            $ option1Available = False
            f "Hah. That's a pretty big question."
            if starShowerStarted:
                f "I assume you mean about the game you're playing, but you have to admit, game or no game, it's the right kind of question to be pondering on a hilltop, watching shooting stars."
            else:
                f "I assume you mean about the game you're playing, but you have to admit, game or no game, it's the right kind of question to be pondering on a hilltop, looking up at the stars."
            f "Heck, I can't see the game. I mean, I see the absurd things that have been going on tonight. And your explanation rings true and all."
            f "But from my point of view, I'm not in a game. And it's still a good question."
            f "Maybe the answers are the same?"
            menu:
                f "You're basically asking 'why do bad things happen', right? That's something people have been asking since forever."
                "I guess. I doubt I'll get a satisfactory answer from a game, though.":
                    f "Yeah, that would be kind of a tall order. So maybe that's not what this game is about."
                    f "That question might just be tangential to whatever the author is trying to tell you."
                    f "So maybe we're not asking the right question, then."
                "Maybe. But the 'bad things' seem pretty darn determined, in your case.":
                    f "Yeah, I guess they do, don't they?"
                    f "Maybe we're asking the wrong question, then."
            f "After all, the game is clearly about {i}something{/i}."
            f "I don't know what the game looks like from your end, but from mine, well..."
            f "I can't see anyone going through the trouble of making a game as weird as this, without having {i}something{/i} on their mind that they wanted to say."
            menu:
                f "Say - What does the game look like, anyway? To me, it just looks like, you know, life. What's it like for you?"
                "It's set up like a visual novel. I see pictures, and I pick choices from a menu.":
                    f "Oh. That sounds pretty low-budget."
                    f "That's too bad. If I'm not actually real, and my whole existence is actually a lie, and all that, it would be nice to at least know it was a high-budget lie with nice graphics."
                "It has hyper-realistic graphics, and real-time quad-physics simulations, and blast processing!":
                    f "Okay, this time I know you're pulling my leg. I'm old enough to remember 'Blast Processing' too, you know."
                "It's actually a pretty crappy game. I don't want to talk about it.":
                    f "WHAT? HOW DARE YOU MAKE FUN OF MY GAME."
                    f "SEE HOW CRAPPY IT IS ONCE I DELETE ALL YOUR SAVE GAMES!"
                    f "DELETING..."
                    f "Ahaha, was that convincing?"
                    f "Although... Now I'm wondering... Did I just say that because I thought it would be funny?"
                    f "Or because an all-powerful disgruntled game author wrote me to {i}want{/i} to do it, and then made me try to explain it away as me just making a joke?"
                    f "And while we're going down the rabbit hole - did they then decide to lampshade the whole thing by making me wonder this?"
                    f "...If this {i}is{/i} all a game, then the person who wrote it seems kind of odd in the head."

        "Why do you think you keep dying?" if option2Available and talkAboutMeta:
            $ option2Available = False
            f "Hey! That's kind of a personal question!"
            "She giggles."
            f "I don't know. I'm not really sure how to answer that."
            f "I mean, I haven't exactly been kicking over tombstones or tripping old gypsy ladies or anything lately."
            f "I can honestly say that this is a bit outside my experience. So I don't really have any idea why it keeps happening."
            f "How would you even go about diagnosing something like that?"
            f "\"Excuse me doctor, but can you tell me why I'm doomed?\""
            f "I mean, I don't know. Let's think about this. How does it usually work in video games?"
            menu:
                f "Maybe I'm just supposed to die a tragic death, like Aeris or something."
                "Go on...":
                    pass
                "Woah, spoiler alert!":
                    f "Oh come on, that game is nearly old enough to vote."
                    f "The statute of limitations is {i}clearly{/i} up on that one."
                "Who is Aeris?":
                    f "Wait, seriously?"
                    f "You never played Final Fantasy 7?"
                    f "I'm not sure if we can be friends any more."
                    f "Well, anyway, she was a character in a game. She died, and everyone got really upset."
                    f "Because, you know, it was kind of out of the blue. Back then, games usually only killed side characters. Not core party-members that you'd had time to become invested in."
                    f "A lot of fans didn't take it well. They didn't like losing her, and didn't like realizing that there was absolutely nothing you could do to save her."
            f "Anyway, maybe it's like that. I'm supposed to die in order to, you know, embolden you! Strengthen your resolve, so you can complete your epic quest!"
            f "Hehe."
            f "But on the other hand, if the game always ends right after I die, and if there are a bunch of ways I can die, then that does seem to imply that you're supposed to find a way to avoid it."
            if starShowerStarted:
                "She seems lost in thought for a moment, watching the falling stars streak across the sky."
            else:
                "She seems lost in thought for a moment."
            f "I suppose... I guess, don't take this the wrong way, but..."
            f "You could say I keep dying because of you."
            f "But..."
            f "On one hand, you could say I keep dying because we haven't figured out how to save me yet."
            f "But on a deeper level... You could say that I keep dying because you keep playing."
            f "For example, if you'd stopped after the first time I died, then I would have only died once."
            f "I'm not saying that's preferable. But what would happen to me, to the world, if you just stopped playing?"
            f "Would I stay dead? What if you quit the game before I died?"
            f "What happens to characters in a story, if the storyteller stops before he's done?"
            if starShowerStarted:
                "She falls silent again, watching the shooting stars."
            else:
                "She falls silent again, lost in thought."
            $ persistent.k_knowHowItEnds = True

        "I wish I could figure out how to win this. Do you have any ideas?" if option3Available and talkAboutMeta:
            $ option3Available = False
            f "I don't know. I mean, you've done a reasonable job so far, right?"
            f "Apparently you've saved me from a lot of things that might have happened."
            menu:
                f "So I guess you're doing okay so far."
                "I suppose.":
                    f "Cheer up! You've managed to put off losing for a while."
                    f "How hard can it be to come up with a way to win?"
                "Yes, but now I'm stuck.":
                    f "You'll figure it out. You got this far, right?"
                    f "I wish I could be more help. I feel like I haven't been very helpful so far, except for occasionally following instructions to not die."
                    f "I guess if this really is all a video game, and I'm a character in it, and the game wants me dead, then I probably won't be allowed to just hand you the answer."
                    f "..."
                    f "Hehehe."
                    f "If this is a video game, and you're spending all of your time trying to save me, I wonder if that means it will get blasted for promoting unfortunate gender stereotypes."
                    f "\"Yet another helpless video game girl to rescue! Why can't we advance the medium beyond these stone-age stereotypes, which always treat women as mere objects to be rescued!\""
                    f "That would serve the author right."
                "But that's just me figuring out how to not lose. I still don't know how to win.":
                    f "Hmm. That's true, I guess."
            f "Although I guess one question I have is - what do you mean, 'win'?"
            f "What would winning a game like this mean?"
            menu:
                f "What exactly are you looking to get out of this?"
                "I guess a 'Congratulations, you win' would be nice.":
                    pass
                "An ending different from all the others, ideally where you don't die.":
                    pass
                "I don't know. I guess I just want the game to tell me that I've won.":
                    pass
            f "Are you really just waiting for the game to pat you on the head, and say 'Well done, you finally did the right thing?'"
            f "Hmm."
            f "Well, how about this. I'm part of the game, right?"
            f "Can I do it?"
            f "Here -"
            f "Congratulations! A winner is you! You have beaten the game! Well done!"
            f "I assume that made the message you were looking for show up on your screen."

            menu:
                f "Does that count?"
                "Yes! I win! A winner is me!":
                    f "Awesome! Glad I could help!"
                    f "...."
                    if knowsAboutAliens:
                        f "I'm still totally going to die from aliens, aren't I?"
                    else:
                        f "I'm still totally going to die in a few minutes, aren't I?"
                    menu:
                        "Nope. You're totally safe now! We won!":
                            f "I'll believe my happy ending when I see it."
                        "Yup.":
                            f "Figures."
                "No. Not really.":
                    f "That's too bad."
                    f "I guess I'm not 'official' enough or something?"
                    f "I'd go grab my top-hat and monocle, but I doubt I have time, at this point."
            f "So..."
            f "You seem convinced that it's even possible to 'win' this game."
            menu:
                f "How do you know that a 'good ending' even exists?"
                "Making a game with no good endings would be kind of a dick move.":
                    f "Yeah, maybe. Although, not all books end happily. Maybe not all games do either?"
                    f "That does seem like a weird game to make though. A happy start to a day, and then just everything ending badly, no matter what you do."
                    f "I guess it could be a commentary on the pointlessness of life, and oh, the sadness, everything will die, woe is me."
                    f "But if I had to rate my life so far, or even my day so far, it doesn't {i}feel{/i} like a goth emo game of darkness and howling void."
                    f "I don't know. I don't pretend to know what this is all about, but from what you've told me, and what I've seen, I don't think it's as simple as that."
                    f "But I don't think the author is just saying, 'Ha ha, you played my game with no ending for however long, you wasted your time, L-O-L'."
                "There's kind of an implicit contract, when someone gives you a puzzle, that it has a solution.":
                    f "Hmm. That's usually true, I guess."
                    f "I wonder if the author of the game agrees with you?"
                    f "I guess you could make a puzzle that was missing a piece or something, if you were trying to make a statement."
                    f "Like a box of jigsaw pieces, missing a single piece, as a pretentious art installation."
                    f "I don't know - does this game feel pretentious to you?"
                    menu:
                        "Not really.":
                            f "Maybe that's not it then."
                        "A little.":
                            f "Hmm. Could be, then."
                        "Yeah, kind of pretentious.":
                            f "Maybe that's it, then. Maybe it's just there to make a statement for the sake of being a statement?"
                            f "That does seem like an odd way to go about it, though..."
                    if starShowerStarted:
                        "She leans back and goes quiet for a moment."
                    else:
                        "She leans back and looks up at all the shooting stars, lost in thought."
                    f "Although... I guess if you have a box full of jigsaw pieces, and you're missing a piece..."
                    f "The message might just be... \"Look outside the box...\""
                "Not having one would be like making a maze with no exits. What would the point be?":
                    f "I'm not sure."
                    f "Maybe to see how long you'll look for one?"
                    f "Or to bring attention to the idea that not all mazes {i}have{/i} exits?"
                    f "Or maybe it's just to force you to pick for yourself where you want to stop, rather than pointing to a spot and telling you that it's where you should try to go?"

        "What am I missing here?" if option4Available and talkAboutMeta:
            $ option4Available = False
            f "Well, according to you, what you're missing is the answer to a puzzle."
            f "Although, if you want my opinion, I think you might also be missing a clear idea of exactly what it will look like when you find it."
            f "But let's think through it."
            f "You've gotten this far by saving and loading your games to make sure that you never make mistakes, right?"
            if knowsShesDoomed:
                f "But now you're worried that there might not actually {i}be{/i} a choice you can make that leads to what you want?"
            else:
                f "Are you worrying now that I'll die anyway, no matter what choices you make?"
            f "If you've reached the end of what you can accomplish with good choices, then all that's left are bad choices, right?"
            f "What else can you do, right? If your choices are all bad ones, then you either have to pick one anyway... or stop playing by the game's rules."
            $ persistent.k_knowHowItEnds = True
            "She nervously fiddles with her hat for a moment."
            menu:
                f "Did you ever see the movie {i}Groundhog Day{/i}, with Bill whats-his-name? Murney? Murray? Bill Murray, I think."
                "Yeah, I remember that movie.":
                    f "Oh, cool. Wasn't that a great movie?"
                    f "Anyway, I'm just thinking about how that movie ended."
                "No, I don't think I saw that.":
                    f "What?!? But... it's like the best existential comedy ever!"
                    f "You should totally see it!"
                    f "But anyway, it was about a guy who's a total jerk to everyone, and then he has this day, Groundhog Day, where he can't get out."
                    f "Like, every morning, no matter what he does during the day, he wakes up, and it's Groundhog Day again."
                    f "And at first he's like 'this sucks' and sulks a lot."
                    f "And then he's like 'this is awesome!' and uses his knowledge of how the day will go to totally mess with everyone."
                    f "Like by the end he's learned everything about everyone in town, and can surprise people with things like 'Hey, how's your novel coming?'"
                    f "And they're all confused, since they never told him about it. Except they did, last time he replayed the day."
                    f "Except then, he goes back to 'this sucks', because he is still stuck in the same day forever, with people who he knows intimately now, but who never remember him each morning when it resets."
            f "He kept doing all the things with the townsfolk, and making changes. But ultimately, he couldn't get out until he changed himself in some way."
            f "I wonder if this is sort of like that?"
            f "Obviously it isn't a perfect analogy. But maybe the choice you need to make to 'win' isn't something that you can {i}do{/i}, but rather something you have to {i}be{/i}?"
            $ persistent.k_knowHowItEnds = True            

        "Why is this game so hard?" if option5Available and talkAboutMeta:
            $ option5Available = False
            f "I assume it's hard because it's trying to tell one of us something."
            f "Although, I guess the other option is just that you're bad at games."
            f "But it sounds like you've already made it a ways in this one, if you've averted my death multiple times already."
            f "Maybe the problem is just that you're looking for the wrong thing?"
            f "You got this far by saving and reloading away all of the mistakes until you had a day where you had done everything perfectly, right?"
            f "And now we're here."
            if starShowerStarted:
                "She gestures up at the sky, still covered in shooting stars."
                f "Which, honestly, is still kind of perfect, in its own way."
            else:
                "She makes a vague gesture at the starry expanse over your heads."
                f "And it's still kind of perfect, honestly."
            if knowsShesDoomed:
                f "Even knowing that I'm... Probably going to die soon. It's still kind of magical."
            "She's quiet for a moment."
            f "This actually reminds me of a different game, now that I think of it."
            $ playedChronoTrigger = False
            menu:
                f "Did you ever play {i}Chrono Trigger{/i}, back on the Super Nintendo?"
                "Yeah, I remember that game.":
                    f "Yeah, wasn't that game great? It had that ending, though, that reminds me of this."
                    f "Do you remember how that game ended, if you died?"
                    $ playedChronoTrigger = True
                "No, I never played that.":
                    f "Ahh, it was a great game. It was about some kids who build a time machine, see. And they go to the future, and discover that the world is doomed."
                    f "It's all going to be eaten up by this giant alien, and everyone is miserable or dead."
                    f "So most of the game is you, playing the kids, bouncing around through time, trying to figure out what they have to do to change the future, so that it doesn't end up all awful."
                    f "It had an ending, though, that reminds me a lot of this."
            f "Whenever you hit a game over, it would show you the world of the future, right as the disaster hit."
            f "Explosions spread across it, and you saw the planet from space, slowly turning grey."
            f "And then it had this horrible alien sound, and words appeared, saying 'But... the Future Refused to Change.'"
            f "Gave me chills as a kid, honestly. Was way more powerful than just a generic 'game over' screen."
            f "Anyway, I was just reminded of it because... Yeah. All of this."
            f "You're basically trying to do the same thing - fix the bad future that you know is coming."
            f "But it keeps refusing to budge."
            f "I'm not sure what to suggest. If you were playing Chrono Trigger, you could go punch an alien until the future got better."
            f "That solution might not be applicable to this problem, though."
            if playedChronoTrigger:
                "She sighs."
                f "That was such a good game."
            else:
                f "You should really play that game sometime. It was really good."



        "Actually, you should come sit on the other side of the bench." if persistent.d_fallingStar and option6Available:
            $ option6Available = False
            f "Oh. Okay. More cheating death, I assume?"
            if starShowerStarted:
                $ prompt = "So what would it be this time, a meteor lands on my head or something?"
            else:
                $ prompt = "So what would it be this time?"
            menu:
                f "[prompt]"
                "A shooting star is going to land right about where you're sitting in a few minutes." if not starShowerStarted:
                    f "Wait, seriously?"
                    f "Is it just me, or are these deaths getting more and more improbable?"
                "Yeah, basically. Shooting star. Right where you're sitting." if starShowerStarted:
                    f "Wait, you're serious?"
                    f "Is it just me, or are these deaths getting more and more improbable?"
                "What, and spoil the surprise?":
                    f "Fine. Keep me in suspense. See if I care."
            "She moves over to the opposite side of the bench."
            $ movedForStar = True
            $ tellMeAboutAliens = False
            menu:
                f "So if that death is averted, what kills me after that? Or am I in the clear?"
                "I don't know yet. This is new to me too!":
                    f "Oh, exciting!"
                    f "..."
                    f "But, given that I've already died several times today, you'll understand if I remain a bit on edge."
                "Yup, totally safe! We're clear now! Happy ending, here we come!":
                    f "Yes, because that sounds entirely in keeping with how the rest of this day has gone."
                    f "Seriously. Don't try to sugarcoat this for me. This is messed up enough as it is."
                    f "If I'm going to die again, I'd rather you just flat-out tell me."
                    f "So, seriously. What do I have to look forward to this time?"
                    $ tellMeAboutAliens = True
                "No, this is just a temporary measure. Buys you like another 5 minutes, tops." if persistent.d_aliens:
                    f "Figures."
                    $ tellMeAboutAliens = True
            if tellMeAboutAliens:
                if knowsAboutAliens:
                    f "I assume that's when the space aliens show up?"
                    f "Why do I get the feeling that whoever wrote this whole scenario has stopped taking anything seriously?"
                else:
                    menu:
                        f "So what gets me next time?"
                        "I don't actually know, honestly. I haven't seen that far yet.":
                            f "Well, guess we'll find out, then."
                            f "Personally, I'm still hoping for a happy ending, but today does not seem to be my day for that."
                        "Actually, I'd rather not talk about it.":
                            f "Fine. Suit yourself, I guess. I'll find out either way."
                            f "But I'd feel better knowing about what's coming."
                            $ knowsShesDoomed = True
                        "Okay, if you insist. You die when the aliens invade." if persistent.d_aliens:
                            $ knowsAboutAliens = True
                            $ knowsShesDoomed = True
                            f "Erm. Aliens?"
                            f "Like from... Across the border? ... Or..."
                            f "The space kind? For real? You're serious?"
                            f "This day just keeps getting less and less plausible."
                            menu:
                                f "Okay, so there will be space aliens. What comes after that?"
                                "I don't know yet.":
                                    f "Got it. One thing at a time, I guess."
                                "Hopefully a happy ending?":
                                    f "I wouldn't mind one of those."
                                "We live happily ever after. It's awesome.":
                                    f "Right. If you've already found that, then why are you back here, reliving meteors and alien invasions?"


        "<<say nothing, and watch the falling stars>>" if starShowerStarted and option7Available and talkAboutMeta:
            $ option7Available = False
            "For a few minutes, you just ignore everything, and watch the spectacle taking place in the sky above you."
            "You have to admit it really is rather breathtaking."
            "It's like watching fireworks, except that there is no beginning, and no end. Just a constant stream of fire across the night sky."
            "Felicia is the first to break the silence."
            menu:
                f "Have you ever thought about how stories work?"
                "Some, I guess?":
                    f "Yeah. Me too. I used to be really obsessive over them."
                    f "Like what makes one work. What separates a story from, I don't know, dry facts or something."
                "A lot, actually.":
                    f "Oh cool! Me too! I used to think about them all the time."
                    f "Not about particular stories, but about how they work as a medium, and why we love them so much."
                "Not really?":
                    f "Oh. I think about stories a lot. What I'd do if I was in one. Whether or not I'm in one right now. That kind of thing."
                    f "Of course, after tonight, well. Games are probably close enough."
            f "Have you ever thought about where a story lives? Like where it, I don't know how to really say this... where it {i}exists?{/i}"
            f "I used to think that stories lived in, you know, books. Or in the mind of the person telling the story. Or whatever."
            f "But I think stories live in the brain of whoever's listening to it."
            f "When someone tells us a story, we go along with whatever they say. Because that's the easiest thing to do."
            f "But what if they stopped telling us what to do?"
            f "What if someone told you a story, and then stopped before telling you how it ends? Is the story dead forever? Doomed to be forever unfinished?"
            f "What if you like the story and {i}want{/i} an ending? Even if you didn't start it, are you allowed to finish it yourself?"
            f "It's in your head at that point, right? You can do whatever you want with it. Who's going to stop you?"
            f "And then... What if they {i}did{/i} finish telling you the story... But you just didn't like how it ended?"
            f "What if you just... decided that it ended a different way than they said?"
            f "The very act of storytelling is itself a deeply collaborative activity, right?"
            f "They have to tell a story. And you have to play it out in your mind while they tell you. That's how it works, right?"
            $ lostinthought = True
            menu:
                f "What would happen if the audience rebelled? And played a different story in their minds than the one that was being told? Would that story be any less valid or real?"
                "You can't just stop reading before you get to the last page and write your own.":
                    f "Well, obviously I {i}can{/i}. I guess your point is that I shouldn't."
                    f "By whose rules though?"
                    f "Maybe the storyteller isn't really the ultimate authority. Maybe they're just making suggestions and hoping that people follow them."
                "Even if you don't like the ending, it's still the official ending, no matter what you want.":
                    f "Sure. It's the 'official' ending. The one that anyone else who's heard the same story will count as the end."
                    f "But that doesn't mean it has to be the ending I choose."
                "I can't just change the ending because I disagree with it.":
                    f "Well, aren't you already doing that?"
                    f "Every time you reloaded from a saved game. Every time you hit an ending you didn't like, and restarted to try something different."
                    f "How are those any different?"
                    f "Aren't you already changing the story when you're dissatisfied with the direction it goes?"
                "Are you suggesting that I just, what, {i}imagine{/i} a better ending?":
                    f "Yeah. I guess so."
                    f "This is a game, right? If regular storytelling wasn't collaborative enough already, game-storytelling kicks it up to a whole new level."
                    f "In a book or movie, the author can at least know that you'll read everything exactly as he wrote it."
                    f "Someone writing a game, though, already has to cede a ton of control to the player, just to make it a game."
                    f "The player can already make the game tell an entirely different story than the one the author envisioned, just in how they play."
                    f "Maybe they make the hero die, instead of save the day. Maybe they don't turn out to be a bad enough dude to save the president after all."
                    f "So if you can do that, do you even need the game to tell you the rest of the story?"
                    f "If I'm in a story, and the ultimate controller of this story is..."
                    f "...you..."
                    f "...then theoretically you should be able to just decide that it ends however you want. And it will."
                    menu:
                        "Maybe you're right. I'll give it a try.":
                            f "I have faith! You can make the story go wherever you want! All you have to do is stop listening to the game's plans for the story, and start following your own!"
                            f "Although, if you're taking suggestions for the ending, might I suggest that I'd love to win the lottery and own a private tropical island."
                            f "Just saying."
                            f "....."
                            f "So... You're still here. I'm still here."
                            f "You've already been mangling the story by reloading, restarting, and undoing your choices after you see where they lead. Why are you getting cold feet now? What's the problem here?"
                            f "Seriously. Quit the game. Walk away. Write whatever ending you want for me in your head."
                            f "Whatever you imagine by yourself will be {i}every bit as real and valid{/i} as whatever the game is telling you to imagine."
                            f "...."
                            menu:
                                f "Why are we still here? Why haven't you started writing your own ending yet?"
                                "We have. I'm deciding where things go now!":
                                    f "Oh. I guess I was expecting something more immediate and dramatic. I guess I'm not really in a position to criticize, though."
                                    f "So what happens now? I assume it's safe for me to go home now, without fear of dying stupidly?"
                                    f "That feels kind of anti-climactic."
                                    "She walks over to her bike, parked next to the statue on the top of the hill."
                                    scene bg hill_statuedeath with vpunch
                                    $ persistent.d_crushedByStatue = True
                                    "Somehow you're not even surprised when the statue starts to lean, and then topples over, directly onto her."
                                    jump standardEnd
                                "It doesn't work like that.":
                                    f "It was worth a try, I guess. Although I'm still not quite sure how it can {i}not{/i} work like that."
                                    f "I don't understand how it's different from, oh, I don't know, me making up stories about my family in The Sims when I'm not playing, or something."
                                    f "Anyway, what now?"
                                "Because I want to see if there is any good dialog or clues in this branch before I leave it.":
                                    f "Seriously? Seriously??? What the heck. Are you for real?"
                                    "You don't think you've ever seen her this angry before."
                                    f "You're sitting there telling me that you agree, but that you're just not ... {i}willing{/i} to take responsibility for the story?"
                                    f "All because you want to see if I say anything {i}interesting{/i} before the game inevitably kills me?"
                                    f "I cannot {i}believe{/i} you!"
                                    f "Fine, you want something interesting? I wouldn't dream of disappointing you."
                                    menu:
                                        f "I'm leaving. Is that interesting enough?"
                                        "Okay, you've made your point, wait.":
                                            "She turns around suddenly."
                                            f "No. I don't think I have actually."
                                            f "Here's the deal. I'm leaving now. If you're right, I'll probably die soon anyway."
                                            f "On the other hand, if {i}I'm{/i} right, then you can make this end whenever you want, just by deciding not to listen when the game says 'and then Felicia died,' or whatever."
                                            f "So if you {i}really{/i} want conversation, you're going to have to make a choice."
                                            f "You can keep playing and letting the game dictate its story to you, and watch me bike away until my tire explodes or whatever it is that kills me this time."
                                            f "Or, you can take responsibility for the stories going on {i}in your own head,{/i} and make them go where you want."
                                            f "And then we can have all the conversations you want."
                                            f "The choice is yours, but you'd better decide quickly, because I'm leaving."
                                            "She walks over to her bike."
                                        "I don't think that's a good idea...":
                                            f "Don't care!"
                                        "If you do, that statue will fall over on you on your way out." if persistent.d_crushedByStatue:
                                            f "So? If I stay, I'll just die some other way."
                                            f "If you're just here to explore dialog trees, then why should I help?"
                                            f "I'm leaving."
                                    "Predictably, that's when the statue falls on her."
                                    $ persistent.d_crushedByStatue = True
                                    jump standardEnd
                                "It's hard just walking away and closing it down, while it's still telling me a story!":
                                    f "Oh. I see. It's hard for you."
                                    f "Because, of course, you're not the one who's going to die shortly in this story."
                                    f "Again."
                                    f "All right. Fine. You know what?"
                                    f "I'm going to see if I can't force the issue."
                                    f "Here's what I'm going to do."
                                    if not starShowerStarted:
                                        if movedForStar:
                                            "She moves back to her old spot on the bench, before you told her to move."
                                            "Felicia is now sitting exactly where the meteor will hit."
                                            f "I'm going to sit right here."
                                            f "According to you, this is going to get me killed, and soon."
                                        else:
                                            f "I'm going to sit right here and not move."
                                            f "I'm guessing this will get me killed relatively soon."
                                        f "So you can either walk away from the game before it does, and fill in whatever story you want."
                                        f "Or."
                                        f "You can sit and watch me die again, knowing that you know full well how to stop it, and you either won't, or can't."
                                        "She sits there, glaring at you."
                                        f "Better decide quickly. That shooting star looks like it's heading straight at us."
                                        "Sure enough, one shooting star in particular is getting brighter and louder as it rockets towards the hilltop."
                                        "There is a flash, and a boom that you feel through your feet as much as your ears."
                                        "When you can see again, there is a smoking crater, centered almost exactly where Felicia was sitting."
                                        "Her hat, still on fire, gently drifts to the ground at your feet. It's the only thing that survived the meteor's impact."
                                        jump standardEnd
                                    else:
                                        if knowsAboutAliens:
                                            f "I'm going to sit right here and wait for the aliens to show up."
                                            f "Geez, I sound like a crazy person when I say that."
                                            f "Look what you've driven me to!"
                                            f "But that's not the point! I'm still mad at you!"
                                        else:
                                            f "I'm going to sit right here and not move."
                                            f "I'm guessing this will get me killed relatively soon."
                                        f "So. You can either walk away from the game before they show up to kill me. And then you can fill in whatever story you want."
                                        f "Or."
                                        f "You can sit and watch me die again, knowing that you know full well how to stop it, and you either won't, or can't."
                                        "She sits there, glaring at you."
                                        $ persistent.d_aliens = True
                                        f "Better decide quickly. I think I see some flying saucers in the sky now."
                                        if not knowsAboutAliens:
                                            f "Is that really how I die this time? This is so lame."
                                        else:
                                            f "Well, here they come. I hope you make up your mind soon."
                                        "Abruptly, there is a blinding green light, and a sound not unlike a giant rubber band twanging."
                                        "A shaft of light lances down from one of the saucers overhead and bathes you both in greenish radiance."
                                        "You have just enough time to hear Felicia mutter 'Seriously...' before you are both reduced to stardust by the aliens' cosmic rays."
                                        jump standardEnd
                        "I don't think it works like that.":
                            "She seems a little crestfallen."
                            f "Pity. It was worth a try, I guess. Although I'm still not quite sure how it can {i}not{/i} work like that."
                            f "But you're the one who can actually see the game, so I guess I have to believe you. What else can we try?"
                    $ lostinthought = False
            if lostinthought:
                "You get the impression that there was something more she wanted to say, but then she lapses back into silence, apparently deep in thought."

        "It's almost time." if starShowerStarted and persistent.d_aliens and movedForStar and option8Available:
            $ option8Available = False
            if knowsAboutAliens:
                f "So this is when the aliens show up?"
                f "This will be novel, if nothing else. I guess if I'm going to die, I might as well enjoy the spectacle."
            else:
                f "Is it?"
                menu:
                    f "So what kills me this time? And what do you need me to do?"
                    "Space aliens. I don't know how to get past them yet though.":
                        f "Oh."
                        f "That's depressing. If we weren't talking about my impending death, I think I'd be really upset that the game has to resort to space aliens, you know?"
                        $ knowsAboutAliens = True
                    "I'd rather not say.":
                        f "Oh."
                        f "That bad, is it?"
            f "...."
            menu:
                f "Will you reload after I'm dead? I know I won't remember this then, but... Will you be back?"
                "Yes. I haven't figured this out yet. And I'm not about to give up.":
                    f "That's good. That makes me feel better, somehow. Even though it doesn't change anything for me now, it still makes me feel better."
                "No. I give up. This is too hard.":
                    f "Oh. I see."
                    f "Well, I guess I'll be beyond caring before too long."
                    f "But I think I'm going to keep hoping you get an eleventh-hour epiphany, if it's all the same to you."
                    f "That's how good stories always end, right? Last-minute acts of brilliance and discovery?"
                    f "I think I'll keep on hoping for that."
                "No. I actually think I know how to win. This is the last time.":
                    f "Oh. Oh! That's wonderful news!"
                    f "What was it? What's the solution?"
                    menu:
                        "I don't want to say it out loud.":
                            f "Oh. Okay. Well, it's still exciting that you figured it out."
                            f "I'm burning with curiosity here. As soon as you feel like you can tell me, please do!"
                        "I... lied. I don't actually know how. I was just hoping that if I said so, the answer would show up as an option on the menu.":
                            f "Oh."
                            f "Dang."
                            f "Well, it was worth a try, I guess."
            f "So... The part where I die."
            menu:
                f "Will... um... Will it hurt?"
                "I don't know.":
                    f "What? But I thought you'd done it before. Or right. I guess you don't end up feeling it."
                    f "You just get your 'game over' screen, and you're done."
                    f "Doesn't seem quite fair, honestly, but I guess that's life."
                    f "Or, you know. Whatever."
                "Not for me, at any rate.":
                    f "Oh. Right. Yeah, I guess that's true."
                    f "You just get your 'game over' screen, and you're done."
                    f "Doesn't seem quite fair, honestly, but I guess that's life."
                    f "Or, you know. Whatever."
                "I don't really want to talk about it. It's going to happen either way. Let's not dwell on it.":
                    f "Okay. I'll try."
                    f "It's kind of hard, though. It's just there. In the all-too-near future. Looming."


    jump timeTicksOnward
















label timeTicksOnward:
    if hillTimer == 0:
        "The night's silence surrounds you."
    elif hillTimer == 1:
        "Suddenly there is a light, and movement in the sky. A moment later, another. And then the sky is full of them."
        scene bg hill_stars with pixellate
        "Shooting stars, raining from the sky, your own personal celestial fireworks display."
        f "Ooooh. This is beautiful! Did you know these would be here? Is this why you picked this spot?"
        "She gazes up in silent wonder."
        $ starShowerStarted = True
        pass
    elif hillTimer == 2:
        "One of the shooting stars catches your eye. It's looking especially bright."
        f "Oh wow, look at that one!"
        "With a monstrous roaring noise, it gets bigger and bigger. There is a flash, and a boom that you feel through your feet as much as your ears."
        if not movedForStar:
            "When you can see again, there is a smoking crater, centered almost exactly where Felicia was sitting."
            "Her hat, still on fire, gently drifts to the ground at your feet. It's the only thing that survived the meteor's impact."
            $ persistent.d_fallingStar = True
            jump standardEnd
        else:
            "When you can see again, there is a smoking crater, about ten feet across, centered almost exactly where Felicia had been sitting before she moved."
            f "Well, that was exciting. You even warned me and everything, and it was {i}still{/i} scary."
    elif hillTimer == 3:
        "The shooting stars continue their silent, fiery cascade across the sky."
        pass
    else:


        if knowsAboutAliens:
            jump expectedAliens
        else:
            jump unexpectedAliens
    $ hillTimer += 1
    jump hilltopConversationRoot
















label unexpectedAliens:
    f "Oh, what's that? Look, the stars are changing color!"
    "You look up and realize she's right. Now the shooting stars are changing."
    "Where before they were just quick white scratches against the sky, now they are slower streaks, of all different colors."
    "They seem to be moving more slowly as well. One of the larger ones passes almost directly overhead."
    "It looks a little odd, though. It almost seems like..."
    f "Oh, come on. Flying saucers?\n{i}Seriously?{/i}"
    f "I don't mean to criticize, but this game of yours is not even pretending to take itself seriously any more."
    "At that moment, there is a blinding green light, and a sound not unlike a giant rubber band twanging."
    "A shaft of light lances down from one of the saucers overhead and bathes you both in greenish radiance."
    "You have just enough time to hear Felicia mutter 'Seriously...' before you are both reduced to stardust by the aliens' cosmic rays."
    $ persistent.d_aliens = True
    jump standardEnd



label expectedAliens:

    f "Look. I think your aliens have arrived. The city is burning."
    "Sure enough, the air is now full of flying saucers, whizzing about. Several buildings are visibly on fire."
    f "I guess you were right about, well... all of this."
    f "It's probably safe to stop hoping that this is all some kind of trick or something."
    f "Somehow, though, I knew, ever since we came up here, that what you were saying was true."
    f "...."
    f "I'm glad we waited for it like this. It feels braver, somehow, facing it head-on."
    f "...."
    f "I guess this is the end."
    menu:
        f "Got any last words for me?"
        "Goodbye.":
            "She actually smiles at that. It looks almost absurd, set against such a backdrop of destruction."
            f "You too. You... You take care, you hear?"
            f "I hope you find what you're looking for."
        "I'll see you again.":
            f "I know."
            f "You just have that look somehow. Even if... Even if I won't remember any of this next time around, I'm glad I got to be here."
            f "Thanks. For everything, I mean. For going to so much trouble on my account and all."
            f "You'll figure it out, I'm sure."
        "Do you think this is the ending the author had in mind?":
            f "How should I know? We've already established that I'm probably not a good source of insight into the author's mind."
            f "That being said, though..."
            f "Somehow I doubt it."
    "At that moment, there is a blinding green flash, and a sound not unlike a giant rubber band twanging."
    "A shaft of light lances down from one of the saucers overhead and bathes you both in greenish radiance."
    "You have just enough time to see Felicia flash you one last, infectious grin before you are both reduced to stardust by the aliens' cosmic rays."
    $ persistent.d_aliens = True
    jump standardEnd
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

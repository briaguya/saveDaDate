
label dinnerStart_tacos:
    scene bg tacos with fade
    $ setmusic("audio/tacos.ogg")

    f "This was a good idea. Everything is better with tacos!"
    f "I've heard good things about this place, and I hear they got a new chef recently, too!"
    f "And I really like how they're out on the docks like this! It's like we're eating right on the water!"


    menu:
        f "Where do you want to sit?"
        "Out on the patio outside, of course!":
            "The tables outside are popular, but your server manages to find a free one for the two of you."
            "You take your seats and start looking at the menu."
        "How about near the window, where we can see the water?":

            "The two of you sit down at a table near a giant window, where you can look out over the water."
            "The sun is just starting to set, and the waves are turning gold-colored. The effect is quite beautiful."
        "Let's see if they have a free booth!":
            "You are directed to a booth, and the server brings out water and menus."


    f "Okay, let's have some tacos! Do you have any recommendations?"
    f "I hear their fish tacos are amazing, but I'm open to other options."


    menu:
        f "What are you going to get?"
        "Fish tacos. You're right. They're to die for!":
            f "You've convinced me! I'll have them too!"
            pass
        "An enchilada plate, actually. I really like their chicken.":
            f "Hmm. Tempting."
            f "But not tempting enough! Fish tacos for me, please!"
            pass
        "I think I'll have the fiesta salad. It's got mango in it!":

            f "Mmm. I do like mango!"
            f "But no. I entered this dinner with a resolution to eat fish tacos."
            f "What would you think of me if I cast aside my ambitions so lightly?!"
            f "Fish tacos, please!"
            pass

    f "Haha. I hope I don't sound obsessed to you. But for some reason I'm just really excited about tacos tonight!"
    f "I'm not normally this obsessive! Honest!"

    menu:
        f "Do you ever get like that? Obsess over some particular thing you want, to the exclusion of everything else?"
        "Not really. I'm pretty easy going.":
            pass
        "Yeah, sometimes I can be pretty single-minded.":
            pass

    f "Haha, yeah, I guess."
    f "Oh! What's that?"
    "She points out the window."
    f "Are those dolphins?! I think those are dolphins!"
    "You follow her as she runs to the railing to look out over the ocean."
    f "It is dolphins! Oh, I'm so glad we came here tonight! This is so awesome!"

    menu:
        f "Have you ever seen anything quite like it?"
        "No. This is incredible!":
            pass
        "Once, maybe. This sort of thing doesn't happen often.":
            pass
        "A lot, actually. Every time I've been here.":
            pass
        "Actually - this is important. Take two steps to your left. Right now." if persistent.d_fellInOcean:
            jump howDidYouKnow_tacos

    "She gazes out at the picturesque scene for a moment longer, and then several things happen all at once."
    f "Woah! What's happening?!"
    "Too quickly for you to react, and yet somehow with agonizing slowness, the railing, and in fact the whole patio, collapses into the sea."
    "Felicia tries to jump for safety as soon as she feels everything begin to move, but she's not quite quick enough. You lose sight of her in the churning water amidst all the debris from the deck."
    $ stopmusic()
    $ persistent.d_fellInOcean = True
    "That was the last time you saw her. The currents near there are known to be treacherous, and they never did manage to find a body."
    jump standardEnd


label howDidYouKnow_tacos:
    "She turns around, obviously a bit surprised at your tone, but obediently takes a step to the left."
    f "What, was I in the way, or HOLY CRAP"
    "The portion of the deck where she was just standing abruptly collapses into the water."
    f "I... I was almost standing there. I... Holy crap, that was close."
    f "I could have died!"
    $ prompt = "How did you know the deck was going to give?  And that it was safe over here?"

    jump howdidyouknow



label waitedTooLong_tacos:
    "Suddenly, you're interrupted by screams and the sound of a lot of things breaking."
    "Your first thought is that suddenly there are snakes everywhere!"
    "Soon enough, though, you realize your mistake. It's actually just tentacles."
    "Countless tentacles, coming in from every window and opening, boiling up from the rolling waters beneath the restaurant."
    "Not snakes at all, you think to yourself, as Felicia is pulled out a window, with a tentacle wrapped around her, over a foot in diameter."
    $ stopmusic()
    "Just a sea monster."
    $ persistent.d_tookTooLong_tacos = True
    jump standardEnd
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

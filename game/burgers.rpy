
label dinnerStart_burgers:
    scene bg burgers with fade
    $ setmusic("audio/burgers.ogg")

    f "Oh wow, everything smells so good!"
    f "I had my doubts when you mentioned this place. It's out of the way, and in kind of a sketchy neighborhood, but this looks great!!"
    f "I think I'll have.... the bacon-burger. With extra ketchup."

menu:
    f "What are you having?"
    "A plain burger for me, please.":

        jump dinnerTalk_burgers
    "I'll have a cheddar cheese burger with bacon!":
        jump dinnerTalk_burgers
    "Swiss cheese with mushrooms! Yum!":
        jump dinnerTalk_burgers








label dinnerTalk_burgers:
    "Your meal is served, and you both dig in. After a few bites, she stops eating and looks wistful."
    f "My Dad would have loved this place. He would have been right at home. He really loved burgers, and this place has great ambiance."

menu:
    "She sighs, and pokes at her burger."
    "What happened to your Dad?":
        "She rewards your question with a brittle smile."
        f "He left Mom and me when I was six."
        "She looks directly at you for the first time since the meal was served."
        f "I'm sorry. I didn't mean to dump that on you out of the blue. I'm just not used to thinking about him."
        f "I honestly don't think it's ever come up since we moved here. Mom still tries to call him sometime, but I..."
        f "It's easier if I just don't think about him."
        "She gives you a much warmer smile this time."
        f "But enough about my personal soap-opera life. I refuse to be upset in the face of such delicious hamburgers."
        $ persistent.k_daddyIssues = True
    "<Say nothing, and keep eating>":

        "After a minute or two of poking at her food, she brightens up."



label dinnerTalk_burgers2:


    "She takes another big bite out of her burger."
    f "So I've been thinking lately. About school. And what comes after."
    "You can hear some kind of commotion coming from outside. Felicia cranes her neck to try to see."


menu:
    f "What's going on? Is something happening out there?"
    "It sounded like someone shouting!":
        jump deathByGunfire
    "It probably doesn't concern us.":
        jump deathByGunfire
    "Okay, this is important. I need you to duck. Now." if persistent.d_gunfire:
        jump howDidYouKnow_gunfire




label deathByGunfire:

    "Suddenly, there is a loud noise from outside - a succession of loud bangs, like a string of firecrackers going off."
    f "I..."
    "It takes you a moment for the red stain spreading across her shirt to register."
    "Felicia looks down in uncomprehending shock."
    f "I think I've... I've been shot?"
    $ persistent.d_gunfire = True
    $ stopmusic()
    "Then, ever so slowly, she crumples into the booth."
    "You're vaguely aware of more sounds of gunfire from outside, but all you can hear is Felicia's labored breathing, each ragged breath sounding louder than anything else in the world."
    "It might have been minutes or centuries later when the ambulance arrives. A kind man with sad eyes loads her onto the gurney, and rushes her off."
    "He tells you not to worry and that everything will be all right, but you both know he is lying. You heard the ragged breathing stop, and you saw the light fade from her eyes."
    "You never do find out what caused the gunfight in the street. Some gang scuffle, or a drug deal gone wrong, or something."
    "All you saw was the terrible aftermath."
    jump standardEnd
    return


label howDidYouKnow_gunfire:
    "She stares at you blankly for a moment, not sure if you're joking or not, and then awkwardly hunches over."
    "There is a loud sound from outside, and an explosion of plaster showers down from the wall she was sitting in front of, moments ago."
    f "I... Oh my god. Was that gunfire?"
    $ prompt = "Did you just save my life?  What...  How did you know that was going to happen?"
    jump howdidyouknow




label waitedTooLong_burgers:
    $ stopmusic()
    "Suddenly, everything goes white, and you're flying through the air."
    "Then everything goes black."
    "You find out later, from the hospital, that there was a gas explosion."
    "Striking with the luck of the mindless, one of the bullets managed to hit the fuel line for the gas ovens."
    "You're shaken and bruised, but ultimately okay."
    "Sadly, the same could not be said for Felicia. The best that the doctors will tell you is that at least it was quick."
    "But, sadly, she did not survive."
    $ persistent.d_tookTooLong_burgers = True
    jump standardEnd
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

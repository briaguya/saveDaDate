
label dinnerStart_thai:
    scene bg thai with fade
    $ setmusic("audio/thai.ogg")


    f "I've always wanted to try Thai food! This will be fun!"
    "Server" "Are you ready to order?"

menu:
    f "I think so! This picture for Pad Thai looks amazing. I think I'll have that. What are you having?"
    "That sounds good. I'll have the Pad Thai, too.":
        f "Excellent choice! May I compliment you on your class and taste!"
    "I'd like some yellow curry with chicken, I think.":
        f "That sounds pretty good too! But no, I'm sticking with my first choice!"
    "The shrimp fried rice sounds good. Let's go with that.":
        f "Oooh. I do like seafood. But no. Pad Thai it is. It looks so delicious in the picture!"
    "Actually - The Pad Thai has peanuts in it." if persistent.d_peanutAllergy:
        jump howDidYouKnow_peanuts








label dinnerTalk_thai:
    "Eventually, dinner arrives, and Felicia dives into her meal with surprising gusto."
    f "Oh, this is delicious! We should have done this a long time ago!"

    menu:
        f "I'm so glad we were able to meet tonight. Do you know why I wanted to do this?"
        "Yes.":
            f "Oh, good. That makes things easier."
        "No.":
            f "Well..."


    "She actually looks flustered for a moment."
    f "I've been really wanting to ask you... well..."
    f "Sorry, this is hard to say."
    "Felicia pauses for a moment, and takes a deep breath."
    f "...Really hard to say. I'm not feeling..."
    f "Were there peanuts in that dish or something? I don't..."


    $ stopmusic()
    "She topples face-first into her food."
    "The rest of the evening is a blur of ambulances and yelling, but somehow you feel like you already know what is coming."
    "You're not really surprised when the ashen-faced medical technician comes to tell you what you already basically know: Felicia had a severe peanut allergy, and it killed her."
    $ persistent.d_peanutAllergy = True
    jump standardEnd

    return



label howDidYouKnow_peanuts:
    f "Wait, for real? Oh... Wow. I'm glad you told me!"
    f "I'm actually like super-allergic to peanuts. That could have been really bad!"
    f "Actually it was kind of silly how they found out."
    f "When I was little, I saw elephants on TV and decided that I wanted to be an elephant when I grew up."
    f "So I ate some peanuts that my Dad had left out."
    f "And my face swelled up and got all puffy, and I was convinced that this was me, turning into an elephant, just like I'd planned!"
    f "So I stumbled into the living room with my face like twice its normal size, and slurred out, 'Look mama, look dada, I'm gonna be an elephant!'"
    f "After I got back from the emergency room, we laughed about that for years."
    "She looks almost wistful."
    $ prompt =  "But how did you know I was allergic?  I don't think I've ever told anyone at school."
    jump howdidyouknow



label waitedTooLong_thai:
    "Suddenly, the restaurant is full of yelling, and there are shiny pieces of metal flying everywhere."
    "Your last thought is something like, 'Why {i}are{/i} there ninjas in a Thai restaurant? Ninjas are Japanese...' before you are hit on the head with a nunchuck, and everything goes dark."
    $ stopmusic()
    "You never do find out what the attack was all about. Some kind of underworld power struggle? Oddly-themed gang warfare? Sinister Naruto cosplayers?"
    "In the end it doesn't really matter. Twelve people died in the attack."
    "Felicia was one of them."
    "And you never even found out what it was about."
    $ persistent.d_tookTooLong_thai = True
    jump standardEnd
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

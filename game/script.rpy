





define f = Character('Felicia', color="#c8ffc8", show_two_window=False, image="felicia")
$ narrator = Character(None, color="#c8ffc8")


init:
    image felicia happy = Image("art/f_happy.png")
    image felicia sad = Image("art/f_sad.png")
    image felicia angry = Image("art/f_angry.png")
    image felicia pensive = Image("art/f_pensive.png")
    image felicia surprised = Image("art/f_surprised.png")
    image felicia suspicious = Image("art/f_suspicious.png")
    image felicia phone = Image("art/phone.png")

    image bg bedroom = Image("art/bg_bedroom.png")
    image bg tacos = Image("art/bg_tacos.png")
    image bg thai = Image("art/bg_thai.png")
    image bg burgers = Image("art/bg_burgers.png")
    image bg hill = Image("art/bg_hill.png")
    image bg hill_stars = Image("art/bg_hill_fallingstars.png")
    image bg hill_statuedeath = Image("art/bg_hill_statuedeath.png")
    image bg credits = Image("art/menu_bg.png")













label start:
    $ quick_menu = True
    $ setmusic("audio/bedroom.ogg")
    $ _game_menu_screen = "save_screen"

    call countDeaths
    call HACKER_SETUP

    if not persistent.initted:
        $ resetPersistentData(False)


    scene bg bedroom with fade

    "*Ring* *Ring*"
    show felicia phone with easeinbottom
    "*Ring* *Ring*\n*Ring* *Ring*"
    f "Hello?"
    f "Oh, you're early! You must be calling about tonight?"
    f "I meant to ask where we were meeting!"
    f "I know we were planning on having dinner, but we never decided where!"


menu:
    f "Where are we having dinner?"
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


    "Change in plans. We can't go out to dinner tonight. It's too dangerous." if persistent.totalDeathsSeen >= 3:
        $ fooddesc = "none"
        $ currentLocation = "hilltop"
        jump hilltop_convince

    "Actually, I thought we could have an awesome dinner in my floating sky castle because I am a hacker!" if I_AM_A_HACKER:
        f "Oh. That sounds nice!"
        "The two of you have a delicious dinner in your magical floating sky castle!"
        "Afterward you fly her home, because you can fly, because you are a hacker and super awesome!"
        jump hackerGoodEnding
    "Actually, I don't think I want to meet up tonight after all.":




        jump noDinner






        return


label noDinner:
    "She seems hurt that you canceled your plans. When you see her the next day, she's friendly enough, but there's a barrier between you now."
    "You remain friendly acquaintances, but that's as far as it ever goes. You never do manage to ask her to dinner again."

    if not persistent.d_aliens:
        $ stopmusic()
        "Eventually, she starts seeing someone else. Years later, they have started a life together, and are extremely happy. You try not to envy them, but sometimes you wonder if things might have gone differently."
        $ gameovermusic()
        "{size=+10}~The End~{/size}\n\nYou never even got a date."
    else:
        "Eventually, she starts seeing someone else. Years later, they have started a life together, and are extremely happy. Sometimes you wonder if things might have gone differently."
        "Not often, though. Because you have seen a lot of the ways it could have gone instead. And all of them are worse."
        "On the balance, maybe this isn't such a bad place to end the story after all."
        "{size=+20}~The{/size} (or at least an) {size=+20}End~{/size}"
    return



label triedToLeave:
    "You finish your [fooddesc] and head out."
    "You haven't made it more than a foot from the door, though, when a car crashes into the front of the restaurant."
    "Unfortunately, the two of you are directly in it's path."
    "You are flung to the side, but Felicia is not so lucky."
    $ persistent.d_leavingEqualsCar = True
    "The ambulance arrives quickly, but she doesn't even make it to the hospital before succumbing to internal bleeding and a punctured lung."
    jump standardEnd



label stayedAtRestaurant:
    if currentLocation == "thai":
        jump waitedTooLong_thai
    if currentLocation == "burgers":
        jump waitedTooLong_burgers
    if currentLocation == "tacos":
        jump waitedTooLong_tacos
    "Error, couldn't figure out where you were. currentLocation = [currentLocation]"
    return



label standardEnd:
    $ persistent.totalDeathsSeen += 1
    $ gameovermusic()
    "{size=+10}~The End~{/size}\n\nYour date has ended in disaster."
    return


label hackerGoodEnding:
    "She grabs the mail on the way in and discovers that she has won like six different lotteries and is now independently wealthy."
    "She also now owns a small island paradise in the Caribbean, full of endangered wildlife and stuff."
    "She is super happy! She moves there the next month, and has a happy, long, and fulfilling life taking care of exotic animals and playing with Bengal tigers."
    "She lives happily ever after, and you do too sometimes, when you visit, which you do by flying, which you can do because you're an awesome hacker."
    "Everyone involved lives happily ever after and nothing bad happens to them ever, and sometimes you think, 'Man, what a great life I have - good thing I'm a hacker!'"
    "{size=+10}~The End~{/size}\n\nYou are an awesome hacker!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

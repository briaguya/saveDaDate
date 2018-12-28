



init -1 python:
    def resetPersistentData(showClearedScreen):
        persistent.initted = True
        
        persistent.d_peanutAllergy = False
        persistent.d_gunfire = False
        persistent.d_fellInOcean = False
        
        persistent.d_leavingEqualsCar = False
        
        persistent.d_tookTooLong_tacos = False
        persistent.d_tookTooLong_thai = False
        persistent.d_tookTooLong_burgers = False
        
        persistent.d_stayedAtHome = False
        
        persistent.d_crushedByStatue = False
        persistent.d_fallingStar = False
        persistent.d_aliens = False
        
        persistent.d_statue = False
        persistent.d_airplane = False
        
        
        persistent.k_daddyIssues = False
        persistent.k_wantsToGoToHogwarts = False
        persistent.k_serverTripsAndFalls = False
        persistent.k_peanutElephant = False
        persistent.k_firstNumber = False
        persistent.k_secondNumber = False
        persistent.k_secretWordSaveGame = False
        
        persistent.k_convincingBookSentence = False
        
        persistent.k_needToKnowASecret = False
        persistent.k_foundOutASecret = False
        persistent.k_knowHowItEnds = False
        
        persistent.totalDeathsSeen = 0
        if (showClearedScreen):
            ui.add(Solid((0, 0, 0, 128)))
            ui.text(_('Cleared.'),
                      xpos=0.5, xanchor='center', ypos=0.5, yanchor='center')
            ui.saybehavior()
            ui.interact(suppress_overlay=True, suppress_underlay=True)



    currentmusic = ""
    def setmusic(newmusic):
        currentmusic = newmusic
        renpy.music.play(newmusic, if_changed=True, loop=True)


    def gameovermusic():
        currentmusic = ""
        renpy.music.play("audio/gameover.ogg", loop=False)


    def stopmusic():
        renpy.music.stop(fadeout=2),


label countDeaths:

    python:
        uniqueDeathsSeen = 0
        if (persistent.d_peanutAllergy):
            uniqueDeathsSeen += 1
        if (persistent.d_gunfire):
            uniqueDeathsSeen += 1
        if (persistent.d_fellInOcean):
            uniqueDeathsSeen += 1
        if (persistent.d_leavingEqualsCar):
            uniqueDeathsSeen += 1
        if (persistent.d_tookTooLong_tacos):
            uniqueDeathsSeen += 1
        if (persistent.d_tookTooLong_thai):
            uniqueDeathsSeen += 1
        if (persistent.d_tookTooLong_burgers):
            uniqueDeathsSeen += 1
        if (persistent.d_stayedAtHome):
            uniqueDeathsSeen += 1
        if (persistent.d_crushedByStatue):
            uniqueDeathsSeen += 1
        if (persistent.d_fallingStar):
            uniqueDeathsSeen += 1
        if (persistent.d_aliens):
            uniqueDeathsSeen += 1


    return

label currentLocationDeath:
    if currentLocation == "burgers":
        $ isCurrentLocationDeathKnown = persistent.d_tookTooLong_burgers
    elif currentLocation == "thai":
        $ isCurrentLocationDeathKnown = persistent.d_tookTooLong_thai
    elif currentLocation == "tacos":
        $ isCurrentLocationDeathKnown = persistent.d_tookTooLong_tacos
    else:
        f "Error - currentLocation couldn't be figured out. It is currently [currentLocation]"
        $ isCurrentLocationDeathKnown = False
    $ totallyDoomed = persistent.d_leavingEqualsCar and isCurrentLocationDeathKnown
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

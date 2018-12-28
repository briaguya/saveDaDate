








init -1 python hide:





    config.developer = False

    config.rollback_enabled = False



    config.screen_width = 800
    config.screen_height = 600




    config.window_title = u"Save the Date!"



    config.name = "Save the Date"
    config.version = "0.2"











    theme.roundrect(
        
        
                                    
        
        widget = "#6A7183",

        
        widget_hover = "#1A2B47",

        
        widget_text = "#C9C9CB",

        
        

        widget_selected = "#ffffff",

        
        disabled = "#ADB9CC",

        

        disabled_text = "#7788AA",

        
        label = "#39435E",

        
        frame = "#ADB9CC",

        
        
        
        
        mm_root = "art/titlescreen.png",

        
        
        
        
        gm_root = "art/menu_bg.png",

        
        
        rounded_window = False,

        
        
        
        )





































































    style.say_thought.italic = True








    config.has_sound = True



    config.has_music = True



    config.has_voice = True




















    config.window_icon = "art/game_icon.png"











    config.help = "README.html"






    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None






python early:
    config.save_directory = "Save the Date-1361735824"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 0









init python:




    build.directory_name = "savethedate-1.0"




    build.executable_name = "savethedate"



    build.include_update = False





























    build.classify('game/I_AM_A_HACKER.rpy', 'all')
    build.classify('game/HOW_TO_BE_A_HACKER.TXT', 'all')
    build.classify('**.rpy', None)


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')





    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc









screen say:


    default side_image = None
    default two_window = False


    if not two_window:


        window:
            id 'window'

            has vbox:
                style 'say_vbox'

            if who:
                text who id 'who'

            text what id 'what'
    else:



        vbox:
            style 'say_two_window_vbox'

            if who:
                window:
                    style 'say_who_window'

                    text who:
                        id 'who'

            window:
                id 'window'

                has vbox:
                    style 'say_vbox'

                text what id 'what'


    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0


    if quick_menu:
        use quick_menu








screen choice:

    window:
        style 'menu_window'
        xalign 0.5
        yalign 0.3

        vbox:
            style 'menu'
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style 'menu_choice_button'

                        text caption style 'menu_choice'
                else:

                    text caption style 'menu_caption'
    use quick_menu


init -2 python:
    config.narrator_menu = True

    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)



    style.default.activate_sound = "audio/select.wav"
    style.default.hover_sound = "audio/hover.wav"








screen input:

    window:
        has vbox

        text prompt
        input id 'input'

    use quick_menu







screen nvl:

    window:
        style 'nvl_window'

        has vbox:
            style 'nvl_vbox'


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id 'menu'

                for caption, action, chosen in items:

                    if action:

                        button:
                            style 'nvl_menu_choice_button'
                            action action

                            text caption style 'nvl_menu_choice'
                    else:


                        text caption style 'nvl_dialogue'

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu tag menu:




    window:
        style 'mm_root'


    frame:
        style_group 'mm'
        xalign 0.98
        yalign 0.98

        has vbox
        textbutton _('Start Game') action Start()
        textbutton _('Load Game') action ShowMenu('load')
        textbutton _('Preferences') action ShowMenu('preferences')

        textbutton _('Credits') action Start('credits')
        textbutton _('Quit') action Quit(confirm=False)

init -2 python:


    style.mm_button.size_group = "mm"








screen navigation:


    window:
        style 'gm_root'


    frame:
        style_group 'gm_nav'
        xalign 0.98
        yalign 0.98

        has vbox

        textbutton _('Return') action Return()
        if currentscreen == 'save':
            textbutton _('Load Game') action ShowMenu('load')
        elif currentscreen == 'load':
            textbutton _('Save Game') action ShowMenu('save')
        elif currentscreen == 'preferences':
            textbutton _('Save Game') action ShowMenu('save')
            textbutton _('Load Game') action ShowMenu('load')

        textbutton _('Main Menu') action MainMenu()

        textbutton _('Preferences') action ShowMenu('preferences')
        textbutton _('Quit') action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"













screen file_picker:

    frame:
        style 'file_picker_frame'

        has vbox



        hbox:
            style_group 'file_picker_nav'
        python:















            columns = 2

        $ rows = 5
        if currentscreen == 'save':
            text '{size=+10}Select a slot to Save your game:{/size}\n'
        elif currentscreen == 'load':
            text '{size=+10}Select a slot to Load from:{/size}\n'
        else:
            text '{size=+10}I have no idea what this is: [currentscreen]{/size}\n'


        grid columns rows:
            transpose True
            xfill True
            style_group 'file_picker'

            button:
                action FileAction('quicksave')
                xfill True

                has hbox


                add FileScreenshot('quicksave')



                text '  Quick Save Slot'

                key 'save_delete' action FileDelete('quicksave')



            for i in range(1, columns * rows + 0):


                button:
                    action FileAction(i)
                    xfill True

                    has hbox


                    add FileScreenshot(i)
                    python:
                        description = '% 2s. %s\n%s' % (
                            FileSlotName(i, columns * rows), 
                            FileTime(i, empty=_('Empty Slot.')), 
                            FileSaveName(i))


                    text description

                    key 'save_delete' action FileDelete(i)






screen save tag menu:



    $ currentscreen = 'save'
    use navigation
    use file_picker

screen load tag menu:



    $ currentscreen = 'load'
    use navigation
    use file_picker



init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)









screen preferences tag menu:




    $ currentscreen = 'preferences'
    use navigation


    grid 3 1:
        style_group 'prefs'
        xfill True


        vbox:
            frame:
                style_group 'pref'
                has vbox

                label _('Display')
                textbutton _('Window') action Preference('display', 'window')
                textbutton _('Fullscreen') action Preference('display', 'fullscreen')

            frame:
                style_group 'pref'
                has vbox

                label _('Transitions')
                textbutton _('All') action Preference('transitions', 'all')
                textbutton _('None') action Preference('transitions', 'none')

            frame:
                style_group 'pref'
                has vbox

                label _('Text Speed')
                bar value Preference('text speed')

            frame:
                style_group 'pref'
                has vbox

                textbutton _('Joystick...') action Preference('joystick')

        vbox:
            frame:
                style_group 'pref'
                has vbox

                label _('Skip')
                textbutton _('Seen Messages') action Preference('skip', 'seen')
                textbutton _('All Messages') action Preference('skip', 'all')

            frame:
                style_group 'pref'
                has vbox

                textbutton _('Begin Skipping') action Skip()

            frame:
                style_group 'pref'
                has vbox

                label _('After Choices')
                textbutton _('Stop Skipping') action Preference('after choices', 'stop')
                textbutton _('Keep Skipping') action Preference('after choices', 'skip')








        vbox:
            frame:
                style_group 'pref'
                has vbox

                label _('Music Volume')
                bar value Preference('music volume')

            frame:
                style_group 'pref'
                has vbox

                label _('Sound Volume')
                bar value Preference('sound volume')

                if config.sample_sound:
                    textbutton 'Test':
                        action Play('sound', config.sample_sound)
                        style 'soundtest_button'
            frame:
                style_group 'pref'
                has vbox
                label _('Persistent Data')
                textbutton _('Clear Data') action myClearData_action()













init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0








screen yesno_prompt:

    modal True

    window:
        style 'gm_root'

    frame:
        style_group 'yesno'

        xfill True
        xmargin 0.05
        ypos 0.1
        yanchor 0
        ypadding 0.05

        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _('Yes') action yes_action
            textbutton _('No') action no_action


init -2 python:
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5







screen quick_menu:


    hbox:
        style_group 'quick'

        xalign 1.0
        yalign 1.0

        textbutton _('Menu (ESC)') action ShowMenu('save') xpos 0.0
        textbutton _('Quicksave (F5)') action myQuickSave_action()
        textbutton _('Quickload (F9)') action myQuickLoad_action()
        textbutton _('Skip (CTRL)') action Skip()
        key 'K_F5' action myQuickSave_action()
        key 'K_F9' action myQuickLoad_action()




init -2 python:
    style.quick_button.set_parent('default')

    style.quick_button.background = "#0008"
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"



    config.default_afm_time = 10
    config.default_afm_enable = False



    class myClearData_action(Action):
        def __call__(self):
            
            renpy.invoke_in_new_context(resetPersistentData, [True])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

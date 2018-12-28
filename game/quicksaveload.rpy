







init python:

    def myQuickSave():
        
        
        renpy.take_screenshot()
        
        renpy.save('1-quicksave', _('Quick Save'))
        
        
        ui.add(Solid((0, 0, 0, 128)))
        ui.text(_('Quicksaved.'),
                  xpos=0.5, xanchor='center', ypos=0.5, yanchor='center')
        ui.saybehavior()
        ui.interact(suppress_overlay=True, suppress_underlay=True)

    def myQuickLoad():
        renpy.load('1-quicksave')




    class myQuickSave_action(Action):
        def __call__(self):
            renpy.invoke_in_new_context(myQuickSave)

    class myQuickLoad_action(Action):
        def __call__(self):
            renpy.invoke_in_new_context(myQuickLoad)



label QuickSaveGame:
    $ myQuickSave()
    return

label QuickLoadGame:
    $ myQuickLoad()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

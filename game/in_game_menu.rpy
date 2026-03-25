screen game_menu(title=None):
    tag menu
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        has vbox
        spacing 8
        xmaximum 400

        text "[title or 'Game Menu']" size 32

        textbutton "Continue" action Return()
        textbutton "Save" action ShowMenu("save")
        textbutton "Load" action ShowMenu("load")
        textbutton "Preferences" action ShowMenu("preferences")
        textbutton "Main Menu" action MainMenu()
        textbutton "Quit" action Quit()

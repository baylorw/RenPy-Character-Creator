#--- RenPy UI controls
# grid, frame, vbox, hbox, fixed, viewport, window
#     frame xalign 0.5 xmaximum 800 xpadding 40 background "bg.png" has vbox spacing 12
# text
# textbutton "text" action Return() or action Jump("label") if "call screen" (modal)
# textbutton "text" action [ToggleScree("this_screen"), Jump("label")] if "show screen" (non-modal)
#    Actions are executed in order
# imagebutton auto "imagename_%s.png" (normal, idle, hover, pressed, action, many others)
#    idle=not focused, normal=focused, hover=mouse hover, pressed=mouse click
# input default "Alice" value VariableInputValue("name")
# mousearea (xpos, ypos, xsize, ysize) hovered Show("screen_name") action Jump("label")
# imagemap: image "x.png" hotspot(10,10,50,50) action Jump("label")
# 

# default attributes = ["brave", "might", "charm", "slick"]

screen text_grid:
    image "backgrounds/classroom.png"
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            # xalign 0.5
            # yalign 0.5
            spacing 20

            hbox:
                spacing 20
                text "Name" yalign 0.5
                frame:
                    xsize 300
                    ysize 60
                    input value VariableInputValue("name") yalign 0.5

            vbox:
                spacing 20
                for attribute_name in attributes:
                    hbox:
                        # spacing 5
                        frame:
                            background None
                            xsize 150
                            # xalign 0.5
                            yalign 0.5
                            text "[attribute_name.capitalize()]"
                        grid 3 1:
                            # xalign 0.5
                            spacing 20
                            frame:
                                # xsize 90
                                # xalign 0.5
                                if getattr(store, attribute_name) <= STAT_MIN:
                                    background None
                                    textbutton " " action Null()
                                else:
                                    textbutton "-":
                                        xsize 50
                                        text_xalign 0.5
                                        action Function(adjust_stat, attribute_name, -1)
                            frame:
                                background None
                                xsize 70
                                xalign 1.0
                                yalign 0.5
                                if getattr(store, attribute_name) == STAT_MAX:
                                    text "{b}[getattr(store, attribute_name)]{/b}":
                                        # xsize 70
                                        xalign 1.0
                                else:
                                    text "[getattr(store, attribute_name)]":
                                        # xsize 70
                                        xalign 1.0
                            frame:
                                # xsize 50
                                # xalign 0.5
                                if getattr(store, attribute_name) >= STAT_MAX:
                                    background None
                                    textbutton " " action Null()
                                else:
                                    textbutton "+":
                                        xsize 50
                                        text_xalign 0.5
                                        action Function(adjust_stat, attribute_name, 1)

            # vbox:
            #     spacing 15
            #     textbutton "left":
            #         xminimum 200
            #         background Solid("#FFCCCC")
            #         text_xalign 0.0
            #     textbutton "center":
            #         xminimum 200
            #         background Solid("#CCFFCC")
            #         text_xalign 0.5
            #     textbutton "right":
            #         xminimum 200
            #         background Solid("#CCCCFF")
            #         text_xalign 1.0

            frame:
                xalign 0.5
                textbutton "{size=45}{color=#FFFF00}All Done{/color}{/size}" action Return()

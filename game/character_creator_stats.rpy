default attributes = ["brave", "might", "charm", "slick"]

screen character_stats_editor:
    image "backgrounds/goth_farmers_market.png" 
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)

        vbox:
            spacing 20

            #--- Name
            hbox:
                spacing 20
                text "Name" yalign 0.5
                frame:
                    xsize 300
                    ysize 60
                    input value VariableInputValue("name") yalign 0.5

            #--- Stats
            vbox:
                spacing 10
                text "Points: [stats_remaining_points()]"
                for attribute_name in attributes:
                    hbox:
                        frame:
                            background None
                            xsize 150
                            yalign 0.5
                            text "[attribute_name.capitalize()]"
                        grid 3 1:
                            spacing 20
                            frame:
                                if getattr(store, attribute_name) <= STAT_MIN:
                                    background None
                                    textbutton " " action NullAction()
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
                                if getattr(store, attribute_name) == STAT_MAX or getattr(store, attribute_name) == STAT_MIN:
                                    text "{b}[getattr(store, attribute_name)]{/b}":
                                        xalign 1.0
                                else:
                                    text "[getattr(store, attribute_name)]":
                                        xalign 1.0
                            frame:
                                if getattr(store, attribute_name) >= STAT_MAX:
                                    background None
                                    textbutton " " action NullAction()
                                else:
                                    textbutton "+":
                                        xsize 50
                                        text_xalign 0.5
                                        action Function(adjust_stat, attribute_name, 1)

            #--- All Done button
            frame:
                xalign 0.5
                textbutton "{size=45}{color=#FFFF00}All Done{/color}{/size}" action Return()

###############################################################################
# Code to set character stats
###############################################################################
init python:
    def stats_combined_total():
        return brave + might + charm + slick

    def stats_remaining_points():
        return STAT_COMBINED_MAX - stats_combined_total()

    def adjust_stat(attribute_name, delta):
        #--- "store" is the default place RenPy puts its variables. 
        current_value = getattr(store, attribute_name)
        new_value     = delta + current_value

        #--- Clamp. Don't let the value exceed min or max.
        new_value    = max(STAT_MIN, min(STAT_MAX, new_value))
        #--- If we clamped we might have changed the delta, so recalculate it.
        delta        = new_value - current_value
        amount_spent = delta + stats_combined_total()

        #--- If they tried to spend more points than they have, reject the entire change.
        if amount_spent > STAT_COMBINED_MAX:
            return

        setattr(store, attribute_name, new_value)

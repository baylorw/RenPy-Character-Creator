label start:
    scene bg background 
    boy "Hi. Who are you?"
    call screen character_stats_editor

    scene bg background 
    boy "Nice to meet you [name]."
    if (brave <= 2) and (might <= 2):
        boy "You're a coward but given how weak you are, that's a good thing."
    elif might <= 2:
        boy "Looks like you skipped leg day. And arm day. And every day."
    elif brave <= 2:
        boy "You're kind of a coward, aren't you?"

    boy "And what do you look like?"
    call screen character_creator_image
    boy "Nice. But this is a tutorial so I'm leaving now."

    return


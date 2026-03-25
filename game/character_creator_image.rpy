###############################################################################
# This is (mostly) the tutorial from Discover with Mia's 
#   Master Character Customization in Ren'Py: Unlock the Secrets.
#   https://www.youtube.com/watch?v=nc9hLt5eLJo
# They used the Awfully Sweet art pack
#   https://butterymilk.itch.io/awfully-sweet
###############################################################################
default hair_index = 0
default skin_index = 0
default eyes_index = 0
default clothes_index = 0
default current_category = "hair"

init python:
    hair_images = ["hair_honey.png", "hair_mousey.png", "hair_mousse.png"]
    skin_images = ["skin_vanilla.png", "skin_caramel.png", "skin_chocolate.png"]
    eyes_images = ["eyes_blue.png", "eyes_green.png", "eyes_brown.png"]
    clothes_images = ["clothes_sunny_sea.png", "clothes_lollipop.png"]

    image_lists = {
        "hair": hair_images,
        "skin": skin_images,
        "eyes": eyes_images,
        "clothes": clothes_images,
    }

    base_xpos = 700
    base_ypos = 100

    transforms = {
        category: Transform(xpos=base_xpos, ypos=base_ypos) 
        for category in image_lists.keys()
    }

    def get_image(category):
        index = globals()[f"{category}_index"]
        images = image_lists[category]
        if 0 <= index < len(images):
            return images[index], transforms[category]
        renpy.error(f"Index {index} out of range for category {category}")
        return None, None

    def change_image(direction):
        category = renpy.store.current_category
        index = globals()[f"{category}_index"]
        if direction == "right":
            index += 1
        else:
            index -= 1
        index %= len(image_lists[category])
        globals()[f"{category}_index"] = index
        # renpy.notify("{} updated".format(category))

screen character_creator_image():
    add "backgrounds/goth_farmers_market.png"
    
    #--- Give credit for work i didn't do.
    frame:
        xalign 0.0
        yalign 1.0
        vbox:
            text "This part taken from Discover with Mia's Master Character Customization in Ren'Py: Unlock the Secrets." size 18
            text "https://www.youtube.com/watch?v=nc9hLt5eLJo" size 18
            text "Character art (Awfully Sweet) by https://butterymilk.itch.io/awfully-sweet" size 18

    #--- Pick category to edit.
    frame:
        xalign 0.5
        hbox:    
            for category in image_lists.keys():
                textbutton category.capitalize() action SetVariable("current_category", category)

    #--- Show the character stats.
    vbox:
        xalign 1.0
        yalign 0.0
        frame:
            hbox:
                spacing 10
                vbox:
                    text "Name:"
                    for attribute_name in attributes:
                        text "[attribute_name.capitalize()]:"
                vbox:
                    text "[name]"
                    for attribute_name in attributes:
                        text "[getattr(store, attribute_name)]"
        frame:
            xalign 0.5
            textbutton "{size=45}{color=#FFFF00}Finished{/color}{/size}" action Return() xalign 0.5

    $skin_img, skin_transform = get_image("skin")
    add skin_img at skin_transform
    $clothes_img, clothes_transform = get_image("clothes")
    add clothes_img at clothes_transform
    $hair_img, hair_transform = get_image("hair")
    add hair_img at hair_transform
    $eyes_img, eyes_transform = get_image("eyes")
    add eyes_img at eyes_transform

    imagebutton:
        idle "ui/arrowLeft.png"
        hover "ui/arrowLeft_hover.png"
        action Function(change_image, "left")
        xpos 0.3
        ypos 0.5
    imagebutton:
        idle "ui/arrowRight.png"
        hover "ui/arrowRight_hover.png"
        action Function(change_image, "right")
        xpos 0.7
        ypos 0.5
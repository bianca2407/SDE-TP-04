#ex 1
def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature()) #display the temperature
    elif input.logo_is_pressed(): #check the light level
        basic.show_icon(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)

#ex 2
def on_logo_touched():
    images.icon_image(IconNames.SQUARE).show_image(0)
    if input.logo_is_pressed():
        images.icon_image(IconNames.SMALL_SQUARE).show_image(0)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
 
 #ex 3
def on_sound_loud():
    for index in range(5):
        led.plot(index, 0)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

#ex 4
degrees = 0

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string("N")
        basic.show_number(input.sound_level())
    elif degrees < 135:
        basic.show_string("E")
        basic.show_number(input.light_level())
    elif degrees < 225:
        basic.show_string("S")
        basic.show_number(input.sound_level())
    elif degrees < 315:
        basic.show_string("W")
        basic.show_number(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)

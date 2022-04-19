def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature()) #display the temperature
    elif input.logo_is_pressed(): #check the light level
        basic.show_icon(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)

from pyfiglet import Figlet

def exit_confirmation(function_name):
    while True:
        try:
            function_name()
        except KeyboardInterrupt:
            sel = input("\n[i] You Pressed Ctrl + C. \n    Exit program? (Y/N): ").lower()
            match(sel):
                case 'y':
                    exit()
                case 'n':
                    pass
                case _:
                    print("Please select a correct option!")

def render_text(text: str, font: str='drpepper'):
    fig = Figlet(font = font)
    return fig.renderText(text)
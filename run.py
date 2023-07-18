from navigation.navigation import Navigation
from pyfiglet import Figlet

loop = True

try:
    with Navigation() as bot:
        while loop == True:
            menu = "1 = Get Router Config\n" \
               "2 = Get Switch Config\n" \
               "3 = Do something like restore all devices\n" \
               "q = Quit"
            f = Figlet(font='slant')
            print(f.renderText('Netgear Automation'))
            print("Welcome to Netgear backup automation tool!")
            print("Choose an option to get started:\n" + menu)
            selection = input().strip().lower()
            if "1" in selection:
                print("Accessing router admin console.")
                bot.router_login()
                print("Lo")
                # bot.access_router_backup_menu()
                # bot.router_save_conf()
                print("Login success!!")
                continue
            elif "2" in selection:
                print("Accessing switch admin console")
                bot.switch_login()
                bot.access_maintenance_tab()
                bot.access_maintenance_menu()
                bot.save_conf()
                print("Config File Saved!!")
                continue
            elif "3" in selection:
                print("third option")
                continue
            elif "q" in selection:
                bot.quit()
                quit()
                print("See you next time!")
                break
            else:
                print("Welcome to Netgear backup automation tool!")
                print("Choose an option to get started:\n" + menu)
                selection = input().strip().lower()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise

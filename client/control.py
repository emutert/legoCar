import rpyc
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_BACKSPACE
import traceback

conn = rpyc.connect('192.168.1.209', port=18812)


curses.initscr()
curses.noecho()
curses.curs_set(0)

def on_press(key):
    if key == KEY_UP:
        conn.root.run()
        
    if key == KEY_DOWN:
        conn.root.back()
        
    if key == KEY_RIGHT:
        conn.root.steering(45)
        

    if key == KEY_LEFT:
        conn.root.steering(-45)
        
    
    if key == KEY_BACKSPACE:
        conn.root.stop()




try:
    # -- Initialize --
    stdscr = curses.initscr()   # initialize curses screen
    curses.noecho()             # turn off auto echoing of keypress on to screen
    curses.cbreak()             # enter break mode where pressing Enter key
                                #  after keystroke is not required for it to register
    stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc
    
    # -- Perform an action with Screen --
    stdscr.border(0)
    stdscr.addstr(5, 5, 'Hello from Curses!', curses.A_BOLD)
    stdscr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)

    while True:
        # stay in this loop till the user presses 'q'
        ch = stdscr.getch()
        if ch == ord('q'):
            break

        on_press(ch)

    # -- End of user code --

except:
    traceback.print_exc()     # print trace back log of the error
    
finally:
    # --- Cleanup on exit ---
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
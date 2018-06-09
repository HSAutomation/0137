#!/usr/bin/python

import time
import os
import sys
import RPi.GPIO as GPIO
import curses

os.system('kbdrate -r 2.0 -d 1000')

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.nodelay(True)
curses.curs_set(False)
stdscr.border(0)
stdscr.addstr(0,11, "               H&S Automation 0137 Board Test              ", curses.A_REVERSE)
stdscr.refresh()

GPIO.setmode(GPIO.BCM)
in_chan_list = [5,6,13,16,19,20,21,26]
GPIO.setup(in_chan_list, GPIO.IN,pull_up_down = GPIO.PUD_UP)
out_chan_list = [14,15,17,18,22,23,24,27]
GPIO.setup(out_chan_list, GPIO.OUT, initial = 0)
timer = True

def get_output():
    line = 6
    for x in out_chan_list:
        if GPIO.input(x) == True:
            state = "     HIGH"
        else:
            state = "      LOW"
        stdscr.addstr(line,45, "Output " + str(x) + state)
        stdscr.refresh()
        line += 1

def get_input():
    line = 6
    for x in in_chan_list:
        if GPIO.input(x) == True:
            state = "     HIGH"
            if x < 10:
                state = "      HIGH"
        else:
            state = "      LOW"
            if x < 10:
                state = "       LOW"
        stdscr.addstr(line,15, "Input " + str(x) + state)
        stdscr.refresh()
        line += 1
     
def main():

    while True:
        time.sleep(.1);
        get_input()
        get_output()
        if  timer == True:
            c = stdscr.getch()
            if c == ord('1'):
                GPIO.output(14, GPIO.HIGH) 
            if c == ord('2'):
                GPIO.output(15, GPIO.HIGH) 
            if c == ord('3'):
                GPIO.output(17, GPIO.HIGH) 
            if c == ord('4'):
                GPIO.output(18, GPIO.HIGH) 
            if c == ord('5'):
                GPIO.output(22, GPIO.HIGH) 
            if c == ord('6'):
                GPIO.output(23, GPIO.HIGH) 
            if c == ord('7'):
                GPIO.output(24, GPIO.HIGH) 
            if c == ord('8'):
                GPIO.output(27, GPIO.HIGH) 
            if (c == ord('a')) or (c == ord('A')):
                GPIO.output(14, GPIO.LOW) 
            if (c == ord('s')) or (c == ord('S')):
                GPIO.output(15, GPIO.LOW) 
            if (c == ord('d')) or (c == ord('D')):
                GPIO.output(17, GPIO.LOW) 
            if (c == ord('f')) or (c == ord('F')):
                GPIO.output(18, GPIO.LOW) 
            if (c == ord('g')) or (c == ord('G')):
                GPIO.output(22, GPIO.LOW) 
            if (c == ord('h')) or (c == ord('H')):
                GPIO.output(23, GPIO.LOW) 
            if (c == ord('j')) or (c == ord('J')):
                GPIO.output(24, GPIO.LOW) 
            if (c == ord('k')) or (c == ord('K')):
                GPIO.output(27, GPIO.LOW) 
            elif (c == ord('q')) or (c == ord('Q')):
                break

               

    GPIO.cleanup()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    os.system('kbdrate -r 11.0 -d 250')
    inb = os.system('clear')

if __name__ == "__main__":
      main()

#!/usr/bin/env python3
from lib import ip_tools, network_scan, speed_test, bandwidth
import time
import curses
import signal
from datetime import datetime

APP_INFO = {
    "title": "NETMONITOR",
    "version": "v1.0",
    "author": "By: Alex Nyambura",
    "description": "A linux network diagnostic tool",
    "license": "MIT License",
    "year": datetime.now().year
}

COLORS = {
    "TITLE": 1,
    "VERSION": 2,
    "AUTHOR": 3,
    "DESC": 4,
    "MENU": 5,
    "HIGHLIGHT": 6,
    "ERROR": 7,
    "WARNING": 8,
    "SUCCESS": 9,
    "BORDER": 10
}

class GracefulExiter:
    def __init__(self):
        self.should_exit = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
    
    def exit_gracefully(self, signum, frame):
        self.should_exit = True

def init_colors():
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(COLORS["TITLE"], curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(COLORS["VERSION"], curses.COLOR_YELLOW, -1)
    curses.init_pair(COLORS["AUTHOR"], curses.COLOR_CYAN, -1)
    curses.init_pair(COLORS["DESC"], curses.COLOR_WHITE, -1)
    curses.init_pair(COLORS["MENU"], curses.COLOR_GREEN, -1)
    curses.init_pair(COLORS["HIGHLIGHT"], curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(COLORS["ERROR"], curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(COLORS["WARNING"], curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(COLORS["SUCCESS"], curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(COLORS["BORDER"], curses.COLOR_BLUE, -1)

def draw_border(stdscr):
    h, w = stdscr.getmaxyx()
    stdscr.border(
        curses.ACS_VLINE, curses.ACS_VLINE,
        curses.ACS_HLINE, curses.ACS_HLINE,
        curses.ACS_ULCORNER, curses.ACS_URCORNER,
        curses.ACS_LLCORNER, curses.ACS_LRCORNER
    )

def show_title_screen(stdscr):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    draw_border(stdscr)
    
    title_block_height = 7
    title_y = h//3 - 2
    for y in range(title_y, title_y + title_block_height):
        stdscr.addstr(y, 0, " " * w, curses.color_pair(COLORS["TITLE"]))
    
    stdscr.addstr(title_y + 1, w//2 - len(APP_INFO["title"])//2,
                f" {APP_INFO['title']} ", 
                curses.color_pair(COLORS["TITLE"]) | curses.A_BOLD | curses.A_STANDOUT)
    
    stdscr.addstr(title_y + 3, w//2 - len(APP_INFO["version"])//2,
                APP_INFO["version"], curses.color_pair(COLORS["VERSION"]))
    
    desc_box_y = title_y + 5
    desc_lines = [APP_INFO["description"][i:i+36] for i in range(0, len(APP_INFO["description"]), 36)]
    for i, line in enumerate(desc_lines):
        stdscr.addstr(desc_box_y + i, w//2 - 18, f"  {line.ljust(36)}  ",
                     curses.color_pair(COLORS["DESC"]))
    
    stdscr.addstr(h - 5, w//2 - len(APP_INFO["author"])//2,
                 APP_INFO["author"], curses.color_pair(COLORS["AUTHOR"]))
    stdscr.addstr(h - 4, w//2 - len(APP_INFO["license"])//2,
                 APP_INFO["license"], curses.color_pair(COLORS["VERSION"]))
    
    continue_msg = " Press any key to continue... "
    stdscr.addstr(h - 2, w//2 - len(continue_msg)//2,
                 continue_msg, curses.color_pair(COLORS["MENU"]) | curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

def show_realtime_bandwidth(stdscr, exiter):
    h, w = stdscr.getmaxyx()
    interval = 0.5  # Update interval in seconds
    
    try:
        import psutil
        iface = psutil.net_io_counters(pernic=True)
        iface = next((i for i in iface if i != 'lo'), None)
        
        old = psutil.net_io_counters(pernic=True).get(iface, None)
        if not old:
            return {"error": "No active network interface found"}
        
        start_time = time.time()
        start_bytes = old.bytes_sent + old.bytes_recv
        
        while not exiter.should_exit:
            stdscr.clear()
            draw_border(stdscr)
            
            now = time.time()
            new = psutil.net_io_counters(pernic=True).get(iface, None)
            if not new:
                break
            
            elapsed = now - start_time
            total_bytes = (new.bytes_sent + new.bytes_recv) - start_bytes
            
            sent = new.bytes_sent - old.bytes_sent
            recv = new.bytes_recv - old.bytes_recv
            
            stdscr.addstr(2, 2, f" Interface: {iface or 'N/A'} ", curses.color_pair(COLORS["HIGHLIGHT"]))
            
            stdscr.addstr(4, 2, " Download Speed: ", curses.color_pair(COLORS["MENU"]))
            stdscr.addstr(4, 20, f"{recv/interval/1024:.2f} KB/s", curses.color_pair(COLORS["DESC"]))
            
            stdscr.addstr(5, 2, " Upload Speed: ", curses.color_pair(COLORS["MENU"]))
            stdscr.addstr(5, 20, f"{sent/interval/1024:.2f} KB/s", curses.color_pair(COLORS["DESC"]))
            
            stdscr.addstr(7, 2, " Total Data: ", curses.color_pair(COLORS["MENU"]))
            stdscr.addstr(7, 20, f"{total_bytes/1024/1024:.2f} MB", curses.color_pair(COLORS["DESC"]))
            
            stdscr.addstr(9, 2, " Duration: ", curses.color_pair(COLORS["MENU"]))
            stdscr.addstr(9, 20, f"{elapsed:.1f} seconds", curses.color_pair(COLORS["DESC"]))
            
            stdscr.addstr(h-2, 2, " Press any key to stop monitoring... ", curses.color_pair(COLORS["WARNING"]))
            
            stdscr.refresh()
            old = new
            
            # Check for keypress without blocking
            stdscr.nodelay(1)
            if stdscr.getch() != -1:
                break
            stdscr.nodelay(0)
            
            time.sleep(interval)
            
        return {"status": "success", "duration": elapsed, "total_bytes": total_bytes}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

def run_selected(stdscr, selected_idx, exiter):
    functions = [
        ("IP Info", lambda: ip_tools.get_network_info()),
        ("Network Scan", lambda: network_scan.scan_network()),
        ("Speed Test", lambda: speed_test.run_speed_test(stdscr)),
        ("Bandwidth", lambda: show_realtime_bandwidth(stdscr, exiter))    
    ]
    return functions[selected_idx][1]()

def display_results(stdscr, result):
    h, w = stdscr.getmaxyx()
    y = 2
    
    if isinstance(result, dict):
        if result.get('status') == 'error':
            stdscr.addstr(y, 2, " ⚠️ ERROR ", curses.color_pair(COLORS["ERROR"]) | curses.A_BOLD)
            stdscr.addstr(y, 12, result.get('message', ''), curses.color_pair(COLORS["ERROR"]))
            y += 2
            if 'solution' in result:
                stdscr.addstr(y, 2, " 💡 TRY THIS ", curses.color_pair(COLORS["WARNING"]) | curses.A_BOLD)
                stdscr.addstr(y, 15, result['solution'], curses.color_pair(COLORS["WARNING"]))
                y += 2
        else:
            for k, v in result.items():
                if k != 'status':
                    label = f" {k.replace('_', ' ').title()}: "
                    stdscr.addstr(y, 2, label, curses.color_pair(COLORS["MENU"]))
                    stdscr.addstr(y, 2 + len(label), str(v), curses.color_pair(COLORS["DESC"]))
                    y += 1
                    if y >= h-3: break
    else:
        for i, line in enumerate(str(result).split('\n')[:h-3]):
            stdscr.addstr(i+2, 2, line, curses.color_pair(COLORS["DESC"]))

def main(stdscr):
    init_colors()
    exiter = GracefulExiter()
    show_title_screen(stdscr)
    
    curses.curs_set(0)
    options = ["IP Info", "Network Scan", "Speed Test", "Bandwidth Monitor"]
    current_idx = 0
    h, w = stdscr.getmaxyx()

    while not exiter.should_exit:
        stdscr.clear()
        draw_border(stdscr)
        
        header = f" {APP_INFO['title']} {APP_INFO['version']} "
        stdscr.addstr(0, w//2 - len(header)//2, header,
                     curses.color_pair(COLORS["TITLE"]) | curses.A_BOLD)
        
        stdscr.addstr(1, 4, "▲/▼: Navigate", curses.color_pair(COLORS["DESC"]))
        stdscr.addstr(1, 20, "ENTER: Select", curses.color_pair(COLORS["DESC"]))
        stdscr.addstr(1, 36, "Q: Quit", curses.color_pair(COLORS["DESC"]))
        stdscr.addstr(1, 46, "Ctrl+C: Exit", curses.color_pair(COLORS["DESC"]))
        
        for i, option in enumerate(options):
            y = 4 + i*2
            x = w//2 - len(option)//2 - 2
            if i == current_idx:
                stdscr.addstr(y, x, f">> {option} <<", curses.color_pair(COLORS["HIGHLIGHT"]) | curses.A_BOLD)
            else:
                stdscr.addstr(y, x, f"   {option}   ", curses.color_pair(COLORS["MENU"]))
        
        try:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                current_idx = max(0, current_idx - 1)
            elif key == curses.KEY_DOWN:
                current_idx = min(len(options) - 1, current_idx + 1)
            elif key in [curses.KEY_ENTER, 10, 13]:
                stdscr.clear()
                draw_border(stdscr)
                try:
                    result = run_selected(stdscr, current_idx, exiter)
                    display_results(stdscr, result)
                except KeyboardInterrupt:
                    continue
                except Exception as e:
                    stdscr.addstr(2, 2, " CRITICAL ERROR ", curses.color_pair(COLORS["ERROR"]) | curses.A_BOLD)
                    stdscr.addstr(2, 18, str(e), curses.color_pair(COLORS["ERROR"]))
                stdscr.getch()
            elif key == ord('q'):
                break
                
        except KeyboardInterrupt:
            exiter.should_exit = True

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            curses.endwin()
            print("\n\033[1;34m»» Thanks for using NetMonitor! ««\033[0m\n")
        except:
            print("\n»» Thanks for using NetMonitor! ««\n")
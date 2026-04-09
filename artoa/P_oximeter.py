
import curses
import psutil
import time

def draw_oximeter(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, 
    curses.COLOR_BLACK)   # Red for
    curses.init_pair(2, curses.COLOR_YELLOW,
                     curses.COLOR_BLACK)  # Yellow for warning
    curses.init_pair(3, curses.COLOR_RED,
                     curses.COLOR_BLACK)   # Red for critical
    
    while True:
        stdscr.clear()
        # Get the current CPU usage
        cpu_usage = psutil.cpu_percent #(interval=1)
        ram = psutil.virtual_memory().percent
        net = psutil.net_io_counters()

        def get_color(value):
            if value < 50:
                return curses.color_pair(1)  # green
            elif value < 80:
                return curses.color_pair(2)  # yellow
            else:
                return curses.color_pair(3)  # red
            
        def draw_bar(y, label, value):
            bar_length = 40
            filled = int(bar_length * value / 100)
            bar="█" * filled + "░" * (
                bar_length - filled)  
            stdscr.addstr(y, 2, f"{label}: [{(bar
               )}] {value:.1f}%", get_color(value))
            
        stdscr.addstr(1, 2, "🖥 Live System Monitor",
                             curses.color_pair(1))
        stdscr.addstr(2, 2, "-" * 55,
                             curses.color_pair(1))
        
        draw_bar(4, "CPU ", cpu_usage)
        draw_bar(6, "RAM ", ram)
        
        stdscr.addstr(8, 2, f"NET: ↑ {net.bytes_sent /
        1024 / 1024:.2f} MB/s ↓  {net.bytes_recv / 1024 /
        1024:.2f} MB/s", curses.color_pair(1))

        stdscr.addstr(10, 2, "Press Ctrl+C to exit",
                             curses.color_pair(2))
        
        stdscr.refresh()
        time.sleep(1)


curses.wrapper(draw_oximeter)


        # # Determine the color based on CPU usage
        # if cpu_usage < 50:
        #     color = curses.color_pair(1)  # Green
        # elif cpu_usage < 80:
        #     color = curses.color_pair(2)  # Yellow
        # else:
        #     color = curses.color_pair(3)  # Red
        
        # # Display the CPU usage with the appropriate color
        # stdscr.addstr(0, 0, f"CPU Usage: {cpu_usage:.2f}%", color)
        # stdscr.refresh()
        
        # time.sleep(1)
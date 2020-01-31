import sys, fhem, logging, time, datetime

fh = fhem.Fhem('IP', port=8083, protocol='https', username="", password="") # change according to your fhem configuration

logging.basicConfig(level=logging.DEBUG)

botname = "NAME"  # set telegram bot name to receive status messages
light = "NAME"  # set light(s) to turn on
path_to_file = "PATH" # ex: /opt/fhem/alarm.txt


def send_message(text):
    if botname != "NAME":
        fh.send_cmd(f"set {botname} message {text} (fhem_wakeup)")


alarm_time_file = open(f'{path_to_file}', 'r')
alarm_time = str(alarm_time_file.read()).strip()
try:
    alarm_time = datetime.datetime.strptime(alarm_time, '%d. %b %Y at %H:%M')
except ValueError:
    if alarm_time == "None":
        send_message("No alarm time given. Input = None")
        sys.exit()
    else:
        send_message("Something went wrong.")
        sys.exit()


def sunrise():
    fh.send_cmd(f"set {light} dim80% 1800")  # Dim all lights to 100% in 30 Minutes


def start_alarm_time(alarm_time):
    now = time.ctime()
    now = datetime.datetime.strptime(now, '%a %b %d %H:%M:%S %Y')
    if alarm_time.day == now.day and now > alarm_time:  # If same day and before midnight
        alarm_time += datetime.timedelta(days=1)  # Add one day
        print(f"New alarm time: {alarm_time}")
        send_message(f"Alarm set for {alarm_time}")
    else:
        send_message(f"Alarm set for {alarm_time}")
    try:
        sleep_seconds = (alarm_time - now).seconds - 900  # Substract 15 minutes
        time.sleep(sleep_seconds)
    except ValueError:
        send_message("The alarm couldn't be set.")


if alarm_time != "None":
    start_alarm_time(alarm_time)
    sunrise()
    send_message("Good Morning!")
    sys.exit()
else:
    send_message("No alarm time was set. Exiting...")

alarm_time_file.close()

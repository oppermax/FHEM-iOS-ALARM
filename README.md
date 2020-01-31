# FHEM-iOS-ALARM
Set a single FHEM wakeup with iOS Shortcuts


Setting up wakeup-routines is farely easy with integrated FHEM modules. If each of your days differ and you don't want to change an entire routine, there is a way to set single wakeup-automations with iOS-Shortcuts, FHEM and Python.

The gain of this is to set the alarm and the routine with one action from your iOS device.

For this to work you need to have Python-Fhem installed. The documentation can be found here: https://github.com/domschl/python-fhem

(1) The Apple Shorcut

  1. Add the shortcut https://www.icloud.com/shortcuts/53561d5e039a4004a8a44f9c2d0e55fa
  2. Configure the ssh module with your credencials
  3. Optional: Add a condition to only execute the ssh command if your device is connected to home wifi (= you are at home)
  
(2) Add the alarm.txt

  1. In /opt/fhem create a file called alarm.txt (in this example)
    This is where the shorcut will write the configured alarm time into.
    Any location or filename will work but you will need to change it in the rest of the locations.
    
(3) Add fhem_wakeup.py to device you are running fhem on (commonly a raspberry pi)

  1. In /opt/fhem create a file called fhem_wakeup.py or copy the file from here
  2. Configure the file to match your requirements (hostname, user, pw, location of alarm.txt, lights to control)
  3. If you want to receive status updates via telegram, add the name of your bot
  
  The shortcut will write the alarm time without changing the date. Therefore, the fhem_wakeup.py will add a day if the alarm   time is before the current time.
  
(4) Issues

  1. iOS-Shortcuts currently has no way to edit existing alarms and will therefore create a new alarm every time
    You will need to clean the alarm list (which can easily be done with siri).
  2. The default alarm tone is always Radar

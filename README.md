# lldb-ram-dump
Utility for dumping RAM from iOS/macOS devices

### How to use?

1. Open your Xcode project & run your app on iOS device.
2. Put a breakpoint and when it is triggered, open `lldb` console.
3. Type `script` command, execute it.
4. Then type `exec(open('/Users/alexlitreev/dump.py').read())` — replace `/Users/alexlitreev/dump.py` with absolute path to `dump.py` script on your Mac.
5. Execute `processRAM()` command, if Xcode requesting desktop permissions — grant it with 'em.
6. Wait till all memory regions saved, `dump.txt` file will be on your Desktop.

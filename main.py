import config
import payload
import time

def main():
    print('Running payload.')
    payload.payload()
    print('Done.')


try:
    import wifi
    try:
        wifi.enable_ap(False)
        if wifi.connect() and config.ENABLED:
            main()
    finally:
        # In any case, setup the access point and light the LED
        wifi.enable_ap(True)
        import machine
        machine.Pin(config.LED_PIN, machine.Pin.OUT).value(0)
        import webrepl
        webrepl.start()
except ImportError:
    main()


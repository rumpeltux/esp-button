SRC:=boot.py webrepl_cfg.py config.py wifi.py payload.py main.py
PORT=/dev/ttyUSB0

flash:
	$(foreach file, $(SRC), echo $(file); /usr/local/bin/ampy --port $(PORT) put $(file); sleep 1; )

.PHONY: flash

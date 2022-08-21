.PHONY: all build install format clean

all: build

build:
	poetry build -f wheel
	web-ext build --overwrite-dest --source-dir extension

install:
	ls ./dist/pmenu-*.whl | sort | tail -n 1 | xargs pipx install
	cp extension/pmenu.json ~/.mozilla/native-messaging-hosts/
	cp scripts/* ~/.local/bin/

format:
	poetry run black pmenu
	prettier --write extension

clean:
	rm -rf dist web-ext-artifacts/

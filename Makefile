.PHONY: all build install format clean check

all: build

build:
	poetry build -f wheel
	web-ext build --overwrite-dest --source-dir extension

install:
	ls ./dist/pmenu-*.whl | sort | tail -n 1 | xargs pipx install
	cp extension/pmenu.json ${HOME}/.mozilla/native-messaging-hosts/
	cp scripts/* ${HOME}/.local/bin/

format:
	poetry run black pmenu
	prettier --write extension

check:
	@set -e; \
	poetry run pyright pmenu; \
	poetry run black --check pmenu; \
	prettier --check extension

clean:
	rm -rf dist web-ext-artifacts/

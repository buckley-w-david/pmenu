# pmenu

domain aware passmenu wrapper script for Firefox

My password store is structured like so, and this code assumes that to be the case.

Password Store  
├── example.com  
│   └── user@example.com  
├── example.ca  
│   └── user@example.ca  
├── example.org  
│   └── user@example.org  
└── example.net  
    └── UserName  

## Native Component Installation

This is a walkthough of how *I* would install it using tools I typically use.

The following tools are required:
 - [poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
 - [pipx](https://pypa.github.io/pipx/#install-pipx)

```bash
$ git clone https://github.com/buckley-w-david/pmenu.git
$ cd pmenu
```

You'll need to edit `pmenu/config.py` and `extension/pmenu.json` to replace some file paths with equivalents for your system.

Once that is done, you can continue:
```bash
$ poetry build -f wheel
$ pipx install ./dist/pmenu-*.whl
$ cp extension/pmenu.json ~/.mozilla/native-messaging-hosts/
```

## Extension Installation

I haven't put it up on [addons.mozilla.org](https://addons.mozilla.org/) yet, no good way to do this right now.

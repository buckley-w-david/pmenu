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

The following tools are required:
 - [poetry](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
 - [pipx](https://pypa.github.io/pipx/#install-pipx)
 - [web-ext](https://github.com/mozilla/web-ext)

```
$ ./configure
$ make
$ make install
```

## Extension Installation

I haven't put it up on [addons.mozilla.org](https://addons.mozilla.org/) yet, which means you'll have to be running a Firefox distribution that allows installing unsigned extensions (Like developer edition).

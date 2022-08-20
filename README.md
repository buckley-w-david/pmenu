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

Since the `recovery.jsonlz4` file is only regenerated every 15 seconds, there can be up to 15 seconds of delay for when switching tabs.

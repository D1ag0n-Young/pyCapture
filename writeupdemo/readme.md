# directory format

```bash
.
├── img
│   ├── 20231010141004.png
│   ├── 20231010141040-1.png
│   └── 20231010141040.png
└── writeup.md
```

The names of img and writeup.md cannot be changed and use the `zip team1 writeup.zip img/writeup.md` command for compression.

# writeup.md format

1. It is necessary to ensure that all first level titles (# problem) are the title of the competition question
2. Use markdown code syntax to write relevant code

# Zip package directory format

The compressed directory structure is as follows

```bash
➜  writeupdemo unzip -l team1-writeup.zip 
Archive:  team1-writeup.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2023-10-10 14:11   img/
     3789  2023-10-10 14:10   img/20231010141004.png
     8550  2023-10-10 14:10   img/20231010141040-1.png
     8550  2023-10-10 14:10   img/20231010141040.png
      959  2023-10-21 00:33   writeup.md
---------                     -------
    21848                     5 files
```




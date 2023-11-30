# Spirit Enigma
#### Video Demo:  https://youtu.be/tGpvV0P576k
#### Description:
My project is a riddle game based with Flask (back), JS (Front) and sqlite(DB)

### app :
    route config for the input of the user
    i use flask blueprint to help me organize in multiple file
    direct relation with service

### dataAcess :
    file who are responsable for acces to the db, return the correct file.
    take in param what is necessary for the query and return the responce in the correct format

### language and language_files :
    Responsable for the traduction, call the get function and it's will return the correct string
    It's a 2 dimentional list, the first param is the language and the second is the id of the string (the n° of the line - 2, the array is in base 0 (the file start at 1) and the first param is the name of the language)
    can return the list of keys to be directly implemented in the html file (with jinja)

### service :
    Responsable of the logic and data processing
    Game service are in direct connexion to effect service.
    When a event is triggers in the game, a post command is fired with the id of our card and the id of the field card.
    game service verify is the 2 id are in the list (list who is saved from the data base)
    If the 2 id are in the list, pass the event id and the param to effect service
    The effect service are in charge of call the right file in function of the param

### gameBoard :
    stock the entire game param who is in the db for faster retreval

## DB schema:
    // User save file, with deck to save new card unlock or ask to link user and ask id
    "users" (
        "id"    INTEGER NOT NULL,
        "name"  TEXT,
        "password"      TEXT,
        "language"      TEXT DEFAULT 'eng',
        "field" TEXT DEFAULT 'lobby',
        "pos"   INTEGER DEFAULT 1,
        PRIMARY KEY("id" AUTOINCREMENT));
     "deck" (
        "user_id"       INTEGER,
        "card_id"       INTEGER,
        "hand"        INTEGER);
    "user_ask" (
        "user_id"       INTEGER,
        "ask_id"        INTEGER);

    // Game param with every info - card event are the first check before map event
    "map_events" (
        "map_id"        INTEGER,
        "user_card"     INTEGER,
        "field_card"    INTEGER,
        "result"        INTEGER,
        "param"       INTEGER);

    "fields" (
        "id"    INTEGER NOT NULL,
        "name"  TEXT,
        "langage_id"    INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT));
     "maps" (
        "id"    INTEGER,
        "field_id"      INTEGER,
        "number"        INTEGER,
        PRIMARY KEY("id"));
    "cards" (
        "id"    INTEGER NOT NULL,
        "name"  TEXT,
        "language_id"   INTEGER,
        "zone_id"       INTEGER,
        PRIMARY KEY("id" AUTOINCREMENT));
    "ask" (
        "id"    INTEGER,
        "text"  TEXT);

    "card_events" (
        "user_card"     INTEGER,
        "field_card"    INTEGER,
        "result"        INTEGER,
        "param" INTEGER);


I learn a lot in cs50.
I start 2 year prior the beginning of the course.
It's help me answers obscure questions and really help me understand how computer works.
I try various challenge in this project
    - css only app
    - language file system (for a new language, just put the trad in language_file)
    - create a program who can grow with just simple addition in the database. (code who are really generic and can adapte to the
      situation)
    - learn flask in details
That was a really fun journey,
glad to have experienced it

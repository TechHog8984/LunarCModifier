# LunarCModifier
This is a python application that allows you to modify the HTML, CSS, &amp; JS of the Lunar Client launcher. This allows limitless possibilities for what the launcher can look like.

## Dependencies
[Python3](placeholder)
[Node.js](placeholder)

## Credits
[SpotiLight](https://github.com/SK3-4121/SpotiLight) - LunarCModifier is pretty much just a remake of this, but for Lunar Client instead of spotify. Credits to SK3-4121

## How it works
The Lunar Client launcher is an electron app, which means that it is pretty much just a website. What we can do is take that electron app, decompile it, edit it (change the css, for example), and then recompile to see your changes.

### Decompile:
First, we get the Lunar Client resource directory (appdata/Local/Programs/lunarclient/resources) where the app.asar file is located).
Then, we extract (unpack) the asar file to a directory called decompiled. That's it! Now you can edit these contents and then compile.

### Compile:
First, we, again, get the Lunar Client resource directory (appdata/Local/Programs/lunarclient/resources) where the app.asar file is located).
Then, we compile (pack) the directory back to an asar file. That's it! Now we can run the Lunar Client launcher like normal, and you should see your changes.
Note that if you get an error, it might be hard to debug it, so don't screw anything up!.

## Options
Once you run the program, you will be presented with some options.
The first option you have is the Exit option.
This will quit the programl.
Press 1 followed by enter to run this.

The second option is the BackupAsar option.
This will backup your app.asar so that if you break anything, you can restore the backup.
Press 2 followed by enter to run this.

The third option is the RestorBackup option.
This will restore the backup, so that (as long as there is a backup, make sure to create one!!!) the launcher will be back to it's original state.
Press 3 followed by enter to run this.

The fourth option is the Decompile option.
This will do as described [here](#decompile).
Press 4 followed by enter to run this.

The fith option is the Compile option.
This will do as described [here](#compile).
Press 5 followed by enter to run this.

## Simple Instructions
Step 1: Run the program (python main.py)
Step 2: Run BackupAsar (Press 2 followed by enter)
Step 3: Run Decompile (Press 4 followed by enter)
Step 4: Modify the contents of the "decompiled" directory.
Step 5: Run Compile (Press 5 followed by enter)
Step 6: Launch Lunar Client
Note: CLOSE THE LAUNCHER BEFORE COMPILING, YOU NEED TO RE-OPEN THE LAUNCHER TO SEE CHANGES
If you experience any issues with the launcher, close the launcher and restore your backup.

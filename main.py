import os;


def getLunarResourcesPath():
    AppdataPath = os.getenv("APPDATA");
    ProgramsPath = AppdataPath + "\\..\\Local\\Programs";
    LunarResourcesPath = ProgramsPath + "\\lunarclient\\resources";

    return LunarResourcesPath;

def backupAsar():
    ResourcePath = getLunarResourcesPath();
    BackupPath = ResourcePath + "\\app.asar.LCM_backup";
    AppPath = ResourcePath + "\\app.asar";

    try:
        file = open(BackupPath);
        if file:
            file.close();
            return "app.asar backup already exists";
    except:
        pass;
    
    app = None;
    try:
        app = open(AppPath, "rb");
    except Exception as e:
        return "Failed to find app.asar in resources (reinstall Lunar Client?): " + str(e);
    
    try:
        backup = open(BackupPath, "wb");
        backup.write(app.read());
        backup.close();
        app.close();
    except Exception as e:
        return "Failed to write to backup: " + str(e);
    
    return "Backed up successfully!";

def restoreBackup():
    ResourcePath = getLunarResourcesPath();
    BackupPath = ResourcePath + "\\app.asar.LCM_backup";
    AppPath = ResourcePath + "\\app.asar";

    app = None;
    try:
        app = open(AppPath, "wb");
    except Exception as e:
        return "Failed to find app.asar in resources (reinstall Lunar Client?): " + str(e);
    
    backup = None;
    try:
        backup = open(BackupPath, "rb");
    except Exception as e:
        app.close();
        return "Failed to find backup: " + str(e);
    
    app.write(backup.read());
    backup.close();
    app.close();
    return "Restored backup successfully!";

def decompile():
    ResourcePath = getLunarResourcesPath();
    AppPath = ResourcePath + "\\app.asar";
    DecompilePath = ResourcePath + "\\decompiled\\";

    try:
        open(AppPath);
    except Exception as e:
        return "Failed to find app.asar in resources (reinstall Lunar Client?): " + str(e);

    os.system(f"npx asar extract {AppPath} {DecompilePath}");
    return "Decompiled successfully!";

def compile():
    ResourcePath = getLunarResourcesPath();
    AppPath = ResourcePath + "\\app.asar";
    DecompilePath = ResourcePath + "\\decompiled";

    if not os.path.isdir(DecompilePath):
        return "Failed to find decompile in resources (run decompile)";

    os.system(f"npx asar pack {DecompilePath} {AppPath}");
    return "Compiled successfully!";

choices = [
    {
        "Name":"Exit",
        "Desc":"Closes the program"
    },
    {
        "Name":"BackupAsar",
        "Desc":"Backs up your app.asar so if anything breaks, you can restore the original.",
        "Func":backupAsar
    },
    {
        "Name":"RestoreBackup",
        "Desc":"Restores your backup of app.asar, restoring the app to it's original state.",
        "Func":restoreBackup
    },
    {
        "Name":"Decompile",
        "Desc":"Decompiles the Lunar Client launcher, and outputs it into a folder called 'decompiled'.",
        "Func":decompile
    },
    {
        "Name":"Compile",
        "Desc":"Compiles the decompiled code, which you are expected to modify.",
        "Func":compile
    }
];

lastMsg = None;

def __main__():
    global lastMsg;
    print("");
    print("LunarCModifier by TechHog#8984");
    print("Credits to contributors of https://github.com/SK3-4121/SpotiLight");
    print("\n");
    if lastMsg:
        print("Message: " + lastMsg + "\n");

    for index in range(1, len(choices) + 1):
        choice = choices[index - 1];

        print(f"[{index}] {choice.get('Name')}: {choice.get('Desc')}");

    inp = input();
    try:
        inp = int(inp);
    except Exception as e:
        lastMsg = "Failed to convert choice to number: " + str(e);
        __main__();
        return;

    chosen = None;
    for index in range(1, len(choices) + 1):
        choice = choices[index - 1];

        if inp == index:
            chosen = choice;
            break;
    
    if not chosen:
        lastMsg = "Invalid choice!";
        __main__();
        return;
    
    if chosen == choices[0]:
        return;

    try:
        lastMsg = chosen.get("Func")();
    except Exception as e:
        lastMsg = "Failed to run choice: " + str(e);
    
    __main__();

if __name__ == "__main__":
    __main__();

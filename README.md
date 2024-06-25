# Smali.Smali 🪄

Welcome to the **Smali.Smali** repository! This project is your one-stop-shop for decompiling APK files and extracting Smali code from `classes.dex` files for modifications. Say goodbye to manual decompiling, and let this script do the heavy lifting for you.

![Example Image](https://github.com/ON00dev/Smali.Smali/blob/main/utils/Img_exemple_Terminal.PNG)

## What does this tool do? ✨

1. **Extract APK Files**: Unzip your APK and delve into its inner secrets.
2. **Decompile DEX to Smali**: Break down those `.dex` files into readable Smali code.

## Getting Started ✨

- Clone the repository: `git clone https://github.com/ON00dev/Smali.Smali.git`.
- Go to the directory: `cd Samli.Smali`.
- Install the required packages: `pip install -r requirements.txt`.
- Run the script: `python3 SmaliSmali.py`.
- Follow the interactive prompts to guide your journey.

## Get the Results.

Your APK will be unzipped.
Smali code will be extracted and optionally saved.

## Requirements

- python3
- unzip
- java

## Example Smali Code 📝

Here's a sneak peek of what Smali code looks like before it morphs into something greater:

```smali
.class public Lcom/example/MyClass;
.super Ljava/lang/Object;
.method public static myStaticMethod(I)V
    .locals 1
    const/4 v0, 0x1
    add-int/2addr v0, p0
    return-void
.end method
```

## Contribute to this tool ✨

Found a bug? Have a feature request? Want to improve the spell? Feel free to open an issue or submit a pull request. Contributions are always welcome!

## Disclaimer

This repository is intended for educational and ethical purposes only. Please ensure you have the right to decompile and analyze any APK file you use with this tool.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

---

Happy Decompiling! ✨

Enjoy exploring the enchanted world of APK decompilation and Smali code extraction with Smali.Smali
.
.

# Smali.Smali 🪄

Welcome to the **Smali.Smali** repository! This project is your one-stop-shop for decompiling APK files and extracting Smali code from `classes.dex` files for modifications. Say goodbye to manual decompiling, and let this script do the heavy lifting for you.

![Example Image](https://github.com/ON00dev/Smali.Smali/blob/main/utils/Img_exemple_Terminal.PNG)

## What's Inside the Cauldron? 🧙‍♂️

1. **Extract APK Files**: Unzip your APK and delve into its inner secrets.
2. **Decompile DEX to Smali**: Break down those `.dex` files into readable Smali code.

## How to Use the Spellbook 🪄📜

1. **Prepare your ingredients**:
   - An APK file.
   - `baksmali.jar` for decompiling DEX to Smali.
   - The Python packages: `colorama`.

2. **Run the Magic**:
   - Clone the repository.
   - Install the required packages: `pip install -r requirements.txt`.
   - Keep `baksmali.jar` in the directory `./tools`.
   - Run the script: `python3 smali_smali.py`.
   - Follow the interactive prompts to guide your transformation journey.

3. **Marvel at the Results**:
   - Your APK will be unzipped.
   - Smali code will be extracted and optionally saved.

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

## Contribute to the Magic ✨

Found a bug? Have a feature request? Want to improve the spell? Feel free to open an issue or submit a pull request. Contributions are always welcome!

## Disclaimer

This repository is intended for educational and ethical purposes only. Please ensure you have the right to decompile and analyze any APK file you use with this tool.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

---

Happy Decompiling! 🧙‍♂️✨

Enjoy exploring the enchanted world of APK decompilation and Smali code extraction with Smali.Smali.

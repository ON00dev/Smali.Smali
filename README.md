# DPY-APK 🪄

Welcome to the **DPY-APK** repository! This project is your one-stop-shop for transforming APK files into Python code, with a sprinkle of C and Smali magic along the way. Say goodbye to manual decompiling and converting, and let this script do the heavy lifting for you.

![Minha Imagem](https://github.com/ON00dev/DPY-APK/blob/main/tools/Img_exemple_Terminal.PNG)

## What's Inside the Cauldron? 🧙‍♂️

1. **Extract APK Files**: Unzip your APK and delve into its inner secrets.
2. **Decompile DEX to Smali**: Break down those `.dex` files into readable Smali code.
3. **Convert Smali to C**: Wave your wand (or run the script) to transform Smali code into C.
4. **Transform C to Python**: Finally, convert the C code into beautiful, readable Python.

## How to Use the Spellbook 🪄📜

1. **Prepare your ingredients**:
   - An APK file.
   - `baksmali.jar` for decompiling DEX to Smali.
   - The Python packages: `ctopython`, `smalitoc`, `colorama`.

2. **Run the Magic**:
   - Clone the repository.
   - Install the required packages: `pip install -r requirements.txt`.
   - Keep `baksmali.jar` in the directory `./tools`.
   - Run the script: `python3 dpy_apk.py`.
   - Follow the interactive prompts to guide your transformation journey.

3. **Marvel at the Results**:
   - Your APK will be unzipped.
   - Smali code will be extracted and optionally saved.
   - Smali will be converted to C, which can also be saved.
   - C will be transformed into Python, ready to be saved and executed.

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

## A Glimpse of the Final Python Code 🐍

And voilà, here's a taste of the final product:

```python
def my_static_method(input):
    result = input + 1
    return result
```

## Contribute to the Magic ✨

Found a bug? Have a feature request? Want to improve the spell? Feel free to open an issue or submit a pull request. Contributions are always welcome!

## Disclaimer

This repository is intended for educational and ethical purposes only. Please ensure you have the right to decompile and analyze any APK file you use with this tool.

## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

---

Happy Converting! 🧙‍♂️✨

Enjoy exploring the enchanted world of APK decompilation and code transformation with the APK-to-Python Magic Converter.

import subprocess
import os
import sys
import logging
from typing import Optional
from colorama import init, Fore
import ctopython
import smalitoc

# Inicialize o colorama
init(autoreset=True)

# Cleaning terminal
operacional_sys =  os.name
if operacional_sys =="posix":
    os.system("clear")
elif operacional_sys =="nt":
    os.system("cls")
    print(Fore.RED+"WARNING: This tool may not work correctly on operating systems such as Windows."+Fore.RESET)
else:
    print(Fore.RED+"Operating System not supported."+Fore.RESET)

print(Fore.BLUE+'''
    8888888b.  8888888b. Y88b   d88P             d8888 8888888b.  888    d8P  
    888  "Y88b 888   Y88b Y88b d88P             d88888 888   Y88b 888   d8P   
    888    888 888    888  Y88o88P             d88P888 888    888 888  d8P    
    888    888 888   d88P   Y888P             d88P 888 888   d88P 888d88K     
    888    888 8888888P"     888             d88P  888 8888888P"  8888888b    
    888    888 888           888    888888  d88P   888 888        888  Y88b   
    888  .d88P 888           888           d8888888888 888        888   Y88b  
    8888888P"  888           888          d88P     888 888        888    Y88b 
                                                                              
-------------------------------------------------------------------------------- 
  
    [☆]Developed by ON00dev
    [☆]Github: https://github.com/ON00dev
    
--------------------------------------------------------------------------------    
''')
# Configure o logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def verify_file_path(file_path: str) -> None:
    logging.debug(f"Verifying file path: {file_path}")
    if not os.path.isfile(file_path):
        logging.error(f"{Fore.RED}File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

def create_output_dir(output_dir: str) -> None:
    logging.debug(f"Creating output directory: {output_dir}")
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            logging.info(f"{Fore.GREEN}Output directory created: {output_dir}")
        except OSError as e:
            logging.error(f"{Fore.RED}Error creating output directory: {e}")
            raise RuntimeError(f"Error creating output directory: {e}")

def unzip_apk(apk_path: str, output_dir: str) -> None:
    create_output_dir(output_dir)
    command = ['unzip', '-o', apk_path, '-d', output_dir]
    logging.debug(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
        logging.info(f"{Fore.GREEN}APK extracted to: {output_dir}")
    except subprocess.CalledProcessError as e:
        logging.error(f"{Fore.RED}Error extracting APK: {e}")
        raise RuntimeError(f"Error extracting APK: {e}")

def decompile_dex_to_smali(dex_path: str, output_dir: str) -> None:
    create_output_dir(output_dir)
    command = ['java', '-jar', './utils/baksmali.jar', 'd', dex_path, '-o', output_dir]
    logging.debug(f"Running command: {' '.join(command)}")
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"{Fore.GREEN}DEX decompiled to Smali in: {output_dir}")
    except subprocess.CalledProcessError as e:
        logging.error(f"{Fore.RED}Error decompiling DEX: {e.stderr.decode()}")
        raise RuntimeError(f"Error decompiling DEX: {e.stderr.decode()}")

def save_code_to_file(code: str, file_path: str) -> None:
    try:
        with open(file_path, 'w') as file:
            file.write(code)
        logging.info(f"{Fore.GREEN}Code saved to {file_path}")
    except IOError as e:
        logging.error(f"{Fore.RED}Error saving code to file: {e}")
        raise RuntimeError(f"Error saving code to file: {e}")

if __name__ == "__main__":
    apk_path: str = input("Enter the path to the APK file: ").strip()
    extracted_dir: str = './extracted_apk'
    smali_output_dir: str = './smali_output'

    if not apk_path:
        logging.critical(f"{Fore.RED}APK path cannot be empty.")
        sys.exit(1)

    try:
        # Verify and extract the APK
        verify_file_path(apk_path)
        unzip_apk(apk_path, extracted_dir)

        # Find the classes.dex file
        dex_path: str = os.path.join(extracted_dir, 'classes.dex')
        verify_file_path(dex_path)

        # Decompile the DEX file to Smali
        decompile_dex_to_smali(dex_path, smali_output_dir)

        # Dummy Smali code for demonstration
        smali_code: str = """
        .class public Lcom/example/MyClass;
        .super Ljava/lang/Object;
        .method public static myStaticMethod(I)V
            .locals 1
            const/4 v0, 0x1
            add-int/2addr v0, p0
            return-void
        .end method
        """
        print(smali_code)
        
        save: str = input("Do you want to save the Smali code to a .smali file? (y/n): ").strip().lower()
        if save == 'y':
            smali_file_path: str = "code.smali"
            save_code_to_file(smali_code, smali_file_path)

        # Convert Smali to C
        try:
            c_code: str = smalitoc.convert_smali_to_c(smali_code)
            print(c_code)
        except Exception as e:
            logging.error(f"{Fore.RED}Error converting Smali to C: {e}")
            raise RuntimeError(f"Error converting Smali to C: {e}")
        
        save = input("Do you want to save the C code to a .c file? (y/n): ").strip().lower()
        if save == 'y':
            c_file_path: str = "code.c"
            save_code_to_file(c_code, c_file_path)
        
        # Convert C to Python
        try:
            python_code: str = ctopython.convert_c_to_python(c_code)
            print(python_code)
        except Exception as e:
            logging.error(f"{Fore.RED}Error converting C to Python: {e}")
            raise RuntimeError(f"Error converting C to Python: {e}")
        
        save = input("Do you want to save the Python code to a .py file? (y/n): ").strip().lower()
        if save == 'y':
            py_file_path: str = "code.py"
            save_code_to_file(python_code, py_file_path)

    except FileNotFoundError as e:
        logging.critical(f"{Fore.RED}{e}")
        sys.exit(1)
    except RuntimeError as e:
        logging.critical(f"{Fore.RED}{e}")
        sys.exit(1)
    except Exception as e:
        logging.critical(f"{Fore.RED}Unexpected error: {e}")
        sys.exit(1)

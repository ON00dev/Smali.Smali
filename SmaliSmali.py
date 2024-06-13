import subprocess
import os
import sys
import logging
from typing import Optional
from colorama import init, Fore

# Inicialize colorama
init(autoreset=True)

# Clean terminal
operacional_sys = os.name
if operacional_sys == "posix":
    os.system("clear")
elif operacional_sys == "nt":
    os.system("cls")
    print(Fore.RED + "WARNING: This tool may not work correctly on operating systems such as Windows." + Fore.RESET)
else:
    print(Fore.RED + "Operating System not supported." + Fore.RESET)

print(Fore.BLUE + '''
                                    888 d8b                                     888 d8b 
                                    888 Y8P                                     888 Y8P 
                                    888                                         888     
    .d8888b  88888b.d88b.   8888b.  888 888     .d8888b  88888b.d88b.   8888b.  888 888 
    88K      888 "888 "88b     "88b 888 888     88K      888 "888 "88b     "88b 888 888 
    "Y8888b. 888  888  888 .d888888 888 888     "Y8888b. 888  888  888 .d888888 888 888 
         X88 888  888  888 888  888 888 888 d8b      X88 888  888  888 888  888 888 888 
     88888P' 888  888  888 "Y888888 888 888 Y8P  88888P' 888  888  888 "Y888888 888 888 
                                                                                        
                                                                                        
                                                                                        
-------------------------------------------------------------------------------------------
  
    [☆]Developed by ON00dev
    [☆]Github: https://github.com/ON00dev
    
-------------------------------------------------------------------------------------------
''')

# Configure logging
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

    if not apk_path:
        logging.critical(f"{Fore.RED}APK path cannot be empty.")
        sys.exit(1)
        
    # Extracting APK's name (no extention) to use as directory name
    apk_name = os.path.splitext(os.path.basename(apk_path))[0]
    extracted_dir = f'./{apk_name}_extracted'
    smali_output_dir = f'./{apk_name}_smali_output'

    try:
        # Check and extract APK
        verify_file_path(apk_path)
        unzip_apk(apk_path, extracted_dir)

        # Find classes.dex archive
        dex_path: str = os.path.join(extracted_dir, 'classes.dex')
        verify_file_path(dex_path)

        # Decompile DEX to Smali
        decompile_dex_to_smali(dex_path, smali_output_dir)

        # Opcional: Save Smali code in an archive
        save: str = input("Do you want to save the Smali code to a .smali file? (y/n): ").strip().lower()
        if save == 'y':
            smali_file_path: str = os.path.join(smali_output_dir, "code.smali")
            smali_code: str = "\n".join(open(os.path.join(smali_output_dir, f)).read() for f in os.listdir(smali_output_dir) if f.endswith('.smali'))
            save_code_to_file(smali_code, smali_file_path)

    except FileNotFoundError as e:
        logging.critical(f"{Fore.RED}{e}")
        sys.exit(1)
    except RuntimeError as e:
        logging.critical(f"{Fore.RED}{e}")
        sys.exit(1)
    except Exception as e:
        logging.critical(f"{Fore.RED}Unexpected error: {e}")
        sys.exit(1)

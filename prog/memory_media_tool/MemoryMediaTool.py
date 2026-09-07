#!/usr/bin/env python3

import subprocess
import os
from datetime import datetime
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_command_in_terminal(command) -> str:
    # Open a terminal and execute the given command

    try:
        completed_process = subprocess.run(
            ['bash', '-c', command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return ""
    except subprocess.CalledProcessError as e:
        return e.stderr

def input_green(string: str = ""):
    answer = input(string + bcolors.OKGREEN)
    print(bcolors.ENDC, end="")

    return answer

# shit to be able to sort files correctly when having numbers in them that take up more than one digit
def natural_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

inputDirectories = (
    {"directory": r"/media/bakso/8076A3FA76A3EEDA/videos/", "name": "D-drive videos"},
    {"directory": r"/home/bakso/Downloads/", "name": "Downloads     "})

outputDirectory = r"/media/bakso/8076A3FA76A3EEDA/memory_media/"

# the input folder has some files that have been generated automatically that I don't know if I can remove
fileTypesToIgnore = ("ini")
# file types that are videos, which the program uses to know if it can compress the file or not
compressibleVideoFileTypes = ("mp4", "mkv")

# if this string is not empty, then the program will not close automatically once it is done, but it will rather
# print out the message, and wait for the user to confirm for it to close down, so that the user can read the message
programEndString: str = ""

def main():

    # tests prints for text formatting
    """print(f"{bcolors.HEADER}HEADER{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}OKBLUE{bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}OKCYAN{bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}OKGREEN{bcolors.ENDC}")
    print(f"{bcolors.WARNING}WARNING{bcolors.ENDC}")
    print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}")
    print(f"{bcolors.BOLD}BOLD{bcolors.ENDC}")
    print(f"{bcolors.UNDERLINE}UNDERLINE{bcolors.ENDC}")"""

    print()
    print(rf"""
    {bcolors.OKBLUE}####################{bcolors.FAIL}////////////\\\\\{bcolors.OKBLUE}#######################
    {bcolors.OKBLUE}###################{bcolors.FAIL}/////////////\\\\\\{bcolors.OKBLUE}######################
    {bcolors.OKBLUE}##################{bcolors.FAIL}//////////////\\\\\\\{bcolors.OKBLUE}#####################
    {bcolors.OKBLUE}#################{bcolors.FAIL}///////////////\\\\\\\\{bcolors.OKBLUE}####################
    {bcolors.OKBLUE}########        {bcolors.FAIL}////////////////\\\\\\\\{bcolors.OKGREEN}///\\       {bcolors.OKBLUE}########
    {bcolors.OKBLUE}########       {bcolors.FAIL}////////////////   \\\\\{bcolors.OKGREEN}////\\\      {bcolors.OKBLUE}########
    {bcolors.OKBLUE}########      {bcolors.FAIL}////////////////      \\{bcolors.OKGREEN}/////\\\\\    {bcolors.OKBLUE}########
    {bcolors.OKBLUE}########     {bcolors.FAIL}////////////////        {bcolors.OKGREEN}//////\\\\\\\  {bcolors.OKBLUE}########
    {bcolors.OKBLUE}########    {bcolors.FAIL}////////////////        {bcolors.OKGREEN}///////\\\\\\\\\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}########   {bcolors.FAIL}////////////////        {bcolors.OKGREEN}////////\\\\\\\\\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}########  {bcolors.FAIL}////////////////        {bcolors.OKGREEN}///////// \\\\\\\\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}######## {bcolors.FAIL}////////////////        {bcolors.OKGREEN}/////////    \\\\\\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}########{bcolors.FAIL}////////////////        {bcolors.OKGREEN}/////////       \\\\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}########{bcolors.FAIL}///////////////        {bcolors.OKGREEN}/////////          \\{bcolors.OKBLUE}########
    {bcolors.OKBLUE}########{bcolors.FAIL}//////////////        {bcolors.OKGREEN}/////////             {bcolors.OKBLUE}########
    {bcolors.OKBLUE}########{bcolors.FAIL}/////////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}////////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}///////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}//////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}/////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}////////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}///////        {bcolors.OKGREEN}/////////{bcolors.WARNING}@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}//////        {bcolors.OKGREEN}/////////                     {bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}/////        {bcolors.OKGREEN}/////////                      {bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}////        {bcolors.OKGREEN}/////////                       {bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}########{bcolors.FAIL}///        {bcolors.OKGREEN}/////////                        {bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}####################################################{bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}####################################################{bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}####################################################{bcolors.WARNING}@@@@@@@@
    {bcolors.OKBLUE}####################################################{bcolors.WARNING}@@@@@@@@
    {bcolors.ENDC}""")

    # the name that the file should get, ignoring the number at the start, and the file extension
    inputtedFileDescription: str = ""
    while True:
        print()
        _input: str = input_green("Input a description for the file:\n")
        if any(x in _input for x in ("\\", "/", ":", "*", "?", '"', "<", ">", "|")):
            print()
            print(f'{bcolors.WARNING}Disallowed character(s) present in file name.\n(\\ / : * ? " < > |){bcolors.ENDC}')
            continue

        _input = _input.strip()
        inputtedFileDescription = _input if _input == "" else (" " + _input)
        break

    # determines if the file should get a new number assigned to it,
    # or if it should get parented to the most recent file in the output directory
    makeFileNumberStandalone: bool = False
    while True:
        print()
        _input: str = input_green(f"Give file standalone number? "
                                  f"If no then it will get parented to the most recent file.\n"
                                  f"({bcolors.UNDERLINE}y{bcolors.ENDC}/n) ")

        if _input.strip().lower() == "n":
            makeFileNumberStandalone = False
            break
        elif _input.strip().lower() == "y" or _input.strip().lower() == "":
            makeFileNumberStandalone = True
            break
        else:
            print()
            print(f'{bcolors.WARNING}Invalid input.{bcolors.ENDC}')

    # find all the files in the input directory that can be handled by this program
    foundFiles = []
    for inputDirectory in inputDirectories:
        for fileName in os.listdir(inputDirectory["directory"]):
            if os.path.isfile(os.path.join(inputDirectory["directory"], fileName)):
                if not fileName.split(".")[-1] in fileTypesToIgnore:
                    foundFiles.append({"path": inputDirectory["directory"] + fileName, "name": inputDirectory["name"] + " / " + fileName, "directory": inputDirectory["directory"], "pureName": fileName})

    # sort all founds files in a way that correctly sorts strings with numbers that use more than one digit
    tempVariable = sorted(foundFiles, key=lambda d: natural_key(d["pureName"]))
    foundFiles = tempVariable  # when not using the temp variable the list isn't properly updated

    selectedFile = {"path": "", "directory": "", "fileType": ""}

    if len(foundFiles) == 0:
        print()
        input_green(f"{bcolors.FAIL}No files in input directory found. Press enter to exit.\n")
        exit()
    elif len(foundFiles) == 1:
        selectedFile["path"] = foundFiles[0]["path"]
        selectedFile["directory"] = foundFiles[0]["directory"]
    else:  # if length > 1
        while True:
            print()
            print("Multiple files found. Input the index of the file you want to select.")
            for index, fileDictionary in enumerate(foundFiles):
                print(f"{index}: {fileDictionary['name']}")

            try:
                _input = input_green()
                selectedFile["path"] = foundFiles[int(_input)]["path"]
                selectedFile["directory"] = foundFiles[int(_input)]["directory"]
                break
            except Exception:
                print(f"{bcolors.WARNING}Invalid input.{bcolors.ENDC}")

    print()
    print("Chosen file: " + bcolors.BOLD + selectedFile["path"] + bcolors.ENDC)
    filesToDelete: list[str] = []

    deleteFiles: bool = False
    while True:
        try:
            print()
            _input: str = input_green(f"Delete original file after program is done?\n"
                                      f"({bcolors.UNDERLINE}y{bcolors.ENDC}/n) ")

            if _input.strip().lower() == "n":
                deleteFiles = False
                break
            elif _input.strip().lower() == "y" or _input.strip().lower() == "":
                deleteFiles = True
                break
            else:
                print()
                print(f'{bcolors.WARNING}Invalid input.{bcolors.ENDC}')
        except Exception:
            print(f"{bcolors.WARNING}Invalid input.{bcolors.ENDC}")

    selectedFile["fileType"] = str(selectedFile["path"]).split(".")[-1]

    if selectedFile["fileType"] in compressibleVideoFileTypes:  # checks if the file is compressible

        compressFile: bool = False
        compressionCodecToUse: str = ""
        while True:
            try:
                inputString = "Compress video file? If so with which codec?"
                # inputString += " (File will be converted into a mp4)." if selectedFile["fileType"] != "mp4" else ""
                inputString += f"\n({bcolors.UNDERLINE}265{bcolors.ENDC}/264/n) "
                print()
                _input: str = input_green(inputString)

                if _input.strip().lower() == "n":
                    compressFile = False
                    break
                elif _input.strip().lower() == "265" or _input.strip().lower() == "":
                    compressFile = True
                    compressionCodecToUse = "libx265"
                    break
                elif _input.strip().lower() == "264":
                    compressFile = True
                    compressionCodecToUse = "libx264"
                    break
                else:
                    print()
                    print(f'{bcolors.WARNING}Invalid input.{bcolors.ENDC}')
            except Exception:
                print(f"{bcolors.WARNING}Invalid input.{bcolors.ENDC}")

        compressionAmount: int = 0
        while True:
            try:
                print()
                _input = input_green(f"Specify compression amount. The higher the value, the more compressed the file gets.\n({bcolors.UNDERLINE}28{bcolors.ENDC}/[int]) ")

                if _input == "":
                    compressionAmount = 28
                    break
                else:
                    compressionAmount = int(_input)
                    break
            except Exception:
                print(f"{bcolors.WARNING}Invalid input.{bcolors.ENDC}")




        print()
        print(f"{bcolors.OKCYAN}Processing file... (process started at {datetime.now().strftime('%I:%M %p')}){bcolors.ENDC}")

        mp4ConvertedFileName: str = "EMILATE_MP4_CONVERTED"
        compressedFileName: str = "EMILATE_COMPRESSED"


        if compressFile:
            if selectedFile["fileType"] == "mkv":

                filesToDelete.append(selectedFile["path"])

                output = run_command_in_terminal(f'ffmpeg -y -i "{selectedFile["path"]}" -vcodec {compressionCodecToUse} -crf {compressionAmount} "{selectedFile["directory"]}{compressedFileName}.mkv"')
                if output != "":
                    print()
                    input_green(f"{bcolors.FAIL}ffmpeg failed converting file. Error code: {output}\nPress enter to exit.")
                    exit()

                # update selectedFile dictionary to the compressed file
                selectedFile["path"] = f'{selectedFile["directory"]}{compressedFileName}.mkv'

            elif selectedFile["fileType"] == "mp4":

                filesToDelete.append(selectedFile["path"])

                output = run_command_in_terminal(f'ffmpeg -y -i "{selectedFile["path"]}" -vcodec {compressionCodecToUse} -crf {compressionAmount} "{selectedFile["directory"]}{compressedFileName}.mp4"')
                if output != "":
                    print()
                    input_green(f"{bcolors.FAIL}ffmpeg failed converting file. Error code: {output}\nPress enter to exit.")
                    exit()

                # update selectedFile dictionary to the compressed file
                selectedFile["path"] = f'{selectedFile["directory"]}{compressedFileName}.mp4'

    # ------------------------------------------------------------------------------------------------------------------
    # Selected file is now ready to be renamed and moved to output folder

    # find the largest existing file index in the output folder
    largestMainNumber: int = 0
    largestSubNumber: int = 0  # 0 means that the file doesn't have a sub number, for example if it is "5" and not "5.1"
    largestFileName: str = ""
    filesToIgnore = ("desktop.ini", "tags.txt")
    for fileName in os.listdir(outputDirectory):
        if os.path.isfile(os.path.join(outputDirectory, fileName)):

            if fileName in filesToIgnore:
                continue

            try:
                mainNumber_ = int(fileName.split()[0].split(".")[0])

                previousMainNumber_ = largestMainNumber
                if mainNumber_ > largestMainNumber:
                    largestMainNumber = mainNumber_

                # checks if the main number was updated, which resets the sub number
                if mainNumber_ > previousMainNumber_:
                    largestSubNumber = 0
                    largestFileName = fileName

                entireNumber_ = fileName.split()[0].split(".")
                if len(entireNumber_) >= 2:
                    if entireNumber_[1].isdigit() and int(entireNumber_[1]) > largestSubNumber and mainNumber_ == largestMainNumber:
                        largestSubNumber = int(entireNumber_[1])
                        largestFileName = fileName


            except Exception:
                print()
                print(f'{bcolors.FAIL}Starting number of file with name "{fileName}" was not able to be detected. '
                      f'Is the number for this file improperly formatted?\n'
                      f'If this file isn\'t the one with the highest number, then the results of this program won\'t be affected. Otherwise the program will think the new file should have a number that is 1 less{bcolors.ENDC}')
                global programEndString
                programEndString = f"{bcolors.WARNING}Non-fatal error occurred. Please look at program's printed lines to look for the issue. Press enter to close down program.{bcolors.ENDC}"

    # number that the file will have when moved to the output directory
    numberToUse: str = f"{largestMainNumber + 1}" if makeFileNumberStandalone else (f"{largestMainNumber}.{largestSubNumber + 1}" if largestSubNumber > 0 else f"{largestMainNumber}.{largestSubNumber + 2}")

    # rename and add a ".1" to the end of the largest file number if it is missing that, where the current file is going to become a child of it
    if not makeFileNumberStandalone and largestSubNumber == 0:
        newLargestFileName: str = "EMILATE_RENAME_ERROR"
        if " " in largestFileName:  # if file name is more than just its number and its filetype (example: 54 taking a fat shit.png)
            newLargestFileName = f'{largestFileName.split(" ", 1)[0]}.1 {largestFileName.split(" ", 1)[1]}'
        else:  # if the filetype is just its number and its filetype (example: 54.png)
            newLargestFileName = f'{largestFileName.split(".", 1)[0]}.1.{largestFileName.split(".", 1)[1]}'

        # rename most recent file to have a sub number of 1
        run_command_in_terminal(f'mv "{outputDirectory}{largestFileName}" "{outputDirectory}{newLargestFileName}"')

    # copy selected file to the output directory
    outputPath: str = f'{outputDirectory}{numberToUse}{inputtedFileDescription}.{selectedFile["fileType"]}'
    run_command_in_terminal(f'cp "{selectedFile["path"]}" "{outputPath}"')

    filesToDelete.append(selectedFile["path"])

    # check if file exists in output directory and that the file size is larger than 0 to make sure that it was copied correctly
    if os.path.exists(outputPath) and os.stat(outputPath).st_size > 0:
        if deleteFiles:

            if len(filesToDelete) > 3:
                print()
                print(
                    f"{bcolors.FAIL}More than 3 files marked for deletion. Should be impossible unless you updated the code without "
                    f"updating this error message. As of writing this max 3 files can be marked for deletion (original.mkv, mp4_converted.mp4, compressed.mp4)."
                    f"Here are the following files marked for deletion:{bcolors.ENDC}\n")

                for file in filesToDelete:
                    print(f"{bcolors.FAIL}{file}{bcolors.ENDC}")

                print()
                input_green(f"{bcolors.FAIL}Program finished processing of file, however no file was deleted. Press enter to exit program.")
                exit()

            else:

                command: str = ""
                for path in filesToDelete:
                    command += f' && rm "{path}"'

                # remove first couple chars from string since it shouldn't start with " && "
                command = command[4:]

                # make it actually run the command!
                run_command_in_terminal(command)
    else:
        input_green(f"{bcolors.FAIL}File failed to get copied into output directory. No files have been deleted, but some might have "
                    f"been created in the same directory as the input file if the file was converted to mp4 or compressed.\n"
                    f"Press enter to exit.{bcolors.ENDC}")
        exit()




    if programEndString == "":
        print()
        print(f"{bcolors.OKGREEN}Program finished successfully.{bcolors.ENDC}")
    else:
        print()
        input_green(programEndString)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(bcolors.ENDC)

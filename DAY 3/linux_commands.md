# Linux Command Cheat Sheet
Here are the core Linux commands I mastered during Day 3:

## 1. Navigation
pwd: Print Working Directory - Shows the exact path of the folder you are currently in.
cd : Change Directory - Moves you into a specific folder.
cd ..: Moves you backward into the parent folder.
cd ~: Immediately takes you back to your Linux home directory.

## 2. Managing Files & Folders
ls: List - Lists all files and folders in your current directory.
ls -l: Lists files with detailed information (permissions, size, modification date).
mkdir : Make Directory - Creates a new folder.
touch : Creates a new empty file.
cp : Copy - Makes a duplicate copy of a file.
mv : Move/Rename - Renames a file or moves it to another folder.
rm : Remove - Permanently deletes a file (Warning: No recycle bin!).

## 3. Viewing & Searching Data
cat : Displays the entire contents of a file on the screen.
head : Shows the first 10 lines of a file (useful for large genomic data).
tail : Shows the last 10 lines of a file.
grep "" : Searches inside a file for a specific sequence motif or text line.
find.-name "*.fasta": Searches the current directory and subdirectories for specific files.

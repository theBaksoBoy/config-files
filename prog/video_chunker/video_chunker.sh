#!/usr/bin/env sh

# disgusting fucking AI generated dogshit because I just want this thing to work and really don't want to play around with it

cd "/home/bakso/Videos/"

# Find the first .mkv or .mp4 file (sorted alphabetically)
file=$(find "/home/bakso/Videos/" -maxdepth 1 -type f \( -iname "*.mkv" -o -iname "*.mp4" \) | sort | head -n 1)

# Check if a file was found
if [ -z "$file" ]; then
    echo "No .mkv or .mp4 files found in ~/Videos"
    exit 1
fi

# Compress using H.264
ffmpeg -i "$file" -c:v libx264 -crf 30 -preset medium -c:a copy "compressed.mkv"

echo "Compressed video saved."

mkvmerge -o output.mkv --split size:17M compressed.mkv



# Set the directory to search in
DIRECTORY="/home/bakso/Videos/"

# Loop through all files matching "output-*.mkv" in the directory
for FILE in "$DIRECTORY"/output-*.mkv; do
    # Remove the .mkv extension to get the base name
    BASENAME="${FILE%.mkv}"

    # Convert the MKV file to MP4
    ffmpeg -i "$FILE" -c copy "${BASENAME}.mp4"

    # Remove the original MKV file
    #rm "$FILE"
done

#rm compressed.mkv

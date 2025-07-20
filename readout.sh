# read logs at /run/media/harrison/17ecf464-7621-46ce-9655-f4cd6538da2b/var/log/journal/ec2d68b2b33b40a4939012ed67b0a46d
#!/bin/bash
# This script reads the log files in the specified directory and outputs the contents to log.txt.
LOG_DIR="/var/log/journal/fa46730e33564e71aa0bc4196801cd6f"

OUTPUT_FILE="log.txt"
rm -f "$OUTPUT_FILE"  # Remove the output file if it exists

# mound the usb drive if not already mounted
# Check if the log directory exists
if [ ! -d "$LOG_DIR" ]; then
    echo "Log directory does not exist: $LOG_DIR"
    exit 1
fi
# Create or clear the output file
> "$OUTPUT_FILE"    
# contents are journal logs
# Read the log files and output to log.txt
for file in "$LOG_DIR"/*; do
    if [ -f "$file" ]; then
        echo "Reading log file: $file" >> "$OUTPUT_FILE"
        # Use journalctl to read the log file
        journalctl --file="$file" >> "$OUTPUT_FILE"
        echo -e "\n" >> "$OUTPUT_FILE"
    else
        echo "Skipping non-file: $file" >> "$OUTPUT_FILE"
    fi
done
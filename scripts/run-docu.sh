#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path/to/folder"
    return 1
fi

# The folder path provided by the user
FOLDER_PATH="$1"

# Name your session
SESSION="small-proj-session"

# Create a new tmux session, detached (-d), named $SESSION. If it exists, don't create a new one.
tmux has-session -t $SESSION 2>/dev/null || tmux new-session -d -s $SESSION

# Command to run in the tmux session, using the provided folder path
CMD="pydoc-markdown -I $FOLDER_PATH  --render-toc --site-dir out --build > $FOLDER_PATH/docs/index.md"

# Send the commands to the tmux session. This activates the conda environment and runs your script.
tmux send-keys -t $SESSION "conda activate small-proj" C-m
tmux send-keys -t $SESSION "$CMD" C-m

# Optional: Send a command to exit after the previous commands complete. Remove the '#' to enable.
# tmux send-keys -t $SESSION "exit" C-m

# Detach from the session
tmux detach -s $SESSION

# Uncomment the following line if you want to kill the session after the command executes
# tmux kill-session -t $SESSION

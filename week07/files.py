#opening files
#must close file that you open- "with" closes file
with (open "filename", "r") as f:
    read_data = f.read():
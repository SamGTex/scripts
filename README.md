# Scripts
A few scripts that make my life easier.

Add all paths in .bashrc to have global access: `export PATH="ABSOLUTE/PATH/TO/SCRIPT:$PATH"`

## Backup
Create a backup of selected folders to a certain directory.
It just copies modified files to save time.

- **path_source.csv:** contains path from your data that you want to save
- **path_target.csv:** contains the path where you want to store the folders
- use `backup` to open the CLI based menu

## Timer
Simple timer that starts playing a video from youtube in your default browser, when the time is over.

- add URLs of some videos in urls.txt (random choice of existing paths)
- use `timer "hours" "minutes" "seconds"`
  - e.g. `timer 0 5 0` to start a 5 minute timer
  
 ## What should I cook?
 Propose a random meal.
 You can add meals manually or select a folder that contains recipes.
 Each file name becomes a meal.
 
 - start program with `whatcook` to open a CLI based menu
 
 ## To-Do
 Simple To-Do list with Tkinter based UI.
 - open the program with `todo`

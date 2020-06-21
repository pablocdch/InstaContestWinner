# InstaContestWinner
I've made this "bot" for auto-commenting on instagram. It's not the most elegant approach, but it's my first standalone Python project.

It uses the pyautogui library, which is based on screen coordinates. This makes the script non-useful for other computers, unless you know how to change the preset coordinates

It works by randomly choosing a comment from the .xlsx file, sopying it, opening the browser and then pasting it in the comment box. It then waits from 20 to 25 seconds to draw another one in order to prevent Instagram from blockin your comments or shadowbanning you.

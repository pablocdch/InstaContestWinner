# InstaContestWinner
I've made this "bot" for auto-commenting on instagram. It's not the most elegant approach, but it's my first standalone Python project.

It uses openpyxl and Selenium.

It works by randomly choosing a comment from the .xlsx file, copying it, opening the browser and then pasting it in the comment box. It then waits from 20 to 25 seconds to draw another one in order to prevent Instagram from blocking your comments or shadowbanning you.

# twitter_internet_speed_bot

Twitter bot that messages your ISP everytime your internet speeds go down under 75% of what you paid for.

It creates a config file for the first time it runs, setting your ISP twitter handle, location and, download/upload speeds.
These config file can be changed later on.
It test for your current internet speeds (ping, download, upload) and then, if conditions are met, tries to send a tweet using the test results
and your location written in the config file.

The bot also records the speeds you get after each test in a .csv file for future analysis.

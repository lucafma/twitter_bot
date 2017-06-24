# twitter_internet_speed_bot

Twitter bot that messages your ISP everytime your internet speeds go down under 75% of what you paid for.

It creates a config file for the first time it runs, setting your ISP twitter handle, location and, download/upload speeds.
These config file can be changed later on.
It test for your current internet speeds (ping, download, upload) and then, if conditions are met, tries to send a tweet using the test results
and your location written in the config file.

The bot also records the speeds you get after each test in a .csv file for future analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3
speedtest-cli
```

### Installing

Use pip to install speedtest-cli

```
pip install speedtest-cli
```

Download twitter_bot_template.py to a directory of your choice.

Open a terminal on the directory and run

```
python twitter_bot_template.py
```

## Built With

* [speedtest-cli](https://github.com/sivel/speedtest-cli) - For testing internet speeds
* [Tweepy](http://www.tweepy.org/) - Twitter API
 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used

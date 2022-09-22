# Campus Groups Bot #

This selenium bot allows you to register for events on the CWRU Campus Groups.

## Setup Instructions ##
Make sure Python 3 is installed on your computer. Run the following command in terminal:

    pip3 install -r requirements.txt

You will need to have a package manager installed on your computer, [Chocolatey](https://chocolatey.org/) for Windows or [Homebrew](https://brew.sh/) for macOS. Run the command that corresponds to which package manager you have installed:

    choco install chromedriver
<!-- -->
    brew install chromedriver

Download the bot.py file to your computer. In terminal, navigate to its folder. 

## Running Instructions ##
Begin running at least a minute before 7:00 AM. The program will wait/keep running until 7:00 AM to register you for your classes. 

    python bot.py

If you run into any problems, ensure you are running Python 3 by doing the following:

    python3 bot.py -u 'https://url-here.com' -i 123456 -t 23:45

To find the ticket ID, go to the page and choose "Inspect Element" on the ticket select HTML element. Then look for the name attribute, and it should be "ticket_######". Type the number as the ID.
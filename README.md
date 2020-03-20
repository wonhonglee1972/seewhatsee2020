# ML Repo
ML/Backend Repo in Python

## Requirements
There is a requirements.txt to run anything in this repo. It is recommended to set up virtual environments first.
Else, please run the below before doing anything:

```
sudo apt -y update && sudo apt -y upgrade
sudo apt-get -y install unixodbc-dev
sudo apt-get -y install python3-pip
sudo apt-get -y install build-essential libssl-dev libffi-dev python3-dev python3.6-dev libmysqlclient-dev
sudo -H pip3 install -r requirements.txt
```

# For MTGCrawlers
This spider is mainly for crawling the website known as Hareruya. I made this spider to do pricechecks on each
website, so I wouldn't have to manually. There are other spiders that I used to run simultaneously, but they are obsolete.
The code to run the spider is:

```
scrapy crawl hareruya -t csv -o hrry.csv
```

`scrapy crawl hareruya` is the command to start up the hareruya spider.
`-t csv` is to output to a CSV
`-o hrry.csv` is to name the CSV that is output
In the location where you run this command, there must be a .txt file called "hrry.txt", filled with card names.

An example would be:

```
Act of Aggression
Arc Runner
Ball Lightning
Basilisk Collar
Bedevil
Blistering Barrier
Burnished Hart
Butcher's Glee
Canyon Slough
Captivating Crew
Chandra's Ignition
Combat Celebrant
Dauthi Embrace
Doom Whisperer
Empyrial Plate
Fire Covenant
Fireshrieker
Fling
Homura, Human Ascendant
Lightning Skelemental
Loxodon Warhammer
Lupine Prototype
Phyresis
```

And so on.

# ML Repo
ML/Backend Repo in Python

## Requirements
There is a requirements.txt to run anything in this repo. Please run the below before doing anything:

```
sudo apt -y update && sudo apt -y upgrade
sudo apt-get -y install unixodbc-dev
sudo apt-get -y install python3-pip
sudo apt-get -y install build-essential libssl-dev libffi-dev python3-dev python3.6-dev libmysqlclient-dev
sudo -H pip3 install -r requirements.txt
```

# For AP
Inside autoprofiler.py there is a automatic xls/xlsx to csv convertor.
To run AP on every CSV, use:

```
python3 autoprofiler.py --csv "./some_values.xls" --output ./png --qmin "90" --qmax "1000" --dampingT "35000"
```

For explanation:
```
- This loops on every .csv file within /csv
- Can change the --output location by changing the directory
- There are some variables you need to input, such as --qmin, --qmax and --dampingT, which are self explanatory.
```

## Also xls_to_csv.py is a xlsx to csv convertor. Run using:
```
for file in ./xlsx/*.*; do python3 xls_to_csv.py --xls "$file" --output ./csv; done
```

# For BMautoschedule
For the autoscheduler, the bunkeringsort.py file has been set up to run as a script, instead of functionally.
It will take all jobs after UTCNOW and attempt to schedule them optimally, from loading to loading.

Within the folder is a db_config, which is our login to the SNJ_DB. This can be changed to whatever DB we require,
but we do need to specify which DB we are using it for.

To run the code, use:
```
python3 ./BM/bunkeringsort.py
```

If no json is provided, it will attempt to look through the OS.environment for login details.

For both the above .py, there are testing settings that can be used to print more error messages etc.
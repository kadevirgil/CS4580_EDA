## Dataset

https://www.kaggle.com/datasets/saife245/english-premier-league

## Kaggle API Docs

https://www.kaggle.com/docs/api

After creating and setting up your new environment use pip to install kaggle

```bash
# With your newly created environment run this
# command to install kaggle
pip install kaggle
```

```bash
# Here is the command for downloading
# the EPL results dataset
kaggle datasets download -d saife245/english-premier-league
```

After running this command the `english-premier-league.zip` file should be added to the project directory

Once you have the zip file, run the `extract.py` file to extract the data from zip into the `data` folder with this command

```bash
# To extract the data from the zip file
# run this command
python extract.py
```

Ater running the above command you should have <br>`2020-2021.csv`,
`2021-2022.csv`,
`final_dataset.csv`,
and a `Datasets` folder containing the data for seasons 2000-2020, in your data folder

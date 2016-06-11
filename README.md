#Year Prediction for Songs

As part of UCSC - CS218 "Deep Learning" class, we wanted to work on The Million Song Dataset [1] of The Echo Nest and LabROSA. Here you can see our attempts at reproducing their results, and trying to improve it.


##Setup
Assuming your machine has ```wget``` and ```unzip```, you can run downloader script by issuing ```. download.sh``` in your terminal. It will download 200MB zip archive, unzip it, and then delete the zip file. Data file (YearPredictionMSD.txt) is added to .gitignore.

If you prefer to use virtual environments, please use following commands to install dependencies.
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

##Results
 - [https://github.com/kyzn/YearPredict/blob/master/ANN/ann.ipynb](KNN experiments)
 - [https://github.com/kyzn/YearPredict/blob/master/ANN/ann.ipynb](ANN experiments)


##License

Please visit [https://github.com/tbertinmahieux/MSongsDB/blob/master/LICENSE](https://github.com/tbertinmahieux/MSongsDB/blob/master/LICENSE) for license details of the *Million Song Dataset project*.

Please visit [https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/README.md](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/README.md) for license details of *Code samples for "Neural Networks and Deep Learning"*.

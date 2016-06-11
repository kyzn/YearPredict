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

| **Results of [1] for Years** | **Diff** | **Sq. Diff** | **Accuracy** |
| --- | --- | --- | --- |
| Constant   | 8.13 | 10.80    | N/A      |
| 1NN        | 9.81 | 13.99    | N/A      |
| 50NN       | 7.58 | 10.20    | N/A      |
| VW         | 6.14 | 8.76     | N/A      |
| **Our Results for Years** | **Diff** | **Sq. Diff** | **Accuracy** |
| Constant      | 9.12 | 12.19    | 0.00    |
| 1NN           | 11.01| 15.79    | 5.21    |
| 50NN          | 9.14 | 13.95    | 6.70    |
| (90,90)       | 8.36 | 13.04    | 7.76    |
| (90,45,90)    | 7.74 | 11.84    | 8.04    |
| (90,60,45,90) | 7.27 | 11.19    | 8.33    |
| **Our Results for Decades** | **Diff** | **Sq. Diff** | **Accuracy** |
| (90,90)         | 7.69 | 13.23    | 57.42    |
| (90,45,90)      | 7.44 | 12.86    | 58.45    |
| (90,60,45,90)   | 7.24 | 12.90    | 59.49    |


##License

Please visit [https://github.com/tbertinmahieux/MSongsDB/blob/master/LICENSE](https://github.com/tbertinmahieux/MSongsDB/blob/master/LICENSE) for license details of the *Million Song Dataset project*.

Please visit [https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/README.md](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/README.md) for license details of *Code samples for "Neural Networks and Deep Learning"*.

[1]: Thierry Bertin-Mahieux, Daniel P.W. Ellis, Brian Whitman, and Paul Lamere. The Million Song Dataset. In Proceedings of the 12th International Society for Music Information Retrieval Conference (ISMIR 2011), 2011.

''' A dictionary object holds key parameters such as:
    - the location and name of the input data file
    - the location and name of the log file
    - the default logging level
    - the number of months in the "lookback window" for identifying "wins"
    - the number of months in the "lookback window" for identifying "losses"
    - how many months to use for Test
    - an indicator allowing execution in Test mode'''

__author__ = "The Hackett Group"

def getConfig():

    d = {}
    d["dataLoc"]    = "/home/tbrownex/data/iot/"
    d["labelColumn"] = "class"
    d["logLoc"]     = "/home/tbrownex/"
    d["logFile"]    = "SUSY.log"
    d["logDefault"] = "info"
    d['valPct'] = 0
    d["testPct"]   = 0.25
    d['batchSize'] = 64
    d['ShuffleBufferSize'] = 64
    return d
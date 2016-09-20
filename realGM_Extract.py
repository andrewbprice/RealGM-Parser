import urllib.request as urllib
from bs4 import BeautifulSoup
import csv
import pandas as pd
import os

##### REALGM URLS #####

urlTeamTotals = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Totals/Team_Totals"
urlTeamAverages = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Averages/Team_Totals"
urlTeamMetrics = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Advanced_Stats/Team_Totals"
urlOppoTotals = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Totals/Opponent_Totals"
urlOppoAverages = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Averages/Opponent_Totals"
urlOppoMetrics = "http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2016/Advanced_Stats/Opponent_Totals"
urlPlayersTotals1 ="http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Totals/All/All/points/All/desc/1/Regular_Season"
urlPlayersTotals2 ="http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Totals/All/All/points/All/desc/2/Regular_Season"
urlPlayersAverages1 = "http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Averages/All/All/points/All/desc/1/Regular_Season"
urlPlayersAverages2 = "http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Averages/All/All/points/All/desc/2/Regular_Season"
urlPlayersMetrics1 = "http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Advanced_Stats/All/All/points/All/desc/1/Regular_Season"
urlPlayersMetrics2 = "http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2016/Advanced_Stats/All/All/points/All/desc/2/Regular_Season"

###################################
##### PULL TEAM DATA FUNCTION #####
###################################

def createData():
    page = urllib.urlopen(url)  
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find('table')
    rows = table.findAll('tr')

    outputWriter.writerow(["Team", "GP", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                       "TOV", "PFS", "ORB", "DRB", "REB", "AST", "STL", "BLK", "PTS"])
    
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Team = str(data[1].get_text())
            GP = str(data[2].get_text())
            MIN = str(data[3].get_text())
            FGM = str(data[4].get_text())
            FGA = str(data[5].get_text())
            FGP = str(data[6].get_text())
            TPM = str(data[7].get_text())
            TPA = str(data[8].get_text())
            TPP = str(data[9].get_text())
            FTM = str(data[10].get_text())
            FTA = str(data[11].get_text())
            FTP = str(data[12].get_text())
            TOV = str(data[13].get_text())
            PFS = str(data[14].get_text())
            ORB = str(data[15].get_text())
            DRB = str(data[16].get_text())
            REB = str(data[17].get_text())
            AST = str(data[18].get_text())
            STL = str(data[19].get_text())
            BLK = str(data[20].get_text())
            PTS = str(data[21].get_text())

            outputWriter.writerow([Team, GP, MIN, FGM, FGA, FGP, TPM, TPA, TPP, FTM, FTA, FTP, TOV, PFS, ORB, DRB,\
                           REB, AST, STL, BLK, PTS])
    outputFile.close()


######################################
##### PULL TEAM METRICS FUNCTION #####
######################################

def createMetrics():
    page = urllib.urlopen(url)  
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find('table')
    rows = table.findAll('tr')

    outputWriter.writerow(["Team", "TS%", "eFG%", "oREB%", "dREB%", "tREB%", "AST%", "TOV%", "STL%", "BLK%", "PPS", "oRAT", "dRAT",\
                       "eDIF", "POS", "PACE"])
    
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Team = str(data[1].get_text())
            TS = str(data[2].get_text())
            EF = str(data[3].get_text())
            oREB = str(data[5].get_text())
            dREB = str(data[6].get_text())
            tREB = str(data[7].get_text())
            AST = str(data[8].get_text())
            TOV = str(data[9].get_text())
            STL = str(data[10].get_text())
            BLK = str(data[11].get_text())
            PPS = str(data[12].get_text())
            oRAT = str(data[14].get_text())
            dRAT = str(data[15].get_text())
            eDIF = str(data[16].get_text())
            POS = str(data[17].get_text())
            PACE = str(data[18].get_text())

            outputWriter.writerow([Team, TS, EF, oREB, dREB, tREB, AST, TOV, STL, BLK, PPS, oRAT, dRAT, eDIF, POS, PACE])
            
    outputFile.close()

#####################################
##### PULL PLAYER DATA FUNCTION #####
#####################################

def createPlayerData():
    page = urllib.urlopen(url)  
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find('table')
    rows = table.findAll('tr')

    outputWriter.writerow(["Player", "Team", "GP", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                       "TOV", "PFS", "ORB", "DRB", "REB", "AST", "STL", "BLK", "PTS"])
    
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Player = str(data[1].get_text())
            Team = str(data[2].get_text())
            GP = str(data[3].get_text())
            MIN = str(data[4].get_text())
            FGM = str(data[5].get_text())
            FGA = str(data[6].get_text())
            FGP = str(data[7].get_text())
            TPM = str(data[8].get_text())
            TPA = str(data[9].get_text())
            TPP = str(data[10].get_text())
            FTM = str(data[11].get_text())
            FTA = str(data[12].get_text())
            FTP = str(data[13].get_text())
            TOV = str(data[14].get_text())
            PFS = str(data[15].get_text())
            ORB = str(data[16].get_text())
            DRB = str(data[17].get_text())
            REB = str(data[18].get_text())
            AST = str(data[19].get_text())
            STL = str(data[20].get_text())
            BLK = str(data[21].get_text())
            PTS = str(data[22].get_text())

            outputWriter.writerow([Player, Team, GP, MIN, FGM, FGA, FGP, TPM, TPA, TPP, FTM, FTA, FTP, TOV, PFS, ORB, DRB,\
                           REB, AST, STL, BLK, PTS])
    outputFile.close()

########################################
##### PULL PLAYER METRICS FUNCTION #####
########################################

def createPlayerMetrics():
    page = urllib.urlopen(url)  
    soup = BeautifulSoup(page, "html.parser")
    table = soup.find('table')
    rows = table.findAll('tr')

    outputWriter.writerow(["Player", "Team", "TS%", "eFG%", "oREB%", "dREB%", "tREB%", "AST%", "TOV%", "STL%", "BLK%", "USG%", "PPS", "oRAT", "dRAT",\
                       "eDIF", "PER"])
    
    for row in rows:
        data = row.find_all('td')
        for row in data:
            Player = str(data[1].get_text())
            Team = str(data[2].get_text())
            TS = str(data[3].get_text())
            EF = str(data[4].get_text())
            oREB = str(data[6].get_text())
            dREB = str(data[7].get_text())
            tREB = str(data[8].get_text())
            AST = str(data[9].get_text())
            TOV = str(data[10].get_text())
            STL = str(data[11].get_text())
            BLK = str(data[12].get_text())
            USG = str(data[13].get_text())
            PPS = str(data[15].get_text())
            oRAT = str(data[16].get_text())
            dRAT = str(data[17].get_text())
            eDIF = str(data[18].get_text())
            PER = str(data[20].get_text())

            outputWriter.writerow([Player, Team, TS, EF, oREB, dREB, tREB, AST, TOV, STL, BLK, USG, PPS, oRAT, dRAT, eDIF, PER])
            
    outputFile.close()
    
##############################################
##### PANDAS CLEANUP TEAM DATA FUNCTION #####
##############################################

def pandaClean():
    inputFile = pd.read_csv(tempFile, encoding = "ISO-8859-1", low_memory=False)
    df = pd.DataFrame(inputFile, columns = ["Team", "GP", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                           "TOV", "PFS", "ORB", "DRB", "REB", "AST", "STL", "BLK", "PTS"])

    export = df.drop_duplicates()
    export.to_csv(exportFile)
    os.remove(tempFile)

################################################
##### PANDAS CLEANUP TEAM METRICS FUNCTION #####
################################################

def pandaCleanMetrics():
    inputFile = pd.read_csv(tempFile, encoding = "ISO-8859-1", low_memory=False)
    df = pd.DataFrame(inputFile, columns = ["Team", "TS%", "eFG%", "oREB%", "dREB%", "tREB%", "AST%", "TOV%", "STL%", "BLK%", "PPS", "oRAT", "dRAT",\
                       "eDIF", "POS", "PACE"])

    export = df.drop_duplicates()
    export.to_csv(exportFile)
    os.remove(tempFile)

###############################################
##### PANDAS CLEANUP PLAYER DATA FUNCTION #####
###############################################

def pandaCleanPlayerData():
    inputFile = pd.read_csv(tempFile, encoding = "ISO-8859-1", low_memory=False)
    df = pd.DataFrame(inputFile, columns = ["Player", "Team", "GP", "MIN", "FGM", "FGA", "FG%", "3PM", "3PA", "3P%", "FTM", "FTA", "FT%",\
                           "TOV", "PFS", "ORB", "DRB", "REB", "AST", "STL", "BLK", "PTS"])

    export = df.drop_duplicates()
    export.to_csv(exportFile)
    os.remove(tempFile)

##################################################
##### PANDAS CLEANUP PLAYER METRICS FUNCTION #####
##################################################

def pandaCleanPlayerMetrics():
    inputFile = pd.read_csv(tempFile, encoding = "ISO-8859-1", low_memory=False)
    df = pd.DataFrame(inputFile, columns = ["Player", "Team", "TS%", "eFG%", "oREB%", "dREB%", "tREB%", "AST%", "TOV%", "STL%", "BLK%", "USG%", "PPS", "oRAT", "dRAT",\
                       "eDIF", "PER"])

    export = df.drop_duplicates()
    export.to_csv(exportFile)
    os.remove(tempFile)

#########################
##### DOWNLOAD DATA #####
#########################

print("creating team data...")

##### CREATE TEAM TOTALS FILE #####

outputFile = open('rawdataTeam' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlTeamTotals
tempFile = 'rawdataTeam.csv'
exportFile = 'teamTotals.csv'

createData()
pandaClean()

##### CREATE TEAM AVERAGES FILE #####

outputFile = open('rawdataTeam' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlTeamAverages
tempFile = 'rawdataTeam.csv'
exportFile = 'teamAverages.csv'

createData()
pandaClean()

##### CREATE TEAM METRICS FILE #####

outputFile = open('rawdataTeam' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlTeamMetrics
tempFile = 'rawdataTeam.csv'
exportFile = 'teamMetrics.csv'

createMetrics()
pandaCleanMetrics()

print("creating opponent data...")

##### CREATE OPPONENT TOTALS FILE #####

outputFile = open('rawdataOppo' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlOppoTotals
tempFile = 'rawdataOppo.csv'
exportFile = 'oppTotals.csv'

createData()
pandaClean()

##### CREATE OPPONENT AVERAGES FILE #####

outputFile = open('rawdataOppo' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlOppoAverages
tempFile = 'rawdataOppo.csv'
exportFile = 'oppAverages.csv'

createData()
pandaClean()

##### CREATE OPPONENT METRICS FILE #####

outputFile = open('rawdataOppo' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlOppoMetrics
tempFile = 'rawdataOppo.csv'
exportFile = 'oppMetrics.csv'

createMetrics()
pandaCleanMetrics()

print("creating player data...")

##### CREATE PLAYER TOTALS FILE #####

outputFile = open('rawdataPlay' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlPlayersTotals1
tempFile = 'rawdataPlay.csv'
exportFile = 'playerTotals.csv'

createPlayerData()
pandaCleanPlayerData()

outputFile = open('rawdataPlay' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

##### CREATE PLAYER AVERAGES FILE #####

outputFile = open('rawdataPlay' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlPlayersAverages1
tempFile = 'rawdataPlay.csv'
exportFile = 'playerAverages.csv'

createPlayerData()
pandaCleanPlayerData()


##### CREATE PLAYER METRICS FILE #####

outputFile = open('rawdataPlay' +'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

url = urlPlayersMetrics1
tempFile = 'rawdataPlay.csv'
exportFile = 'playerMetrics.csv'

createPlayerMetrics()
pandaCleanPlayerMetrics()


print("RealGM Parsing Complete")

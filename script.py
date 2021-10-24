import pandas as pd
import numpy as np

# Census tract
def extractId(censusTract): # to extract last 6 digits
    return str(censusTract)[-6:]

def checkTractNum(num):
    isNotValid = True
    while isNotValid:
        if len(str(num)) == 6 and num.isnumeric():
            return num
        else:
            num = input("Enter Census ")

def findTractNum(num, listValidTractNum):
    num = checkTractNum(num)
    listValidTractNum.sort()
    low = 0
    high = len(listValidTractNum) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if listValidTractNum[mid] < num:
            low = mid + 1
        elif listValidTractNum[mid] > num:
            high = mid - 1
        else:
            return num
    return listValidTractNum[mid]

# County
def addCounty(c):
    if (c[-7:].lower() != " county"):
        c = c.lower().capitalize() + " County"
    return c

def checkCounty(c, listValidCounties):
    c = addCounty(c)
    if c in listValidCounties:
        return c
    else:
        print("Please enter valid county")

# State
def checkState(state):
    if len(state) == 2:
        state = state.upper()
        states = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
                  "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "FL": "Florida", "GA": "Georgia",
                  "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
                  "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
                  "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
                  "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico",
                  "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
                  "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
                  "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont",
                  "VA": "Virginia", "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"}
        if state in states:
            return states.get(state)
        else:
            return "Please enter valid state"
    else:
        state = state.split(" ")
        state = state.capitalize()
        states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
        if (state in states):
            return state
        else:
            return "Please enter valid state"

# LA tract
def defFlag(integer):
    return integer == 1

# LILA and LI
def calcRatio(num1, num2):
    if num1 == "Unknown":
        return "Value is unknown"
    else:
        ratio = num1 / num2 * 100
        ratio = round(ratio, 2)     # round to 2 decimal places
        return ratio


'''df["CensusTract"] = df["CensusTract"].apply(extractId)  # changes CensusTract # to last 6 digits
df.replace({np.NaN : "Unknown"}, inplace=True)  # replaces NaN with "Unknown"

# build dictionary
listValidCounties = df["County"].tolist()
listValidTractNum = df["CensusTract"].tolist()
df = df.set_index(["CensusTract", "State", "County"]).T.to_dict("list")'''

# take user input
'''tractNum = input("Enter Census Tract Number: ")
tractNum = findTractNum(tractNum)
state = input("Enter state: ")
state = checkState(state)
county = input("Enter county: ")
county = addCounty(county)
print(tractNum + state + county)

list = [tractNum, state, county]
tup = tuple(list)

data = df.get(tup)  # get list of data
population = data[0]
flag = data[1]              # flag of 0 or 1, 33% or 500 people are LALI
flagTrue = defFlag(flag)   # boolean of if flag is 0 or 1
lali = data[2]  # number of low access low income people
laliRatio = calcRatio(lali, population)
li = data[3]    # number of low income people
liRatio = calcRatio(li, population)'''

# print(df)
#print(data)
#print(str(population) + ", " + str(flagTrue) + ", " + str(laliRatio) + ", " + str(liRatio))

def mainFunction(censusTractCode, state, county):
    df = pd.read_csv("FoodAccessData.csv")
    df["CensusTract"] = df["CensusTract"].apply(extractId)  # changes CensusTract # to last 6 digits
    df.replace({np.NaN: "Unknown"}, inplace=True)  # replaces NaN with "Unknown"

    # build dictionary
    listValidCounties = df["County"].tolist()
    listValidTractNum = df["CensusTract"].tolist()
    df = df.set_index(["CensusTract", "State", "County"]).T.to_dict("list")

    tractNum = findTractNum(censusTractCode, listValidTractNum)
    state = checkState(state)
    county = checkCounty(county, listValidCounties)

    list = [tractNum, state, county]
    tup = tuple(list)

    data = df.get(tup)  # get list of data
    population = data[0]
    flag = data[1]  # flag of 0 or 1, 33% or 500 people are LALI
    flagTrue = defFlag(flag)  # boolean of if flag is 0 or 1
    lali = data[2]  # number of low access low income people
    laliRatio = calcRatio(lali, population)
    li = data[3]  # number of low income people
    liRatio = calcRatio(li, population)

    return [censusTractCode, flagTrue, population, laliRatio, liRatio]




from fredapi import Fred
'''Place to store key, value pairs used for accessing APIs'''

COMMODITIES = {
    'Gold':'CC=F',
    'Crude Oil':'CL=F',
    'Nat Gas':'NG=F',
    'Corn':'ZC=F',
    'Silver':'SI=F',
    'Copper':'HG=F',
    'Soybean':'ZS=F',
    'Feeder Cattle':'GF=F',
    'Live Cattle':'LE=F',
    'Lean Hogs':'HE=F',
    'Lumber':'LBS=F',
    'Orange Juice':'OJ=F',
    'Sugar':'SB=F',
    'Cotton':'CT=F',
    'Coffee':'KC=F',

}

FRED_INDICATORS = {
    'GDP':'GDP',
    'SP500':'SP500',
    'Housing Inventory Est.':'ETOTALUSQ176N',
}


# Apply Fred API key - not super sensitive info but should move somewhere else
FRED_API_KEY = '55b9ebb1f9d23c04330baa4d9f2abd40'
fred = Fred(api_key=FRED_API_KEY)

""
"Module for IQ Option API constants."
""#~~~need to update~~~
ACTIVES = {
	"EURUSD": 1,
	"EURGBP": 2,
	"GBPJPY": 3,
	"EURJPY": 4,
	"GBPUSD": 5,
	"USDJPY": 6,
	"AUDCAD": 7,
	"NZDUSD": 8,
	"USDRUB": 10,
	"AMAZON": 31,
	"APPLE": 32,
	"BAIDU": 33,
	"CISCO": 34,
	"FACEBOOK": 35,
	"GOOGLE": 36,
	"INTEL": 37,
	"MSFT": 38,
	"YAHOO": 40,
	"AIG": 41,
	"CITI": 45,
	"COKE": 46,
	"GE": 48,
	"GM": 49,
	"GS": 50,
	"JPM": 51,
	"MCDON": 52,
	"MORSTAN": 53,
	"NIKE": 54,
	"USDCHF": 72,
	"XAUUSD": 74,
	"XAGUSD": 75,
	"EURUSD-OTC": 76,
	"EURGBP-OTC": 77,
	"USDCHF-OTC": 78,
	"EURJPY-OTC": 79,
	"NZDUSD-OTC": 80,
	"GBPUSD-OTC": 81,
	"GBPJPY-OTC": 84,
	"USDJPY-OTC": 85,
	"AUDCAD-OTC": 86,
	"ALIBABA": 87,
	"YANDEX": 95,
	"AUDUSD": 99,
	"USDCAD": 100,
	"AUDJPY": 101,
	"GBPCAD": 102,
	"GBPCHF": 103,
	"GBPAUD": 104,
	"EURCAD": 105,
	"CHFJPY": 106,
	"CADCHF": 107,
	"EURAUD": 108,
	"TWITTER": 113,
	"FERRARI": 133,
	"TESLA": 167,
	"USDNOK": 168,
	"EURNZD": 212,
	"USDSEK": 219,
	"USDTRY": 220,
	"MMM:US": 252,
	"ABT:US": 253,
	"ABBV:US": 254,
	"ACN:US": 255,
	"ATVI:US": 256,
	"ADBE:US": 258,
	"AAP:US": 259,
	"AA:US": 269,
	"AGN:US": 272,
	"MO:US": 278,
	"AMGN:US": 290,
	"T:US": 303,
	"ADSK:US": 304,
	"BAC:US": 313,
	"BBY:US": 320,
	"BA:US": 324,
	"BMY:US": 328,
	"CAT:US": 338,
	"CTL:US": 344,
	"CVX:US": 349,
	"CTAS:US": 356,
	"CTXS:US": 360,
	"CL:US": 365,
	"CMCSA:US": 366,
	"CXO:US": 369,
	"COP:US": 370,
	"ED:US": 371,
	"COST:US": 374,
	"CVS:US": 379,
	"DHI:US": 380,
	"DHR:US": 381,
	"DRI:US": 382,
	"DVA:US": 383,
	"DAL:US": 386,
	"DVN:US": 388,
	"DO:US": 389,
	"DLR:US": 390,
	"DFS:US": 391,
	"DISCA:US": 392,
	"DOV:US": 397,
	"DTE:US": 400,
	"DNB:US": 403,
	"ETFC:US": 404,
	"EMN:US": 405,
	"EBAY:US": 407,
	"ECL:US": 408,
	"EIX:US": 409,
	"EMR:US": 413,
	"ETR:US": 415,
	"EQT:US": 417,
	"EFX:US": 418,
	"EQR:US": 420,
	"ESS:US": 421,
	"EXPD:US": 426,
	"EXR:US": 428,
	"XOM:US": 429,
	"FFIV:US": 430,
	"FAST:US": 432,
	"FRT:US": 433,
	"FDX:US": 434,
	"FIS:US": 435,
	"FITB:US": 436,
	"FSLR:US": 437,
	"FE:US": 438,
	"FISV:US": 439,
	"FLS:US": 441,
	"FMC:US": 443,
	"FBHS:US": 448,
	"FCX:US": 450,
	"FTR:US": 451,
	"GILD:US": 460,
	"HAS:US": 471,
	"HON:US": 480,
	"IBM:US": 491,
	"KHC:US": 513,
	"LMT:US": 528,
	"MA:US": 542,
	"MDT:US": 548,
	"MU:US": 553,
	"NFLX:US": 569,
	"NEE:US": 575,
	"NVDA:US": 586,
	"PYPL:US": 597,
	"PFE:US": 603,
	"PM:US": 605,
	"PG:US": 617,
	"QCOM:US": 626,
	"DGX:US": 628,
	"RTN:US": 630,
	"CRM:US": 645,
	"SLB:US": 647,
	"SBUX:US": 666,
	"SYK:US": 670,
	"DIS:US": 689,
	"TWX:US": 692,
	"VZ:US": 723,
	"V:US": 726,
	"WMT:US": 729,
	"WBA:US": 730,
	"WFC:US": 733,
	"SNAP": 756,
	"DUBAI": 757,
	"TA25": 758,
	"AMD": 760,
	"ALGN": 761,
	"ANSS": 762,
	"DRE": 772,
	"IDXX": 775,
	"RMD": 781,
	"SU": 783,
	"TFX": 784,
	"TMUS": 785,
	"QQQ": 796,
	"SPY": 808,
	"BTCUSD": 816,
	"XRPUSD": 817,
	"ETHUSD": 818,
	"LTCUSD": 819,
	"DSHUSD": 821,
	"BCHUSD": 824,
	"OMGUSD": 825,
	"ZECUSD": 826,
	"ETCUSD": 829,
	"BTCUSD-L": 830,
	"ETHUSD-L": 831,
	"LTCUSD-L": 834,
	"BCHUSD-L": 836,
	"BTGUSD": 837,
	"QTMUSD": 845,
	"XLMUSD": 847,
	"TRXUSD": 858,
	"EOSUSD": 864,
	"USDINR": 865,
	"USDPLN": 866,
	"USDBRL": 867,
	"USDZAR": 868,
	"DBX": 889,
	"SPOT": 891,
	"USDSGD": 892,
	"USDHKD": 893,
	"LLOYL-CHIX": 894,
	"VODL-CHIX": 895,
	"BARCL-CHIX": 896,
	"TSCOL-CHIX": 897,
	"BPL-CHIX": 898,
	"HSBAL-CHIX": 899,
	"RBSL-CHIX": 900,
	"BLTL-CHIX": 901,
	"MRWL-CHIX": 902,
	"STANL-CHIX": 903,
	"RRL-CHIX": 904,
	"MKSL-CHIX": 905,
	"BATSL-CHIX": 906,
	"ULVRL-CHIX": 908,
	"EZJL-CHIX": 909,
	"ADSD-CHIX": 910,
	"ALVD-CHIX": 911,
	"BAYND-CHIX": 912,
	"BMWD-CHIX": 913,
	"CBKD-CHIX": 914,
	"COND-CHIX": 915,
	"DAID-CHIX": 916,
	"DBKD-CHIX": 917,
	"DPWD-CHIX": 919,
	"DTED-CHIX": 920,
	"EOAND-CHIX": 921,
	"MRKD-CHIX": 922,
	"SIED-CHIX": 923,
	"TKAD-CHIX": 924,
	"VOW3D-CHIX": 925,
	"ENELM-CHIX": 926,	
	"ENIM-CHIX": 927,
	"PIRCM-CHIX": 929,
	"PSTM-CHIX": 930,
	"TITM-CHIX": 931,
	"UCGM-CHIX": 932,
	"CSGNZ-CHIX": 933,
	"NESNZ-CHIX": 934,
	"ROGZ-CHIX": 935,
	"UBSGZ-CHIX": 936,
	"SANE-CHIX": 937,
	"BBVAE-CHIX": 938,
	"TEFE-CHIX": 939,
	"AIRP-CHIX": 940,
	"HEIOA-CHIX": 941,
	"ORP-CHIX": 942,
	"AUDCHF": 943,
	"AUDNZD": 944,
	"CADJPY": 945,
	"EURCHF": 946,
	"GBPNZD": 947,
	"NZDCAD": 948,
	"NZDJPY": 949,
	"EURSEK": 950,
	"EURNOK": 951,
	"CHFSGD": 952,
	"EURSGD": 955,
	"USDMXN": 957,
	"JUVEM": 958,
	"ASRM": 959,
	"MANU": 966,
	"UKOUSD": 969,
	"XPTUSD": 970,
	"USOUSD": 971,
	"W1": 977,
	"AUDDKK": 983,
	"AUDMXN": 985,
	"AUDNOK": 986,
	"AUDSEK": 988,
	"AUDSGD": 989,
	"AUDTRY": 990,
	"CADMXN": 992,
	"CADNOK": 993,
	"CADPLN": 994,
	"CADTRY": 995,
	"CHFDKK": 996,
	"CHFNOK": 998,
	"CHFSEK": 1000,
	"CHFTRY": 1001,
	"DKKPLN": 1004,
	"DKKSGD": 1005,
	"EURDKK": 1007,
	"EURMXN": 1008,
	"EURTRY": 1010,
	"EURZAR": 1011,
	"GBPILS": 1013,
	"GBPMXN": 1014,
	"GBPNOK": 1015,
	"GBPPLN": 1016,
	"GBPSEK": 1017,
	"GBPSGD": 1018,
	"GBPTRY": 1019,
	"NOKDKK": 1023,
	"NOKJPY": 1024,
	"NOKSEK": 1025,
	"NZDDKK": 1026,
	"NZDMXN": 1027,
	"NZDNOK": 1028,
	"NZDSEK": 1030,
	"NZDSGD": 1031,
	"NZDTRY": 1032,
	"NZDZAR": 1033,
	"PLNSEK": 1036,
	"SEKDKK": 1037,
	"SEKJPY": 1038,
	"SGDJPY": 1041,
	"USDDKK": 1045,
	"NZDCHF": 1048,
	"GBPHUF": 1049,
	"USDCZK": 1050,
	"USDHUF": 1051,
	"CADSGD": 1054,
	"EURCZK": 1056,
	"EURHUF": 1057,
	"USDTHB": 1062,
	"IOTUSD-L": 1116,
	"XLMUSD-L": 1117,
	"NEOUSD-L": 1118,
	"ADAUSD-L": 1119,
	"XEMUSD-L": 1120,
	"XRPUSD-L": 1122,
	"EEM": 1203,
	"FXI": 1204,
	"IWM": 1205,
	"GDX": 1206,
	"XOP": 1209,
	"XLK": 1210,
	"XLE": 1211,
	"XLU": 1212,
	"IEMG": 1213,
	"XLY": 1214,
	"IYR": 1215,
	"SQQQ": 1216,
	"OIH": 1217,
	"SMH": 1218,
	"EWJ": 1219,
	"XLB": 1221,
	"DIA": 1222,
	"TLT": 1223,
	"SDS": 1224,
	"EWW": 1225,
	"XME": 1227,
	"QID": 1229,
	"AUS200": 1230,
	"FRANCE40": 1231,
	"GERMANY30": 1232,
	"HONGKONG50": 1233,
	"SPAIN35": 1234,
	"US30": 1235,
	"USNDAQ100": 1236,
	"JAPAN225": 1237,
	"USSPX500": 1239,
	"UK100": 1241,
	"TRXUSD-L": 1242,
	"EOSUSD-L": 1244,
	"BNBUSD-L": 1279,
	"ACB": 1288,
	"CGC": 1289,
	"CRON": 1290,
	"GWPH": 1291,
	"MJ": 1292,
	"TLRY": 1293,
	"BUD": 1294,
	"LYFT": 1313,
	"PINS": 1315,
	"ZM": 1316,
	"UBER": 1334,
	"MELI": 1335,
	"BYND": 1336,
	"BSVUSD-L": 1338,
	"ONTUSD-L": 1339,
	"ATOMUSD-L": 1340,
	"WORK": 1343,
	"FDJP": 1350,
	"CAN": 1351,
	"VIAC": 1352,
	"TFC": 1353,	
	"USDXOF-OTC": 1379,	
	"USDZAR-OTC": 1380,
	"USDINR-OTC":1381,
	"USDSGD-OTC":1382,
	"USDHKD-OTC":1383
}

ACT = ["USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'EOSUSD','XRPUSD','ETHUSD','LTCUSD','BTCUSD','USDJPY-OTC','AUDCAD-OTC','EURUSD-OTC','EURGBP-OTC','USDCHF-OTC','EURJPY-OTC','NZDUSD-OTC','GBPUSD-OTC','GBPJPY-OTC','EURCAD','EURAUD''AUDNZD','GBPNZD','USDCAD','AUDJPY','GBPCAD','GBPAUD','EURUSD','EURGBP','GBPJPY','EURJPY','GBPUSD','USDJPY','AUDCAD','NZDUSD','USDCHF','AUDUSD']


ACTIVESLi = ["USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'ETHUSD','EURJPY-OTC','NZDUSD-OTC','GBPJPY','EURJPY','GBPUSD','USDJPY','AUDCAD','NZDUSD','USDCHF','EURUSD-OTC','EURGBP-OTC','USDCHF-OTC','EURJPY-OTC','NZDUSD-OTC','XRPUSD','GBPUSD-OTC','GBPJPY-OTC','USDJPY-OTC','AUDCAD-OTC','BTCUSD','AUDUSD','USDCAD','AUDJPY','GBPCAD','GBPCHF','GBPAUD','CHFJPY','CADCHF','EURAUD','EURNZD','AUDCHF','AUDNZD','GBPNZD','NZDCAD','NZDJPY','NZDCHF']
ACTIVCATALAG = ["USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'EURUSD','GBPJPY','EURNZD','GBPUSD','EURUSD-OTC','EURGBP-OTC','AUDCAD-OTC']
ACTIVCATALAGVip = ['TODOS','ABERTOS',"USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'ETHUSD','EURJPY-OTC','NZDUSD-OTC','GBPJPY','EURJPY','GBPUSD','USDJPY','AUDCAD','NZDUSD','USDCHF','EURUSD-OTC','EURGBP-OTC','USDCHF-OTC','EURJPY-OTC','NZDUSD-OTC','XRPUSD','GBPUSD-OTC','GBPJPY-OTC','USDJPY-OTC','AUDCAD-OTC','BTCUSD','AUDUSD','USDCAD','AUDJPY','GBPCAD','CHFJPY','GBPCHF','GBPAUD','CADCHF','EURAUD','EURNZD','AUDCHF','AUDNZD','GBPNZD','NZDCAD','NZDJPY','NZDCHF']
ACTIVCATALAGVn = '''['TODOS','ABERTOS',"USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'ETHUSD','EURJPY-OTC','NZDUSD-OTC','GBPJPY','EURJPY','GBPUSD','USDJPY','AUDCAD','NZDUSD','USDCHF','EURUSD-OTC','EURGBP-OTC','USDCHF-OTC','EURJPY-OTC','NZDUSD-OTC','XRPUSD','GBPUSD-OTC','GBPJPY-OTC','USDJPY-OTC','AUDCAD-OTC','BTCUSD','AUDUSD','USDCAD','AUDJPY','GBPCAD','GBPCHF','GBPAUD','CADCHF','EURAUD','EURNZD','AUDCHF','AUDNZD','GBPNZD','NZDCAD','NZDJPY','NZDCHF']'''
acc =  ['1707085217','-597680809','1406327626','971655878','1327135922','1071818653','1681822582','1758367026','1696977654','1067849834','1660586923','1777688530','1048339448','1620800660','1030197575','1296363864','1675812690']


pares = {"pares":{
      "digital":{
         
      },
      "turbo":{
         
      },
      "binary":{
         
      }
   }
}

Activ = ["USDINR-OTC","USDSGD-OTC","USDHKD-OTC",'ETHUSD','EURJPY-OTC','NZDUSD-OTC','GBPJPY','EURJPY','GBPUSD','ETHUSD','EURJPY-OTC','NZDUSD-OTC','GBPJPY','EURJPY','GBPUSD','USDCAD','AUDJPY','GBPCAD','CHFJPY','GBPCHF','GBPAUD','CADCHF','EURAUD','EURNZD','AUDCHF','AUDNZD','GBPNZD','NZDCAD','NZDJPY','NZDCHF']

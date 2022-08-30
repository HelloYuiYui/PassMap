from cmath import nan
from tokenize import Triple
import pandas as pd
import numpy as np

#df = pd.read_csv("passport-index-tidy-cleaned.csv")

#print(df[["Requirement", "Destination_ISO2"]][df.Passport == "Turkey"].set_index(["Requirement", "Destination_ISO2"]))


df = pd.read_csv("passport-index-dataset/passport-index-tidy.csv")

valsOld = {
    "-1": 0, "FoM": 0,
    "visa free": 1, "7": 1, "14": 1, "15": 1, "21": 1, "28": 1, "30": 1,  "31": 1, "42": 1, "45": 1, 
        "60": 1, "90": 1, "120": 1, "180": 1, "240": 1, "360": 1,
    "visa on arrival": 2, "e-visa": 2,
    "visa required": 3,
    "no admission": 4, "covid ban": 4
}

vals = {
    "-1": 4, "FoM": 4,
    "visa free": 3, "7": 3+7/365, "14": 3+14/365, "15": 3+15/365, "21": 3+21/365, 
        "28": 3+28/365, "30": 3+30/365,  "31": 3+31/365, "42": 3+42/365, "45": 3+45/365, 
        "60": 3+60/365, "90": 3+90/365, "120": 3+120/365, "180": 3+180/365, 
        "240": 3+240/365, "360": 3+360/365,
    "visa on arrival": 2, "e-visa": 2,
    "visa required": 1,
    "no admission": 0, "covid ban": 0
}

def getPass(passport): 
    return df[df.Passport == passport]

def getVisaReqs(country):
    return df[df.Destination == country]

c = {"Afghanistan":"AF","Aland Islands":"AX","Albania":"AL","Algeria":"DZ","American Samoa":"AS","Andorra":"AD","Angola":"AO","Anguilla":"AI","Antarctica":"AQ","Antigua and Barbuda":"AG","Argentina":"AR","Armenia":"AM","Aruba":"AW","Australia":"AU","Austria":"AT","Azerbaijan":"AZ","Bahamas":"BS","Bahrain":"BH","Bangladesh":"BD","Barbados":"BB","Belarus":"BY","Belgium":"BE","Belize":"BZ","Benin":"BJ","Bermuda":"BM","Bhutan":"BT","Bolivia":"BO","Bonaire":"BQ","Bosnia and Herzegovina":"BA","Botswana":"BW","Bouvet Island":"BV","Brazil":"BR","British Indian Ocean Territory":"IO","Brunei":"BN","Bulgaria":"BG","Burkina Faso":"BF","Burundi":"BI","Cambodia":"KH","Cameroon":"CM","Canada":"CA","Cape Verde":"CV","Cayman Islands":"KY","Central African Republic":"CF","Chad":"TD","Chile":"CL","China":"CN","Christmas Island":"CX","Cocos (Keeling) Islands":"CC","Colombia":"CO","Comoros":"KM","Congo":"CG","DR Congo":"CD","Cook Islands":"CK","Costa Rica":"CR","Ivory Coast":"CI","Croatia":"HR","Cuba":"CU","Curaçao":"CW","Cyprus":"CY","Czech Republic":"CZ","Denmark":"DK","Djibouti":"DJ","Dominica":"DM","Dominican Republic":"DO","Ecuador":"EC","Egypt":"EG","El Salvador":"SV","Equatorial Guinea":"GQ","Eritrea":"ER","Estonia":"EE","Ethiopia":"ET","Falkland Islands (Malvinas)":"FK","Faroe Islands":"FO","Fiji":"FJ","Finland":"FI","France":"FR","French Guiana":"GF","French Polynesia":"PF","French Southern Territories":"TF","Gabon":"GA","Gambia":"GM","Georgia":"GE","Germany":"DE","Ghana":"GH","Gibraltar":"GI","Greece":"GR","Greenland":"GL","Grenada":"GD","Guadeloupe":"GP","Guam":"GU","Guatemala":"GT","Guernsey":"GG","Guinea":"GN","Guinea-Bissau":"GW","Guyana":"GY","Haiti":"HT","Heard Island and McDonald Islands":"HM","Vatican":"VA","Honduras":"HN","Hong Kong":"HK","Hungary":"HU","Iceland":"IS","India":"IN","Indonesia":"ID","Iran":"IR","Iraq":"IQ","Ireland":"IE","Isle of Man":"IM","Israel":"IL","Italy":"IT","Jamaica":"JM","Japan":"JP","Jersey":"JE","Jordan":"JO","Kazakhstan":"KZ","Kenya":"KE","Kiribati":"KI","Kosovo":"XK","North Korea":"KP","South Korea":"KR","Kuwait":"KW","Kyrgyzstan":"KG","Laos":"LA","Latvia":"LV","Lebanon":"LB","Lesotho":"LS","Liberia":"LR","Libya":"LY","Liechtenstein":"LI","Lithuania":"LT","Luxembourg":"LU","Macao":"MO","North Macedonia":"MK","Madagascar":"MG","Malawi":"MW","Malaysia":"MY","Maldives":"MV","Mali":"ML","Malta":"MT","Marshall Islands":"MH","Martinique":"MQ","Mauritania":"MR","Mauritius":"MU","Mayotte":"YT","Mexico":"MX","Micronesia":"FM","Moldova":"MD","Monaco":"MC","Mongolia":"MN","Montenegro":"ME","Montserrat":"MS","Morocco":"MA","Mozambique":"MZ","Myanmar":"MM","Namibia":"NA","Nauru":"NR","Nepal":"NP","Netherlands":"NL","New Caledonia":"NC","New Zealand":"NZ","Nicaragua":"NI","Niger":"NE","Nigeria":"NG","Niue":"NU","Norfolk Island":"NF","Northern Mariana Islands":"MP","Norway":"NO","Oman":"OM","Pakistan":"PK","Palau":"PW","Palestine":"PS","Panama":"PA","Papua New Guinea":"PG","Paraguay":"PY","Peru":"PE","Philippines":"PH","Pitcairn":"PN","Poland":"PL","Portugal":"PT","Puerto Rico":"PR","Qatar":"QA","Réunion":"RE","Romania":"RO","Russia":"RU","Rwanda":"RW","Saint Barthélemy":"BL","Saint Helena":"SH","Saint Kitts and Nevis":"KN","Saint Lucia":"LC","Saint Martin (French part)":"MF","Saint Pierre and Miquelon":"PM","Saint Vincent and the Grenadines":"VC","Samoa":"WS","San Marino":"SM","Sao Tome and Principe":"ST","Saudi Arabia":"SA","Senegal":"SN","Serbia":"RS","Seychelles":"SC","Sierra Leone":"SL","Singapore":"SG","Sint Maarten (Dutch part)":"SX","Slovakia":"SK","Slovenia":"SI","Solomon Islands":"SB","Somalia":"SO","South Africa":"ZA","South Georgia and the South Sandwich Islands":"GS","South Sudan":"SS","Spain":"ES","Sri Lanka":"LK","Sudan":"SD","Suriname":"SR","Svalbard and Jan Mayen":"SJ","Swaziland":"SZ","Sweden":"SE","Switzerland":"CH","Syria":"SY","Taiwan":"TW","Tajikistan":"TJ","Tanzania":"TZ","Thailand":"TH","Timor-Leste":"TL","Togo":"TG","Tokelau":"TK","Tonga":"TO","Trinidad and Tobago":"TT","Tunisia":"TN","Turkey":"TR","Turkmenistan":"TM","Turks and Caicos Islands":"TC","Tuvalu":"TV","Uganda":"UG","Ukraine":"UA","United Arab Emirates":"AE","United Kingdom":"GB","United States":"US","United States Minor Outlying Islands":"UM","Uruguay":"UY","Uzbekistan":"UZ","Vanuatu":"VU","Venezuela":"VE","Vietnam":"VN","Virgin Islands British":"VG","Virgin Islands U.S.":"VI","Wallis and Futuna":"WF","Western Sahara":"EH","Yemen":"YE","Zambia":"ZM","Zimbabwe":"ZW"}

eea = ["Bulgaria", "Romania", "Greece", "Cyprus", "Italy", "Monaco", "Spain", "Portugal", "France",
       "Switzerland", "Austria", "Slovakia", "Croatia", "Slovenia", "Hungary", "Czech Republic", "Poland", "Lithuania",
       "Latvia", "Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland", "Germany", "Netherlands", "Luxembourg", "Belgium",
       "Ireland"]
ukie = ["United Kingdom", "Ireland"]
rubl = ["Russia", "Belarus"]
merc = ["Argentina", "Brazil", "Paraguay", "Uruguay", "Chile", "Peru", "Bolivia", "Colombia", "Ecuador", "Guyana", "Suriname"]
anz = ["New Zealand", "Australia"]

df["Requirement"] = np.where((df.Passport.isin(eea)) & df.Destination.isin(eea) & (df.Passport != df.Destination), "FoM", df["Requirement"]) 
df["Requirement"] = np.where((df.Passport.isin(ukie)) & df.Destination.isin(ukie) & (df.Passport != df.Destination),  "FoM", df["Requirement"]) 
df["Requirement"] = np.where((df.Passport.isin(rubl)) & df.Destination.isin(rubl) & (df.Passport != df.Destination), "FoM", df["Requirement"]) 
df["Requirement"] = np.where((df.Passport.isin(merc)) & df.Destination.isin(merc) & (df.Passport != df.Destination), "FoM", df["Requirement"]) 
df["Requirement"] = np.where((df.Passport.isin(anz)) & df.Destination.isin(anz) & (df.Passport != df.Destination), "FoM", df["Requirement"]) 

df["Mobility"] = df["Requirement"]
df["Passport_ISO2"] = df["Passport"]
df["Destination_ISO2"] = df["Destination"]

df = df.reindex(columns=["Passport", "Passport_ISO2", "Destination", "Destination_ISO2", "Requirement", "Mobility"])

df.replace({"Mobility": vals, "Passport_ISO2": c, "Destination_ISO2": c}, inplace=True)
df.Mobility = np.round(df.Mobility, 2)

passPowers = df[["Passport", "Mobility"]].groupby("Passport").sum()

df.to_csv("passport-index-tidy-cleaned.csv", index=False)
def process(file):
    with open(file,"rt") as f:
        while True:
            line = f.readline()
            if line ==  "":
                break
            line = line.strip(" \n").split(",")[1:]
            MsSubClass = [0 for x in range(16)]
            categories = ["20","30","40","45","50","60","70","75","80","85","90","120","150","160","180","190"]
            for x in range(len(categories)): #does one-hot encoding for each of the house types
                if categories[x] == line[0]:
                    MsSubClass[x] = 1
            line[0] = MsSubClass


            MsZoning = [0 for x in range(8)]
            categories = ["A","C","FV","I","RH","RL","RP","RM"]
            for x in range(len(categories)): #One hot encode MsZoning
                if categories[x] == line[1]:
                    MsZoning[x] = 1
            line[1] = MsZoning

            LotFrontage = line[2] #casting LotFrontage to float for tensor
            if LotFrontage == "NA":
                line[2] = 0
            else:
                line[2] = float(LotArea)


            LotArea = line[3] #casting LotArea to float for tensor
            if LotArea == "NA":
                line[3] = 0
            else:
                line[3] = float(LotArea)

            Street = [0 for x in range(2)] #one hot encode street entrance type
            match (line[4]):
                case "Grvl":
                    Street[0] = 1
                case "Pave":
                    Street[1] = 1
            line[4] = Street


            Alley = [0 for x in range(2)] #one hot encode street entrance type
            match (line[5]):
                case "Grvl":
                    Alley[0] = 1
                case "Pave":
                    Alley[1] = 1
            line[5] = Alley

            match (line[6]): #asign value 0-3 for LotShape (Regular - Very Irregular)
                case "Reg":
                    line[6] = 0
                case "IR1":
                    line[6] = 1
                case "IR2":
                    line[6] = 2
                case "IR3":
                    line[6] = 3


            LandCountour = [0 for x in range(4)] #One hot encode for flatness of property
            match (line[7]):
                case "Lvl":
                    LandCountour[0] = 1
                case "Bnk":
                    LandCountour[1] = 1
                case "HLS":
                    LandCountour[2] = 1
                case "Low":
                    LandCountour[3] = 1


            match (line[8]): #Pick number to represent available utilities (the higher the number the more utilities)
                case "AllPub":
                    line[8] = 3
                case "NoSewr":
                    line[8] = 2
                case "NoSeWa":
                    line[8] = 1
                case "ELO":
                    line[8] = 0


            LotConfig = [0 for x in range(5)] #One hot encode Lot config
            match (line[9]):
                case "Inside":
                    LotConfig[0] = 1
                case "Corner":
                    LotConfig[1] = 1
                case "CulDSac":
                    LotConfig[2] = 1
                case "FR1":
                    LotConfig[3] = 1
                case "FR2":
                    LotConfig[4] = 1
            line[9] = LotConfig
            match (line[10]): #Ordinal assignment for the Slope of property
                case "Gtl":
                    line[10] = 1
                case "Mod":
                    line[10] = 2
                case "Sev":
                    line[10] = 3
            Neighbourhood = [0 for x in range(25)]
            match(line[11]): #One hot encoding of location of Neighbourhood
                case "Blmngtn":
                    Neighbourhood[0] = 1
                case "Blueste":
                    Neighbourhood[1] = 1
                case "BrDale":
                    Neighbourhood[2] = 1
                case "BrkSide":
                    Neighbourhood[3] = 1
                case "ClearCr":
                    Neighbourhood[4] = 1
                case "CollgCr":
                    Neighbourhood[5] = 1
                case "Crawfor":
                    Neighbourhood[6] = 1
                case "Edwards":
                    Neighbourhood[7] = 1
                case "Gilbert":
                    Neighbourhood[8] = 1
                case "IDOTRR":
                    Neighbourhood[9] = 1
                case "MeadowV":
                    Neighbourhood[10] =1
                case "Mitchel":
                    Neighbourhood[11] = 1
                case "Names":
                    Neighbourhood[12] = 1
                case "NoRidge":
                    Neighbourhood[13] = 1
                case "NPkVill":
                    Neighbourhood[14] = 1
                case "NridgHt":
                    Neighbourhood[15] = 1
                case "NWAmes":
                    Neighbourhood[16] = 1
                case "OldTown":
                    Neighbourhood[17] = 1
                case "SWISU":
                    Neighbourhood[18] = 1
                case "Sawyer":
                    Neighbourhood[19] = 1
                case "SawyerW":
                    Neighbourhood[20] = 1
                case "Somerst":
                    Neighbourhood[21] = 1
                case "StoneBr":
                    Neighbourhood[22] = 1
                case "Timber":
                    Neighbourhood[23] = 1
                case "Veenker":
                    Neighbourhood[24] = 1
            line[11] = Neighbourhood
            Condition1 = [0 for x in range(9)]
            match(line[12]): #One hot encode Condition1
                case "Artery":
                    Condition1[0] = 1
                case "Feedr":
                    Condition1[1] = 1
                case "Norm":
                    Condition1[2] =1
                case "RRNn":
                    Condition1[3] = 1
                case "RAn":
                    Condition1[4] = 1
                case "PosN":
                    Condition1[5] = 1
                case "PosA":
                    Condition1[6] = 1
                case "RRNe":
                    Condition1[7] = 1
                case "RRAe":
                    Condition1[8] = 1
            line[12] = Condition1
            Condition2 = [0 for x in range(9)]
            match(line[13]): #One hot encode Condition2
                case "Artery":
                    Condition2[0] = 1
                case "Feedr":
                    Condition2[1] = 1
                case "Norm":
                    Condition2[2] =1
                case "RRNn":
                    Condition2[3] = 1
                case "RAn":
                    Condition2[4] = 1
                case "PosN":
                    Condition2[5] = 1
                case "PosA":
                    Condition2[6] = 1
                case "RRNe":
                    Condition2[7] = 1
                case "RRAe":
                    Condition2[8] = 1
            line[13] = Condition2


            BldgType = [0 for x in range(5)]
            match(line[14]): #One hot encode BldgType
                case "1Fam":
                    BldgType[0] = 1
                case "2FmCon":
                    BldgType[1] = 1
                case "Duplx":
                    BldgType[2] = 1
                case "TwnhsE":
                    BldgType[3] = 1
                case "Twnhs":
                    BldgType[4] = 1
            line[14] = BldgType


            HouseStyle = [0 for x in range(8)] #ONe hot encode Houstyle
            categories = ["1Story","1.5Fin","1.5Unf","2Story","2.5Fin","2.5Unf","SFoyer","SLvl"]
            for x in range(len(categories)):
                if categories[x] == line[15]:
                    HouseStyle[x] = 1
            line[15] = HouseStyle


            OverallQual = line[16] #Convert Overall qual value to float
            line[16] = float(OverallQual)


            OverallCond = line[17] #Convert Overall qual value to float
            line[17] = float(OverallCond)

            YearBuilt = line[18] #Convert Year built to float
            line[18] = float(YearBuilt)

            YearRemodAdd = line[18] #Convert Year built to float
            line[18] = float(YearRemodAdd)

            RoofStyle = [0 for x in range(6)]
            categories = ["Flat","Gable","Gambrel","Hip","Mansard","Shed"]
            for x in range(len(categories)):
                if categories[x] == line[19]:
                    RoofStyle[x] = 1
            line[19] = RoofStyle

            RoofMatl = [0 for x in range(8)]
            categories = ["ClyTile","CompShg","Mebran","Metal","Roll","Tar&Grv","WdShake","WdShngl"]
            for x in range(len(categories)):
                if categories[x] == line[20]:
                    RoofMatl[x] = 1
            line[20] = RoofMatl

            Exterior1st = [0 for x in range]








            


        

                



            


            





                
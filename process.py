def process(file):
    with open(file,"rt") as f:
        while True:
            line = f.readline()
            if line ==  "":
                break
            line = line.strip(" \n").split(",")[1:]
            MsSubClass = [0 for x in range(16)]

            match (line[0]):#does one-hot encoding for each of the house types
                case "20":
                    MsSubClass[0] = 1
                case "30":
                    MsSubClass[1] = 1
                case "40":
                    MsSubClass[2] = 1
                case "45":
                    MsSubClass[3] = 1
                case "50":
                    MsSubClass[4] = 1
                case "60":
                    MsSubClass[5] = 1
                case "70":
                    MsSubClass[6] = 1
                case "75":
                    MsSubClass[7] = 1
                case "80":
                    MsSubClass[8] = 1
                case "85":
                    MsSubClass[9] = 1
                case "90":
                    MsSubClass[10] = 1
                case "120":
                    MsSubClass[11] = 1
                case "150":
                    MsSubClass[12] = 1
                case "160":
                    MsSubClass[13] = 1
                case "180":
                    MsSubClass[14] = 1
                case "190":
                    MsSubClass[15] = 1
            line[0] = MsSubClass
            MsZoning = line[1]
            match (line[1]):#does one-hot encoding for MSZoning
                case "A":
                    MsZoning[0] = 1
                case "C":
                    MsZoning[1] = 1
                case "FV":
                    MsZoning[2] = 1
                case "I":
                    MsZoning[3] = 1
                case "RH":
                    MsZoning[4] = 1
                case "RL":
                    MsZoning[5] = 1
                case "RP":
                    MsZoning[6] = 1
                case "RM":
                    MsZoning[7] = 1
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
            match(line[11]):
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
        

                



            


            





                
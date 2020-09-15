import pandas as pd
import json
import os



def json_csv():
    ##############################################################
    ######### Hier muss nur der Ordner angepasst werden ##########
    ##############################################################
    directory = 'c:/Users/szcze/Gitrepos/JsonParseCSV/json/json/'
    ##############################################################
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            
            print(filename)
            df = pd.read_json(directory+str(filename))
            header = ["part", "score", "position"]
            #print(df.size)
            for n in range(df.size):
                #print(filename + ": "+ str(n))
                for x in range(20):
                    #print(filename + ": "+ str(x))
                    if int(x) == 6 or int(x) == 8 or int(x) == 10:
                        inputx = "input"+str(x)
                        dt=pd.DataFrame(df["data"][n]["xs"][str(inputx)])
                        base = os.path.splitext(filename)[0]
                        print(inputx)
                        if int(x)== 6 and int(n) == 0:
                            dt.to_csv(directory+str(base)+'.csv', mode= 'a', index = True, header=True , columns= header)
                        else:
                            dt.to_csv(directory+str(base)+'.csv', mode= 'a', index = True, header=False , columns= header)
        

json_csv()





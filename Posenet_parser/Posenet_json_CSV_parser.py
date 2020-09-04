import pandas as pd
import json
import os



def json_csv():
    directory = 'c:/Users/szcze/Gitrepos/JsonParseCSV/json/json/'
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            
            print(filename)

            for n in range(20):
                print(filename + ": test: "+ str(n))
            """
            df = pd.read_json(str(filename))
            header = ["part", "score", "position"]
            n = 0
            for n in df.count():
                print("n: "+str(n))
                for x in df.count(axis='index'):
                    if int(x) == 6 or int(x) == 8 or int(x) == 10:
                        inputx = "input"+str(x)
                        dt=pd.DataFrame(df["data"][n]["xs"][str(inputx)])
                        base = os.path.splitext(filename)[0]
                        if int(n) == 0 and int(x)== 6:
                            dt.to_csv(str(base)+'.csv',mode= 'a', index = True, header=True , columns= header)
                        else:
                            dt.to_csv(str(base)+'.csv',mode= 'a', index = True, header=False , columns= header)
                            """                   
json_csv()





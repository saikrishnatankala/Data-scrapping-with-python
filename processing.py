from csv import reader

def find(x):
    with open('players.csv', 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if x in row[0]:
                if(row[8]=="-"):
                    return ["Not Enough Data",row[0]]
                if(float(row[8])>150):
                    row.append("1")
                if(150>float(row[8])>120):
                    row.append("2")
                else:
                    row.append("3")
                return row

        return [x]

def FantasyTeam(x,y):
    with open('points.csv','r') as file2:
        csv_reader2= reader(file2)
        output=[]
        count=0
        for row in csv_reader2:
            if(count==11):
                return output

            if (row[11]==x)|(row[11]==y):
                output.append(row[1])
                count=count+1

        return output

def GTopBat():
    with open('points.csv','r') as file3:
        csv_reader3= reader(file3)
        output=[]
        count=0
        for row in csv_reader3:
            if(count==10):
                return output

            if row[12]=='bt':
                output.append(row[1])
                count=count+1

        return output


def GTopBowl():
    with open('points.csv', 'r') as file4:
        csv_reader4 = reader(file4)
        output = []
        count = 0
        for row in csv_reader4:
            if (count == 10):
                return output
            if (row[12] == 'bw'):
                output.append(row[1])
                count = count + 1

        return output
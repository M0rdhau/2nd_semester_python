import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import random
import xlsxwriter as xc
import pandas as pd


def imagedataformat(x):
    x = float(x)
    if (x > 100):
        x /= 10
    return x


def readgraphdata():
    dataread = pytesseract.image_to_string(Image.open("plots.png"))
    start = dataread.find("43")
    stringneeded = dataread[start:]
    data = stringneeded.replace("\n", ",").replace(",,", ",").replace(" ", ",").split(",")[0:-1]
    data = list(map(imagedataformat, data))
    return data


def plothistogram():
    data = readgraphdata()
    datadict = {}
    for i in range(30, 65, 5):
        keystr = str(i - 5) + "-" + str(i)
        datadict[keystr] = len(list(filter(lambda x: i - 5 < x < i, data)))
    plt.bar(range(len(list(datadict.keys()))), list(datadict.values()), tick_label=list(datadict.keys()))
    plt.show()


def plotpichart():
    label = "Favorite type of music"
    datadict = {
        "Comedy": 4,
        "Action": 5,
        "Romance": 6,
        "Drama": 1,
        "SciFi": 4
    }
    plt.figure(figsize=(6, 4))
    plt.pie(list(datadict.values()), labels=list(datadict.keys()))
    plt.title(label)
    plt.show()


def getrandomname():
    return r''.join(chr(random.randint(97, 122)) for i in range(6)) + ".xlsx"


def createrandomexcel(filename):
    workbook = xc.Workbook(filename)
    worksheet = workbook.add_worksheet()

    worksheet.write(0, 0, "Amount")
    worksheet.write(0, 1, "Price")

    for i in range(1, 21):
        worksheet.write(i, 0, random.randint(1, 15))
        worksheet.write(i, 1, random.randint(1, 100))
    workbook.close()


def concatexcel():
    firstfile = getrandomname()
    secondfile = getrandomname()
    createrandomexcel(firstfile)
    createrandomexcel(secondfile)
    firstDF = pd.read_excel(firstfile)
    secondDF = pd.read_excel(secondfile)
    frames = [firstDF, secondDF]
    res = pd.concat(frames)
    resfilename = getrandomname()
    res.to_excel(resfilename)
    print("Your excel is written in: " + resfilename + "\n")


def main():
    num = input("Which action would you like to take:\n1. plot a histogram\n2. plot a pie chart\n"
                "3. concatenate random excel files\n4. exit\n")
    if num == "1":
        plothistogram()
        main()
    elif num == "2":
        plotpichart()
        main()
    elif num == "3":
        concatexcel()
        main()
    elif num == "4":
        exit()
    else:
        print("Wrong number!")
        main()


main()
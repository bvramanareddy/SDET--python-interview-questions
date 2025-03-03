import pandas as pd


def read_Excel():
    file_path= r"C:\Users\sanje\PycharmProjects\PYTEST FRAMEWORK\TestData.xlsx"
    excel = pd.read_excel(file_path)  # Explicitly define engine

    namesList = list(excel['Names'])
    idList = list(excel['ID'])
    mobileNumsList = list(excel['Mobile'])
    print(namesList)
    print(idList)
    print(mobileNumsList)
    dict1= {}
    for i in range(len(namesList)):
        dict1[namesList[i]] = (idList[i], mobileNumsList[i])


    print(dict1)
    return dict1, namesList, idList ,mobileNumsList

read_Excel()




def Analyze(path):
    #import bilbiotek oraz modelu do rozpoznawania znakow
    import cv2
    from roboflow import Roboflow
    rf = Roboflow (api_key="Ox9EnqPo6BpmOWSX9sTr") 
    project = rf.workspace().project("zdjecia-drogowe")
    model = project.version(6).model
    #img = "C:\\Users\\kacpe\\Desktop\\OSP\\dataset\\g6.jpg"
    img = cv2.imread(path,0)
    predictions = model.predict(img, confidence=70, overlap=40).json()

    #obliczenie wspolrzednych bounding boxa
    for predictions in predictions['predictions']:
        x0 = predictions['x'] - predictions['width'] / 2
        x1 = predictions['x'] + predictions['width'] / 2
        y0 = predictions['y'] - predictions['height'] / 2
        y1 = predictions['y'] + predictions['height'] / 2
        
    #zamiana skrotu na odpowiednia reprezentatywna nazwe znaku
    if predictions["class"] == "zielone":
        predictions["class"] = "Zielone swiatlo"
    elif predictions["class"] == "czerwone":
        predictions["class"] = "Czerwone swiatlo"
    elif predictions["class"] == "ust":
        predictions["class"] = "Znak ustap pierwszenstwa"
    elif predictions["class"] == "pierw":
        predictions["class"] = "Znak drogi z pierwszenstwem"
    elif predictions["class"] == "stop":
        predictions["class"] = "Znak Stop"

    #zwrocenie nazwy
    return predictions["class"]
#cv2.imshow("example_with_predictionses.jpg", img)
#cv2.waitKey(0) # waits until a key is pressed
#cv2.destroyAllWindows() # destroys the window showing image
#print(Analyze("C:\\Users\\kacpe\\Desktop\\OSP\\dataset\\g6.jpg"))

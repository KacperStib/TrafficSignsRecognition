
def Analyze(path):
    #import bilbiotek oraz modelu do rozpoznawania znakow
    import cv2
    from roboflow import Roboflow
    rf = Roboflow (api_key="Ox9EnqPo6BpmOWSX9sTr") #(api_key="Ox9EnqPo6BpmOWSX9sTr")
    project = rf.workspace().project("zdjecia-drogowe")
    model = project.version(6).model
    #img = "C:\\Users\\kacpe\\Desktop\\OSP\\dataset\\g6.jpg"
    img = cv2.imread(path,0)

    predictions = model.predict(img, confidence=70, overlap=40).json()
    
    #obliczenie wspolrzednych bounding boxa
    for bounding_box in predictions['predictions']:
        x0 = bounding_box['x'] - bounding_box['width'] / 2
        x1 = bounding_box['x'] + bounding_box['width'] / 2
        y0 = bounding_box['y'] - bounding_box['height'] / 2
        y1 = bounding_box['y'] + bounding_box['height'] / 2
        
    #zwrocenie wspolrzednych bounding boxa
    return [int(x0),int(y1),int(x1),int(y0)]
#cv2.imshow("example_with_bounding_boxes.jpg", img)
#cv2.waitKey(0) # waits until a key is pressed
#cv2.destroyAllWindows() # destroys the window showing image
#print(Analyze("C:\\Users\\kacpe\\Desktop\\OSP\\dataset\\g6.jpg"))
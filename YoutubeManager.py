import json

def loadData():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def saveData(videos):
     with open("youtube.txt","w") as file:
         json.dump(videos,file)
def showAllVideos(videos):
    print("\n")
    print("_"*100)
    print("\n"*3)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.Title:{video['name']}, time:{video['time']}")
    print("\n")
    print("_"*100)

def addVideos(videos):
    showAllVideos(videos)
    name=input("Enter Video name:")
    time=input("Enter Video time:")
    videos.append({"name":name,"time":time})
    saveData(videos)
    showAllVideos(videos)
    
def updateVideos(videos):
    showAllVideos(videos)
    index=int(input("Enter the index for Update:"))
    if 1<=index<=len(videos):
        name=input("Enter new Video name:")
        time=input("Enter new Video time:")
        videos[index-1]={"name":name,"time":time}
        saveData(videos)
        showAllVideos(videos)
    else:
        print(f"Oops! index {index} does not exist in the system the index should be in 1-{len(videos)}")
def deleteVideos(videos):
    showAllVideos(videos)
    index=int(input("Enter the video index to be deleted:"))
    if 1<=index<=len(videos):
        del videos[index-1]
        saveData(videos)
        showAllVideos(videos)
    else:
        print(f"Oops! index {index} does not exist in the system the index should be in 1-{len(videos)}")
def main():
    videos=loadData()
    while True:
        print("\nYoutube Manager|Choose an option")
        print("1.List all Youtube Videos")
        print("2.Add Youtube Videos")
        print("3.Update Youtube Videos")
        print("4.Delete Youtube Videos")
        print("5.Exit the App")

        choice=input("Enter Your Choice: ")

        match choice:
            case "1":
                showAllVideos(videos)
            case "2":
                addVideos(videos)
            case "3":
                updateVideos(videos)
            case "4":
                deleteVideos(videos)
            case "5":
                print("Thanks for using our Software")
                break
            case _:
                print("Something Went wrong")
if __name__=="__main__":
    main()
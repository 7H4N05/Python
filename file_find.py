# word=input("Enter a word:")
# def check_for_word():
#     with open("text.txt","r") as f:
#         data = f.read()
#         if (data.find(word))!=-1:
#             print("found","\n",(data.index))
#         else:
#             print("Not found")
# check_for_word()
# word=input("Enter a word:")
# def check_for_word():
#     with open("text.txt","r") as f:
#         data = f.read()
#         if (word in data):
#             print("found")
#         else:
#             print("Not found")
# check_for_word()
word="learning"
def check_line():
    data=True
    line=1
    with open("text.txt","r") as f:
            while data:
                data=f.readline()
                if(word in data):
                  print("Found in line:",line)
                else:print("Not found")
                line+=1
check_line()

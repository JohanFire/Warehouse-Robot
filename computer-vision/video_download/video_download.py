# # importing the module 
# from pytube import YouTube 

# # where to save 
# # SAVE_PATH = "E:/" #to_do 
# SAVE_PATH = "C:/Users/johan/OneDrive/Documentos/Github/Warehouse-Robot/computer-vision/video_download"


# # link of the video to be downloaded 
# link="https://www.youtube.com/watch?v=eLTLtUVuuy4&list=PLi5obeKYpstlktQQyLjV4gda0O-zfBcT2&index=11&t=1108s"

# try: 
# 	# object creation using YouTube 
# 	# which was imported in the beginning 
# 	yt = YouTube(link) 
# except: 
# 	print("Connection Error") #to handle exception 

# # filters out all the files with "mp4" extension 
# mp4files = yt.filter('mp4') 

# #to set the name of the file 
# yt.set_filename('GeeksforGeeks Video') 

# # get the video with the extension and 
# # resolution passed in the get() function 
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
# try: 
# 	# downloading the video 
# 	d_video.download(SAVE_PATH) 
# except: 
# 	print("Some Error!") 
# print('Task Completed!') 


from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
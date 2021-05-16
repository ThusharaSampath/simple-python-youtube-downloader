from pytube import YouTube  # package nad get one module out

while(True):

    link = input("Paste YouTube link: ")

    print("\n Fetching....")

    # its a Youtube class , we create an instance of it. yt is that.
    yt = YouTube(link)
    # constructor require a link. like  self.link = link 😂

    print("\n Title: ", yt.title,)  # here title is a attribute of yt object

    print("\nNumber of views:\t", yt.views)

    print("\nLength of video:\t", yt.length, " seconds")

    print("\nRatings:\t", yt.rating)

    print("\nIs this the video you looking for ? ")
    print("\nPress 'y' and hit Enter to proceed.")
    print("\nPress 'n' and hit Enter to Cancel.")
    proceed = input(" : ")

    if(proceed == "y"):

        # [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">,
        #  <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">]
        print("\n Fetching Download Options...")

        streams = yt.streams

        video_streams = streams.filter(progressive=True)  # its a array

        audio_streams = streams.filter(only_audio=True)  # its a array

        # printing download options in friendly manner

        if(len(video_streams) == 0 and len(audio_streams) == 0):
            print("\nNo Download Option Available.")
        else:
            print("\nHere is Download Options Available.")
            index = 1
            print("\nVideo")
            for stream in (video_streams):
                print("\n", index, " - Type : Video | Resoltion : ",
                    stream.resolution, " | format : ", stream.mime_type, )
                index = index+1
            print("Audio")
            for stream in (audio_streams):
                print("\n", index, " - Type : Audio | Quality : ",
                    stream.abr, " | format : ", stream.mime_type, )
                index = index+1

            number = int(input("Enter Number of the choice and hit Enter : "))
            tag = 0
            ys=""
            if(number <= len(video_streams)):
                tag = number
                ys = video_streams[tag-1]
            else:
                tag = number-len(video_streams)
                ys = audio_streams[tag-1]

            
            print("\nDownloading...")
            ys.download()
            print("\nDownload completed!!")

        # ys = yt.streams.get_highest_resolution()
        # ys = yt.streams.get_by_itag('22')

    elif(proceed == "n"):
        print("\n Exiting...")
        pass
    print("\nDo you have more link ? ")
    print("\nPress 'y' and hit Enter to Download New vedio.")
    print("\nPress 'n' and hit Enter to Exit.")
    next = input(" : ")

    if(next=="y"):
        pass
    else:
        break


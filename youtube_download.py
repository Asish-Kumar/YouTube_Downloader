# import subprocess
# youtube-dl is required to be up-to-date
# subprocess.call('pip install --upgrade youtube-dl', shell=True)
import requests
import youtube_dl
import subprocess

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

print("################## Online Video Downloader ##################")
# url = input("I am asking you for a URL: ")
url = 'https://www.youtube.com/watch?v=aJmmsKIjQm0&app=desktop'

with ydl:
    result = ydl.extract_info(
        url=url,
        download=False,
        process=True  # this parameter gives extra information about the video like fps
    )

# for key,value in result.items():
#     print(key,"  :::  ",value)

available_formats = []

for value in result['formats']:
    print(value)
    available_formats.append('extension: {}, Quality: {}, acodec: {}, vcodec: {}'.format(value['ext'], value['format_note'], value['acodec'], value['vcodec']))

print("\nAll available qualities with their extensions are: \n")
i=1
for x in available_formats:
    print(i, x)
    i += 1



choice = input('Enter the serial numbers separated by space to download those videos: ')
choice_list = list(map(int, choice.split()))
print(choice_list)

for x in choice_list:
    download_link = result['formats'][x-1]['url']
    file_name = result['title']
    ext = result['formats'][x-1]['ext']
    quality = result['formats'][x-1]['format_note']
    print('\n{}     {}    {}    {}'.format(file_name,quality,ext,download_link))
    r = requests.get(download_link)
    file_name = ''.join(e for e in file_name if (e.isalnum() or e.isspace()))
    with open(file_name+' '+quality+'.'+ext, 'wb') as file:
        file.write(r.content)


# if 'entries' in result:
#     # Can be a playlist or a list of videos
#     video = result['entries'][0]
# else:
#     # Just a video
#     video = result

# #print(video)


####### Combining audio and video files ############
# cmd = 'ffmpeg -y -i Audiofile.extension  -r 30 -i Videofile.extension  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
# subprocess.call(cmd, shell=True)                                     # "Muxing Done
# print('Muxing Done')
# import subprocess
#
# cmd = 'ffmpeg -y -i audio.webm  -r 30 -i video.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
# # cmd = 'pip install ffmpeg'
# subprocess.call(cmd, shell=True)
#
import requests
import ffmpeg
# help(ffmpeg)

# audio only
download_link1 = 'https://r1---sn-cnoa-qxal.googlevideo.com/videoplayback?ei=L6bAXMbWB6K2z7sPoOi2sAk&itag=249&keepalive=yes&requiressl=yes&signature=C6E27347AA0328B86DEDE7B5163CC9B172A0C9EF.3D0EEC58A7D7A0100FD6C55E4C4E48D533DA1B86&expire=1556150927&key=yt6&initcwndbps=230000&source=youtube&dur=230.041&clen=1365612&txp=5531432&c=WEB&lmt=1556127916671948&ipbits=0&beids=9466587&gir=yes&mn=sn-cnoa-qxal%2Csn-cvh76nek&ip=117.196.237.253&mm=31%2C29&fvip=1&ms=au%2Crdu&mv=m&mt=1556129210&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire&pl=22&id=o-AHnxUg_0hMyctyHYDWARz4RDX1Wxv7TjKthYr_xAL7Dk&mime=audio%2Fwebm&ratebypass=yes'

# video only
download_link2 = 'https://r1---sn-cnoa-qxal.googlevideo.com/videoplayback?ei=L6bAXMbWB6K2z7sPoOi2sAk&itag=136&keepalive=yes&requiressl=yes&signature=DD2D13CB8B03CE1F92B8CF42EDD79A6DC089191C.0DC8CC0E1F0350564F4E1FBB7A0FD65384389EEC&expire=1556150927&key=yt6&initcwndbps=230000&source=youtube&dur=230.021&clen=10411555&txp=5535432&c=WEB&lmt=1556128211098425&ipbits=0&beids=9466587&gir=yes&mn=sn-cnoa-qxal%2Csn-cvh76nek&ip=117.196.237.253&mm=31%2C29&fvip=1&ms=au%2Crdu&mv=m&mt=1556129210&sparams=aitags%2Cclen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Ckeepalive%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Crequiressl%2Csource%2Cexpire&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&pl=22&id=o-AHnxUg_0hMyctyHYDWARz4RDX1Wxv7TjKthYr_xAL7Dk&mime=video%2Fmp4&ratebypass=yes'

r1 = requests.get(download_link1)
r2 = requests.get(download_link2)

# r3 = ffmpeg.merge_outputs(ffmpeg.output(ffmpeg.input(r1.content)), ffmpeg.output(ffmpeg.input(r2.content)))




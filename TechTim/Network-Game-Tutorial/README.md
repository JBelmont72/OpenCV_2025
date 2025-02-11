# Network Game Tutorial
https://www.youtube.com/watch?v=KQasIwElg3w&t=652s


This is the code for my network game tutorial series on YouTube.

You can view the video tutorial on YouTube here: https://www.youtube.com/watch?v=_fx7FQ3SP0U&list=PLzMcBGfZo4-kR7Rh-7JCVDN8lm3Utumvq
PUTTY link  https://www.putty.org
Winscp file manager            https://winscp.net/eng/index.php is only for windows
alternatives for MAC os  https://rigorousthemes.com/blog/best-winscp-alternatives-for-mac/



from comments found this 'This video covered everything I needed to know right now 💯👍🏻 on Mac I followed along but using the built-in Terminal instead of installing Putty and just do Shell > New Remote Connection and then use FileZilla for the FTP '

'none of the commands worked untill i did sudo apt update first'
flask + socketio librareis to look at
+++++++++
Question: can you use a pyinstaller (client.exe) with linode?  I followed this video and was able to run your tictactoe client.py off the linode server (server.py), but a client.exe (created by pyinstaller) would not run.  I'm looking into it and will post the answer if I find it, but figured I'd give it a shot here 1st.  Thanks
So there appeared to be 2 problems.  #1 pygame.font.SysFont("comicsans", 20).  This worked with the client.py but not with client.exe.  I used a default instead. all_fonts = pygame.font.get_fonts().  pygame.font.SysFont(all_fonts, 20).  #2 was related to the hidden import and it couldn't find game module.  Just updated the client.spec file to include that module and reran pyinstaller client.spec.  hiddenimports=[ ], --> hiddenimports=['game'],
Yes, I commented on the problem as a reply to my original post.  Oddly enough I was not able to use pyinstaller for Mac and had to use py2app but with workarounds documented here, https://stackoverflow.com/questions/61602656/pygame-py2app-library-not-loaded-loader-path-dylibs-libsdl-1-2-0-dylib
++++++++

# Running The Game
To run the game you will need to run an instane of *server.py* on one machine. Then you can run instances of *run.py* on other machines to connect.

You will need to change the **server** address in both *server.py* and *network.py* to be the IPV4 address of your machine or the server ips you'll be using.

# Run in Gitpod

You can also run Network Game Tutorial in Gitpod, a free online dev environment for GitHub:

If you're intersted in a paid subscription with GitPod use the coupon code: **TECHWITHTIM2FQBMX**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/techwithtim/Network-Game-Tutorial/blob/master/run.py)

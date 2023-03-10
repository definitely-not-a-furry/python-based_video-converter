# video converter

Description
---

A converter made using python based on ffmpeg to convert any video file to .mp4 (mpeg)

Requirements
---

You need to have [FFmpeg](https://ffmpeg.org/) installed properly:

  1. Download FFmpeg from [this repository](https://github.com/BtbN/FFmpeg-Builds/releases)
  2. Extract the zip archive to C:\
  3. Press win+s and search "Edit the system environment variables" then press enter
  4. Click "Environment Variables...", then click on the row named "Path" and press alt+E
  5. Press alt+N and type in "C:\ffmpeg\bin\" end press enter
  6. Lastly, close all windows (by clicking Ok)

Operation
---

1. Extract the release zip file and execute "mp4conv.exe"
2. Click "Select" and select the files you want to convert
3. Click "Done"
4. Wait until the terminal window closes (it may take some time)
5. Your .mp4 files should be in the same directory as the selected files and are called "[original file name (including extention)].mp4"

Future plans
---

My future plans are to add support for a wider range of video formats and to make the UI more user-friendly. I'm considering intergrating ffmpeg rather than installing it being a pre-requisite.

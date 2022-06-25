import os
import sys

def main():
    work_dir = sys.path[0]
    print(work_dir)
    old_dir=os.path.join(work_dir, "temp_trans")
    print(old_dir)
    new_dir=os.path.join(work_dir, "temp_after")
    print(new_dir)
    ffmpeg=work_dir+"\\ffmpeg\\bin\\ffmpeg"
    filespace=os.listdir(old_dir)
    for file in filespace:
        infilepath=old_dir+"\\"+str(file)
        outfilepath=new_dir+"\\"+str(file)+".mp4"
        print(infilepath)
        print(outfilepath)
        for i in os.listdir(infilepath):  # 循环处理
            for o in os.listdir(os.path.join(infilepath, i)): # 开始循环内部
                if(os.path.isdir(os.path.join(infilepath, i, o))): # 进入二级循环
                    innerpath=os.path.join(infilepath, i, o)
                    print (innerpath)
                    videopath=os.path.join(innerpath,"video.m4s")
                    audiopath=os.path.join(innerpath,"audio.m4s")
                    print(videopath)
                    print(audiopath)
                    cmd = ffmpeg + " -i " + videopath + " -i " + audiopath  + " -c:v copy -strict experimental " + outfilepath
                    print(cmd)
                    os.popen(cmd)
if __name__ == "__main__":
    main()
    exit()
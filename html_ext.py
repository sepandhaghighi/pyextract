import urllib.request as url
import time
import sys
import tkinter
video_type=[".mp4",".3gp",".wmv",".flv",".mkv",".swf"]
def find_video_tag(string):
    link_list=[]
    for i in range(len(video_type)):
        index=0
        while(index!=-1):
            index=string.find(video_type[i],index)
            if index!=-1:
                link_list.append(index)
                index=index+4
    return link_list
def extract(link_list,string):
    direct_link=[]
    for i in link_list:
        index=0
        while(True):
            index_temp=index
            index=string.find('"',index+1)
            if index>i:
                index_1=index_temp
                index_2=index
                direct_link.append(string[index_1+1:index_2])
                break
    return direct_link
                
            
def print_out(link_name,link_list):
    print("Link : "+link_name)
    if len(link_list)!=0:
        for i in link_list:
            print(i)
    else:
        print("No File")
def run():
    try:
        raw_url=input("Please Copy Your URL Here(E for Exit & C for Clipboard):")
        if raw_url=="C":
            f=tkinter.Tk()
            raw_url=f.clipboard_get()
            f.destroy()
        if raw_url.find("http")==-1:
            raw_url="http://"+raw_url
        page=url.urlopen(raw_url)
        html=page.read()
        link_list=find_video_tag(str(html))
        links=extract(link_list,str(html))
        print_out(raw_url,links)
        run()
    except:
        if raw_url=="E":
            sys.exit()
        print("Error In Input URL or Clipboard Content")
        run()
if __name__=="__main__":
    run()
    
            
            
    

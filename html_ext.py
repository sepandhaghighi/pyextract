import urllib.request as url

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
                
            
            
            
if __name__=="__main__":
    try:
        raw_url=input("Please Copy Your URL Here : ")

        page=url.urlopen(raw_url)
        html=page.read()
        link_list=find_video_tag(str(html))
        print(extract(link_list,str(html)))
    except:
        print("Error In Input URL")
    
            
            
    

def geturlandtime(imgpath,loctime):
    import base64
    import requests
    import time
    with open(imgpath,"rb") as f:
        url="https://api.imgbb.com/1/upload"

        payload={
            "key": "bbf5ba45259d6eaa2cec3e74fdd19671",
            "image": base64.b64encode(f.read()),
            "name" : loctime,
            }
        res=requests.post(url,payload)
        a=res.json()
    

    if res.status_code == 200:
        print("Server Response: " + str(res.status_code))
        print("Image Successfully Uploaded")
    else:
        print("ERROR")
        print("Server Response: " + str(res.status_code)) 
    #將time_sec轉為日期
    time_sec=int(a['data']['time'])
    timeString = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_sec))
    return a['data']['display_url'],timeString,time_sec

if __name__=='__main__':
    print(geturlandtime("./test.jpg",'testpic'))
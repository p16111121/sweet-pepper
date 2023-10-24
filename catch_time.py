def rmoldimg(directory: str,delamount: int):
    import os
    import time
    import heapq
    ftimelist=[]
    fpath=[]
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            file_directory = os.path.join(directory, filename)
            fpath.append(file_directory)

            ftime=os.path.getmtime(file_directory)
            ftimelist.append(ftime)
                
    min_times=heapq.nsmallest(delamount,ftimelist)
    for min_time in min_times:
        index_min=ftimelist.index(min_time)
        min_fpath=fpath[int(index_min)]
        try:
            os.remove(min_fpath)
        except OSError as e:
            print(e)
        else:
            print("{} is deleted successfully".format(min_fpath))
if __name__=='__main__':
    rmoldimg('./testpic',2)

import argparse
import psutil 
parser = argparse.ArgumentParser(description='( CPU RAM NETWORK DISK_SPACE ) usage percentage')
parser.add_argument('--input', default='non' , type=str,
                    help='{RAM , CPU  , NETWORK(Ethernet) , DISK  , GPU  }select the device you need to get usage percentage')

args = parser.parse_args()
    
if(args.input=="RAM"):
    
    print( psutil.virtual_memory()[2]) # RAM usage
    
elif(args.input=="CPU"):
    
    val=psutil.cpu_percent(interval=1, percpu=True) # CPU usage
    for i in val:
        print(i)
    
elif(args.input=="NETWORK"):

    print(psutil.net_io_counters(pernic=True)["eth0"][0]) #send data
    print(psutil.net_io_counters(pernic=True)["eth0"][1]) #resive data
    print(psutil.net_io_counters(pernic=True)["eth0"][2]) #send package
    print(psutil.net_io_counters(pernic=True)["eth0"][3]) #resive package 

elif(args.input=="DISK"):
    
    ssd=psutil.disk_usage('/')
    used=ssd.used/(2**30)
    free=ssd.total/(2**30)
    oran=(used/free)*100
    print(oran)
    
elif(args.input=="GPU"):

    print(-1)

else:    

    print(-1)




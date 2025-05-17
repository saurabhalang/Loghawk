import re
import os
from datetime import datetime

def handle_access_log(filepath):

    print(f"\nProcessing ACCESS LOG FILE at: {filepath}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    try:
        # This is the function that will be executed when the pattern is matched
        err_403=0
        err_401=0
        log_countno=0

        with open(filepath,"r") as f:
            #writing the flagged logs onto a comp_log.txt file
            with open("/home/student/comp_log","a") as compile:
                for line in f:
                    log_countno+=1 
                    if "403" in line:
                        err_403+=1
                        compile.write(line)
                            
                    if "401" in line:
                        err_401+=1
                        compile.write(line)
                
        if err_403>0:
            print("") 
            print('"'+"403 Forbidden!! Server understands the request but refuses to authorize it.")
            print("It could indicate an access control issue, where attackers are attempting to access restricted resources!"+'"')
            print("")  
            print(err_403," Logs with 403 Error were found")
            
        if err_401>0:
            print("") 
            print('"'+"401 Unauthorized!! Authentication is required, client has not provided valid credentials")
            print("Attackers might be trying to access resources without authentication or attempting to brute-force credentials. "+'"')
            print("")
            print(err_401," Logs with 401 Error were found")

        print("")            
        print("Total ",log_countno," Logs were scanned") 
        print("") 
        
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")

def handle_app_log(filepath):
    """Process application log file"""
    print(f"\nProcessing APP LOG at: {filepath}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    try:
        # This is the function that will be executed when the app log pattern is matched
        err_no=0
        criti_no=0
        warning_no=0
        log_countno=0

        with open(filepath,"r") as f:
            #writing the flagged logs onto a comp_log.txt file
            with open("/home/student/comp_log.txt","a") as compile:
                for line in f:
                    log_countno+=1 
                    if "ERROR" in line:
                        err_no+=1
                        compile.write(line)
                            
                    if "CRITICAL" in line:
                        criti_no+=1
                        compile.write(line)

                    if "WARNING" in line:
                        warning_no+=1
                        compile.write(line)
                
        if err_no>0:
            print("") 
            print(err_no," Logs with Error were found")
            
        if criti_no>0:
            print("") 
            print(criti_no," Logs with Error were found")

        if warning_no>0:
            print("")
            print(warning_no," Logs with Warning were found")
        
        issue=err_no+criti_no+warning_no

        print("")
        print(issue," Critical System Errors, something could be failing fast.")
        print("")            
        print("Total ",log_countno," Logs were scanned") 
        print("") 
        
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")

def handle_auth_log(filepath):
    """Process auth log file"""
    print(f"\nProcessing AUTH LOG at: {filepath}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    try:
        # This is the function that will be executed when the auth log pattern is matched
        failed_count=0
        log_countno=0

        with open(filepath,"r") as f:
            #writing the flagged logs onto a comp_log.txt file
            with open("/home/student/comp_log.txt","a") as compile:
                for line in f:
                    log_countno+=1 
                    if "Failed" in line:
                        failed_count+=1
                        compile.write(line)

        if failed_count>0:
            print("") 
            print(failed_count," Logs with Too Many Failed Logins were found")

        print("")
        print("Possible brute-force attack!")
        print("Watch for multiple 401 Unauthorized errors in web server logs or failed SSH login attempts")
        print("")            
        print("Total ",log_countno," Logs were scanned") 
        print("")    
    
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")

def handle_system_log(filepath):
    """Process system log file"""
    print(f"\nProcessing SYSTEM LOG at: {filepath}")
    try:
        cron_count=0
        warn_count=0
        alert_count=0
        Un_auth=0
        log_countno=0

        with open(filepath,"r") as f:
            #writing the flagged logs onto a comp_log.txt file            
            with open("/home/student/comp_log.txt","a") as compile:
                for line in f:
                    log_countno+=1 
                    if "CRON" in line:
                        cron_count+=1
                        compile.write(line)
                    if "WARNING" in line:
                        warn_count+=1
                        compile.write(line)
                    if "ALERT" in line:
                        alert_count+=1
                        compile.write(line)
                    if "Unauthorized Access" in line:
                        Un_auth+=1
                        compile.write(line)

            if cron_count>0:
                print("")  
                print(cron_count," Unexpected cron jobs found")
                
            if warn_count>0:
                print("") 
                print(warn_count," Logs with a Warning message require attention!!")

            if alert_count>0:
                print("")
                print(alert_count, " Logs with ALERT message found that require attention!!")

            if Un_auth>0:
                print("")
                print(Un_auth," Logs with Unauthorized Access have been detected")

            print("")            
            print("Total ",log_countno," Logs were scanned") 
            print("") 
        
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")


def main():

#Add Access Log file path here
    access_path = "/media/sf_shared/access.log"
#the Access log file will be passed onto the function
    handle_access_log(access_path)
#******************************************************
#Add Application Log file path here
    app_path = "/media/sf_shared/app.log"
#the Application log file will be passed onto the function
    handle_app_log(app_path)
#******************************************************
#Add Auth Log file path here
    auth_path = "/media/sf_shared/auth.log"
#the Auth log file will be passed onto the function
    handle_auth_log(auth_path)
#******************************************************
#Add System Log file path here    
    system_path = "/media/sf_shared/system.log"
#the System log file will be passed onto the function
    handle_system_log(system_path)
#******************************************************

if __name__ == "__main__":
    main()

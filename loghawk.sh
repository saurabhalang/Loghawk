#to look in bash directory only
#./bin/bash
#below are the bash commands as asked in project3

#to search for all ip adrresses

grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' access.log

#to search 401 errors

grep ' 401 ' /var/log/apache2/access.log | wc -l


#to see number of times of occurrence of each ip address

awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr

#to see the ERROR letter in logs and its count.

grep -i -E "error|critical" /var/log/syslog | sort | uniq -c | sort -nr

#to check for cronjobs like in malware

grep -r -E "wget|curl" /etc/cron* /var/spool/cron/



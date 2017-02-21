# external_ip

Text your ip address to yourself.

Useful if your ISP assigns you a dynamic IP and you don't want to go through the hassle of setting up a static IP.  

Uses twilio as the SMS gateway.  
`pip install twilio`

Set it to automatically run every 15 minutes and text you if your IP has changed with cron.

**set external_ip.sh permission with chmod a+x**
```
crontab -e
#Set path
*/15 * * * * /home/{user}/external_ip.sh 
```

# Pterodactyl_Wings_Log_Monitor

<pre>
clone this repo on to your wings server.
edit the main.py script and fill in the following variables.

from_address = '' ###Example:  Cool Server <servername@cooldomain.com>
to_address = '' ### Example: cool dude <coolguy@example.com>
api_key = '' ## Example: kdjfalsdjflaksfkjadl;kfjlsdfk
post_url = '' ##### https://api.mailgun.net/v3/sanc5361f5f55dd2.mailgun.org/messages
machine_name = '' ### Machine name that will be in the email subject line. Example: Bigboi

## mk the dir for the program
mkdir /opt/log_auditor/


### copy main.py to /opt/log_auditor/main.py
### make the program execuable

## copy and pasta this file ##edit as you wish
/etc/systemd/system/log_auditor.service


## run these commands at bash console
systemctl daemon-reload
systemctl enable log_auditor
systemctl start log_auditor --no-block

###Debug
Pretty easy just run the script manualy python and watch for the errors

</pre>

import time
import requests
import subprocess
from_address = '' ###Example:  Cool Server <servername@cooldomain.com>
to_address = '' ### Example: 'cool dude <coolguy@example.com>'
api_key = '' ## Example: 'kdjfalsdjflaksfkjadl;kfjlsdfk'
post_url = '' ##### https://api.mailgun.net/v3/sandbox911560439eda4a10bc2c5361f5f55dd2.mailgun.org/messages


clear = 'echo " " > /var/log/pterodactyl/wings.log'
subprocess.call(clear, shell=True)

f = open('/var/log/pterodactyl/wings.log','r')

def send_simple_message(message,subjec):
    return requests.post(
        "{}".format(post_url),
        auth=("api", "{}".format(api_key)),
        files=[("attachment", open('/var/log/pterodactyl/wings.log'))],
        data={"from": "{}".format(from_address),
              "to": "{}".format(to_address),
              "subject": subjec,
              "text": message})

def process(x):
    if 'ERROR' in x:
        send_simple_message(x,'Error on Atomic')
        print('sending error')
    elif 'crashed' in x:
        send_simple_message(x, 'Container Crash on Atomic')
        print('sending Crash email')
    elif 'stacktrace' in x:
        send_simple_message(x, 'Stacktrace on Nitro ')
        print('sending Crash email')
    else:
        pass


while True:
    line = ''
    while len(line) == 0 or line[-1] != '\n':
        tail = f.readline()
        if tail == '':
            time.sleep(0.2)
            continue
        line += tail
    process(line)

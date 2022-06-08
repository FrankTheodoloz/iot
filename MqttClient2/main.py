''' These are only the CHANGES on main.py'''


def check_conn():
    '''This is a new function'''
    while (mqttclient.state()['broker_address'] == ""):
        sleep(5)
        mqttclient.connect("192.168.1.150", "", "")
    while (len(mqttclient.state()['subscriptions']) < 1):
        sleep(5)
        mqttclient.subscribe("LOG")
        check_conn()


def main():
    '''ADD check_conn() right before "while True:"'''
    check_conn()

    while True:
        delay(60000)

# -*- coding: mbcs -*-
import win32serviceutil
import win32api
import time

def service_running(service, machine):
    return win32serviceutil.QueryServiceStatus(service, machine)[1]==4

def service_info(action, machine, service):
    running = service_running(service, machine)
    servnam = 'service (%s) on machine(%s)' % (service, machine)
    action = action.lower()
    if action == 'stop':
        if not running:
                print "Can't stop, %s not running"%servnam
                return 0
        win32serviceutil.StopService(service, machine)
        running = service_running(service, machine)
        if running:
            print "Can't stop, %s (???)"%servnam
            return 0
        print '%s stopped successfully' % servnam

    elif action == 'start':
        if running:
            print "Can't start, %s already running"%servnam
            return 0
        win32serviceutil.StartService(service) #machine 을 빼니 start가 되는군.!
        time.sleep(1)
        running = service_running(service, machine)
        if not running:
                print "Can't start, %s (???)"%servnam
                return 0
        print '%s started successfully' % servnam

    elif action == 'restart':
        running = service_running(service, machine)
        if not running:
                print "Can't restart, %s not running"%servnam
                return 0
        win32serviceutil.RestartService(service, machine)
        running = service_running(service, machine)
        if not running:
                print "Can't restart, %s (???)"%servnam
                return 0
        print '%s restarted successfully' % servnam

    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            print "%s is running normally" % service
        else:
            print "%s is *not* running" % service

    else:
        print "Unknown action (%s) requested on %s"%(action, servnam)


if __name__ == '__main__':
    machine = 'eric-s2'
    service = 'Apache2'
    action = 'start'

    crash_happen=0
    while 1:
        running = service_running(service, machine)
        cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if not running:
            print cur_time + ' : Maybe the service shutted, trying to start again...'
            win32api.Beep(2000, 500)
            crash_happen=1
            service_info(action, machine, service)
        else:
            if crash_happen:
                print cur_time + ' : The service is still running well.'
                crash_happen=0
            
        time.sleep(5)



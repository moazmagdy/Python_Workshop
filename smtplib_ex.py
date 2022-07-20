import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('moazmagdy91@gmail.com',
        'moaztawfeek91@gamil.com',
        "This is a test message!")
server.quit()
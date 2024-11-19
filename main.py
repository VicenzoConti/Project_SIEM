import win32evtlog


def read_event_log(server, logtype='Application'):
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    handle = win32evtlog.OpenEventLog(server, logtype)

    total = win32evtlog.GetNumberOfEventLogRecords(handle)

    print(f"Total records: {total}")

    try:
        events = win32evtlog.ReadEventLog(handle, flags, 0)

        for event in events:
            print(f"Event Category: {event.EventCategory}")
            print(f"Time Generated: {event.TimeGenerated}")
            print(f"Source Name: {event.SourceName}")
            print(f"Event ID: {event.EventID}")
            print(f"Event Type: {event.EventType}")
            print(f"Event Data: {event.StringInserts}")
            print("----------------------------")
    finally:
        win32evtlog.CloseEventLog(handle)


# Chama a função para ler o log do evento
read_event_log(None, 'Application')  # 'Application', 'System' e 'Security' são comuns
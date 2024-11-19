import win32evtlog
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import datetime

# Configurações do gráfico e da janela de tempo
fig, ax = plt.subplots()
log_type = "Application"
window_time = deque(maxlen=50)  # últimos eventos
window_categories = deque(maxlen=50)


def read_event_log():
    handle = win32evtlog.OpenEventLog(None, log_type)
    flags = win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(handle, flags, 0)

    event_times = []
    event_categories = []

    for event in events:
        event_times.append(event.TimeGenerated)
        event_categories.append(event.EventCategory)

    win32evtlog.CloseEventLog(handle)

    return event_times, event_categories


def update_graph(i):
    event_times, event_categories = read_event_log()

    for t, c in zip(event_times, event_categories):
        # Adiciona somente eventos novos
        if not window_time or (t > window_time[-1]):
            window_time.append(t)
            window_categories.append(c)

    # Atualiza os dados do gráfico
    ax.clear()
    ax.plot(list(window_time), list(window_categories), marker="o")
    ax.set_title('Event Monitor - Security')
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('Event Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()


ani = animation.FuncAnimation(fig, update_graph, interval=50)

plt.show()
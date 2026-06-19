import pywhatkit as wkit

# wkit.sendwhatmsg_instantly("+55 75 99920-7767", "Message test")


def sendWppMsg(group_id, message):
    wkit.sendwhatmsg_to_group_instantly(group_id, message)

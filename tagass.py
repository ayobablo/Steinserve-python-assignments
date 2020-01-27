
def myself(tag,body):
    the_story= f"<{tag}>{body}, </{tag}>"
    return the_story
data_list=[
    "a",
    "b",
    {"tag":"c","body": "I am a girl"},
    "d",
]

body=" my name is ayo"

for data in data_list:
    if type(data) == dict:
        tagged_string=myself(data["tag"], data["body"])
    else:
        tagged_string=myself(data, body)
    print (tagged_string)




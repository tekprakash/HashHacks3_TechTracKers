import nexmo

client = nexmo.Client(key='03a93241', secret='97af4fc9b97a6cc1')

client.send_message({
    'from': 'Nexmo',
    'to': '917291872075',
    'text': 'Hello from Nexmo',
})

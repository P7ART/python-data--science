contacts = {
    'police' : '112',
    'ambulance':'102',
}
while True:
    print('🔍 search a contact:')
    q = input('>>>')
    if len(q) == 0:
        print('closing down...')
        break
    if q in contacts:
        print(f' {q}:{contacts[q]}')    
    else:
        print('not found')    
        print('adding new contact')
        new_contact=input('>>)
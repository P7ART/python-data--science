contacts = {
    'police' : '112',
    'ambulance':'102',
}
while true:
    print('🔍 search a contact:')
    q = input('>>>')
    if len(q) == 0:
        print('closing down...')
    if q in contacts:
        print(f'{g}')    
        
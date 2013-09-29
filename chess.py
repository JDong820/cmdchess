from colorama import Back, Fore
import time
data = {
    (0, 0): Fore.BLACK+'\xe2\x99\x9c',
    (0, 1): Fore.BLACK+'\xe2\x99\x9e',
    (0, 2): Fore.BLACK+'\xe2\x99\x9d',
    (0, 3): Fore.BLACK+'\xe2\x99\x9b',
    (0, 4): Fore.BLACK+'\xe2\x99\x9a',
    (0, 5): Fore.BLACK+'\xe2\x99\x9d',
    (0, 6): Fore.BLACK+'\xe2\x99\x9e',
    (0, 7): Fore.BLACK+'\xe2\x99\x9c',
    (1, 0): Fore.BLACK+'\xe2\x99\x9f',
    (1, 1): Fore.BLACK+'\xe2\x99\x9f',
    (1, 2): Fore.BLACK+'\xe2\x99\x9f',
    (1, 3): Fore.BLACK+'\xe2\x99\x9f',
    (1, 4): Fore.BLACK+'\xe2\x99\x9f',
    (1, 5): Fore.BLACK+'\xe2\x99\x9f',
    (1, 6): Fore.BLACK+'\xe2\x99\x9f',
    (1, 7): Fore.BLACK+'\xe2\x99\x9f',
    (7, 0): Fore.WHITE+'\xe2\x99\x9c',
    (7, 1): Fore.WHITE+'\xe2\x99\x9e',
    (7, 2): Fore.WHITE+'\xe2\x99\x9d',
    (7, 3): Fore.WHITE+'\xe2\x99\x9b',
    (7, 4): Fore.WHITE+'\xe2\x99\x9a',
    (7, 5): Fore.WHITE+'\xe2\x99\x9d',
    (7, 6): Fore.WHITE+'\xe2\x99\x9e',
    (7, 7): Fore.WHITE+'\xe2\x99\x9c',
    (6, 0): Fore.WHITE+'\xe2\x99\x9f',
    (6, 1): Fore.WHITE+'\xe2\x99\x9f',
    (6, 2): Fore.WHITE+'\xe2\x99\x9f',
    (6, 3): Fore.WHITE+'\xe2\x99\x9f',
    (6, 4): Fore.WHITE+'\xe2\x99\x9f',
    (6, 5): Fore.WHITE+'\xe2\x99\x9f',
    (6, 6): Fore.WHITE+'\xe2\x99\x9f',
    (6, 7): Fore.WHITE+'\xe2\x99\x9f',
    #user input
    (-1, 0): '00 00',
    #move color
    (-1, -1): 1,
    #status
    (-2, -2): 0
}

def go(v):
    for c in v:
        if 'a' <= c <= 'z':
            print c
    time.sleep(3)
    return True

while 1:
    #Set move valid status (data[(-2, -2)]) to 0.
    #Display board.
    #Display who's turn it is based on data[(-1, -1)].
    print '' if data.update({(-3, -3): 0}) else ''+'' if data.update({(-2, -2): 0}) else ''+'\x1B[2J\x1B[H'+(''.join([(('\x1b[49m\n')*(len%2)+'\x1b[49m\n')[:6] if hgt==8 else Back.MAGENTA+(data[(len, hgt)] if (len, hgt) in data.keys() else ' ') if (len+hgt)%2 else Back.CYAN+(data[(len, hgt)] if (len, hgt) in data.keys() else ' ') for len in xrange(8) for hgt in xrange(9)]))+'\n'+(("White"*data[(-1, -1)]+'Black')[:5])+"'s turn."
    #Puts the user input into data[(-1, 0)].
    #If the move is invalid, do not set status (data[(-2, -2)]) to 1.
    (((data.update({(-2, -2): 1}),
    data.update({(-1, -1): (data[(-1, -1)]-1)**2})) if\
        int(data[(8-int(data[(-1, 0)].split(' ')[0][1]),
                 ord(data[(-1, 0)].split(' ')[0][0])-ord('a'))][3])/7 == data[(-1, -1)] else\
            '') if\
                data[(-1, 0)].count('')-1 == 5 and\
                '1' <= data[(-1, 0)][1] <= '8' and '1' <= data[(-1, 0)][4] <= '8' and\
                'a' <= data[(-1, 0)][0] <= 'h' and 'a' <= data[(-1, 0)][3] <= 'h' else\
                    raw_input('Invalid input.')) if\
                        data.update({(-1, 0): raw_input(Fore.WHITE+">>")}) or True else\
                            ''
    #Apply move on data if valid
    data[(8-int(data[(-1, 0)].split(' ')[1][1]), ord(data[(-1, 0)].split(' ')[1][0])-ord('a')) if data[(-2, -2)] else (-2, -2)] = data.pop((8-int(data[(-1, 0)].split(' ')[0][1]), ord(data[(-1, 0)].split(' ')[0][0])-ord('a')) if data[(-2, -2)] else (-3, -3))

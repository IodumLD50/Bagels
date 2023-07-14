import random


NUM_DIGITS = 3 #(!) Попробуй задать эту константу равной 1 или 10
MAX_GUESSES = 10 #(!) Попробуй задать эту константу равной 1 или 100

def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
    Pico             One digit is correct but in the wrong position.
    Fermi            One digit is correct and in the right position.
    Bagels           No digit is correct.
    
For example, if the secret number was 248 and your guess was 843, the
26. clues would be Fermi Pico.'''.format(NUM_DIGITS))    

    while True: # Основной цикл игры
        # Переменная в которой хранится секретное число,
        # Которое должен угадать игрок
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guess to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            quess = ''
            # Продолжаем играть до получение проавильной догадки:
            while len(quess) != NUM_DIGITS or not quess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                quess = input('> ')
                
                clues = qetClues(quess, secretNum)
                print (clues)    
                numGuesses += 1
            
                if quess == secretNum:
                    break # Правильно выходим из цикла
                if numGuesses > MAX_GUESSES:
                    print('You ran out of quesses.')
                    print('The answer was {}.'.format(secretNum))
        
        # Спрашиваем игрока, хочет ли он сыграть ещё раз.
            print('Do you want to play aqain? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playinq!')        
    
    
    
def getSecretNum():
    """Возвращает строку из NUM_DIGITS уникальных случайных цифр."""
    numbers = list('0123456789') # Создаёт список цифр от 0 до 9
    random.shuffle(numbers) # Перемешиваем их случайным образом.
    
    # Берём первые NUM_DIGITS цифр списка для нашего секретного числа:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum
    
def qetClues(quess, secretNum):
    '''Возвращаем строку с подсказками pico, fermi и baqels
    для полученной на входе пары из догадки и секретного числа.'''
    if quess == secretNum:
        return 'You qot it'
    
    clues = []
    
    for i in range(len(quess)):
        if quess[i] == secretNum[i]:
            # Правильная цифра на правильном месте.
            clues.append('Fermi')
        elif quess[i] in secretNum:
            # Правильная цифра на неправильном месте.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Baqels' # Правильных цифр нет вообще.
    else:
        # Сортируем подсказки в алфовитном порядке, чтобы их исходный порядок  
        # ничего не выдавал.
        clues.sort()
        # Склеиваем список подсказок в одно строковое значение.
        return ' '.join(clues)
    
    
    
if __name__ == '__main__':
    main()               
    
    
            

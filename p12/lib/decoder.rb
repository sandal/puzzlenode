def possibleWords(word, shift, alpha)
    key = alpha[shift..-1]+alpha[0..shift]
    newWord = ''
    
    word.each_char do |char|
      wordIndex = alpha.index(char)
      newWord += key[wordIndex]
    end
    
    return newWord
end

def returnShiftedLetter(char, shift, alpha)
    charIndex = alpha.index(char)
    shiftDown = (charIndex.to_i - shift)

    newLetter = alpha[shiftDown]
end

def returnVigKeys(word, alpha)
    keys = []
    word.split('').each do |i|
      key = alpha.index(i)
      keys.push(key)
    end
    return keys
end

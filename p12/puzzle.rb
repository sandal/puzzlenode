file = File.open('input.txt', 'r')
lines = file.readlines
word = lines.shift.strip
text = lines.join

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def possibleWords(word, shift, alpha)
    key = alpha[shift..-1]+alpha[0..shift]
    newWord = ''
    
    word.each_char do |char|
      wordIndex = alpha.index(char)
      newWord += key[wordIndex]
    end
    
    return newWord
end

for shift in (1..alpha.length)
    puts possibleWords(word, shift, alpha)
end

def returnShiftedLetter(char, shift, alpha)
    charIndex = alpha.index(char)
    shiftDown = (charIndex.to_i - shift)

    newLetter = alpha[shiftDown]
end

puts returnShiftedLetter('C', 1, alpha)
def returnVigKeys(word, alpha)
    keys = []
    word.split('').each do |i|
      key = alpha.index(i)
      keys.push(key)
    end
    return keys
end
dangerous = 'DANGEROUS'

vigKeys = returnVigKeys(dangerous, alpha)

output = ''
vigIndex = 0
text.each_char do |b|

    if (alpha.include?(b))
      newLetter = returnShiftedLetter(b, vigKeys[vigIndex], alpha)
      output += newLetter
      vigIndex +=1
    else
      output += b
    end
    
    if vigIndex == vigKeys.length
      vigIndex = 0
    end
    
end
print output

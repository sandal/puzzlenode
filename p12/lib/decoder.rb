def possibleWords(word, shift, alpha)
  key = alpha[shift..-1]+alpha[0..shift]

  word.chars.each_with_object('') do |char, new_word|
    wordIndex = alpha.index(char)
    newWord << key[wordIndex]
  end
end
    
def returnShiftedLetter(char, shift, alpha)
  charIndex = alpha.index(char)
  shiftDown = (charIndex.to_i - shift)

  newLetter = alpha[shiftDown]
end

def returnVigKeys(word, alpha)
  word.chars.map  { |e| alpha.index(e) }
end

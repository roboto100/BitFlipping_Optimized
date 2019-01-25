size = 5


def getStrings(length):
    '''
    Get's all binary strings of size length
    :param length: the length of the binary strings
    :return: A list containing binary strings
    '''

    # Create empty list
    lst = []

    # For every integer from 0 to the 2^length
    for i in range(2 ** length):
        # Create the binary representation of that number
        newString = bin(i)[2:]
        # Append any 0's to the start of the string so it's of length length
        newString = "0" * (length - len(newString)) + newString
        # Add to the list
        lst.append(newString)
    # Return the list
    return lst


def correct(bitString, guess):
    '''
    Calculates how many places the guess matches the bitString
    :param bitString: a string, the known sequence of 0's and 1's
    :param guess: a guess for what the bitString is
    :return: The number of places guess matches bitString
    '''

    count = 0
    # For every index in the guess
    for index in range(len(guess)):
        # If bitString at that index is the same as guess at that index, increment count
        if bitString[index] == guess[index]:
            count += 1
    return count


def split(options, guess):
    '''
    Takes the possible bitstrings (options) and a guess to apply. Splits the options based on the knowledge gained by
    applying the guess. Returns the split options
    :param options: A single string specifying the possible bitstrings. Place each bitstring directly after the first,
                    eg. "000001010" specifies ["000","001","010"]. Based on global variable size
    :param guess: A string specifying which guess to apply when splitting the options
    :return: A list of new possible options. eg. ["000","001010100","011101011","111"] = [[000],[001,010,100],...
            [011,101,011],[111]]
    '''

    lst = []
    # Calculate this once to be used later
    rangeLimit = round(len(options) / size)

    # For all bitStrings in options
    for index in range(rangeLimit):
        # Note down how many correct bits are in that option based on the guess
        lst.append(correct(options[size * index:size * index + size], guess))

    newLst = []

    # Create a space for all possible different groups (eg, 0 correct, 1 correct, 2 correct, ....)
    for i in range(max(lst) + 1):
        newLst.append('')

    # For each option
    for index in range(rangeLimit):
        # Add that option to its grouping
        newLst[lst[index]] += options[size * index:size * index + size]

    # Remove all empty groups (eg, if the 1-correct group is empty, delete it)
    usedList = [sublst for sublst in newLst if sublst != '']

    return usedList


def calcualteScore(options, guess):
    '''
    Takes the possible options the string could be, a guess to apply, and calculates the average number of guesses we
    would require if we applied that guess
    :param options: A bitstring describing the possible options. eg "000010101"->[000,010,101]
    :param guess: A bitstring describing the guess we would like to apply
    :return: A score (float) describing the average number of guesses we expect to require if applying guess to options
    '''

    # Determine the new options we have when applying guess
    newList = split(options, guess)
    score = 1

    # For each group we have (after applying guess)
    for code in newList:

        # Try to obtain how manay average guesses it would require to solve that portion
        subScore = guessesRequired.get(code, 1000)

        # If we've already solved that code, we'll have a list; so take the first element of the list which is the
        # average number of guesses
        if type(subScore) is list:
            subScore = subScore[0]
        else:
            # We don't have a list, so we've never solved for this code before
            # If applying our guess hasn't done anything (eg, [001,100] apply 000 doesn't seperate), we want the score
            # to be massive (1000) so we never choose the guess. Otherwise (code!=options)
            if code != options:
                # Calculate the best score possible for the code
                getBestScore(code)

                # The code is now solved, retrieve it
                subScore = guessesRequired.get(code, 1000)
                subScore = subScore[0]
        # Add the score for the group specified, time the probability of that group being chosen
        score += subScore * len(code) / len(options)
    return score


def getBestScore(options):
    '''
    Determines the best bitstring to guess to split options. Minimizes the average number of guesses
    :param options: The possible bitstrings we could choose from
    :return: A list containing [minimum average number of guesses, what guess to apply]
    '''

    # Assume the best score is really bad
    bestScore = 100
    bestGuess = ""

    # If this is the first split we're doing (all possible bitstrings are avaliable), we do something different
    if len(options) >= (size * (2 ** (size))) - 1:
        # We always want to guess 00000..., this is the same as the rest of the code otherwise
        item = "0" * size
        newScore = calcualteScore(options, item)
        if newScore < bestScore:
            bestScore = newScore
            bestGuess = item
    else:
        # For possible bitstrings we have
        for item in Bits:
            # Calcualte the score if we apply that guess
            newScore = calcualteScore(options, item)
            # If that score beats our current best, then update
            if newScore < bestScore:
                bestScore = newScore
                bestGuess = item

    # Add the best guesses to our dictionary to be retrieved later
    guessesRequired[options] = [bestScore, bestGuess]


def populateDictionary():
    '''
    Populates guessesRequired with the minimum average guesses for various bitstring options
    :return: None
    '''

    # For all single bitstrings (only 1 option), add that we need 0 guesses to solve them
    for item in Bits:
        guessesRequired[item] = [0, '...']

    # Build up the string containing all possible bitstring's as options
    newCode = ""
    for item in Bits:
        newCode += item

    # Solve for the best score for this bitstring
    getBestScore(newCode)


def buildMathematicaChart(referenceStore):
    '''
    Builds an array we can copy/paste into mathematica which will create a flowchart of the logic behind the guesses
    :param: referenceStore: A boolean telling us whether to return a reference to our storage of vertices
    :return: String to be copied to Mathematica, OR reference to dictionary storing labels for vertices
    '''

    # Build up all options in 1 bitstring, and add them to a todo list
    Bits = getStrings(size)
    allOptions = ""
    for item in Bits:
        allOptions += item
    toDo = [allOptions]

    # We're going to be building a long string
    bigString = '{'

    # Mathematica needs us to have different vertex names for each new vertex. This k will keep track of which guesses
    # are different. Store them in a dictionary
    k = 0
    store = {}

    # While we have something to do
    while len(toDo) > 0:
        # Grab the first bits in toDo and pop it out
        Bits = toDo[0]
        toDo.pop(0)

        # Determine what we need to apply to those Bits
        apply = guessesRequired[Bits]

        # Split the Bits with that guess
        newBits = split(Bits, apply[1])

        # For each of the new options we obtain when splitting Bits
        for item in newBits:
            # Determine what guess we should apply to that item (name of that vertex)
            apply2 = guessesRequired[item]

            # Get the k number which distinguishes different vertices that use the same guess
            tempNum = store.get(Bits, -1)
            tempNum2 = store.get(item, -1)

            # If we couldn't get a k for Bits
            if tempNum == -1:
                # Create a k value for Bits
                store[Bits] = k
                tempNum = k
                k += 1
            # If we couldn't get a k for the new options
            if tempNum2 == -1:
                # Create a k value for the new options
                store[item] = k
                tempNum2 = k
                k += 1

            # set the vertex we're going to as what it should be
            endVertex = apply2[1]

            # If endVertex is not a guess (ie, we know what the string is at that point), do something different
            if endVertex == "...":
                # Add the important bits to the code
                bigString += '{"' + str(tempNum) + "? " + apply[1] + '"->"' + item + '","' + str(
                    correct(item, apply[1])) + '"},'
            else:
                # Add the important bits to the code
                bigString += '{"' + str(tempNum) + "? " + apply[1] + '"->"' + str(
                    tempNum2) + "? " + endVertex + '","' + str(correct(item, apply[1])) + '"},'

        # Append all the new Options to our toDo list (if they are longer than the size, IE we need to apply a guess to them)
        for item in newBits:
            if len(item) > size:
                toDo.append(item)

    if (referenceStore):
        return store
    else:
        print(bigString[:-2] + "}};")


def createPythonFunctions():
    '''
    Creates a series of python functions that call each other, simulating a flow chart. These functions are built to be
    pasted into a different python project which will call them and use them to solve the bit-flipping puzzle
    :return: None
    '''

    # We need to build the dictionary, we've modified buildMathematicaChart to let us do this (little bit inefficient,
    # but it works
    store = buildMathematicaChart(True)

    # For every vertex we might be at
    for key in store:
        # Create a function for that vertex
        print('def f' + str(size) + "_" + str(store[key]) + '():')

        # If we're can immediately return; do that
        apply = str(guessesRequired[key][1])
        if (apply == "..."):
            print('    return "' + key + '"')
        elif (store[key] == 0):
            # Otherwise if we're on the first vertex, we need to specify how many we have correct in our section:
            # We know how many we had correct previously, and how many are now correct, but we need to know how many
            # in our section is correct. So calculate that and procueed as usual
            print('    guess = myBitSolver.guess("' + str(guessesRequired[key][1]) + '")')
            print('    myBitSolver.secOnes = round((' + str(size) + ' + myBitSolver.allOnes - guess) / 2)')
            print('    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)')
            newString = '    path = {'
            newBits = split(key, apply)
            for item in newBits:
                correctNum = str(correct(item, apply))
                newString += correctNum + ':f' + str(size) + "_" + str(store[item]) + ','
            newString = newString[:-1] + "}"
            print(newString)
            print('    return path[correct]()')
        else:
            # We're not on the first vertex. Specify the guess, calculate how many are correct
            print('    guess = myBitSolver.guess("' + str(guessesRequired[key][1]) + '")')
            print('    correct = -(myBitSolver.allOnes - guess - myBitSolver.secOnes)')
            newString = '    path = {'
            # Move to a new vertex depending on how many were correct
            newBits = split(key, apply)
            for item in newBits:
                correctNum = str(correct(item, apply))
                newString += correctNum + ':f' + str(size) + "_" + str(store[item]) + ','
            newString = newString[:-1] + "}"
            print(newString)
            print('    return path[correct]()')


def minimumAverageGuesses():
    # Build up all options in 1 bitstring
    Bits = getStrings(size)
    allOptions = ""
    for item in Bits:
        allOptions += item
    # Get the number of guesses required and print them out
    print("Minimum average guesses: " + str(guessesRequired[allOptions][0]))
    print("Effective ratio (lower is better): " + str(guessesRequired[allOptions][0] / size))


Bits = getStrings(size)
guessesRequired = {}
populateDictionary()

#minimumAverageGuesses()
#buildMathematicaChart(False)
#createPythonFunctions()

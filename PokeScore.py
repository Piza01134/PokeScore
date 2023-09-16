import pypokedex

"""
Returns a scrabble score for a given word

Param: word - word to calculate the score of
"""
def scrabble_score( word ):

    values = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    
    score = 0

    for letter in word:
        score += values.get( letter, 0 )

    return score


"""
Returns the Pokemon with the largest product of Pokemon name scrabble score and defence
"""
def scrabble_defense_score():

    highScore = 0
    highScorePokemon = None
    dex = 0

    for x in range( 1, 1011 ):

        pokemon = pypokedex.get( dex = x )

        score = pokemon.base_stats.defense * scrabble_score( pokemon.name )

        print( str( x ) + "  " + str( score ) )

        if score > highScore:

            highScore = score
            highScorePokemon = pokemon
            dex = x

    return highScorePokemon



if __name__ == "__main__":

    pokemon = scrabble_defense_score()
    print( "The pokemon with the highest scrabble defense score is " + pokemon.name + " with a score of " 
          + str( pokemon.base_stats.defense * scrabble_score( pokemon.name ) ) )
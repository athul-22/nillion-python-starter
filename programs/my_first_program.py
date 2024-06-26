from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform a different computation
    result = my_int1 - my_int2  # Example computation: subtracting the second secret integer from the first

    # Output the result
    return [Output(result, "my_output", party1)]

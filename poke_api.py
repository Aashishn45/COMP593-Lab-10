'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import image_lib
import os

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
   
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    
def get_pok_names():
    print("Getting lists of pokemon names....", end="")
    param = {
        "limit": 2000,
        "offset": 0,
    }
    rep_msg = requests.get(POKE_API_URL, params=param)
    if rep_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        pok_dic =  rep_msg.json()
        return [pok["name"] for pok in pok_dic["results"]]
    else:
        print('failure')
        print(f'Response code: {rep_msg.status_code} ({rep_msg.reason})')
    return

def get_pok_art(pokemon, image_dir):
    pok_inf = get_pokemon_info(pokemon)
    if not pok_inf:
        return
    
    art_url = pok_inf["sprites"]["other"]["official-artwork"]["front_default"]
    if not art_url:
        print(f"No artwork found for {pokemon.capitalize()}.")
        return
    
    file_ext = art_url.split(".")[-1]
    img_path = os.path.join(image_dir, f"{pokemon}.{file_ext}")
    if os.path.isfile(img_path):
        print(f"{pokemon.capitalize()} artwork already exists.")

    
    img_data = image_lib.download_image(art_url)
    if not img_data:
        return
    
    
    if image_lib.save_image_file(img_data, img_path):
        return img_path
    

if __name__ == '__main__':
    main()
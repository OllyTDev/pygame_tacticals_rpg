class Terrain:
    """
    Terrain base class
    Sets the base values for creating a new terrain type
    
    Parameters
    ----------
    name : string
        the name of the particular terrain created
    colour : (int, int, int)
        Takes the colour as (red, green, blue)
        Only used in the base program for debugging     

    """
    def __init__(self, name, image):
        self.name = name
        self.image = image

grass = Terrain("grass", 'Asset\GrassV2.png')
sand = Terrain("sand", 'Asset\Sand.png')
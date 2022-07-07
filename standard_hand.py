from blok import Blok

# Manually define each blok
def get_standard():
    return [
    Blok(
    [[1]], False, 1),

    Blok(
    [[1],
     [1]], False, 2),

    Blok(
    [[1],
     [1],
     [1]], False, 2),

    Blok(
    [[1,0],
     [1,1]], False, 4),

    Blok(
    [[1],
     [1],
     [1],
     [1]], False, 2),

    Blok(
    [[0,1],
     [0,1],
     [1,1]], True, 4),

    Blok(
    [[1,0],
     [1,1],
     [1,0]], False, 4),

    Blok(
    [[1,1],
     [1,1]], False, 1),

    Blok(
    [[1,1,0],
     [0,1,1]], True, 2),

    Blok(
    [[1],
     [1],
     [1],
     [1],
     [1]], False, 2),

    Blok(
    [[0,1],
     [0,1],
     [0,1],
     [1,1]], True, 4),

    Blok(
    [[0,1],
     [0,1],
     [1,1],
     [1,0]], True, 4),

    Blok(
    [[0,1],
     [1,1],
     [1,1]], True, 4),

    Blok(
    [[1,1],
     [0,1],
     [1,1]], False, 4),

    Blok(
    [[1,0],
     [1,1],
     [1,0],
     [1,0]], True, 4),

    Blok(
    [[0,1,0],
     [0,1,0],
     [1,1,1]], False, 4),

    Blok(
    [[1,0,0],
     [1,0,0],
     [1,1,1]], False, 4),

    Blok(
    [[1,1,0],
     [0,1,1],
     [0,0,1]], False, 4),

    Blok(
    [[1,0,0],
     [1,1,1],
     [0,0,1]], True, 2),

    Blok(
    [[1,0,0],
     [1,1,1],
     [0,1,0]], True, 4),

    Blok(
    [[0,1,0],
     [1,1,1],
     [0,1,0]], False, 1),
    ]
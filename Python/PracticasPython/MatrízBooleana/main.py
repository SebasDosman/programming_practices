labyrinth = [   
                [False, False, True , False, False, False, False, False], 
                [False, False, True , False, False, False, False, False], 
                [False, False, True , True , True , False, False, False], 
                [False, False, False, False, True , False, False, False], 
                [True , True , True , True , True , False, False, False], 
                [True , False, False, False, False, True , True , True ], 
                [True , True , True , True , False, True , False, False], 
                [False, False, False, True , True , True , False, False]
            ]

aux_labyrinth = [[False if cell else False for cell in row] for row in labyrinth]

def search_index(value : list) -> list:
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if i == value[0] and j == value[1] and labyrinth[i][j]:
                return [i, j]
    
    raise Exception(f'The index { value } is not found in the list')

def add_index_visited(value : list) -> None:
    aux_labyrinth[value[0]][value[1]] = True

def is_way(value : list) -> bool:
    try:
        aux = labyrinth[value[0]][value[1]]
        
        return True
    except IndexError:
        return False

def is_visited(value : list) -> bool:
    if aux_labyrinth[value[0]][value[1]]:
        return True
    
    return False

def validate_way(value : list) -> bool:
    if is_way([value[0], value[1]]) and labyrinth[value[0]][value[1]] and not is_visited([value[0], value[1]]):
        return True
    
    return False

def chosen_way(value : list, way : str) -> None:
    add_index_visited([value[0], value[1]])
    
    print(way)

def search_way(value : list) -> None:
    DOWN_WAY = [value[0] + 1, value[1]]
    RIGHT_WAY = [value[0], value[1] + 1]
    LEFT_WAY = [value[0], value[1] - 1]
    UP_WAY = [value[0] - 1, value[1]]
    
    add_index_visited([value[0], value[1]])
    
    if validate_way(DOWN_WAY):
        chosen_way(DOWN_WAY, '👇')
        search_way(DOWN_WAY)
    elif validate_way(RIGHT_WAY):
        chosen_way(RIGHT_WAY, '👉')
        search_way(RIGHT_WAY)
    elif validate_way(LEFT_WAY):
        chosen_way(LEFT_WAY, '👈')
        search_way(LEFT_WAY)
    elif validate_way(UP_WAY):
        chosen_way(UP_WAY, '👆')
        search_way(UP_WAY)
    
    raise Exception('You are in a dead end')

def main():
    try:
        start_index = search_index([int(input('Enter the first index: ')), 
                                    int(input('Enter the second index: '))])
        
        print('\nYou are in the start index \n')	
        
        search_way(start_index)
    except Exception as e:
        print(f'\n{ e }')

if __name__ == '__main__':
    main() 
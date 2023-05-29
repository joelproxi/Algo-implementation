
table = [3, 5, 9, 29, 38, 40, 50, 58, 69, 77, 82, 83, 86, 90]


def binary_search(table: list[int], nber: int) -> str:
    min: int = 0
    max: int = len(table) - 1
    is_found = True
    mid: int = ( min + max) // 2
    
    while is_found:
        if min == max:
            if nber != table[mid]:
                return "Not found"
        
        elif nber == table[mid]:
            return f" {nber} found in possition {mid}"
        
        elif table[mid] > nber:
            max = mid - 1   
            mid = (min + max) // 2
            print(table[min:mid])
            if nber == table[mid]:
                return f" {nber} found in possition {mid}"
            
        elif  table[mid] < nber:
            min = mid + 1
            mid = (min + max) // 2
            print(table[mid:max])
            if nber == table[mid]:
                return f" {nber} found in possition {mid}"
            
            

print(binary_search(table, 5))

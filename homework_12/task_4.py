def merge_lists(list1, list2):
    merged = [] 
    i = 0  
    e = 0  
 
    while i < len(list1) and e < len(list2):
        if list1[i] <= list2[e]:
            merged.append(list1[i])
            i += 1  
        else:
            merged.append(list2[e]) 
            e += 1  

    while i < len(list1):
        merged.append(list1[i])
        i += 1
        
    while e < len(list2):
        merged.append(list2[j])
        e += 1
    
    return merged

def main():
   # დავალების მაგალითი
    list1 = [1, 3, 10]
    list2 = [0, 4, 7, 9]
    print("Merged numbers #1 - ", merge_lists(list1, list2))
    
   # ცდა 2
    list3 = [3, 50]
    list4 = [0, 4, 7, 9]
    print("Merged numbers #2 - :", merge_lists(list3, list4))

if __name__ == "__main__":
    main()
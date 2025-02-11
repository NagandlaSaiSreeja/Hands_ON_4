import heapq

def merge_sorted_arrays(arrays):
    min_heap = []
    
    # Push the first element of each array into the heap along with array index and element index
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
    
    merged_result = []
    
    # Extract elements from the heap and push next elements from the same arrays
    while min_heap:
        value, arr_idx, elem_idx = heapq.heappop(min_heap)
        merged_result.append(value)
        
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_value = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_value, arr_idx, elem_idx + 1))
    
    return merged_result

# Example test cases
arrays_1 = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
print(merge_sorted_arrays(arrays_1))  
arrays_2 = [[1, 3, 7], [2, 4, 8], [9, 10, 11]]
print(merge_sorted_arrays(arrays_2))  
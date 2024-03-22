def find_min1(nums: list[int]) -> int:
    min_idx: int = 0
    idx: int = 0
    while idx < len(nums):
        if nums[idx] < nums[min_idx]:
            min_idx = idx
        idx += 1
    return min_idx

def find_min2(nums: list[int]) -> int:
    min_idx: int = 0
    min_val: int = nums[min_idx]
    idx: int = 0
    while idx < len(nums):
        val: int = nums[idx]
        if val < min_val:
            min_idx = idx
            min_val = val
        idx += 1
    return min_idx

search_vals: list[int] = [10, 9, 8]
find_min1(search_vals)
find_min2(search_vals)






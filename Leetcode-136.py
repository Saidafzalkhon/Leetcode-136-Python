if __name__ == "__main__":
    nums = list(map(int,input().split()))
    for i in nums:
            if nums.count(i) == 1:
                print(i)
class Majority:

    def majorityNumber(nums):
        key,count=None,0

        for num in nums:
            if key is None:
                key,count=num,1
            else:
                if key==num:
                    count+=1
                else:
                    count-=1

            if count==0 :
                key=None
        return key

if __name__ == '__main__':
    nums=[1,1,1,1,1,1,1,2,2,3,3,4]
    x=Majority
    print(x.majorityNumber(nums))
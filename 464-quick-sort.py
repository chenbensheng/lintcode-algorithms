class QuickSort :

    def quick_sort(self,A,start,end):
        if start>=end:
            return

        left,right=start,end
        #推荐 用左端、右端和中心位置上的三个元素的中值作为“基准” 三数中值分割方法
        #拿出第一个数当作基准数
        pivot = A[int((start+end)/2)];

        while left<=right:
            while left<= right and A[left]<pivot :
                left+=1

            while left<= right and A[right]>pivot :
                right-=1

            if left<=right:
                A[left],A[right]=A[right],A[left]

                left+=1
                right-=1

        self.quick_sort(A,start,right)
        self.quick_sort(A,left,end)

if __name__ == '__main__':
     li = [5,4,3,7,2,1]
     a=QuickSort()
     a.quick_sort(li ,0, len(li)-1)
     print(li)
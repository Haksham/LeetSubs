class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        k=0
        fin=[0]*(m+n)
        while(i<m and j<n):
            if nums1[i]<nums2[j]:
                fin[k]=nums1[i]
                k+=1
                i+=1
            elif nums2[j]<=nums1[i]:
                fin[k]=nums2[j]
                k+=1
                j+=1
        while(i<m):
            fin[k]=nums1[i]
            i+=1
            k+=1
        while(j<n):
            fin[k]=nums2[j]
            j+=1
            k+=1
        for i in range(m+n):
            nums1[i]=fin[i]

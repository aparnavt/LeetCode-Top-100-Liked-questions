class Solution:
  def mergesortedlists(self, nums1: List[int], nums2: List[int])->List[int]:
 
    index1,index2=0, 
    i = 0
    for i in range(0, len(nums1)+len(nums2)-2):
      if (nums1[index1]== nums2[index2]):
        out[i], out[i+1]= nums1[index1], nums2[index2]
        i=i+2
        index1+=1
        index2+=1
      else if(nums1[index1]< nums2[index2]) :
        out[i] = nums1[index1], nums2[index2]
        i=i+1
        index1+=1
      else:
        out[i] = nums1[index1], nums2[index2]
        i=i+1
        index2+=1
     return out   
          
      

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){return false;}
        String str=Integer.toString(x);
        char[] arr = str.toCharArray();

        int f=0;
        int n=str.length();
        for(int i=0;i<n;i++){
            if(arr[i] != arr[n-i-1]){
                return false;
            }
        }
        return true;
    }
}
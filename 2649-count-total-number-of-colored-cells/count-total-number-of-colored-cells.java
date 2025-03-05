class Solution {
    public long coloredCells(int n) {
        long ans=0;
        long i;
        for(i=1;i<n;i++){
            ans+=(2*i-1);
        }
        ans*=2;
        ans+=(2*i-1);
        return ans;
    }
}
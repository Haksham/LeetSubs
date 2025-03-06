class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int n=grid.length;
        int[] ans=new int[2];
        int[] ls=new int[n*n+1];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                ls[grid[i][j]]++;
            }
        }
        for(int i=1;i<=n*n;i++){
            if (ls[i]==0){
                ans[1]=i;
            }
            if(ls[i]==2){
                ans[0]=i;
            }
        }
        return ans;
    }
}
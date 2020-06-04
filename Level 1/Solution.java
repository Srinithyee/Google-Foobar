public class Solution 
{
    public static int solution(String x)
    {
    	int number_slice = -1;
        int len = x.length();
        for(int i = len; i > 0; i--)
        {           
            int n = len/i;
            if( n * i == len)
            {
                boolean flag = true;
                String sub = s.substring(0,n);
                for(int j = 1; j < i; j++)
                    {
                        if(!s.substring(j*n,j*n+n).equals(sub))
                        {
                            flag = false;
                            break;
                        }
                    }
                    if(flag)
                    {
                        number_slice = i;
                        break;
                    }
            }
        }
        return number_slice;
    }
}
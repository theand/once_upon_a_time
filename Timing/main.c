
#include "inst.h"

int recursive_fibonacci_number(int n) 
{ 
	if (n <= 1) 
		return 1; 
			         
	return( recursive_fibonacci_number(n-1) + recursive_fibonacci_number(n-2) );
} 

int iterative_fibonacci_number(int n) 
{ 
        int last = 1; 
        int nextToLast = 1; 
        int answer = 1; 
 
        if (n <= 1) 
                return 1; 
 
        for (int i=2; i <= n; ++i) 
        { 
                answer = last + nextToLast; 
                nextToLast = last; 
                last = answer; 
        } 
 
        return answer; 
} 
int main(void)
{
	start_clock("fibo");
	recursive_fibonacci_number(33);
	stop_clock("fibo");

	start_clock("fibo2");
	iterative_fibonacci_number(33);
	stop_clock("fibo2");


	clock_report();
	return 0;
}

using System;

namespace question2
{
    class Program
    {
        static void Main(string[] args)
        {
            long previousNum = 0;
            int counter = 1;
            long num = 1;
            long sum = 0;
            while (counter <= 32)
            {
                long fib = previousNum + num;
                previousNum = num;
                num = fib;
                if (fib % 2 == 0)
                {
                    sum += fib;
                }
                counter++;
            }
            Console.WriteLine(sum);
        }
    }
}

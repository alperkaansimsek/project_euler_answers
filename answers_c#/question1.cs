using System;

namespace question1
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            for(int i = 3; i < 1000; i++)
            {
                if(i % 3 == 0 || i % 5 == 0)
                {
                    sum += i;
                }
            }
            Console.WriteLine(sum);
        }
    }
}

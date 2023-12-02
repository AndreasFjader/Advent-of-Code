namespace Advent_of_Code
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Day2 day2 = new Day2();
            Console.WriteLine("<Test>");
            day2.Solve(false);
            Console.WriteLine("<Real>");
            day2.Solve(true);
        }
    }
}
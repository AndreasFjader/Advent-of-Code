namespace Advent_of_Code
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Day3 day3 = new Day3();
            Console.WriteLine("<Test>");
            day3.Solve(false);
            Console.WriteLine("<Real>");
            day3.Solve(true);
        }
    }
}
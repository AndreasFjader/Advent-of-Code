using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Advent_of_Code
{
    internal class Day1
    {
        string[] test;
        string[] input;

        public Day1() 
        {
            test = File.ReadAllLines("../../../Day 1/test.txt");
            input = File.ReadAllLines("../../../Day 1/input.txt");
        }

        public void Solve(bool real = false)
        {
            Console.WriteLine("<Solving day 1>");
            int sumPart1 = 0;
            int sumPart2 = 0;
            string pattern = "1|2|3|4|5|6|7|8|9";
            string pattern2 = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine";

            foreach (string calibrationValue in real ? input : test)
            {
                // Part 1
                var first = Regex.Match(calibrationValue, pattern);
                var last = Regex.Match(calibrationValue, pattern, RegexOptions.RightToLeft);
                sumPart1 += int.Parse(TextToDigitString(first.Value) + TextToDigitString(last.Value));

                // Part 2
                var first2 = Regex.Match(calibrationValue, pattern2);
                var last2 = Regex.Match(calibrationValue, pattern2, RegexOptions.RightToLeft);
                sumPart2 += int.Parse(TextToDigitString(first2.Value) + TextToDigitString(last2.Value));
            }

            Console.WriteLine($"Part 1: {sumPart1}");
            Console.WriteLine($"Part 2: {sumPart2}");
        }

        string TextToDigitString(string input) => input switch
        {
            "one" => "1",
            "two" => "2",
            "three" => "3",
            "four" => "4",
            "five" => "5",
            "six" => "6",
            "seven" => "7",
            "eight" => "8",
            "nine" => "9",
            _ => input,
        };
    }
}

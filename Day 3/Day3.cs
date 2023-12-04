using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_of_Code
{
    internal class Day3
    {
        string filePath = "Day 3";
        string[] input;
        string[] test;
        public Day3()
        {
            input = File.ReadAllLines($"{filePath}/in.txt");
            test = File.ReadAllLines($"{filePath}/test.txt");
        }

        public void Solve(bool real = false)
        {
            string[] chart = real ? input : test;
            List<Point> asterixes = new List<Point>();
            HashSet<Point> numberCoords = new HashSet<Point>();
            for (int r = 0; r < chart.Length; r++) {
                for (int c = 0; c < chart[r].Length; c++)
                {
                    if (char.IsDigit(chart[r][c]) || chart[r][c] == '.')
                        continue;

                    int[] nx = { r, r + 1, r - 1 };
                    int[] ny = { c, c + 1, c - 1 };
                    foreach (var nr in nx) {
                        foreach (var nc in ny)
                        {
                            if (nc < 0 || nc >= chart[r].Length || nr < 0 || nr >= chart.Length)
                                continue;

                            char symbol = chart[nr][nc];
                            if (symbol == '*')
                                asterixes.Add(new Point(nr, nc));

                            if (!char.IsDigit(symbol))
                                continue;

                            int cc = nc;
                            while (cc > 0 && char.IsDigit(chart[nr][cc - 1]))
                            {
                                cc--;
                            }
                            numberCoords.Add(new Point(nr, cc));
                        }
                    }
                }
            }

            List<int> numbers = new List<int>();
            foreach (var number in numberCoords)
            {
                int c = number.Y;
                int r = number.X;
                string n = "";
                while (c < chart[r].Length && char.IsDigit(chart[r][c])) 
                {
                    n += chart[r][c];
                    c++;
                }
                numbers.Add(int.Parse(n));
            }

            // Part 1
            int sum = 0;
            foreach (var item in numbers) sum += item;
            Console.WriteLine("Part 1: {0}", sum);

            // Part 2. Unfortunately with some duplicate code, but this doesn't go onto production so...
            List<int> gearRatios = new List<int>();
            foreach (Point ast in asterixes)
            {
                HashSet<Point> adjNumbers = new HashSet<Point>();
                List<int> newNumbers = new List<int>();
                int r = ast.X, 
                    c = ast.Y;
                int[] nx = { r, r + 1, r - 1};                
                int[] ny = { c, c + 1, c - 1};
                
                foreach (int nr in nx) {
                    foreach (int nc in ny)
                    {
                        if (nc < 0 || nc >= chart[r].Length || nr < 0 || nr >= chart.Length)
                            continue;
                        
                        char ch = chart[nr][nc];
                        if (char.IsDigit(ch))
                        {
                            // Digit found in the surrounding area, start backtracking to its root.
                            int cc = nc;
                            while (cc > 0 && char.IsDigit(chart[nr][cc - 1]))
                            {
                                cc--;
                            }
                            adjNumbers.Add(new Point(nr, cc));
                        }
                    }
                }
                if (adjNumbers.Count == 2)
                {
                    // Only two adjecant gears, find the numbers.
                    foreach (Point adj in adjNumbers)
                    {
                        int ra = adj.X;
                        int ca = adj.Y;
                        string n = "";
                        
                        while (ca < chart[ra].Length && char.IsDigit(chart[ra][ca]))
                        {
                            n += chart[ra][ca];
                            ca++;
                        }
                        newNumbers.Add(int.Parse(n));
                    }
                    gearRatios.Add(newNumbers[0] * newNumbers[1]);
                }                
            }
            Console.WriteLine("Part 2: {0}", gearRatios.Sum(x => x));
            
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advent_of_Code
{
    internal class Day2
    {
        string filePath = "../../../Day 2";
        string[] input;
        string[] test;
        public Day2() 
        {
            input = File.ReadAllLines($"{filePath}/in.txt");
            test = File.ReadAllLines($"{filePath}/test.txt");
        }

        public void Solve(bool real = false)
        {
            List<Game> games = new List<Game>();
            
            // Parsing input
            foreach (string game in real ? input : test)
            {
                // We don't need to actively track the game's index.
                var g = new Game();
                var sets = game.Split(':')[1].Split(";");

                foreach (string set in sets)
                {
                    Set s = new Set();
                    string[] colors = set.Split(",");
                    foreach (var color in colors)
                    {
                        string[] t = color.Trim().Split(" ");
                        int amount = int.Parse(t[0]);
                        string c = t[1];

                        switch(c)
                        {
                            case "red":
                                s.Red = amount; break;
                            case "blue":
                                s.Blue = amount; break;
                            case "green":
                                s.Green = amount; break;
                            default:
                                throw new Exception($"Parsing colors - found unexpected color: {c}");
                        }
                    }
                    g.AddSet(s);
                }
                games.Add(g);
            }

            // Part 1 - check if any game contains a set with red > 12, green > 13, blue > 14.
            int gameId = 1;
            int sum1 = 0;
            int sum2 = 0;
            foreach (Game game in games)
            {
                // For part 1
                if (!game.HasAnySetMoreThanAllowedCubes())
                {
                    sum1 += gameId;
                }
                gameId++;

                // For part 2
                sum2 += game.GetPowerOfFewestRequiredCubes();
            }
            Console.WriteLine($"Solution part 1: {sum1}");
            Console.WriteLine($"Solution part 2: {sum2}");
        }

    }

    class Game
    {
        List<Set> sets;
        public Game() 
        {
            sets = new List<Set>();
        }

        public void AddSet(Set s) => sets.Add(s);

        public bool HasAnySetMoreThanAllowedCubes() => sets.Any(x => x.Red > 12 || x.Green > 13 || x.Blue > 14);

        public int GetPowerOfFewestRequiredCubes()
        {
            int minimumRed = sets.Max(x => x.Red);
            int minimumGreen = sets.Max(x => x.Green);
            int minimumBlue = sets.Max(x => x.Blue);

            return minimumRed * minimumGreen * minimumBlue;
        }
    }

    struct Set
    {
        public int Red = 0;
        public int Green = 0;
        public int Blue = 0;

        public Set() { }
    }
}

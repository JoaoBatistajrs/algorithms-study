// See https://aka.ms/new-console-template for more information
using BinarySearch;
Console.WriteLine("Hello, World!");

BinarySearchMethod search = new BinarySearchMethod();

int[] numbers = { 1, 3, 5, 7, 9, 11, 13, 15 };

int target = 7;

string result = search.BinarySearch(numbers, target);

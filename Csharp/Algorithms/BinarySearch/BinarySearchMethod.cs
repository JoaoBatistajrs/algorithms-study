namespace BinarySearch;

public class BinarySearchMethod
{
    public string BinarySearch(int[] arr, int target)
    {
        int left = 0;
        int right = arr.Length - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;

            if(arr[mid] == target)
            {
                return mid.ToString();
            }
            else if (arr[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
               
        }

        return "Not found";
    }
}

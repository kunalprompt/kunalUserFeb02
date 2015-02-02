// #include <stdio.h>

// //quick Sort function to Sort Integer array list
// void quicksort(int array[], int firstIndex, int lastIndex)
// {
//     //declaaring index variables
//     int pivotIndex, temp, index1, index2;

//     if(firstIndex < lastIndex)
//     {
//         //assigninh first element index as pivot element
//         pivotIndex = firstIndex;
//         index1 = firstIndex;
//         index2 = lastIndex;

//         //Sorting in Ascending order with quick sort
//         while(index1 < index2)
//         {
//             while(array[index1] <= array[pivotIndex] && index1 < lastIndex)
//             {
//                 index1++;
//             }
//             while(array[index2]>array[pivotIndex])
//             {
//                 index2--;
//             }

//             if(index1<index2)
//             {
//                 //Swapping opertation
//                 temp = array[index1];
//                 array[index1] = array[index2];
//                 array[index2] = temp;
//             }
//         }

//         //At the end of first iteration, swap pivot element with index2 element
//         temp = array[pivotIndex];
//         array[pivotIndex] = array[index2];
//         array[index2] = temp;

//         //Recursive call for quick sort, with partiontioning
//         quicksort(array, firstIndex, index2-1);
//         quicksort(array, index2+1, lastIndex);
//     }
// }

// int main()
// {
//     //Declaring variables
//     int array[100],n,i;

//     //Number of elements in array form user input
//     printf("Enter the number of element you want to Sort : ");
//     scanf("%d",&n);

//     //code to ask to enter elements from user equal to n
//     printf("Enter Elements in the list : ");
//     for(i = 0; i < n; i++)
//     {
//         scanf("%d",&array[i]);
//     }

//     //calling quickSort function defined above
//     quicksort(array,0,n-1);

//     //print sorted array
//     printf("Sorted elements: ");
//     for(i=0;i<n;i++)
//     printf(" %d",array[i]);

//     return 0;
// }


/* qsort example 2*/
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* qsort */

int values[] = { 40, 10, 100, 90, 20, 25 };

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main ()
{
  int n;
  qsort (values, 6, sizeof(int), compare);
  for (n=0; n<6; n++)
     printf ("%d ",values[n]);
  return 0;
}
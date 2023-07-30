#include<stdio.h>
#include<stdlib.h>

void merge(int* arr1, int size1, int* arr2, int size2, int* arr3) {
    int i = 0, j = 0, k = 0;

    // Traverse both arrays
    while (i < size1 && j < size2) {
        if (arr1[i] < arr2[j])
            arr3[k++] = arr1[i++];
        else
            arr3[k++] = arr2[j++];
    }

    // Store remaining elements of first array
    while (i < size1)
        arr3[k++] = arr1[i++];

    // Store remaining elements of second array
    while (j < size2)
        arr3[k++] = arr2[j++];
}

int main() {
    int size1 = 4;
    int* arr1 = (int*)malloc(size1*sizeof(int));
    arr1[0] = 1;
    arr1[1] = 3;
    arr1[2] = 5;
    arr1[3] = 7;

    int size2 = 4;
    int* arr2 = (int*)malloc(size2*sizeof(int));
    arr2[0] = 2;
    arr2[1] = 4;
    arr2[2] = 6;
    arr2[3] = 8;

    int* arr3 = (int*)malloc((size1+size2)*sizeof(int));
    merge(arr1, size1, arr2, size2, arr3);

    printf("Array after merging\n");
    for (int i=0; i < size1+size2; i++)
        printf("%d ", arr3[i]);
    printf("\n");

    free(arr1);
    free(arr2);
    free(arr3);
    
    return 0;
}

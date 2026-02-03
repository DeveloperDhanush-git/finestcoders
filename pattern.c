// left aligned triangle
#include <stdio.h>
#include <string.h>
int main() {
    char arr[100];
    scanf("%s",arr);
    for (int i = 0; i < strlen(arr); i++) {
        for (int j = 0; j <=i ; j++) {
            printf("%c",arr[j]);
        }
        printf("\n");
    }
    return 0;
}
// right aligned triangle

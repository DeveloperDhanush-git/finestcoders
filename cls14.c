#include <stdio.h>
#include <ctype.h>
int main() {
    char ch;
    scanf("%c", &ch);
    ch = tolower(ch);
    if(isalpha(ch)){
    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
        ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
        printf("Vowel");
    } else {
        printf("Consonant");
    }
    }
    else{
        printf("Invalid Input");
    }
    

    return 0;
}

#include <stdio.h>
#include <string.h> // Needed for strcmp

int main()
{
    char Signal[100];
    scanf("%s", Signal);  // No need for & with arrays

    if (strcmp(Signal, "Red") == 0) {
        printf("Stop\n");
    }
    else if (strcmp(Signal, "Yellow") == 0) {
        printf("Wait\n");
    }
    else if (strcmp(Signal, "Green") == 0) {
        printf("Go\n");
    }
    else {
        printf("Invalid Input\n");
    }
    return 0;
}


#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    if(a>=1 || b<=1000){
    printf("Flour:%d \n",a);
    printf("Sugar:%d",b);   
    }
    else{
        printf("dfdbvu");
    }
    return 0;
}


#include <stdio.h>
int main()
{
    int a,b,temp;
    scanf("%d",&a);
    scanf("%d",&b);
    if(a>= -100 || b<=100){
    temp = a;
    a = b;
    b =temp;
    printf("Swapped values : %d,%d",a,b);
    }
    return 0;
}


#include <stdio.h>

int main() {
    float weight, height, bmi;

    scanf("%f", &weight);
    scanf("%f", &height);

    bmi = weight / (height * height);

    printf("Your BMI is: %.2f\n", bmi);

    return 0;
}

#include <stdio.h>


int main()
{
    char name[100], mark[100];
    int roll,marks[100];
    scanf("%s",name);
    scanf("%d",&roll);
    for (int i = 0; i < 4; i++) {
        scanf("%d",&marks[i]);
    }
    printf("Name : %s \n",name);
    printf("RollNo : %d \n",roll);
    printf("Marks :");
     for (int i = 0; i < 4; i++) {
        printf(" %d ",marks[i]);
    }
    return 0;
}


#include <stdio.h>


int main()
{
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    if(a>=-103 && a<=103 && b>=-103 && b<=103){
    printf("%d \n",a*b);
    if(b!=0){
    printf("%d",a/b);
    }
    else{
        printf("zero division error");
    }
    }
}

#include <stdio.h>

int main()
{
    char str[100] = "Dennis Ritchie";
    printf("%s",str);
    return 0;
}


#include <stdio.h>

int main()
{
    int angle1,angle2,angle3;
    scanf("%d %d",&angle1,&angle2);
    int add = angle1+angle2;
    if(angle1>=0 && angle2 <=180 && add <=180){
         angle3 = 180-add;
         printf("%d",angle3);
    }
   else{
        printf("Invalid Input");
    }

    return 0;
}


#include <stdio.h>

int main()
{
    int age;
    scanf("%d",&age);
    if(age<=0 || age<1 || age>120){
        printf("Invalid Input");
    }
    else if(age<18){
        printf("Not Eligible");
    }
    else{
        printf("Eligible");
    }
    return 0;
}



#include <stdio.h>

int reverse(int num) {
    int rev = 0;
    while (num > 0) {
        rev = rev * 10 + (num % 10);
        num /= 10;
    }
    return rev;
}

int isPalindrome(int num) {
    return num == reverse(num);
}

int main() {
    int num, rev, sum;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (1) {
        rev = reverse(num);
        sum = num + rev;
        printf("%d + %d = %d\n", num, rev, sum);

        if (isPalindrome(sum)) {
            break;
        }
        num = sum; // Continue with the new sum
    }

    return 0;
}


#include <stdio.h>
#include <math.h>
#include <ctype.h>
int main()
{
    float deg,rad,den;
    
    if(scanf("%f",&deg)==1){
        den = 3.14/180;
    rad = deg*den;
    printf("%.2f",rad);
    }
    else{
        printf("invalid input");
    }
    
    return 0;
}


#include <stdio.h>

int main() {
    int upp, low, sum = 0;
    scanf("%d %d", &low, &upp);

    if (low > upp || low<0 || upp<0) {
        printf("invalid input");
    } else {
        for (int i = low; i <= upp; i++) {
            if (i % 7 == 0) {
                sum = sum + i;
            }
        }
        printf("%d", sum);
    }

    return 0;
}


#include <stdio.h>

int main()
{
	int num,sum =0;
	scanf("%d",&num);

		for (int i = 1; i <= num;i++) {
		    if(i%2 == 0) {
			sum = sum+i;
		}
	}
	printf("%d",sum);
	return 0;
}


#include <stdio.h>

int main() {
    int c, sum = 0, rem;
    printf("Enter a number: ");
    scanf("%d", &c);

    while (c != 0) {
        rem = c % 10; 
        sum += rem;     
        c /= 10;        
    }

    printf("Sum of digits = %d\n", sum);
    if(sum%2 == 0){
        printf("even");
    }
    else{
        printf("odd");
    }
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <ctype.h> 

int main() {
    char num[100];
    scanf("%s", num);
    for (int i = 0; i < strlen(num); i++) {
        if (!isdigit(num[i])) {
            printf("Invalid input: Only digits are allowed.\n");
            return 1;
        }
    }
    
    for (int i = 0; i < strlen(num); i++) {
        if (num[i] == '0') {
            num[i] = '1';
        }
    }

    printf("%s\n", num);
    return 0;
}


#include <stdio.h>

int main() {
    int arr[100];
    int num,sma;
    scanf("%d",&num);
    for (int i = 0; i < num; i++) {
        scanf("%d",&arr[i]);
        if(arr[i]<0){
            printf("invalid input");
            return  0;
        }
    }
    sma=arr[0];
    for (int i = 1; i <= num; i++) {
        if(arr[i]<sma){
            sma = arr[i];
        }
    }
    printf("small is %d",sma);
    return 0;
}


#include <stdio.h>

int main() {
    int num,sum=0;
    scanf("%d",&num);
    if(num<1){
        printf("invalid input");
    }
    else{
    for (int i = 1; i <= num; i++) {
        if(i%2!=0){
            sum = sum+i;
        }
    }
        printf("%d",sum);
    }
    return 0;
}



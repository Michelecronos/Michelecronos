#include<stdio.h>
int main(void){
  int a,b;
  int operation;
    printf("GradeA,perform basic operation between two numbers at your choice\n");
  printf("Enter an integer a:");
  scanf("%d", &a);
  printf("\nEnter an integer b:");
  scanf("%d", &b);
  printf("Press 1 for addition\nPress 2 for division\nPress 3 for "
         "multiplication\nPress 4 for subtraction\n");
  scanf("%d", &operation);

  if (operation == 1) {
    printf("%d + %d = %d", a, b, a + b);
  } else if (operation == 2) {
    printf("%d / %d = %d", a, b, a / b);
  } else if (operation == 3) {
    printf("%d * %d = %d", a, b, a * b);
  } else if (operation == 4)
    printf("%d - %d = %d", a, b, a - b);
  else
    printf("Please enter 1 to 4 only.");
}
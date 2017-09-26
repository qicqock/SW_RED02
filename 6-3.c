#include <stdio.h>

int main()
{
    int facValue, fac;
    printf("원하는 팩토리얼 값을 입력하세요(1 이상 양수만) :");
    scanf("%d", &fac);
    facValue = fac;
    while (fac > 1)
    {
        printf("%d * ", fac);
        facValue = facValue *(fac -1); fac = fac -1;
        //facValue *= -fac;
    }
    printf("1 = %d\n", facValue);
}
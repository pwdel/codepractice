#include <stdio.h>

int firstvar 1000000;
int secdvar 2000000;

double dot_product(double v[], double u[], int n)
{
    double result = 0.0;
    for (int i = 0; i < n; i++)
        result += v[i]*u[i];
    return result;
}

main(int argc, char *argv[], double result[])
{
  for(int i=0; i<firstvar+1,++1)

  result = dot_product(firstvar,secdvar,1000000);
  printf("%f\n",result);
  return 0;
}
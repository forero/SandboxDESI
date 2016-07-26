#include <stdio.h>

int main(void){
  int FLAG0 = 1<<0;
  int FLAG1 = 1<<1;
  int FLAG2 = 1<<2;
  int FLAG3 = 1<<3;

  int NO_FLAGS = 0;
  int ALL_FLAGS = FLAG0 | FLAG1 | FLAG2 | FLAG3;
  
  fprintf(stdout, "%d\n", FLAG0);
  fprintf(stdout, "%d\n", FLAG1);
  fprintf(stdout, "%d\n", FLAG2);
  fprintf(stdout, "%d\n", FLAG3);

  int mask = FLAG1 | FLAG2;

  int flag = FLAG2 | FLAG3;
  // checks if there is some overlap
  if((mask & flag)){
    fprintf(stdout, "mask has FLAG %d\n", flag);
  }else{
    fprintf(stdout, "mask does not have FLAG %d\n", flag);
  }

  // checks for strict overlap
  if((mask & flag)==flag){
    fprintf(stdout, "mask has FLAG %d\n", flag);
  }else{
    fprintf(stdout, "mask does not have FLAG %d\n", flag);
  }

  return 0;
  }

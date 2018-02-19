#include <stdio.h>
#include <stdlib.h>
int k=0;
void sort(unsigned int *num,unsigned int num_len,unsigned int *index){
  int i=0,j=0,buf=0;
  for (i=0;i<num_len-1;i++){
    for (j=i+1;j<num_len;j++){
      if (num[i] > num[j]){
        buf=num[i];
        num[i]=num[j];
        num[j]=buf;
        buf=index[i];
        index[i]=index[j];
        index[j]=buf;
      }
    }
  }
}

int binSearch (unsigned int *num,unsigned int num_len,int t){
  int bottom=0,ceiling=num_len-1,mid;
    while (bottom <= ceiling){
    k+=1;
        mid = (bottom + ceiling) / 2;
        if (num[mid] == t)
        {
            return mid;
        }
        else if (num[mid] > t)
        {
            ceiling = mid - 1;
        }
        else if (num[mid] < t)
        {
            bottom = mid + 1;
        }
    }
return -1*mid;
}
int main(){
  unsigned int num[]={0, 27, 27, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 2};
  int num_len=sizeof(num)/sizeof(int),target=0 ,i=0,j=0;
  unsigned char exit_for=0;
  unsigned int *index = malloc(num_len*sizeof(int));
  for(i=0;i<num_len;i++){index[i]=i;}
  sort(num,num_len,index);
  int z=0;
  printf("Enter the target number which you are searching for: ");
  scanf("%d", &target);


for ( z=0; z<1;  z++) {
  if ( target < num[num_len -1] ) {
    i=binSearch(num,i,target);
    num_len=( i < 0)?i *-1:i+1;
  } 
  for (i=num_len-1;i>0 && exit_for==0;i--){
     if( num[0] > target) break;
    if(num[i]>target) continue;
    //resolving quiz
    j=binSearch(num,i,target-num[i]);
    if ((j > -1) && target-num[i]==num[j]){
      printf("index[%d]=%d, index[%d]=%d\n",index[i],num[i],index[j],num[j]); exit_for=1;break;
    }
  }
  exit_for=0;
}
  free(index);
  printf("search iteration:%d\n",k);
return 0;
}

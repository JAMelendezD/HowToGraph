#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>


int f(int i, int j)
{
	return(i+101*j);
}

void copyT(float *inicio, float*fin, int len){
  	int i;
	int j;
  	for(j=0;j<len;j++)
	{
		for(i=0;i<len;i++)
		{
    		fin[f(i,j)] = inicio[f(i,j)];
		}
	}
}

void copy(float *inicio, float*fin, int len){
  	int i;
  	for(i=0;i<len;i++)
	{
    		fin[i] = inicio[i];
	}
}


int main()
{
	FILE *in;
	int NT;
	NT = 101;
	int i,j,t,N,ta;
	float dx,dt,v,r,L,pi;
	ta = 100000;
	N = 129;
	float *ftambor = malloc(NT*NT*sizeof(float)); 
	float *futT = malloc(NT*NT*sizeof(float)); 
	float *pasT = malloc(NT*NT*sizeof(float)); 
	float *preT = malloc(NT*NT*sizeof(float)); 
	int k;
	float dxy, dtT, LT,rT;
	dtT = 0.00001;
	LT = 0.5;
	v = 250.0;
	v = 250;
	dt = 0.00001;

	scanf("%d",&t);

	dt = 0.00001;
	in = fopen("./data/cond_ini_tambor.dat", "r");
	for(j = 0 ; j<NT; j++)
	{
		for(i = 0; i<NT; i++)
		{
			fscanf(in,"%f\n",&ftambor[f(i,j)]);
		}
	}
	fclose(in);


	dxy = LT/NT;
	rT = v*dtT/dxy;
	
	for(j = 1; j<NT-1; j++)
	{
		for(i = 1; i<NT-1; i++)
		{
		futT[f(i,j)] = ftambor[f(i,j)] + (rT*rT/2.0) * (ftambor[f(i+1,j)] - 4.0 * ftambor[f(i,j)] +ftambor[f(i-1,j)] +ftambor[f(i,j+1)] + ftambor[f(i,j-1)]);
		}
	}		

	copyT(ftambor, pasT, NT);
	copyT(futT, preT, NT);

	for(k = 0 ; k<t; k++)
	{
		for(j = 1; j<NT-1; j++)
		{
			for(i = 1; i<NT-1; i++)
			{
				futT[f(i,j)] = (2.0*(1.0-2*rT*rT))*preT[f(i,j)] - pasT[f(i,j)] + (rT*rT)*(preT[f(i+1,j)] +preT[f(i,j+1)] + preT[f(i-1,j)] +  preT[f(i,j-1)]);
			}
		}		
		copyT(preT, pasT, NT);
		copyT(futT, preT, NT);	
		
	}


	in = fopen("data2.txt", "w");

	for(j = 0 ; j<NT; j++)
	{
		for(i = 0; i<NT; i++)
		{

			fprintf(in, "%f\n", preT[f(i,j)]);
		}
	}
	fclose(in);

	free(ftambor);
	free(futT);
	free(pasT);
	free(preT);
 	return 0;
}


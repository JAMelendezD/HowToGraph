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
	int i,j,t,N,ta;
	ta = 100000;
	N = 129;
	float dx,dt,v,r,L,pi;
	float *f1 = malloc(N*sizeof(float)); 
	float *f2 = malloc(N*sizeof(float));
	float *u_p1 = malloc(N*sizeof(float)); 
	float *u_pas1 = malloc(N*sizeof(float)); 
	float *u_f1 = malloc(N*sizeof(float));
	float *u_p2 = malloc(N*sizeof(float)); 
	float *u_pas2 = malloc(N*sizeof(float)); 
	float *u_f2 = malloc(N*sizeof(float)); 
	float *x = malloc(N*sizeof(float)); 
	float *A = malloc(ta*sizeof(float)); 
	  
	

	L = 0.64;
	v = 250;
	pi = 3.1415;

	scanf("%d",&t);

	dt = 0.00001;

	in = fopen("./data/cond_ini_cuerda.dat", "r");
	for(i = 0; i< N; i++)
	{
		fscanf(in,"%f %f" , &x[i] , &f1[i]);
	}
	fclose(in);

	for(i = 0; i<N; i++)
	{
		f2[i] = 0;
	}

	dx = x[1] - x[0];	
	r = v*(dt/dx);

	for(i = 1; i<N-1; i++)
	{
		u_f1[i] = f1[i] + (r*r/2.0) * (f1[i+1] - 2.0 * f1[i] + f1[i-1]);
		u_f2[i] = f2[i] + (r*r/2.0) * (f2[i+1] - 2.0 * f2[i] + f2[i-1]);
	}

	f1[0] = 0.0; 
	f1[N-1] = 0.0;
	u_f1[0] = 0.0;
	u_f1[N-1] = 0.0;
	
	f2[0] = 0.0; 
	f2[N-1] = 0.0;
	u_f2[0] = 0.0;
	u_f2[N-1] = 0.0;
		
	copy(f1, u_pas1, N);
	copy(u_f1, u_p1, N);

	copy(f2, u_pas2, N);
	copy(u_f2, u_p2, N);

	for(j = 0 ; j<t; j++)
	{
		u_f2[0] = sin(2*pi*v*dt*j/L);
		for(i = 1; i<N-1; i++)
		{
			u_f1[i] = (2.0*(1.0-r*r))*u_p1[i] - u_pas1[i] + (r*r)*(u_p1[i+1] +  u_p1[i-1]);
			u_f2[i] = (2.0*(1.0-r*r))*u_p2[i] - u_pas2[i] + (r*r)*(u_p2[i+1] +  u_p2[i-1]);
		}
		A[j] = u_p1[65];
		copy(u_p1, u_pas1, N);
		copy(u_f1, u_p1, N);
		

		copy(u_p2, u_pas2, N);
		copy(u_f2, u_p2, N);
		
	}

	in = fopen("data1.txt", "w");
	for(i = 0; i< N; i++)
	{
		fprintf(in, "%f,%f,%f\n", x[i],u_p1[i],u_p2[i]);
	}
	fclose(in);

	free(f1);
	free(f2);
	free(u_p1);
	free(u_p2);
	free(u_pas1);
	free(u_pas2);
	free(u_f1);
	free(u_f2);
	free(x);
	free(A);


 	return 0;
}



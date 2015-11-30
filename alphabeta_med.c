#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int g_depth=5;
//int count=0;
struct Node
	{
			int val;
			struct Node * child[81];
	};
int *moves;
char movea,moveb,movec,moved;
char check_winner(char [][3]);
char check_win_main(char [][3]);
int * check_empty(char [3][3][3][3], char [][3],int, int);
int max(int,int);
int min(int,int);
int scoreline (int com, int opp);
int value (char main_matrix[3][3], char matrix[3][3][3][3]);
void printboard(char matrix[3][3][3][3])
	{
		int i,k,j,l;
		for(i=0;i<3;i++)
        {
                for(j=0;j<3;j++)
                {
                        for(k=0;k<3;k++)
                        {
                                for(l=0;l<3;l++)
                                {
                                        printf("%c",matrix[i][k][j][l]);
                                }
                        }
                        printf("\n");
                }
        }
	}
int scoreline (int com, int opp)
{
	if (com == 3)
		return 100;
	else if (opp == 3)
		return -100;
	else if (com == 2 && opp == 0)
		return 10;
	else if (com == 0 && opp == 2)
		return -10;
	else if (com == 1 && opp == 0)
		return 1;
	else if (com == 0 && opp == 1)
		return -1;
	else
		return 0;
}
int getPower(int power, int val)
{
	int ans=0;
	if(!power)
		return ans;
	else
		ans = val;
	if(power==1)
		return ans;
	else if(power==2)
		return ans*10;
	else
		return ans*100;
}
int d=1;
int evalString(char* string, int val)
{
	if(!(strcmp(string, "x--") && strcmp(string, "-x-") && strcmp(string, "--x")))
		return d*val;
	if(!(strcmp(string, "o--") && strcmp(string, "-o-") && strcmp(string, "--o")))
		return -1*d*val;
	if(!(strcmp(string, "xx-") && strcmp(string, "-xx") && strcmp(string, "x-x")))
		return d*val*10;
	if(!(strcmp(string, "oo-") && strcmp(string, "-oo") && strcmp(string, "o-o")))
		return -1*d*val*10;
	if(!strcmp(string, "xxx"))
		return d*100*val;
	if(!strcmp(string, "ooo"))
		return -1*d*100*val;
	return 0;
}
int getValue(char tmp_matrix[3][3], int val)
{
	int ans=0;
	int count,count1;
	int i,j;
	char string[4];
	string[3]='\0';
	for(i=0;i<3;i++)
	{
		for(j=0;j<3;j++)
		{
			if(tmp_matrix[i][j]=='x' || tmp_matrix[i][j]=='o')
				string[j]=tmp_matrix[i][j];
			else
				string[j]='-';
			/*if(tmp_matrix[i][j]=='x')
			  count++;
			  else if(tmp_matrix[i][j]=='o')
			  count1++;*/
		}
		string[3]='\0';
		ans+= evalString(string,val);
	}
	for(j=0;j<3;j++)
	{
		for(i=0;i<3;i++)
		{
			if(tmp_matrix[i][j]=='x' || tmp_matrix[i][j]=='o')
				string[i]=tmp_matrix[i][j];
			else
				string[i]='-';
		}
		string[3]='\0';
		ans+= evalString(string,val);
	}
	for(i=0,j=0;i<3;i++,j++)
	{
		if(tmp_matrix[i][j]=='x' || tmp_matrix[i][j]=='o')
			string[j]=tmp_matrix[i][j];
		else
			string[j]='-';
	}
	string[3]='\0';
	ans+= evalString(string,val);
	for(i=2,j=0;i>=0;i--,j++)
	{
		if(tmp_matrix[i][j]=='x' || tmp_matrix[i][j]=='o')
			string[j]=tmp_matrix[i][j];
		else
			string[j]='-';
	}
	string[3]='\0';
	ans+= evalString(string,val);
	return ans;
}
int value (char main_matrix[3][3], char matrix[3][3][3][3])
{
	int i,j,k;
	int score = 0;
	score = getValue(main_matrix, 100000);
	for(i=0;i<3;i++)
		for(j=0;j<3;j++)
		{
			//if(main_matrix[i][j] == 's')
			score += getValue(matrix[i][j], 1);
		}	
	return score;
	/*int i, j, k, com = 0, opp = 0, score = 0,flag = 0;

	for (i = 0; i < 3; i++)
	{
		com = 0, opp = 0, flag = 0;
		for (j = 0; j < 3; j++)
		{
			if (matrix[i][2-i] == 't')
                        {flag=1;
                        break;}

			if (matrix[i][j] == 'x')
				com++;
			else if (matrix[i][j] == 'o')

				opp++;
		}
		if(flag == 0)
		score = score + scoreline(com, opp);

	
	}
	for (j = 0; j < 3; j++)
	{
		com = 0, opp = 0, flag = 0;
		for (i = 0; i < 3; i++)
		{
			if (matrix[i][2-i] == 't')
                        {flag=1;
                        break;}

			if (matrix[i][j] == 'x')
				com++;
			else if (matrix[i][j] == 'o')
				opp++;
		}

		if (flag == 0)
		score = score + scoreline(com, opp);	
	}
	
	com = 0, opp = 0, flag = 0;
	for (i = 0; i < 3; i++)
	{
		if (matrix[i][2-i] == 't')
                        {
				flag=1;
                        	break;
			}

		if (matrix[i][i] == 'x')
			com++;
		else if (matrix[i][i] == 'o')
			opp++;
	}

	if (flag == 0)
	score = score + scoreline(com, opp);

	com = 0, opp = 0, flag = 0;
	for (i = 0; i < 3; i++)
	{
		if (matrix[i][2-i] == 't')
			{flag=1;
			break;}
		if (matrix[i][2-i] == 'x')
			com++;
		else if (matrix[i][2-i] == 'o')
			opp++;
	}

	if (flag == 0)
	score = score + scoreline(com, opp);
//	printf("score = %d\n",score);	
	return score;*/
}


int max(int a,int b)
	{
		if(a>b)
			return a;
		else
			return b;
	}
int min(int a,int b)
	{
		if(a<b)
			return a;
		else
			return b;
	}
void printmatrix2d(char matrix[3][3])
	{
		int i,j;
		for(i=0;i<3;i++)
			{
			for(j=0;j<3;j++)
			printf("%c",matrix[i][j]);
			printf("\n");
			}
	}

int * check_empty(char matrix[3][3][3][3],char main_matrix[3][3], int a, int b)
        {
                int i,j,k,l,count=0;
                moves = (int *) malloc(sizeof(int)*81);
		if(a==-1&&b==-1)
                {
                for(i=0;i<3;i++)
                        {
                        for(j=0;j<3;j++)
                                {
                                        for(k=0;k<3;k++)
                                                {
                                                        for(l=0;l<3;l++)
                                                                {

                                                                        if(matrix[i][j][k][l]=='s'&&main_matrix[i][j]=='s')
                                                                                {
                                                                                        moves[count]=i*1000+j*100+k*10+l;
                                                                                //      printf("%d\n",moves[count]);
											count++;
                                                                                }
                                                                }
                                                }
                                }
                        }
                
                }
                else
                {       for(i=0;i<3;i++)
                        {
                        for(j=0;j<3;j++)
                                {
                                        if(matrix[a][b][i][j]=='s')
                                        {
                                                if(main_matrix[a][b]!='s')
							{printf("What the Hell\n");
								getchar();
							}
						moves[count]=a*1000+b*100+i*10+j;
                                                count++;
                                        }

                                }
                        }
		
                }
		moves[count]=-1;
                return moves;
        }

char check_winner(char matrix[][3])
{
        if(matrix[0][0]==matrix[0][1]&&matrix[0][1]==matrix[0][2]&&matrix[0][2]!='s')
                return matrix[0][0];
        if(matrix[1][0]==matrix[1][1]&&matrix[1][1]==matrix[1][2]&&matrix[1][2]!='s')
                return matrix[1][0];
        if(matrix[2][0]==matrix[2][1]&&matrix[2][1]==matrix[2][2]&&matrix[2][2]!='s')
                return matrix[2][0];

        if(matrix[0][0]==matrix[1][0]&&matrix[1][0]==matrix[2][0]&&matrix[2][0]!='s')
                return matrix[0][0];
        if(matrix[0][1]==matrix[1][1]&&matrix[1][1]==matrix[2][1]&&matrix[2][1]!='s')
                return matrix[0][1];
        if(matrix[0][2]==matrix[1][2]&&matrix[1][2]==matrix[2][2]&&matrix[2][2]!='s')
                return matrix[0][2];

        if(matrix[0][0]==matrix[1][1]&&matrix[1][1]==matrix[2][2]&&matrix[2][2]!='s')
                return matrix[0][0];
        if(matrix[0][2]==matrix[1][1]&&matrix[1][1]==matrix[2][0]&&matrix[2][0]!='s')
                return matrix[0][2];

        int x,y;
        for(x=0;x<3;x++)
        {
                for(y=0;y<3;y++)
                {
                        if(matrix[x][y]=='s')
                                return 's';
                }
        }

        return 't';
}

char check_win_main(char main_matrix[][3])
{
        char copy_main[3][3];

        int x,y;
        for(x=0;x<3;x++)
        {
                for(y=0;y<3;y++)
                {
                        if(main_matrix[x][y]=='t')
                        {
                                copy_main[x][y]='s';
                        }

                        else
                        {
                                copy_main[x][y]=main_matrix[x][y];
                        }
                }
        }

        if(check_winner(copy_main)=='o')
        {
                return 'o';
        }
        if(check_winner(copy_main)=='x')
        {
                return 'x';
        }

        int flag=0;

        for(x=0;x<3;x++)
        {
                for(y=0;y<3;y++)
                {
                        if(main_matrix[x][y]=='s')
                        {
                                flag=1;
                                break;
                        }
                }
        }

        if(flag==0)
        {
                return 't';
        }

        return 's';
}
int minimax(struct Node * present,int alpha, int beta, int depth, char turn,char matrix[3][3][3][3], char main_matrix[3][3],char w,char x, char y, char z)
        {
		//count++;
	//	printf("depth=%d\n",depth);
		int *empty,i,p,j,f,l,temp;
                char a,b,c,d,copy[3][3][3][3],temp2,copy_main[3][3];
                for(i=0;i<81;i++)
                        present->child[i]=NULL;

                if(depth==0)
                {
                	if(w==-1&&x==-1)
                                w=x=0;
			main_matrix[w][x]=check_winner(matrix[w][x]);	
			temp2=check_win_main(main_matrix);
			if(temp2=='x')
				return 100000;
			else if(temp2=='o')
				return -100000;
			else if(temp2=='t')
				return 0;
			else
				return value(main_matrix, matrix);
                }
                else if(w!=-1&&x!=-1)
			{	
					main_matrix[w][x]=check_winner(matrix[w][x]);
                                        if(main_matrix[w][x]!='s')
					{
					temp2=check_win_main(main_matrix);
					if(temp2=='x')
                                		return 100000;
                        		else if(temp2=='o')
                                		return -100000;
                        		else if(temp2=='t')
                                		return 0;
					else
						return value(main_matrix, matrix);
					}
                 	}
	//	printmatrix2d(main_matrix);
		if(main_matrix[y][z]!='s')
			y=z=-1;
		empty=check_empty(matrix,main_matrix,y,z);
		if(turn=='x')
		{	
			for(i=0;empty[i]!=-1&&i<81;i++)
			{
				a=empty[i]/1000;
				b=empty[i]/100 - a*10;
				c=empty[i]/10 - a*100 - b*10;
				d=empty[i]-a*1000 - b*100 - c*10;
				for(p=0;p<3;p++)
                        	{
                        	for(j=0;j<3;j++)
                                {
                                        for(f=0;f<3;f++)
                                                {
                                                        for(l=0;l<3;l++)
                                                                {
                                                                	copy[p][j][f][l]=matrix[p][j][f][l]; 
                                                                }
                                                }
                                }
                       		}
				for(f=0;f<3;f++)
                                                {
                                                        for(l=0;l<3;l++)
                                                                {
                                                                        copy_main[f][l]=main_matrix[f][l];
                                                                }
                                                }
				present->child[i]=(struct Node *) malloc(sizeof(struct Node));
				copy[a][b][c][d]=turn;
                                temp=alpha;
			//	printmatrix2d(main_matrix);
				alpha=max(alpha,minimax(present->child[i],alpha,beta,depth-1,'o',copy,copy_main,a,b,c,d));
			//	if(alpha==100)
			//		{
			//			printf("depth = %d \n i=%d",depth,i);
			//			printf("%d %d %d %d\n",a,b,c,d);
						//printboard(copy);
						//printmatrix2d(main_matrix);
						//getchar();
		//			}
		//		printf("beta=%d alpha=%d i=%d\n",beta,alpha,i);
				if(depth==g_depth)
                                {       //printf("beta=%d alpha=%d i=%d\n",beta,alpha,i);
					//printf("beta= %d i=%d %d %d %d %d\n",beta,i,a,b,c,d);
					if(i==0)
                                        {
                                                movea=a;
                                                moveb=b;
                                                movec=c;
                                                moved=d;
                                        }
                                        if(temp!=alpha)
                                        {
                                                movea=a;
                                                moveb=b;
                                                movec=c;
                                                moved=d;
                        		   //     printf("%d %d %d %d\n",a,b,c,d);
                                        }
                                }
                                
				if(beta<=alpha)
					break;
			}
		//	printf("beta=%d alpha=%d depth=%d\n",beta,alpha,depth);
		//	printmatrix2d(main_matrix);
		//	getchar();
			present->val=alpha;
			return alpha;
		}
		else
		{
			for(i=0;empty[i]!=-1&&i<81;i++)
                        {
                                a=empty[i]/1000;
                                b=empty[i]/100 - a*10;
                                c=empty[i]/10 - a*100 - b*10;
                                d=empty[i]-a*1000 - b*100 - c*10;
                                for(p=0;p<3;p++)
                                {
                                for(j=0;j<3;j++)
                                {
                                        for(f=0;f<3;f++)
                                                {
                                                        for(l=0;l<3;l++)
                                                                {
                                                                        copy[p][j][f][l]=matrix[p][j][f][l];
                                                                }
                                                }
                                }
                                }
				present->child[i]=(struct Node *) malloc(sizeof(struct Node));
                                copy[a][b][c][d]=turn;
				temp=beta;
				for(f=0;f<3;f++)
                                                {
                                                        for(l=0;l<3;l++)
                                                                {
                                                                        copy_main[f][l]=main_matrix[f][l];
                                                                }
                                                }
				beta=min(beta,minimax(present->child[i],alpha,beta,depth-1,'x',copy,copy_main,a,b,c,d));
				if(depth==g_depth)
                                {       //printf("beta= %d i=%d %d %d %d %d\n",beta,i,a,b,c,d);
					if(i==0)
                                        {
                                                movea=a;
                                                moveb=b;
                                                movec=c;
                                                moved=d;
                                        }
                                        if(temp!=beta)
                                        {
                                                movea=a;
                                                moveb=b;
                                                movec=c;
                                                moved=d;
                                      
                                        }
                                }
                                
				if(beta<=alpha)
                                        break;
                        }
		//	printf("beta=%d alpha=%d depth=%d\n",beta,alpha,depth);
                //        printmatrix2d(main_matrix);
                  //      getchar();

			present->val=beta;
                        return beta;

		}	
 }
int main()
	{
	char input[] = "./data/matrixforai.txt";
	char output[] = "./data/aimove.txt";			// Location for the I/O files

	FILE *finput = fopen(input, "r");
	FILE *foutput = fopen(output, "w+");

	char matrix[3][3][3][3];
	char main_matrix[3][3];
	int iplay,jplay,move;
	char temp,turn;
	fscanf(finput, "%c%c",&turn,&temp);
	if(turn=='O')
                turn='o';
        else
                turn='x'; 
	fscanf(finput, "%d %d",&iplay,&jplay);
	fscanf(finput, "%c",&temp);

	int i,j,k,l,a,b,c,d;
	for(i=0;i<3;i++)
        {
                for(j=0;j<3;j++)
                {
                        for(k=0;k<3;k++)
                        {
                                for(l=0;l<3;l++)
                                {
                                        fscanf(finput, "%c",&matrix[i][k][j][l]);
                                        if(matrix[i][k][j][l]=='X')matrix[i][k][j][l]='x';
                                        else if(matrix[i][k][j][l]=='O')matrix[i][k][j][l]='o';
                                        else if(matrix[i][k][j][l]=='-')matrix[i][k][j][l]='s';
                                }
                        }
                        fscanf(finput, "%c",&temp);
                }
        }
        for (i=0;i<3;i++)
        {
                for(j=0;j<3;j++)
                {
                        main_matrix[i][j]=check_winner(matrix[i][j]);
                }
        }
	struct Node * root= (struct Node *) malloc(sizeof(struct Node));
	move=minimax(root,-101,101,g_depth,turn,matrix,main_matrix,-1,-1,iplay,jplay);
	fprintf(foutput, "%d %d %d %d\n",movea,moveb,movec,moved);

	fclose(finput);
	fclose(foutput);

        return 0;
	}

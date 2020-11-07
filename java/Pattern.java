import java.io.*;
import java.util.*;

public class Pattern
{
  public static void main(String Args[])
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter value of integer n: ");
    int n = sc.nextInt();

    // Pattern 1
    for(int i = 1; i <= n; i++)
    {
      for(int j = 1;j<=n-i;j++)
      {
        System.out.print(" ");
      }
      for(int j = 1; j<=2*i-1; j++)
      {
        if(i==n)
          System.out.print("*");
        else
          if(j==1 || j == 2*i-1)
            System.out.print("*");
          else
            System.out.print(" ");
      }
      System.out.println();
    }
    
    System.out.println();
    // Pattern 2
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=n;j++)
      {
        System.out.print("*");
      }
      System.out.println();
    }
    
    System.out.println();
    // Pattern 3
    for(int i=1; i<=n; i++)
    {
      for(int j=1; j<=n; j++)
      {
        if(i==1 || i==n)
          System.out.print("*");
        else
          if(j==1 || j==n)
            System.out.print("*");
          else
            System.out.print(" ");
      }
      System.out.println();
    }

    System.out.println();
    // Pattern 4
    for(int i=1; i<=n; i++)
    {
      for(int j=1; j<=n; j++)
      {
        if(i==1 || i==n)
          System.out.print("*");
        else
          if(j==1 || j==n)
            System.out.print(" ");
          else
            System.out.print("*");
      }
      System.out.println();
    }
  }
}
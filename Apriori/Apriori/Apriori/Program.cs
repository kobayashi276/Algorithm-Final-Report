// See https://aka.ms/new-console-template for more information
using System.Collections;
using System.Linq;

//Console.WriteLine("Hello, World!");

class Apriori
{
    static List<List<string>> Apriori_Function(List<List<string>> D,int minsup)
    {
        List<List<string>> F = new List<List<string>>();
        List<string> elements = new List<string>();

        for (int i = 0; i < D.Count; i++)
        {
            for (int j =0; j < D[i].Count; j++)
            {
                if (!elements.Contains(D[i][j]))
                {
                    elements.Add(D[i][j]);

                }
            }
        }
        elements.Sort();
        for (int i = 0; i < elements.Count; i++)
        {
            F.Add(new List<String> { elements[i]});
        }
        List<List<string>> L = new List<List<string>>();
        List<List<string>> preL = L;
        while (F.Count !=0)
        {
            preL = L;
            L = new List<List<string>>();
            //Console.WriteLine(F.Count);
            for (int i = 0; i < F.Count; i++)
            {
                int count = 0;
                //Console.WriteLine(string.Join(",", F[i]));
                for (int j = 0; j < D.Count; j++)
                {
                    //Console.WriteLine(issubset(D[j], F[i]));
                    if (issubset(D[j], F[i]))
                    {
                        count++;
                    }
                }
               // Console.WriteLine(count);
                if (count >= minsup){
                    L.Add( F[i] );
                }
            }
            //Console.WriteLine("L count: " + L.Count);
            if (L.Count == 0)
            {
                break;
            }
            else F = Generate_Set(L, elements);
            //Console.WriteLine("preLL count: "+preL.Count);
        }
        return preL;
        //Console.WriteLine(String.Join(",", F[4]));
    }

    static List<List<string>> Generate_Set(List<List<string>> a, List<string> b)
    {
        if (a.Count==0 || b.Count == 0)
        {
            return new List<List<string>>();
        }
       // Console.WriteLine(a.Count + " " + b.Count);
        List<List<string>> result = new List<List<string>>();
        for (int i = 0; i < a.Count; i++)
        {
            //if (b.Contains(a[i][-1]))
            //{
            //Console.WriteLine(a[i][0]);
                for (int j = 1+ b.IndexOf(a[i][a[i].Count-1]);j < b.Count; j++)
                {
                     result.Add(concat(a[i], b[j]));
                }
            //}
        }
        return result;
    }

    static bool issubset(List<string> a, List<string> b)
    {
        for (int i = 0; i < b.Count; i++)
        {
            if (!a.Contains(b[i]))
            {
                return false;
            }
        }
        return true;
    }

    static List<string> concat(List<string> a, string b)
    {
        List<string> result = new List<string>();
        for (int i=0; i < a.Count; i++)
        {
            result.Add(a[i]);
        }
        result.Add(b);
        return result;
    }

    static void Main(string[] args)
    {
        List<List<string>> D = new List<List<string>>();
        D.Add(new List<string> { "I1", "I2", "I5" });
        D.Add(new List<string> { "I2", "I4" });
        D.Add(new List<string> { "I2", "I3" });
        D.Add(new List<string> { "I1", "I2","I4" });
        D.Add(new List<string> { "I1", "I3"});
        D.Add(new List<string> { "I2", "I3"});
        D.Add(new List<string> { "I1", "I3"});
        D.Add(new List<string> { "I1","I2", "I3","I5"});
        D.Add(new List<string> { "I1","I2", "I3"});
        List<List<string>> res = Apriori_Function(D, 2);
        for (int i=0; i < res.Count; i++)
        {
            Console.WriteLine(String.Join(",", res[i]));
        }
    }
}
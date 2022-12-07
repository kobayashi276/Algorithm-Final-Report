// See https://aka.ms/new-console-template for more information
class Apriori_TID
{
    static List<List<string>> Apriori_TID_Function(List<List<string>> D,int minsup)
    {
        List<List<string>> L = new List<List<string>>();
        List<List<string>> preL = L;
        while (D.Count != 0)
        {
            preL = L;
            L = new List<List<string>>();
            for (int i = 0; i < D.Count; i++)
            {
                if (D[i].Count >= minsup && !contains(L, D[i]))
                {
                    //Console.WriteLine("Added to L");
                    L.Add(D[i]);
                }
            }

            if (L.Count == 0)
                {
                    break;
                }
            D = generate_intersection(L);
            //for (int i = 0; i < L.Count; i++)
            //{
            //    Console.WriteLine(string.Join(",", L[i]));
            //    Console.WriteLine();
            //}
            
        }
        return preL;
    }

    static List<List<string>> generate_intersection(List<List<string>> a)
    {
        List<List<string>> result = new List<List<string>>();
        for (int i = 0; i < a.Count-1; i++)
        {
            for (int j = i + 1; j < a.Count; j++)
            {
                List<string> tmp =  intersection(a[i], a[j]);
                tmp.Sort();
                result.Add(tmp);
            }
        }
        return result;
    }

    static List<string> intersection(List<string> a, List<string> b)
    {
        List<string> result = new List<string>();
        for (int i = 0; i < a.Count; i++)
        {
            if (b.Contains(a[i]))
            {
                result.Add(a[i]);
            }
        }
        return result;
    }

    static bool contains(List<List<string>> a, List<string> b)
    {
        bool result = false;
        for (int i = 0; i < a.Count; i++)
        {
            int count = 0;
            for (int j = 0; j < b.Count; j++)
            {
                if (a[i].Contains(b[j]))
                {
                    count++;
                }
            }
            if (count== a[i].Count)
            {
                result = true;
            }
        }
        return result;
    }

    static void Main(string[] args)
    {
        List<List<string>> D = new List<List<string>>();
        D.Add(new List<string> { "T1", "T4", "T5", "T7", "T8", "T9" });
        D.Add(new List<string> { "T1", "T2", "T3", "T4", "T6", "T8", "T9" });
        D.Add(new List<string> { "T3", "T5", "T6", "T7", "T8", "T9" });
        D.Add(new List<string> { "T2", "T4" });
        D.Add(new List<string> { "T1", "T8" });

        //Console.WriteLine(contains(D, new List<string> { "T2", "T4" }));
        D = Apriori_TID_Function(D,2);
        for (int i=0; i<D.Count; i++)
        {
            Console.WriteLine(string.Join(",", D[i]));
        }
    }
}

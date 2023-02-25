# ��������

> ά��һ�����У����߽簴Ҫ���ƶ���
>
> �����ƶ�����������ʱ�ұ߽�right�����ƶ���Ԫ�ؼ�����У���������������߽�left�����ƶ���Ԫ���Ƴ����У���

#### [3. ���ظ��ַ�����Ӵ�](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

ʹ�����򼯺�����ʹ��find()����

``` c++
int lengthOfLongestSubstring(string s) {
    if(s.size() == 0) return 0;
    unordered_set<char> lookup;//ʹ�����򼯺�����
    int maxStr = 0;
    int left = 0;
    for(int i = 0; i < s.size(); ++i)
    {
        while (lookup.find(s[i]) != lookup.end())
        {
            lookup.erase(s[left]);//���һ�������
            ++left;
        }
        maxStr = max(maxStr,i-left+1);
        lookup.insert(s[i]);
    }
    return maxStr;
}
```

���������ʹ�������Ŷ�Ӧ�ַ�������

``` c++
int lengthOfLongestSubstring(string s) {
    int freq[128] = {0};//��������ַ�����������鿴��Ӧ����
    int left = 0, ans = 0;
    for(int j = 0; j < s.size(); ++j)
    {
        ++freq[s[j]];
        while(freq[s[j]]>1)
            --freq[s[left++]];//�ظ������һ���
        ans = max(ans,j-left+1);
    }
    return ans;
}
```



#### [567. �ַ���������](https://leetcode-cn.com/problems/permutation-in-string/)

``` c++
bool checkInclusion(string s1, string s2) {
    int n = s1.length(), m = s2.length();
    if (n > m)
    {
        return false;
    }
    vector<int> cnt1(26), cnt2(26);//����Ƚ�
    //�ɲ�ʹ������Ƚϣ���ͬһ��vector�Ͻ��в���
    for (int i = 0; i < n; ++i)
    {
        ++cnt1[s1[i] - 'a'];
        ++cnt2[s2[i] - 'a'];
    }
    if (cnt1 == cnt2)
    {
        return true;
    }
    for (int i = n; i < m; ++i)
    {
        ++cnt2[s2[i] - 'a'];
        --cnt2[s2[i - n] - 'a'];
        if (cnt1 == cnt2)
        {
            return true;
        }
    }
    return false;
}
```



#### [76. ��С�����Ӵ�](https://leetcode-cn.com/problems/minimum-window-substring/)



#### [30. �������е��ʵ��Ӵ�](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)



#### [209. ������С��������](https://leetcode-cn.com/problems/minimum-size-subarray-sum/)



#### [239. �����������ֵ](https://leetcode-cn.com/problems/sliding-window-maximum/)



#### [438. �ҵ��ַ�����������ĸ��λ��](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)




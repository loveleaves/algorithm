# 排序算法

## c++ function

std::sort()

## 基本排序算法

### 快速排序（Quicksort）

``` c++
void quick_sort(vector<int> &nums, int l, int r) {
    if (l + 1 >= r) {
    	return;
    }
    int first = l, last = r - 1, key = nums[first];
    while (first < last){
        while(first < last && nums[last] >= key) {
        	--last;
        }
        nums[first] = nums[last];
        while (first < last && nums[first] <= key) {
        	++first;
        }
        nums[last] = nums[first];
    }
    nums[first] = key;
    quick_sort(nums, l, first);
    quick_sort(nums, first + 1, r);
}
```

### 归并排序（Merge Sort）

``` c++
void merge_sort(vector<int> &nums, int l, int r, vector<int> &temp) {
    if (l + 1 >= r) {
    	return;
    }
    // divide
    int m = l + (r - l) / 2;
    merge_sort(nums, l, m, temp);
    merge_sort(nums, m, r, temp);
    // conquer
    int p = l, q = m, i = l;
    while (p < m || q < r) {
        if (q >= r || (p < m && nums[p] <= nums[q])) {
        	temp[i++] = nums[p++];
        } else {
        	temp[i++] = nums[q++];
        }
    }
    for (i = l; i < r; ++i) {
    	nums[i] = temp[i];
    }
}
```

### 插入排序（Insertion Sort）

``` c++
void insertion_sort(vector<int> &nums, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = i; j > 0 && nums[j] < nums[j-1]; --j) {
        	swap(nums[j], nums[j-1]);
        }
    }
}
```

### 冒泡排序（Bubble Sort）

``` c++
void bubble_sort(vector<int> &nums, int n) {
    bool swapped;
    for (int i = 1; i < n; ++i) {
        swapped = false;
        for (int j = 1; j < n - i + 1; ++j) {
            if (nums[j] < nums[j-1]) {
                swap(nums[j], nums[j-1]);
                swapped = true;
            }
        }
        if (!swapped) {
        	break;
        }
    }
}
```

### 选择排序（Selection Sort）

``` c++
void selection_sort(vector<int> &nums, int n) {
    int mid;
    for (int i = 0; i < n - 1; ++i) {
        mid = i;
        for (int j = i + 1; j < n; ++j) {
            if (nums[j] < nums[mid]) {
                mid = j;
            }
        }
        swap(nums[mid], nums[i]);
    }
}
```

**以上排序代码调用方法为**

``` c++
void sort() {
    vector<int> nums = {1,3,5,7,2,6,4,8,9,2,8,7,6,0,3,5,9,4,1,0};
    vector<int> temp(nums.size());
    sort(nums.begin(), nums.end());
    quick_sort(nums, 0, nums.size());
    merge_sort(nums, 0, nums.size(), temp);
    insertion_sort(nums, nums.size());
    bubble_sort(nums, nums.size());
    selection_sort(nums, nums.size());
}
```



## 快速选择

#### [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

> **基于快速排序的选择方法**, 一般用于求解k-th Element 问题。
>
> Time : O(n) ,   Space : O(1)

``` c++
int findKthLargest(vector<int>& nums, int k) {
    int l = 0, r = nums.size() - 1, target = nums.size() - k;
    while (l < r) {
        int mid = quickSelection(nums, l, r);
        if (mid == target) {
            return nums[mid];
        }
        if (mid < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return nums[l];
}
// 辅函数- 快速选择
int quickSelection(vector<int>& nums, int l, int r) {
    int i = l + 1, j = r;
    while (true) {
        while (i < r && nums[i] <= nums[l]) {
            ++i;
        }
        while (l < j && nums[j] >= nums[l]) {
            --j;
        }
        if (i >= j) {
            break;
        }
        swap(nums[i], nums[j]);
    }
    swap(nums[l], nums[j]);
    return j;
}
```

>  **基于堆排序的选择方法**
>
> 利用**大根堆**实现，在这道题中尤其要搞懂「建堆」、「调整」和「删除」的过程
>
> Time : O(n log n) ,  Space : O(log n)

``` c++
void maxHeapify(vector<int>& a, int i, int heapSize) {
    int l = i * 2 + 1, r = i * 2 + 2, largest = i;
    if (l < heapSize && a[l] > a[largest]) {
        largest = l;
    } 
    if (r < heapSize && a[r] > a[largest]) {
        largest = r;
    }
    if (largest != i) {
        swap(a[i], a[largest]);
        maxHeapify(a, largest, heapSize);
    }
}

void buildMaxHeap(vector<int>& a, int heapSize) {
    for (int i = heapSize / 2; i >= 0; --i) {
        maxHeapify(a, i, heapSize);
    } 
}

int findKthLargest(vector<int>& nums, int k) {
    int heapSize = nums.size();
    buildMaxHeap(nums, heapSize);
    for (int i = nums.size() - 1; i >= nums.size() - k + 1; --i) {
        swap(nums[0], nums[i]);
        --heapSize;
        maxHeapify(nums, 0, heapSize);
    }
    return nums[0];
}
```



## 桶排序

> 桶排序 : 为每个值设立一个桶，桶内记录这个值出现的次数（或其它属性），然后对桶进行排序

#### [347. 前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

``` c++
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> counts;
    int max_count = 0;
    for (const int & num : nums) {
        max_count = max(max_count, ++counts[num]); //记录每个元素出现的次数
    }
    vector<vector<int>> buckets(max_count + 1);
    for (const auto & p : counts) {//对桶按出现次数排序
        buckets[p.second].push_back(p.first);
    }
    vector<int> ans;
    for (int i = max_count; i >= 0 && ans.size() < k; --i) {
        for (const int & num : buckets[i]) {
            ans.push_back(num);
            if (ans.size() == k) {
                break;
            }
        }
    }
    return ans;
}
```



#### [451. 根据字符出现频率排序](https://leetcode-cn.com/problems/sort-characters-by-frequency/)

``` c++
string frequencySort(string s) {
    unordered_map<char, int> mp;
    int maxFreq = 0, length = s.size();
    for (auto &ch : s) {
        maxFreq = max(maxFreq, ++mp[ch]);
    }
    vector<string> buckets(maxFreq + 1);
    for (auto &[ch, num] : mp) {
        buckets[num].push_back(ch);
    }
    string ret;
    for (int i = maxFreq; i > 0; i--) {
        string &bucket = buckets[i];
        for (auto &ch : bucket) {
            for (int k = 0; k < i; k++) {
                ret.push_back(ch);
            }
        }
    }
    return ret;
}
```

#### [75. 颜色分类](https://leetcode-cn.com/problems/sort-colors/)

``` c++
//单指针，遍历两遍
void sortColors(vector<int>& nums) {
    int n = nums.size(), ptr = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == 0) {
            swap(nums[i], nums[ptr]);
            ++ptr;
        }
    }
    for (int i = ptr; i < n; ++i) {
        if (nums[i] == 1) {
            swap(nums[i], nums[ptr]);
            ++ptr;
        }
    }
}
//或双指针，遍历一遍
void sortColors(vector<int>& nums) {
    int n = nums.size(), l = 0, r = n-1;
    for (int i = 0; i <= r; ++i) {
        if (nums[i] == 0) {
            swap(nums[i], nums[l++]);
        } else if (nums[i] == 2 && i < r) {
            swap(nums[i--],nums[r--]); //r--是因为交换过来的数可能是1或2
        }
    }
}
```


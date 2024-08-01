# stats.py

class DataProcessor:
    def __init__(self, data_list):
        """初始化数据处理器，接收一个数据列表"""
        self.data_list = data_list
        self.value_counts = {}
        self.unique_values = []
        self.duplicate_values = []

    def process_data(self):
        """处理数据，统计不重复值和重复值"""
        # 统计每个值的出现次数
        for value in self.data_list:
            if value in self.value_counts:
                self.value_counts[value] += 1
            else:
                self.value_counts[value] = 1
        
        # 找出不重复值和重复值
        self.unique_values = [value for value, count in self.value_counts.items() if count == 1]
        self.duplicate_values = [value for value, count in self.value_counts.items() if count > 1]

    def get_num_elements(self):
        """返回数据列表中的总元素数量"""
        return len(self.data_list)

    def get_unique_values(self):
        """返回所有不重复的值"""
        return self.unique_values

    def get_duplicate_values(self):
        """返回所有重复的值"""
        return self.duplicate_values

# 你的数据列表
data_list = [
    "2", "面01.02", "58", "9", "1108", "LCR 182", "1486", "771", "1431", "832",
    "LCP 06", "1450", "1757", "1313", "2114", "1480", "1725", "14", "LCP 01", "2006",
    "561", "1252", "1920", "LCR 140", "1570", "2315", "2413", "1678", "1769", "1684",
    "2535", "2185", "1378", "94", "145", "144", "1683", "26", "613", "175", "1470",
    "2619", "35", "3", "1729", "1050", "2667", "1119", "1142", "1741", "1693", "面17.04",
    "1365", "1873", "面16.07", "1251", "1789", "620", "1890", "1581", "627", "182",
    "1795", "744", "610", "2678", "2656", "2441", "704", "1455", "1672", "1550", "2283",
    "2418", "2574", "2490", "1623", "1114", "2651", "2652", "1979", "1518", "2351", "1512",
    "1773", "2703", "1929", "1342", "728", "2810", "LCR 003", "2236", "509", "1281", "1748",
    "303", "1389", "2319", "2544", "228", "2824", "229", "872", "1812", "461", "2295", "2769",
    "2828", "136", "191", "231", "1688", "349", "2103", "342", "2520", "326", "1832", "1134",
    "2331", "541", "2586", "LCP 50", "2974", "2894", "3194", "2037", "804", "2886", "2648",
    "3065", "2723", "1476", "LCR 158", "LCR 189", "3099", "2951", "2923", "3162", "3146",
    "3151", "2878", "3168", "2864", "1351", "3190", "2888", "2798", "2670", "2965", "3033", "42"
]

# 创建 DataProcessor 对象
processor = DataProcessor(data_list)

# 处理数据
processor.process_data()

# 获取并打印结果
print(f"总元素数量: {processor.get_num_elements()}")
print(f"不重复值的数量: {len(processor.get_unique_values())}")
print(f"不重复值: {processor.get_unique_values()}")
print(f"重复的元素: {processor.get_duplicate_values()}")

# stats.py

import sqlite3

class DataProcessor:
    def __init__(self, data_list):
        """初始化数据处理器，接收一个数据列表，并清理数据"""
        self.data_list = self.clean_data(data_list)  # 清理并标准化数据
        self.value_counts = {}
        self.unique_values = []
        self.duplicate_values = []

    def clean_data(self, data_list):
        """对数据列表进行清理，去重、去除空格和统一小写"""
        return list(set([str(value).strip().lower() for value in data_list]))

    def process_data(self):
        """处理数据，统计不重复值和重复值"""
        for value in self.data_list:
            if value in self.value_counts:
                self.value_counts[value] += 1
            else:
                self.value_counts[value] = 1
        
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

    def calculate_difference(self, other_list):
        """使用SQL计算当前数据列表中不在另一个列表中的元素"""
        other_clean = self.clean_data(other_list)  # 清理和标准化其他列表的数据
        
        # 创建SQLite数据库和连接
        conn = sqlite3.connect(':memory:')  # 使用内存数据库
        cursor = conn.cursor()

        # 创建表并插入数据
        cursor.execute("CREATE TABLE current_data (value TEXT)")
        cursor.executemany("INSERT INTO current_data (value) VALUES (?)", [(v,) for v in self.data_list])

        cursor.execute("CREATE TABLE other_data (value TEXT)")
        cursor.executemany("INSERT INTO other_data (value) VALUES (?)", [(v,) for v in other_clean])

        # 查询 current_data 中不在 other_data 中的差集
        cursor.execute("""
        SELECT value FROM current_data
        WHERE value NOT IN (SELECT value FROM other_data)
        """)
        difference = cursor.fetchall()

        # 关闭连接
        conn.close()

        return [row[0] for row in difference]

    def calculate_reverse_difference(self, other_list):
        """使用SQL计算另一个列表中不在当前数据列表中的元素"""
        other_clean = self.clean_data(other_list)
        
        # 创建SQLite数据库和连接
        conn = sqlite3.connect(':memory:')  # 使用内存数据库
        cursor = conn.cursor()

        # 创建表并插入数据
        cursor.execute("CREATE TABLE current_data (value TEXT)")
        cursor.executemany("INSERT INTO current_data (value) VALUES (?)", [(v,) for v in self.data_list])

        cursor.execute("CREATE TABLE other_data (value TEXT)")
        cursor.executemany("INSERT INTO other_data (value) VALUES (?)", [(v,) for v in other_clean])

        # 查询 other_data 中不在 current_data 中的差集
        cursor.execute("""
        SELECT value FROM other_data
        WHERE value NOT IN (SELECT value FROM current_data)
        """)
        reverse_difference = cursor.fetchall()

        # 关闭连接
        conn.close()

        return [row[0] for row in reverse_difference]

# 测试使用 DataProcessor 类

# 你的数据列表
solved = [
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
    "3151", "2878", "3168", "2864", "1351", "3190", "2888", "2798", "2670", "2965", "3033",
    "42", "2620", "3232", "27", "1732", "2882", "2194", "2220"
]

completed = [
    "1539", "1", "2", "面01.02", "58", "9", "1051", "2235", "LCR 182", "1486", "1431",
    "2011", "832", "LCP 06", "1450", "1313", "2114", "1480", "1725", "14", "2006", "LCP 01",
    "561", "804", "2037", "1252", "2367", "1920", "2469", "2315", "LCR 140", "1570", "2413",
    "1678", "13", "1769", "1684", "2535", "2500", "760", "1068", "LCP 17", "94", "1729", "144",
    "1821", "613", "175", "1683", "1470", "26", "35", "1108", "3", "1378", "2619", "1050", "2667",
    "1741", "2325", "1142", "1119", "145", "2185", "1266", "1784", "1890", "LCP 66", "771",
    "面17.04", "1365", "1623", "1873", "2356", "面16.07", "1789", "1251", "1693", "1757", "610",
    "914", "620", "1581", "627", "182", "1795", "744", "2656", "2678", "2441", "2373", "1455",
    "2574", "1672", "1550", "2490", "2283", "2418", "LCR 135", "2432", "1114", "2651", "2652",
    "1979", "506", "1518", "2351", "面16.01", "2341", "860", "1773", "1929", "1512", "2357",
    "1827", "LCR 189", "2703", "922", "728", "1342", "258", "2621", "2176", "1603", "LCR 042",
    "171", "1720", "344", "338", "2810", "LCR 003", "1572", "509", "2236", "1281", "1389", "1748",
    "303", "704", "2319", "2544", "1528", "228", "2824", "229", "872", "1030", "1812", "461",
    "2295", "191", "2769", "136", "2828", "1688", "349", "2103", "231", "326", "2520", "342",
    "LCR 158", "1832", "1828", "1134", "LCP 44", "2331", "2496", "2586", "557", "2485", "2506",
    "541", "1837", "LCP 50", "2427", "1228", "2148", "1791", "2974", "2894", "3194", "2942",
    "3174", "3110", "2960", "2697", "2859", "3079", "面02.02", "1227", "2881", "118", "2744",
    "2879", "2884", "2798", "2670", "2965", "2888", "2710", "2796", "2864", "1351", "3190",
    "3168", "3151", "2878", "42", "2723", "3146", "2923", "2951", "3099", "3162", "2886", "2648",
    "3065", "3033", "2620", "3232", "27", "1732", "2220", "1476", "2194", "2882"
]

# 创建 DataProcessor 对象
processor_solved = DataProcessor(solved)
processor_completed = DataProcessor(completed)

# 处理数据
processor_solved.process_data()
processor_completed.process_data()

# 获取并打印 solved 列表的结果
print("solved 列表的结果：")
print(f"总元素数量: {processor_solved.get_num_elements()}")
print(f"不重复值的数量: {len(processor_solved.get_unique_values())}")
print(f"不重复值: {processor_solved.get_unique_values()}")
print(f"重复的元素: {processor_solved.get_duplicate_values()}")

# 获取并打印 completed 列表的结果
print("\ncompleted 列表的结果：")
print(f"总元素数量: {processor_completed.get_num_elements()}")
print(f"不重复值的数量: {len(processor_completed.get_unique_values())}")
print(f"不重复值: {processor_completed.get_unique_values()}")
print(f"重复的元素: {processor_completed.get_duplicate_values()}")

# 获取并打印差集
solved_not_in_completed = processor_solved.calculate_difference(completed)
print(f"\nsolved 中不在 completed 中的元素: {solved_not_in_completed} (数量: {len(solved_not_in_completed)})")

# 获取并打印反向差集
completed_not_in_solved = processor_completed.calculate_reverse_difference(solved)
print(f"completed 中不在 solved 中的元素: {completed_not_in_solved} (数量: {len(completed_not_in_solved)})")

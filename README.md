# Cloud_MapReducer

## Average Rating MapReduce Project

This project calculates the average rating for each smartphone brand from a large CSV dataset using Hadoop Streaming with Python.

---

## Workflow

### Mapper (`mapper_avg_rating.py`)
- Reads CSV input line by line.
- Cleans and normalizes the brand name.
- Returns `<brand>\t<rating>` for valid entries.

### Reducer (`reducer_avg_rating.py`)
- Groups all ratings by brand.
- Calculates the average rating for each brand.
- Returns `<brand>\t<average_rating>`.

---

## Running the Project on Hadoop

### Prerequisites

- **Hadoop** installed and configured on Ubuntu
- **HDFS** and **YARN** running
- Python 3 available on all nodes
- Dataset (`Amazon_Unlocked_Mobile.csv`) ([Dataset Link](https://www.kaggle.com/datasets/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones))


---

### 1. **Start Hadoop Services**

- Hadoop installed and configured
- HDFS and YARN running:
  ```bash
  start-dfs.sh
  start-yarn.sh
---

### 2. **Prepare HDFS Directories**

- Remove old input/output if only they exist (run only if needed)
  ```bash
    hdfs dfs -rm -r /user/umeshgayashan/input
    hdfs dfs -rm -r /user/umeshgayashan/output_avg_rating
- Create input directory
  ```bash
    hdfs dfs -mkdir -p /user/umeshgayashan/input

- Upload your CSV file to HDFS
  ```bash
    hdfs dfs -put /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/Amazon_Unlocked_Mobile.csv /user/umeshgayashan/input/


---

### 3. **Make Mapper and Reducer Executable**
  ```bash
    chmod +x /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/mapper_avg_rating.py
    chmod +x /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/reducer_avg_rating.py 
```

---

---

### 4. **Verify Hadoop Installation**
```bash
    which hadoop
```

### 5. **Run the MapReduce Job**
```bash
hadoop jar /home/umeshgayashan/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -files /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/mapper_avg_rating.py,/home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/reducer_avg_rating.py \
  -mapper "python3 mapper_avg_rating.py" \
  -reducer "python3 reducer_avg_rating.py" \
  -input /user/umeshgayashan/input/Amazon_Unlocked_Mobile.csv \
  -output /user/umeshgayashan/output_avg_rating
```

---

### 6. **Check the Output**
```bash
hdfs dfs -ls /user/umeshgayashan/output_avg_rating
hdfs dfs -cat /user/umeshgayashan/output_avg_rating/part-00000
```
### 7. **Output Visualization - in Visualization Brach**
![Average Ratings of Major Brands](/brand_ratings_major.png)


---

## **Testing Locally (without Hadoop)**

### Make Scripts Executable

```bash
chmod +x ./avg_rating/mapper_avg_rating.py ./avg_rating/reducer_avg_rating.py 
```

### Test Mapper Output (Sample Check) - first few output lines
```bash
cat Amazon_Unlocked_Mobile.csv | ./avg_rating/mapper_avg_rating.py | head
```
### Test Complete Pipeline

```bash
cat Amazon_Unlocked_Mobile.csv | ./avg_rating/mapper_avg_rating.py | sort | ./avg_rating/reducer_avg_rating.py
```
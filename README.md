# Cloud_MapReducer

# Average Rating

### chmod +x ./avg_rating/mapper_avg_rating.py ./avg_rating/reducer_avg_rating.py 
### cat Amazon_Unlocked_Mobile.csv | ./mapper_avg_rating.py | head
### cat Amazon_Unlocked_Mobile.csv | ./mapper_avg_rating.py | sort | ./reducer_avg_rating.py


## Run Through Hadoop

stop-dfs.sh
stop-yarn.sh

hdfs dfs -rm -r /user/umeshgayashan/input

hdfs dfs -rm -r /user/umeshgayashan/output_avg_rating


start-dfs.sh
start-yarn.sh

hdfs dfs -ls /user/umeshgayashan/

hdfs dfs -mkdir -p /user/umeshgayashan/input

hdfs dfs -put /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/Amazon_Unlocked_Mobile.csv /user/umeshgayashan/input/

chmod +x /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/mapper_avg_rating.py
chmod +x /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/reducer_avg_rating.py 

which hadoop

hadoop jar /home/umeshgayashan/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -files /home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/mapper_avg_rating.py,/home/umeshgayashan/Documents/GitHub/Cloud_MapReduce/avg_rating/reducer_avg_rating.py \
  -mapper "python3 mapper_avg_rating.py" \
  -reducer "python3 reducer_avg_rating.py" \
  -input /user/umeshgayashan/input/Amazon_Unlocked_Mobile.csv \
  -output /user/umeshgayashan/output_avg_rating
  
 hdfs dfs -ls /user/umeshgayashan/output_avg_rating
 
 hdfs dfs -cat /user/umeshgayashan/output_avg_rating/part-00000

 ## Visualization

### Create Virtual Environment
python3 -m venv venv
### Step: Activate Virtual Environment
source venv/bin/activate
### Step: Install Packages
pip install pandas matplotlib seaborn
### Step: Get png output
python ./avg_rating/visualize_output_avg_rating.py

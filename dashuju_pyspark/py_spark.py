# coding=gbk
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


def readMysqlTime(spark, path):
    struct1 = StructType([
        StructField("userId", StringType(), True),
        StructField("makeId", StringType(), True),
        StructField("videoId", StringType(), True),
        StructField("videoName", StringType(), True),
        StructField("category", StringType(), True),
        StructField("videoLength", StringType(), True),
        StructField("viewsLength", StringType(), True),
        StructField("rate", StringType(), True),
        StructField("comments", StringType(), True),
        StructField("commentSum", StringType(), True),
        StructField("click_like", StringType(), True),
        StructField("click_store", StringType(), True),
        StructField("click_share", StringType(), True),
        StructField("create_time", StringType(), True),

    ])

    data = spark.read.csv(path, sep='|', schema=struct1,
                          header=False)
    data.createTempView("userTable");
    df = spark.sql("""select * from userTable 
                        where  click_like = true or 
                        click_store = true  or
                        click_share = true""")

    return df


if __name__ == '__main__':
    # 本地local,开启2个线程
    spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("pyspark") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    df = readMysqlTime(spark, "D:/home/user/data_201908231650.log")
    df = df.select(df.videoName, when(df.click_like == 'true', 1).otherwise(0).alias("like"),
                   when(df.click_store == 'true', 1).otherwise(0).alias("store"),
                   when(df.click_share == 'true', 1).otherwise(0).alias("share"))
    df.show()
    pass
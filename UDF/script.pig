-- Register the Python UDF script
REGISTER 'hdfs://localhost:9000/udfs/uppercase_udf.py' USING jython AS udf;

-- Load some data
data = LOAD 'hdfs://localhost:9000/pigdemo/pig_udf_text.txt' AS (text:chararray);

-- Use the Python UDF
uppercased_data = FOREACH data GENERATE udf.uppercase(text) AS uppercase_text;

-- Store the result
STORE uppercased_data INTO 'hdfs://localhost:9000/pigdemo/output';

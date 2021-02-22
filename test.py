# import your library
import records

# get an instance given some query parameters
rec = records.Records(genusKey=1340278, year="1990,1991")

# access the dataframe results
print(rec.get_single_batch())
rec.get_all_records()
print(rec.json)

print(f"DATAFRAME: \n{rec.df[18:]}")
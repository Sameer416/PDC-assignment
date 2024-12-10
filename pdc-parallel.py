import dask.dataframe as dd
from datetime import datetime


start_time = datetime.now()

year = start_time.year

students_df = dd.read_csv('data/students.csv', encoding='utf-8')
fees_df = dd.read_csv('data/student_fees.csv', encoding='utf-8')

fees_df['Payment Status'] = fees_df['Payment Status'].str.lower().str.strip()

fees_df['Payment Date'] = fees_df['Payment Date'].map_partitions(
    lambda part: part + f" {year}", meta=('Payment Date', 'str')
)
fees_df['Payment Date'] = dd.to_datetime(fees_df['Payment Date'], format='%B %d %Y', errors='coerce')

paid_fees_df = fees_df[fees_df['Payment Status'] == 'paid']


paid_fees_df['Day of Month'] = paid_fees_df['Payment Date'].dt.day

day_count_df = (
    paid_fees_df.groupby(['Student ID', 'Day of Month']).size().reset_index()
)
day_count_df.columns = ['Student ID', 'Day of Month', 'Payment Count']


day_count_pd = day_count_df.compute()

most_frequent_days = (
    day_count_pd.loc[day_count_pd.groupby('Student ID')['Payment Count'].idxmax()]
)

students_pd = students_df.compute()

final_output = students_pd.merge(
    most_frequent_days[['Student ID', 'Day of Month', 'Payment Count']],
    on='Student ID',
    how='left'
)

end_time = datetime.now()
execution_duration = end_time - start_time

print("Final Output:")
print(final_output[['Student ID', 'Day of Month', 'Payment Count']])

print("\nExecution Time:")
print(f"Start Time: {start_time}")
print(f"End Time: {end_time}")
print(f"Total Duration: {execution_duration}")

import labelbox
import sage_data_client

df = sage_data_client.query(
    start="-30d",
    filter={
        "name":"upload",
        "vsn": "W01D",
        "job": "sage",
        "task": "videosampler-bottom",
    }
)

for url in df.value:
    print(url)

# data_rows = [{"row_data": url} for url in df.value]

# client = labelbox.Client()

# ds = client.create_dataset(name="Test Image Dataset W01D")

# task = ds.create_data_rows(data_rows)
# task.wait_till_done()
# print(task.status)

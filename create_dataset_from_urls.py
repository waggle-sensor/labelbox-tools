import labelbox
import requests


def create_dataset_from_urls(name, urlfile):
    r = requests.get(urlfile)
    urls = r.text.splitlines()

    data_rows = [{"row_data": url} for url in urls]

    client = labelbox.Client()

    ds = client.create_dataset(name=name)

    task = ds.create_data_rows(data_rows)
    task.wait_till_done()
    print(task.status)


create_dataset_from_urls("water_depth_images_set1", "https://web.lcrc.anl.gov/public/waggle/datasets/water_depth_images_set1/urls.txt")
create_dataset_from_urls("water_depth_images_set2", "https://web.lcrc.anl.gov/public/waggle/datasets/water_depth_images_set2/urls.txt")

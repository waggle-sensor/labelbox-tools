import labelbox
import pandas as pd


# TODO(sean) Look at ontologies in Labelbox and see if we can define standard fields
# they should be mapped to for label files.
def get_water_height(label):
    cls = label["Label"]["classifications"]
    for c in cls:
        if c["value"] == "water_height":
            return int(c["answer"])
    return None


def main():
    client = labelbox.Client()
    project = client.get_project('cl1v1kfpz10710z65184wcnw2')
    labels = project.export_labels(download=True)

    items = []

    for label in labels:
        height = get_water_height(label)
        if height is None:
            continue
        items.append({
            "image": label["External ID"],
            "height": height,
            "is_valid": False,
        })

    df = pd.DataFrame(items)

    # mark 20% per class as valid
    for height, df_cls in df.groupby("height"):
        # if len(df_cls) == 1:
        #     print(f"warning: too few samples for {height}")
        #     continue
        if len(df_cls) <= 2:
            print(f"warning: too few samples for {height}")
            continue
        df.loc[df_cls.sample(frac=0.20).index, "is_valid"] = True

    print(df)
    df.to_csv("labels.csv")


if __name__ == "__main__":
    main()

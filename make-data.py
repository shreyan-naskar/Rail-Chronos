from pathlib import Path
import pandas as pd

def process_target_csv(filepath: str, start_time: str = "2024-01-01"):
    filepath = Path(filepath)
    name = filepath.stem.replace("_target", "")

    df = pd.read_csv(filepath, header=None)
    # print(df.shape)
    output_dir = Path("data") / name
    output_dir.mkdir(parents=True, exist_ok=True)

    for col_number, (_, col) in enumerate(df.items()):        
        values = col.values
        timestamps = pd.date_range(start=start_time, periods=len(values), freq="h")

        out_df = pd.DataFrame({"timestamp": timestamps, "target": values})
        out_df.to_csv(output_dir / f"{col_number}.csv", index=False)

if __name__ == "__main__":
  data_dir = Path("raw-data")
  for csv_file in sorted(data_dir.glob("*.csv")):
      process_target_csv(csv_file)
    
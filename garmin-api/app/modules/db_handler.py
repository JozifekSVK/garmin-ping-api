import clickhouse_connect
import pandas as pd

def warehouse_ch_load(df: pd.DataFrame) -> None:
    """Load the data to clickhouse DB."""
    print("Starting loading data")
    client = clickhouse_connect.get_client(
        host="clickhouse_db", 
        port=8123,
    )

    print(df)

    summary_ids = tuple(df["summaryId"].to_list())
    summary_ids = ", ".join([f"'{i}'" for i in summary_ids])

    print(df.columns)

    print('deletujem')
    client.query(
        f"""delete from garmin_data.accepted_requests
            where summaryId in ({summary_ids})
            """
    )

    print('loadujem')
    client.insert_df("garmin_data.accepted_requests",df)


    print(f"Inserted {len(df)} rows")
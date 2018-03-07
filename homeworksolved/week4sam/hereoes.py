import pandas as pd
import os
readfile= os.path.join(('purchase_data.json')
        pur_data = pd.read_json(readfile)
        player_count=len(pur_data['SN'].unique())
        players_df = pd.DataFrame({'Total Players': player_count}])
        players_df.set_index('Total Players', inplace= True)


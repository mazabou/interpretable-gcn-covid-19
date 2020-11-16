import numpy as np
import torch
from torch_geometric.data import Dataset, Data
from torch_geometric.utils import dense_to_sparse


top_20_counties = np.array([ 185,  577, 2454,   86,  203,  196,  339, 2412,  199, 1621, 2772, 202, 2559, 2373,  302,  209, 1242,  167, 1160, 2142])
tc_mask = np.zeros(2942)
tc_mask[top_20_counties] = 1


class COVIDDataset(Dataset):
    def __init__(self, subset='train', normalization_params=None, rm_unemployment=False, transform=None, pre_transform=None):
        super().__init__(None, transform, pre_transform)
        self.subset = subset
        self.rm_unemployment = rm_unemployment
        self.filename = '../data/%s.npy' % subset
        static_node_feats, temp_node_feats, self.edge_matrix, y = self._load_data()
        
        static_node_feats = static_node_feats.astype('float')
        
        if normalization_params is None:
            self.normalization_params = {}
            self.normalization_params['static'] = {'mean': static_node_feats.mean(), 'std': static_node_feats.std()}
            self.normalization_params['temp'] = {'mean': temp_node_feats.mean(axis=(0,1)), 'std':temp_node_feats.std(axis=(0,1))}
            self.normalization_params['y'] = {'mean': y.mean(), 'std': y.std()}
        else:
            self.normalization_params = normalization_params
        
        self.static_node_feats = (static_node_feats - self.normalization_params['static']['mean'])/self.normalization_params['static']['std']
        self.temp_node_feats = (temp_node_feats - self.normalization_params['temp']['mean'])/self.normalization_params['temp']['std']
        self.y = (y - self.normalization_params['y']['mean'])/self.normalization_params['y']['std']
        
        if self.rm_unemployment:
            print(self.temp_node_feats.shape)
            self.temp_node_feats = self.temp_node_feats[:, :, :-1]
            print(self.temp_node_feats.shape)

        self.num_days = self.temp_node_feats.shape[1]
        if self.subset == 'test':
            self.num_days += 1
        self.d = 7

    def len(self):
        return self.num_days - self.d

    def get(self, idx):
        idx = idx + self.d - 1
        temp_features = torch.tensor(self.temp_node_feats[:, idx - self.d + 1:idx + 1], dtype=torch.float32)
        temp_features = temp_features.view((temp_features.shape[0], -1))
        temp_y = torch.tensor(self.y[:, idx - self.d + 1:idx + 1], dtype=torch.float32)

        temp_features = torch.cat([temp_features, temp_y], dim=-1)

        static_features = torch.tensor(self.static_node_feats.astype(np.float32), dtype=torch.float32)

        edge_weights = self.edge_matrix[idx]
        edge_index, edge_attr = dense_to_sparse(torch.tensor(edge_weights, dtype=torch.float32))
        edge_index = edge_index.long()

        # edge_index: 2, num_edges
        # edge_attr: num_edges, num_features --> 1

        y = torch.tensor(self.y[:, idx+1] - self.y[:, idx], dtype=torch.float32)
        
        tc = torch.tensor(tc_mask, dtype=torch.float32)

        data = Data(x=temp_features, sx=static_features, edge_index=edge_index, edge_attr=edge_attr, y=y, tc=tc)
        return data

    def _load_data(self):
        data = np.load(self.filename, allow_pickle=True)
        return data.item()['static_node_feats'], data.item()['temp_node_feats'], data.item()['edge_matrix'], data.item()['y']


    #static_node_feat: num_counties x num_features
    #temp_node_feats : num_counties x num_days x num_features
    #edge_matrix: num_days x num_counties x num_counties
    #y: case_counts :  num_counties x num_days
import torch
from torch.nn import Sequential as Seq, Linear, ReLU
from torch_geometric.nn import MessagePassing


class SpatioTemporalGCN_Noflow(SpatioTemporalGCN):
    def __init__(self, num_temp_features, num_static_features, d=7):
        super().__init__(num_temp_features, num_static_features, d)
        
    def forward(self, data):
        x, sx, edge_index, edge_attr, batch = data.x, data.sx, data.edge_index, data.edge_attr, data.batch
        
        edge_attr = (edge_attr > 0).type(torch.float32)
        # temporal embeddings
        x_embed = torch.cat([x, sx], dim=-1)
        x_0 = self.temp_conv(x_embed)
        
        x_embed = torch.cat([x_0, sx], dim=-1)
        out = self.space_conv_1(x_embed, edge_attr, edge_index)
        
        x_embed = torch.cat([out, x_0, sx], dim=-1)
        out = self.space_conv_2(x_embed, edge_attr, edge_index)
        
        # readout
        x_embed = torch.cat([out, x_0, sx], dim=-1)
        out = self.mlp(x_embed)
        
        # num_counties x 1
        return out
    
    
class SpatioTemporalGCN_Nostatic(torch.nn.Module):
    def __init__(self, num_temp_features, num_static_features, d=7):
        super().__init__()
        self.temp_conv = TempConv(num_temp_features * d, 32, 32)
        self.space_conv_1 = SpaceConv(32, 32, 64)
        self.space_conv_2 = SpaceConv(64 + 32, 64, 64)
        self.mlp = PredictLayer(64 + 32, 16, 1)
        
    def forward(self, data):
        x, sx, edge_index, edge_attr, batch = data.x, data.sx, data.edge_index, data.edge_attr, data.batch
        
        # temporal embeddings
        x_embed = x
        x_0 = self.temp_conv(x_embed)
        
        x_embed = x_0
        out = self.space_conv_1(x_embed, edge_attr, edge_index)
        
        x_embed = torch.cat([out, x_0], dim=-1)
        out = self.space_conv_2(x_embed, edge_attr, edge_index)
        
        # readout
        x_embed = torch.cat([out, x_0], dim=-1)
        out = self.mlp(x_embed)
        
        # num_counties x 1
        return out
    
    
class SpatioTemporalGCN_Nounemploy(torch.nn.Module):
    def __init__(self, num_temp_features, num_static_features, d=7):
        super().__init__()
        self.temp_conv = TempConv(num_temp_features * d + num_static_features, 32, 32)
        self.space_conv_1 = SpaceConv(32 + num_static_features, 32, 64)
        self.space_conv_2 = SpaceConv(64 + 32 + num_static_features, 64, 64)
        self.mlp = PredictLayer(64 + 32 + num_static_features, 16, 1)
        
    def forward(self, data):
        x, sx, edge_index, edge_attr = data.x, data.sx, data.edge_index, data.edge_attr
        
        # temporal embeddings
        x_embed = torch.cat([x, sx], dim=-1)
        x_0 = self.temp_conv(x_embed)
        
        x_embed = torch.cat([x_0, sx], dim=-1)
        out = self.space_conv_1(x_embed, edge_attr, edge_index)
        
        x_embed = torch.cat([out, x_0, sx], dim=-1)
        out = self.space_conv_2(x_embed, edge_attr, edge_index)
        
        # readout
        x_embed = torch.cat([out, x_0, sx], dim=-1)
        out = self.mlp(x_embed)
        
        # num_counties x 1
        return out

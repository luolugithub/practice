import torch
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class LuoluDataset(Dataset):
    def __init__(self, filepath):
        import pandas as pd
        import numpy as np
        df = pd.read_csv(filepath, delimiter=',', dtype=np.float32)
        self.len = df.shape[0]
        self.data = torch.from_numpy(df[:, :-1])
        self.labels = torch.from_numpy(df[:, [-1]])

    def __getitem__(self, index):
        return self.data[index], self.labels[index]

    def __len__(self):
        return self.len


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmod = torch.nn.Sigmoid()
        
    def forward(self, x):
        x = self.sigmod(self.linear1(x))
        x = self.sigmod(self.linear2(x))
        x = self.sigmod(self.linear3(x))
        return x


if __name__ == '__main__':
    EPOCH = 100
    file_path = "../../.csv"
    dataset = LuoluDataset(file_path)
    train_dataset = DataLoader(dataset=dataset,
                               batch_size=64,
                               shuffle=True,
                               pin_memory=True,
                               num_workers=4)
    model = Model()
    criterion = torch.nn.BCELoss(size_average=True)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    for epoch in range(EPOCH):
        for i, data in enumerate(train_dataset, 0):
            # 1，准备数据
            inputs, labels = data
            # 2, 前向传播
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            # 3, 后向传播
            optimizer.zero_grad()
            loss.backward()
            # 4, 更新优化参数
            optimizer.step()




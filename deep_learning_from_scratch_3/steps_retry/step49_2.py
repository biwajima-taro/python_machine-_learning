import sys
import os
sys.path.append(os.pardir)


if __name__ == "__main__":
    import dezero
    train_set = dezero.datasets.Spiral()
    batch_index = [0, 1, 2]
    batch = [train_set[i] for i in batch_index]
    print(batch)

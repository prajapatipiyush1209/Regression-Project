from src.components.data_transformation import DataTransformer
from src.components.data_ingetion import DataIngetion
from src.components.model_train import model_train


if __name__ =="__main__"  :   
    o = DataIngetion()
    train_data_path, test_data_path = o.data_ingetion_intiate()

    object_data_transformation = DataTransformer()
    train_arr, test_arr, _ = object_data_transformation.intiate_data_transformation(train_data_path, test_data_path)

    object_model_train = model_train()
    object_model_train.intate_model_train(train_arr, test_arr)
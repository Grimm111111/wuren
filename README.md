创建data件夹 放入数据 格式如下
-data 
-----uav
-------------xsubu2
--------------------test_data.npy  
--------------------test_label.npy 
--------------------train_data.npy 
--------------------train_label.npy 
命令行输入
训练：
python main.py --config config/uav-cross-subjectv2/train.yaml --work-dir work_dir/2104 --model_saved_name runs/2104 --device 0 --batch-size 16 --test-batch-size 16 --warm_up_epoch 5 --only_train_epoch 100 --seed 777
测试：
python main.py --config config/uav-cross-subjectv2/test.yaml --work-dir work_dir/3003 --model_saved_name runs/3003 --device 0 --batch-size 128 --test-batch-size 128 --weights "D:/AI Competition/TE-GCN-main/runs/2103-49-25650.pt"

脚本3可以将生成的pkl文件转为npy 进行评分

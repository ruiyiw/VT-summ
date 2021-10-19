cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --v2 --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 16 --lr 0.0002 --pretrain_emb --kl_ceiling 0.3 --aux_ceiling 1 --full_kl_step 30000 --num_var_layers 1 --save_path_pretrained pretrain-64/trs_v2/model_epoch99_iter91970_3.8188_45.5497_0.0000_6.5500_0.0000 --save_path svt-64/cvae_trs_v2/ > svt-64/cvae_trs_v2/out.txt

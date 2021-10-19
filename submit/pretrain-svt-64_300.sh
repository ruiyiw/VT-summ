cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model trs --v2 --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 64 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 20000 --num_var_layers 1 --save_path pretrain-64/trs_v2/ > pretrain-64/trs_v2/out.txt

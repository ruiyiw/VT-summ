cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model trs --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 128 --lr 0.001 --pretrain_emb --kl_ceiling 0.48 --aux_ceiling 1 --full_kl_step 20000 --save_path tmp-128/trs_new_bow_batch/ 2>&1 > tmp-128/trs_new_bow_batch/out.txt

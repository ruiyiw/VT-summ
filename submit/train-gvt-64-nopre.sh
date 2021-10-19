cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 64 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path tmp/gvt-64-nopre-test/cvae_trs/ > tmp/gvt-64-nopre-test/cvae_trs/out.txt

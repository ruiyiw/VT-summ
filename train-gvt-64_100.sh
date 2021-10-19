cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 64 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path_pretrained gvt-64/cvae_new_bow_batch/model_699999_14.7866_8.9201_0.0000_7.1400_12.5983 --save_path gvt-64_100/cvae_new_bow_batch/ > gvt-64_100/cvae_new_bow_batch/out.txt

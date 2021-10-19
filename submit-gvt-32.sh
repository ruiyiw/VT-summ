cd /share03/rwang/wry/vae-trans || exit
source env/bin/activate
cd VT-summ

python3 main.py --dataset gigaword --model cvaetrs --emb_dim 300 --hidden_dim 300 --hop 4 --heads 4 --cuda --batch_size 32 --lr 0.001 --pretrain_emb --kl_ceiling 0.08 --aux_ceiling 1 --full_kl_step 15000 --save_path_pretrained tmp-32/trs_new_bow_batch/model_99999_4.7853_119.7341_0.0000_0.0000_0.0000 --save_path gvt-32/cvae_new_bow_batch/ > gvt-32/cvae_new_bow_batch/out.txt
